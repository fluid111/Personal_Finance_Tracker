from . import views
from django.urls import path
from .views import *
# from .views import chart_view, category_chart_view

urlpatterns = [
    path('', views.list , name= 'list'),
    # path('chart/', chart_view, name= 'chart_view'),
    path('category-chart/', category_chart_view, name='category_chart_view'),
    path('search/', searchTable, name='searchTable')
    # path('add/', views.addData , name= 'addData'),
]