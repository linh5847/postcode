from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostcodeListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostcodeDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostcodeCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostcodeUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostcodeDeleteView.as_view(), name='post_delete'),
]
