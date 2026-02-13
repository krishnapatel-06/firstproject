from django.urls import path
from clothing import views

urlpatterns = [
    path('', views.home),
    path('shirt/',views.shirt),
    path('jeans/',views.jeans),
    path('tshirt/',views.tshirt),
    path('shoes/',views.shoes)
]