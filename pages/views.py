from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import ContactMessage
from .forms import ContactForm

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class ContactUsPageView(FormView):
    template_name = 'pages/contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('pages:contact-us')

    def form_valid(self, form):
        # Save the message to the database
        ContactMessage.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            message=form.cleaned_data['message']
        )
        messages.success(self.request, 'Thank you for contacting us! We will get back to you soon.')
        return super().form_valid(form)




