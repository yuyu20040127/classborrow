from django.urls import path
from .views import *

urlpatterns = [
    path('', LogList.as_view(), name='log_list'),
    path('checkout/', CheckoutBorrower.as_view(), name='checkout_borrower'), 
    path('checkout/<int:rid>/', CheckoutClassrooms.as_view(), name='checkout_classrooms'), 
    path('checkout/<int:rid>/<int:bid>/', CheckoutLog.as_view(), name='checkout_log'),
    path('return/', ReturnClassrooms.as_view(), name='return_classrooms'), 
    path('return/<int:lid>/', ReturnLog.as_view(), name='return_log'),
]