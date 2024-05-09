from django.urls import path

from . import views

urlpatterns = [
    path('vendor/', views.VendorViewset.as_view()),
    path('vendor/<int:pk>/', views.VendorDetailViewset.as_view()),
    path('purchase_order/', views.PurchaseOrderTrackingViewset.as_view()),
    path('purchase_order/<int:pk>/', views.PurchaseOrderDetailViewset.as_view()),
    path('vendors/<int:pk>/performance', views.VendorPerformanvceViewset.as_view()),
]