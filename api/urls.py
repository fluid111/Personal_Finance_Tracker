from . import views
from django.urls import path

urlpatterns = [
    path('', views.apiOverview , name= 'apiOverview'),
    path('list/', views.userlist , name= 'userlist'),
    path('detail/<str:pk>', views.userdetail , name= 'userdetail'),
    path('create/', views.usercreate , name= 'usercreate'),
    path('update/<str:pk>', views.userupdate , name= 'userupdate'),
    path('delete/<str:pk>', views.userdelete , name= 'userdelete'),
   
    path('datalist/', views.datalist , name= 'datalist'),
    path('datadetail/<str:pk>', views.datadetail , name= 'datadetail'),
    path('datacreate/', views.datacreate , name= 'datacreate'),
    path('dataupdate/<str:pk>', views.dataupdate , name= 'dataupdate'),
    path('datadelete/<str:pk>', views.datadelete , name= 'datadelete'),
]