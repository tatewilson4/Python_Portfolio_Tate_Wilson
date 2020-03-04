from django.shortcuts import render



def base(request, template_name = 'base.html'):
    return render(request, template_name)
