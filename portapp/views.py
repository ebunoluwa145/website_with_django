from django.shortcuts import render
import requests
import json
from .models import Contact

# This line of code makes sure our index.html file looks like a website


def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')

        r = requests.get(
            'http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        
        context = {'joke' : joke}

        return render(request, 'portapp/index.html',context)
    else:
        firstname = 'Kick'
        lastname = 'Seller'

        r = requests.get(
            'http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joke': joke}

        return render(request, 'portapp/index.html', context)


def about(request):
    return render(request, 'portapp/about.html')


def portfolio(request):
    return render(request, 'portapp/portfolio.html')


def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'portapp/thanks.html')
    else:
        return render(request, 'portapp/contact.html')
