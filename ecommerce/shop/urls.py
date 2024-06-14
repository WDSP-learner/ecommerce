from django.urls import path 
from . import views


app_name = 'shop'

urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.productlist,name='productlist')
]