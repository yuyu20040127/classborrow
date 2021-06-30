from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse

class StaffList(PermissionRequiredMixin, ListView):
  permission_required = 'auth.view_user'
  model = User
  ordering = ['username']
  paginate_by = 15

class StaffAdd(PermissionRequiredMixin, CreateView):
  permission_required = 'auth.add_user'
  model = User
  fields = ['username', 'first_name', 'password']

  def get_success_url(self):
    return reverse('staff_list')

  def form_valid(self, form):
    user = form.save(commit=False)
    user.set_password(form.cleaned_data['password'])
    return super().form_valid(form)

class StaffUpdate(PermissionRequiredMixin, UpdateView):
  permission_required = 'auth.change_user'
  model = User
  fields = ['username', 'first_name']

  def get_success_url(self):
    return reverse('staff_list')

class StaffPasswd(PermissionRequiredMixin, UpdateView):
  permission_required = 'auth.change_user'
  model = User
  fields = ['password']

  def get_success_url(self):
    return reverse('staff_list')

  def get_initial(self):
    return {
      'password': '',
    }

  def form_valid(self, form):
    user = form.save(commit=False)
    user.set_password(form.cleaned_data['password'])
    return super().form_valid(form)

