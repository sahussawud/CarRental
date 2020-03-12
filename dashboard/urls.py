
from django.urls import path  
from dashboard import views
  
urlpatterns = [ 
    path('', views.dashboard, name = 'dashboard'),
    path('rent_approve/<int:id_rent>/', views.rent_approve, name='rent_approve'),
    path('rent_deniel/<int:id_rent>/', views.rent_deniel, name='rent_deniel'),
    
]