from django.shortcuts import render
from django.views.generic import DeleteView, DetailView, ListView, UpdateView, TemplateView, FormView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from braces.views import LoginRequiredMixin
from django.db.models import Count, Sum

from home.models import Country, Language
from .models import Agency
from property.models import Basic
from .forms import MyAgencyForm


class AgenciesListView(ListView):
    # model = Agency
    queryset = Agency.objects.all().order_by('-pk')
    context_object_name = 'agencies_list'
    template_name = 'agency/list.html'


class AgencyDetailView(DetailView):
    model = Agency
    context_object_name = 'agency_detail'
    template_name = 'agency/detail.html'

    def get_context_data(self, **kwargs):
        context = super(AgencyDetailView, self).get_context_data(**kwargs)
        context['property_list'] = Basic.objects.filter(agency=self.object.pk)
        context['property_num'] = Basic.objects.filter(agency=self.object.pk).aggregate(total=Count('pk'))
        # Save visit
        visit = self.get_object()
        visit.visit += 1
        visit.save()
        return context


# Admin #

# List
class MyAgencyListView(LoginRequiredMixin, ListView):
    # model = Agency
    queryset = Agency.objects.all().order_by('-pk')
    template_name = 'agency/admin/my_agency.html'
    context_object_name = 'my_agency'
    paginate_by = 10

    def get_queryset(self):
        qs = super(MyAgencyListView, self).get_queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(user=self.request.user)
        return qs


# Add
class MyAgencyAddView(LoginRequiredMixin, FormView):
    template_name = 'agency/admin/add_agency.html'
    model = Agency
    form_class = MyAgencyForm
    success_url = reverse_lazy('go_my_agency_add_success')
    initial = {'price': 0, 'bedroom': 0, 'bathroom': 0, 'area': 0, 'garage': 0, }

    def get_context_data(self, **kwargs):
        context = super(MyAgencyAddView, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        success = False
        if form.is_valid():

            language = Language.objects.get(pk=1)
            user = User.objects.get(pk=request.user.id)

            basic = form.save(commit=False)
            basic.language = language
            basic.user = user
            basic.save()

            return HttpResponseRedirect(reverse('go_my_agency_add_success'))
        else:
            return render(request, self.template_name, {'form': form, 'success': success, })


class PropertyAddSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'agency/admin/add_success.html'


# Edit
class MyAgencyEditView(LoginRequiredMixin, UpdateView):
    template_name = 'agency/admin/edit_agency.html'
    model = Agency
    form_class = MyAgencyForm
    success_url = reverse_lazy('go_my_agency_edit_success')

    def get_context_data(self, **kwargs):
        context = super(MyAgencyEditView, self).get_context_data(**kwargs)
        context['latitude'] = self.object.latitude
        context['longitude'] = self.object.longitude
        context['agency_logo'] = self.object.logo
        return context

    def post(self, request, *args, **kwargs):

        get_agency = Agency.objects.get(pk=self.kwargs['pk'])
        form = self.form_class(request.POST, request.FILES, instance=get_agency)
        print request.FILES

        if form.is_valid():

            language = Language.objects.get(pk=1)
            user = User.objects.get(pk=request.user.id)

            basic = form.save(commit=False)
            basic.language = language
            basic.user = user
            basic.save()

            return HttpResponseRedirect(reverse('go_my_agency_edit_success'))
        else:
            return render(request, self.template_name, {'form': form, })


class MyAgencyEditSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'agency/admin/edit_success.html'


class MyAgencyDeleteView(LoginRequiredMixin, DeleteView):
    """
    Sub-class the DeleteView to restrict a User from deleting other
    user's data.
    """
    model = Agency
    success_url = reverse_lazy('go_my_agency_list')

    def get_queryset(self):
        qs = super(MyAgencyDeleteView, self).get_queryset()
        return qs.filter(user=self.request.user)
