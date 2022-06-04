from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Search/', views.Search, name='Search'),
    path('Add_Contract/', views.Add_Contract, name='Add_Contract'),
    path('Details/<int:details_id>', views.Details, name='Details'),
    path('Update/<int:details_id>', views.Update, name='Update'),
    path('Delete/<int:details_id>', views.Delete, name='Delete'),
    path('csv_File/', views.csv_File, name='csv_File'),
    path('TextFile/', views.TextFile, name='TextFile'),
]