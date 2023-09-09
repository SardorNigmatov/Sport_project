from django.urls import path
from .views import ListCoachViews

urlpatterns = [
    path('coach-all/', ListCoachViews.as_view(), name='coach_all')
]
