from django.urls import path
from .views import *

urlpatterns=[
    path('',index_view,name='index'),
    path('home/',home_view,name='home'),
    path('about/',about_view,name='about'),
    path('coach/',coach_view,name='coach'),
    path('time/',time_view,name='time'),
    path('contact/',contact_view,name='contact'),
    path('userpage/',userpage_view,name='userpage'),
    path('course/<int:id>/', courseView, name = 'course')
]
