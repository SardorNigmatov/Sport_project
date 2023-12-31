from django.urls import path
from .views import (AllYangilikView,
                    DeleteYangilikView,
                    CreatYangilikView,
                    UpdateYangilikView,
                    DetailYangilikView,
                    CoachListViews,
                    CoachDeleteViews,
                    CoachCreateViews,
                    CoachUpdateViews,
                    GymsListView,
                    GymsCreateView,
                    GymsDeleteView,
                    GymsDetailView,
                    GymsUpdateView,
                    )

urlpatterns = [
    path('get_all/', AllYangilikView.as_view()),
    path('get_by_index/<int:yangilik_id>', DetailYangilikView.as_view()),
    path('create/', CreatYangilikView.as_view()),
    path('update/<int:yangilik_id>/', UpdateYangilikView.as_view()),
    path('delete/<int:yangilik_id>/', DeleteYangilikView.as_view()),
    path('coach-all/', CoachListViews.as_view(), name='coach_all'),
    path('coach-create/',CoachCreateViews.as_view(),name='coach-create'),
    path('coach-delete/',CoachDeleteViews.as_view(),name='coach-delete'),
    path('coach-update/',CoachUpdateViews.as_view(),name='coach-update'),
    path('gyms-all/',GymsListView.as_view(),name='gyms-all'),
    path('gyms/detail/<int:pk>/',GymsDetailView.as_view(),name='detail'),
    path('gyms/delete/<int:pk>/',GymsDeleteView.as_view(),name='delete'),
    path('gyms/create/',GymsCreateView.as_view(),name='create'),
    path('gyms/update/<int:pk>/',GymsUpdateView.as_view(),name='update'),
]
