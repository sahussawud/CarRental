
from django.urls import path  
from detail import views
  
urlpatterns = [ 
    path('<int:id_car>/', views.detail, name = 'detail'),
    path('<int:id_car>/booking/', views.booking, name = 'booking'),
    path('confirm/<int:id_rent>/', views.confirm, name = 'confirm'),
    path('reservation/', views.reservation_list, name='reservation_list'),
    
] 
