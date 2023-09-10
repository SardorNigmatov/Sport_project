from django.urls import path
from .views import (AllYangilikView,DeleteYangilikView,
                    CreatYangilikView,
                    UpdateYangilikView,DetailYangilikView)

from . import views

urlpatterns = [

    path('get_all/', AllYangilikView.as_view()),
    path('get_by_index/<int:yangilik_id>', DetailYangilikView.as_view()),

    path('create/', CreatYangilikView.as_view()),
    path('update/<int:yangilik_id>/', UpdateYangilikView.as_view()),
    path('delete/<int:yangilik_id>/', DeleteYangilikView.as_view()),
]