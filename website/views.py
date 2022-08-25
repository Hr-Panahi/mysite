from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.save(commit=False)
            name.name = 'unkown'
            name.save()
            messages.add_message(request, messages.SUCCESS, 'Ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, "Your ticket didn't submit.")
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your email address has been submitted successfully.')
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.ERROR, "Your ticket didn't submit.")
        
            
    form = ContactForm()
    return render(request, 'test.html', {'form':form})