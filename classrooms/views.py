from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

class ClassroomsList(LoginRequiredMixin, ListView):
    model = Classrooms
    paginate_by = 10

class ClassroomsView(LoginRequiredMixin, DetailView): 
    model = Classrooms

class ClassroomsAdd(LoginRequiredMixin, CreateView):  
    model = Classrooms
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('classrooms_list')

class ClassroomsEdit(LoginRequiredMixin, UpdateView): 
    model = Classrooms
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('classrooms_list')

class ClassroomsDelete(LoginRequiredMixin, DeleteView):   
    model = Classrooms
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('classrooms_list')