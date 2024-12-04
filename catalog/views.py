from django.shortcuts import render


def home_page(request):
    return render(request, 'html/home.html')


def contacts_page(request):
    return render(request, 'html/contacts.html')
