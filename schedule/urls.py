from django.urls import path
from .views import TaskList,TaskDetail,NewTask


urlpatterns = [

    path('',TaskList.as_view(),name='task_list'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task_detail'),
    path('task/new/',NewTask.as_view(), name='task_new'),

]