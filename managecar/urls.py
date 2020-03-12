
from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from managecar import views
  
urlpatterns = [ 
    # path('image_upload', views.image_upload, name = 'image_upload'), 
    # path('success', views.success, name = 'success'), 
    path('car-hidden/<int:id_car>/', views.car_hide, name='car_hide'),
    path('car-unhidden/<int:id_car>/', views.car_unhide, name='car_unhide'),
    path('home-car-hidden/<int:id_car>/', views.home_car_hide, name='home_car_hide'),
    path('available/<int:id_rent>/', views.available, name='available'),
    path('notavailable/<int:id_rent>/', views.notavailable, name='notavailable'),

    path('', views.car_dashboard, name='car_dashboard'),


] 
  
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 