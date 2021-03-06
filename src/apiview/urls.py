from django.urls import path
from . import views
urlpatterns = [


    path('', views.List_api.as_view(), name='list'),
    path('list-create/', views.List_create.as_view()),
    path('retrive/<str:pk>/', views.Retrive.as_view(), name= 'agent-detail'),
    path('retrive-update/<str:pk>/', views.Retrive_update.as_view()),
    path('retrive-destroy/<str:pk>/', views.Retrive_destroy.as_view()),
    path('retrive-update-destroy/<str:pk>/', views.Retrive_update_destroy.as_view()),
    
]
