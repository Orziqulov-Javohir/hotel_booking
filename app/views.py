from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import orderForm

class IndexPageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


""" class ContactPageView(TemplateView):
    template_name = 'contact.html' """

def contact(request):
    if request.method == 'POST':
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()


    form = orderForm()
    context = {
        'form' : form
    }
    return render(request, 'contact.html', context)


# Create your views here.
