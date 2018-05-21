from django.shortcuts import render, render_to_response
from django.views.generic import FormView
from django.conf import settings
from datetime import datetime

from .forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = 'thanks'

    initial = {}

    def get(self, request, *args, **kwargs):
        form_contact = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form_contact': form_contact, })

    def post(self, request, *args, **kwargs):
        form_contact = self.form_class(request.POST)
        success = False
        if form_contact.is_valid():
            date = datetime.today()
            form_contact.save()
            success = True

            from django.core.mail import EmailMessage
            msg = EmailMessage(subject="R | Contact", from_email=settings.DEFAULT_FROM_EMAIL,
                               to=[settings.DEFAULT_TO_EMAIL])
            msg.template_name = "rmp_contact"           # A Mandrill template name
            msg.template_content = {                        # Content blocks to fill in
                'TRACKING_BLOCK': "<a href='.../*|TRACKINGNO|*'>track it</a>"
            }

            msg.global_merge_vars = {                       # Merge tags in your template
                'SITE_URL': settings.SITE_URL,
                'STATIC_URL': settings.STATIC_URL,
                'TXT_NAME': request.POST['name'],
                'TXT_EMAIL': request.POST['email'],
                'TXT_MESSAGE': request.POST['message'],
                'TXT_YEAR': date.year
            }
            msg.merge_vars = {                              # Per-recipient merge tags
                'a@.': {'NAME': "Pat"},
            }
            msg.send()

        return render(request, self.template_name, {'form_contact': form_contact, 'success': success})

    def form_invalid(self, form_contact):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render(
            self.get_context_data(form_contact=form_contact,))

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super(ContactView, self).form_valid(form)
