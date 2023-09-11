from django.urls import path
from .views import CoachListViews ,CoachCreateViews, CoachUpdateViews , CoachDeleteViews

urlpatterns = [
    path('coach-all/', CoachListViews.as_view(), name='coach_all'),
    path('coach-create/', CoachCreateViews.as_view(), name='coach_create'),
    path('coach-update/<int:pk>', CoachUpdateViews.as_view(), name='coach_update'),
    path('coach-delete/<int:pk>', CoachDeleteViews.as_view(), name='coach_delete'),
]
