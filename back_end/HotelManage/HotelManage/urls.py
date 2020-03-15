from django.contrib import admin
from django.urls import path
from ManageApp import index, post_test, get_test

urlpatterns = [
    path('', index.index),
    path('admin/', admin.site.urls),
    path('post/', post_test.post_test),
    path('get/', get_test.get_test),
]
