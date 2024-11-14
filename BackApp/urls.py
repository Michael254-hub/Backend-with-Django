from django.urls import path

from BackApp import views

urlpatterns[

    path('',views.blog_list,name='blog_list'),

    path('<int;id>',views.blog_details,name='blog_details'),
]