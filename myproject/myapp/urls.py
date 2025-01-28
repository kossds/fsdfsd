from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-data/', views.get_data, name='get_data'),
    path('post-data/', views.post_data, name='post_data'),
    path('json-data/', views.json_data, name='json_data'),
    path('api/', views.api, name='api'),
]