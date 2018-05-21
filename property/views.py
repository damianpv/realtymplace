from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, FormView, UpdateView
from django.views.generic.edit import FormMixin
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404, HttpResponse, HttpResponseRedirect
from braces.views import LoginRequiredMixin
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _

from home.models import Country, Language
from .models import Basic, BasicImages
from account_profile.models import Bookmark
from .forms import PropertyBasicForm, PropertyImagesForm
from agency.models import Agency
from agency.forms import AgencyContactForm


class PropertyListView(ListView):
    # model = Basic
    queryset = Basic.objects.all().order_by('-pk')
    context_object_name = 'property_basic'
    template_name = 'property/list_grid.html'
    paginate_by = 9


class PropertyDetailView(FormMixin, DetailView):
    model = Basic
    form_class = AgencyContactForm
    context_object_name = 'property_detail'
    template_name = 'property/detail.html'

    def get_initial(self):
        user_fullname = None
        user_email = None
        message = _('I am interested in this rent and would like to schedule a viewing. Please let me know when this would be possible.')
        if self.request.user.is_authenticated():
            user_fullname = '%s %s' % (self.request.user.first_name, self.request.user.last_name)
            user_email = self.request.user.email
        self.initial.update({
            'name': user_fullname,
            'email': user_email,
            # 'message': message,
            'agency': self.object.agency.pk
            })
        return super(PropertyDetailView, self).get_initial()

    def get_success_url(self):
        return reverse('go_property_detail', kwargs={'slug': self.kwargs.get('slug', None)})

    def get_context_data(self, **kwargs):
        context = super(PropertyDetailView, self).get_context_data(**kwargs)
        post = self.get_object()
        form_class = self.get_form_class()

        post.visit += 1
        post.save()

        try:
            get_user = self.request.user
            property = Basic.objects.get(pk=post.pk)
            bookmarked = Bookmark.objects.get(property=property, user=get_user)
            context['bookmarked'] = True
        except:
            pass
        context['site_url'] = settings.SITE_URL
        context['static_url'] = settings.STATIC_URL
        # context['form_agency_contact'] = AgencyContactForm
        context['form_agency_contact'] = self.get_form(form_class)
        return context

    '''
    def get_object(self):
        # Call the superclass
        object = super(PropertyDetailView, self).get_object()
        # Record the visit
        object.visit = object.visit+1
        object.save()
        # Return the object
        return object
    '''

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super(PropertyDetailView, self).form_invalid(form)

    def form_valid(self, form):
        get_agency = Agency.objects.get(pk=form.cleaned_data['agency'])
        form_agency = form.save(commit=False)
        form_agency.agency = get_agency
        form_agency.save()
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super(PropertyDetailView, self).form_valid(form)


# ##### ADMIN ######


class MyPropertiesListView(LoginRequiredMixin, ListView):
    # model = Basic
    queryset = Basic.objects.all().order_by('-pk')
    template_name = 'property/admin/my_property.html'
    context_object_name = 'my_property'
    paginate_by = 10

    def get_queryset(self):
        qs = super(MyPropertiesListView, self).get_queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(user=self.request.user)
        return qs


class MyPropertiesDeleteView(LoginRequiredMixin, DeleteView):
    """
    Sub-class the DeleteView to restrict a User from deleting other
    user's data.
    """
    model = Basic
    success_url = reverse_lazy('go_my_property_list')

    def get_queryset(self):
        qs = super(MyPropertiesDeleteView, self).get_queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(user=self.request.user)
        return qs


class PropertyAddView(LoginRequiredMixin, FormView):
    template_name = 'property/admin/create.html'
    model = Basic
    form_class = PropertyBasicForm
    second_form_class = PropertyImagesForm
    success_url = 'success/'
    success_url = '/thanks/'
    initial = {'price': 0, 'bedroom': 0, 'bathroom': 0, 'area': 0, 'garage': 0, }

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        return self.initial

    '''
    def get(self, request, *args, **kwargs):
        form_basic = self.form(initial=self.initial)
        return render(request, self.template_name, {'form_basic': form_basic, })
    '''
    def get_context_data(self, **kwargs):
        context = super(PropertyAddView, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        context['form_basic'] = self.get_form(form_class)
        context['form_images'] = PropertyImagesForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form_basic = self.form_class(request.POST)
        form_images = self.second_form_class(request.POST)
        success = False
        if form_basic.is_valid():

            form_images = PropertyImagesForm(request.POST, request.FILES)
            # print form_images.is_valid()
            if form_images.is_valid():
                # TODO: actions
                language = Language.objects.get(pk=1)
                user = User.objects.get(pk=request.user.id)

                basic = form_basic.save(commit=False)
                basic.language = language
                basic.user = user
                basic.save()
                form_basic.save_m2m()

                print request.FILES.getlist('property_image')

                for image in request.FILES.getlist('property_image'):
                    # print image
                    new_image = BasicImages()
                    new_image.image = image
                    new_image.user = request.user
                    new_image.basic = basic
                    new_image.save()

            return HttpResponseRedirect(reverse('go_my_property_list'))
            # return HttpResponseRedirect(reverse('go_property_add_images', kwargs={'pk': basic.pk}))
        else:
            return render(request, self.template_name, {'form_basic': form_basic, 'form_images': form_images,
                                                        'success': success, })


class PropertyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'property/admin/edit.html'
    model = Basic
    form_class = PropertyBasicForm
    second_form_class = PropertyImagesForm
    success_url = reverse_lazy('go_property_updated_success')

    def get_object(self, *args, **kwargs):
        qs = super(PropertyUpdateView, self).get_object(*args, **kwargs)
        if not self.request.user.is_superuser:
            if not qs.user == self.request.user:
                raise PermissionDenied  # maybe you'll need to write a middleware to catch 403's same way
        return qs

    def get_context_data(self, **kwargs):
        context = super(PropertyUpdateView, self).get_context_data(**kwargs)
        context['country'] = self.object.country
        context['state'] = self.object.state
        context['latitude'] = self.object.latitude
        context['longitude'] = self.object.longitude

        obj_images = BasicImages.objects.filter(basic=self.object)
        context['obj_images'] = obj_images

        context['form_images'] = PropertyImagesForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        basic = Basic.objects.get(pk=self.kwargs['pk'])

        form_basic = self.form_class(request.POST, instance=basic)
        form_images = self.second_form_class(request.POST, instance=basic)
        success = False

        if form_basic.is_valid():

            form_images = PropertyImagesForm(request.POST, request.FILES)
            if form_images.is_valid():
                # TODO: actions
                language = Language.objects.get(pk=1)
                user = User.objects.get(pk=request.user.id)

                basic = form_basic.save(commit=False)
                basic.language = language
                basic.user = user
                basic.save()
                form_basic.save_m2m()

                print request.FILES.getlist('property_image')

                for image in request.FILES.getlist('property_image'):
                    new_image = BasicImages()
                    new_image.image = image
                    new_image.user = request.user
                    new_image.basic = basic
                    new_image.save()

            return HttpResponseRedirect(reverse('go_my_property_list'))
            # return HttpResponseRedirect(reverse('go_property_add_images', kwargs={'pk': basic.pk}))
        else:
            return render(request, self.template_name, {'form': form_basic, 'form_images': form_images,
                                                        'success': success, })


class PropertyAddImagesView(LoginRequiredMixin, View):
    template_name = 'property/admin/add_images.html'

    def get(self, request, *args, **kwargs):
        pk_property = kwargs['pk']

        validate = Basic.objects.filter(pk=pk_property, user=request.user).count()

        if validate >= 1:
            print 'ok'
        else:
            return HttpResponseRedirect(reverse("go_my_property_list"))

        test = request.user.id
        return HttpResponse(test)


class PropertyCreatedSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'property/admin/created_success.html'


class PropertyUpdatedSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'property/admin/updated_success.html'
