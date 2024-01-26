from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='test'),
    path('create',views.create_post,name='create'),
    path('create_post_handler',views.create_post_handler)
]
