from django.views.generic import ListView, TemplateView, UpdateView
from braces.views import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponse
from json import dumps
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render

from property.models import Basic
from .models import Bookmark, UserProfile
from .forms import UserForm, ProfileForm, PasswordUpdateForm


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'profile/profile.html'
    form_class = UserForm
    second_form_class = ProfileForm
    third_form_class = PasswordUpdateForm
    model = User
    success_url = reverse_lazy('go_profile')

    def get_object(self, queryset=None):
        obj = User.objects.get(pk=self.request.user.pk)  # self.kwargs['id']
        return obj

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        form_class = self.get_form_class()

        context['form'] = self.get_form(form_class)
        try:
            context['form2'] = ProfileForm(instance=UserProfile.objects.get(user=self.request.user))

            # FOR TEST RESIZE IMAGE
            '''
            from sorl.thumbnail import get_thumbnail
            a = UserProfile.objects.get(user=self.request.user)
            im = get_thumbnail(a.avatar, '100x100', crop='center', quality=99)
            print im
            '''

        except UserProfile.DoesNotExist:
            create_profile = UserProfile()
            create_profile.user = self.request.user
            create_profile.save()

            context['form2'] = ProfileForm(instance=UserProfile.objects.get(user=self.request.user))
        context['form3'] = PasswordUpdateForm(instance=User.objects.get(pk=self.request.user.pk))

        '''# generate gravatar
        from hashlib import md5
        email_hash = md5(self.request.user.email.strip().lower()).hexdigest()
        context['gravatar'] = email_hash'''
        return context

    def get(self, request, *args, **kwargs):
        super(ProfileView, self).get(request, *args, **kwargs)
        form = self.form_class(self.request.GET, instance=request.user)
        try:
            form2 = self.second_form_class(self.request.GET, instance=request.user.userprofile)
        except:
            form2 = self.second_form_class(self.request.GET)
        form3 = self.third_form_class(self.request.GET, instance=request.user)

        return self.render_to_response(self.get_context_data(object=self.object, form=form, form2=form2, form3=form3))

    def post(self, request, *args, **kwargs):

        if 'update_profile' in request.POST:
            is_ok = False
            msg = ''
            success = False

            self.object = self.get_object()
            form = UserForm(request.POST, instance=request.user)
            form2 = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
            form3 = PasswordUpdateForm(instance=request.user.userprofile)

            if form.is_valid() and form2.is_valid():
                userform = form.save(commit=False)
                userform.save()

                profileform = form2.save(commit=False)
                profileform.save()

                is_ok = True
                success = True
                msg = 'Your profile has been updated.'

            else:
                success = True
                msg = 'An error occured while saving your profile.'

            return render(request, self.template_name, {'form': form, 'form2': form2, 'form3': form3,
                                                        'success': success, 'is_ok': is_ok, 'msg': msg, })

        elif 'update_pwd' in request.POST:
            is_ok = False
            msg = ''
            success = False

            form = UserForm(instance=request.user)
            form2 = ProfileForm(instance=request.user.userprofile)
            form3 = PasswordUpdateForm(request.POST, instance=request.user)

            old_password = request.POST['old_password']
            password = request.POST['password']
            repassword = request.POST['repassword']

            if old_password:
                if request.user.check_password(old_password):
                    if form3.is_valid():
                        userform = form3.save(commit=False)
                        if password == repassword:
                            userform.set_password(password)
                            userform.save()

                        is_ok = True
                        msg = 'Password changed.'
                        success = True
                    else:
                        msg = 'An error occurred during your password change.'
                        success = True

                else:
                    msg = 'Your current password is wrong.'
                    success = True
            else:
                msg = "An error occurred during your password change."
                success = True

            return render(request, self.template_name, {'form': form, 'form2': form2, 'form3': form3,
                                                        'success': success, 'msg': msg, 'is_ok': is_ok, })


# Bookmarked View
class BookmarkedView(LoginRequiredMixin, ListView):
    context_object_name = 'bookmarked_list'
    template_name = 'bookmarked/my_bookmarked.html'
    paginate_by = 10

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user).order_by('-pk')


class BookmarkedAjaxView(View):

    def get(self, context, **response_kwargs):
        response = {
            'status': 404,
        }
        return HttpResponse(dumps(response))  # , mimetype="application/json"

    def post(self, context, **response_kwargs):
        property_slug = self.request.POST.get('property_slug', '')
        user_id = self.request.user.id

        property = Basic.objects.get(slug=property_slug)
        user = User.objects.get(pk=user_id)

        try:
            status = 200
            action = 0

            bookmarked = Bookmark.objects.get(property=property, user=user)
            bookmarked.delete()
        except:
            status = 200
            action = 1

            bookmarked = Bookmark()
            bookmarked.user = user
            bookmarked.property = property
            bookmarked.save()

        response = {
            'status': status,
            'action': action
        }
        return HttpResponse(dumps(response))  # , mimetype="application/json"
