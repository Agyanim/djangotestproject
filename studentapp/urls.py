from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("counter",views.counter,name="counter"),
    path("about",views.about,name="about"),
    path("aboutpage",views.aboutpage,name="aboutpage"),
    path("signup",views.signup, name="signup"),
    path('signin',views.signin,name='signin'),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
]