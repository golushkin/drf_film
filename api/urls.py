from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('user/', views.UserView.as_view(), name='user'),
    path('man/', views.ManView.as_view(), name='man'),
    path('man/<int:pk>/', views.ManDetailView.as_view(), name='man-detail'),
])