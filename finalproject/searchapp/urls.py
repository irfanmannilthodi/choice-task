from django.urls import path
from. import views

app_name='searchapp'
urlpatterns=[
    path('',views.search,name='search'),
    path('search1',views.search1,name='search1'),
    path('search2', views.search2, name='search2'),
]