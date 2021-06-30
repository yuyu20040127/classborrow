from django.urls import path
from .views import *

urlpatterns = [
    path('', ClassroomsList.as_view(), name='classrooms_list'),
    path('add/', ClassroomsAdd.as_view(), name= 'classrooms_add'),
    path('<int:pk>/', ClassroomsView.as_view(), name='classrooms_view'),
    path('<int:pk>/edit/', ClassroomsEdit.as_view(), name='classrooms_edit'),
    path('<int:pk>/delete/', ClassroomsDelete.as_view(), name='classrooms_delete'),
]
