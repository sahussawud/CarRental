from django.urls import include, path
from homepage import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admin/managecar/car/add/', views.add_edit_car, name='add_edit_car'),
    path('admin/managecar/car/<int:id_car>/change/', views.change_car, name='change_car'),
    path('car_detail/<int:id_car>', views.car_detail, name='car_detail')

]
