from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('course_list'), name='home'),  # Redirect to courses
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/<int:pk>/payment/', views.payment_view, name='payment_view'),
    path('courses/payment_success/', views.payment_success, name='payment_success'),
]
