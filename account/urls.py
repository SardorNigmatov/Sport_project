from django.urls import path
from .views import SignUpUserViews

urlpatterns = [
    path('sign-up/', SignUpUserViews.as_view(),name='SignUp'),
]