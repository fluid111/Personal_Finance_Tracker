from . import views
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
# from .views import chart_view, category_chart_view

urlpatterns = [
    path('', views.list , name= 'list'),
    # path('chart/', chart_view, name= 'chart_view'),
    path('category-chart/', category_chart_view, name='category_chart_view'),
    path('search/', searchTable, name='searchTable'),
    # path('add/', views.addData , name= 'addData'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', signup, name='signup'),
]