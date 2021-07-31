from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('post/api_view/', views.APIViewPostList.as_view()),
    path('post/api_view/<int:pk>/', views.APIViewPostDetail.as_view()),

    path('post/mixin/', views.MixinPostList.as_view()),
    path('post/mixin/<int:pk>/', views.MixinPostDetail.as_view()),

    path('post/generics/', views.GenericPostList.as_view()),
    path('post/generics/<int:pk>/', views.GenericPostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)