from django.urls import path, include
from profile_api import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
routers.register('profile', views.UserProfileModelViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(routers.urls)),
]
