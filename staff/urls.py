from django.urls import path
from .views import *

urlpatterns = [
    path('', StaffList.as_view(), name='staff_list'),
    path('add/', StaffAdd.as_view(), name='staff_add'),
    path('<int:pk>/update/', StaffUpdate.as_view(), name='staff_update'),
    path('<int:pk>/passwd/', StaffPasswd.as_view(), name='staff_passwd'),
]