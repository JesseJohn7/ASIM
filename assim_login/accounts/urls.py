from django.urls import path
from . import views

urlpatterns = [
    path('signup/step1/', views.signup_step1, name='signup_step1'),
    path('signup/step2/', views.signup_step2, name='signup_step2'),
    path('signup/step3/', views.signup_step3, name='signup_step3'),
    path('signup/congratulations/', views.congratulations, name='congratulations'),
    path('logout/', views.logout_view, name='logout'),
]
