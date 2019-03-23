from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path(r'', views.DataEntryView),
    path('Data/<int:Emp>/', views.ViewData, name="Data"),
    path('AdminView/', views.AdminView, name="AdminView"),
    path('export/xls/<fromdate>,<todate>', views.export_users_xls, name='export_users_xls'),
]
