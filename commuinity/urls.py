from django.urls import path
from . import views

urlpatterns = [
    path('courses/<int:course_id>/payment/', views.payment_view, name='payment'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/<int:pk>/payment/', views.payment_view, name='payment_view'),
    path('payment-success/', views.payment_success, name='payment_success'),

]
