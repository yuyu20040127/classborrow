from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

class BorrowerList(LoginRequiredMixin, ListView):    
    model = Borrower
    ordering = ['realname']     
    paginate_by = 20

class BorrowerView(LoginRequiredMixin, DetailView):   
    model = Borrower

class BorrowerAdd(LoginRequiredMixin, CreateView): 
    model = Borrower
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('borrower_list')

class BorrowerEdit(LoginRequiredMixin, UpdateView):  
    model = Borrower
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('borrower_list')

class BorrowerDelete(LoginRequiredMixin, DeleteView): 
    model = Borrower
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('borrower_list')
