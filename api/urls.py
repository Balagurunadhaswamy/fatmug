from django.urls import path

from . import views

urlpatterns = [
    path('vendor', views.VendorViewset.as_view()),
]