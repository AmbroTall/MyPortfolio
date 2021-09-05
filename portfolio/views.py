from django.shortcuts import render
from .models import Projects, Skills, User_profile
from django.views.generic import ListView, DetailView, CreateView


class HomePageView(ListView):
    model = Skills
    template_name = 'portfolio/homepage.html'
    context_object_name = 'skills'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['profile']=User_profile.objects.all()
        context['projects']=Projects.objects.all().order_by('-date_created')
        return context