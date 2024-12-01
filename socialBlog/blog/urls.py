from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('post/<int:id>/', views.post_details, name = 'post_detail'),
    path('post/new/', views.post_new, name = 'post_new'),
    path('post/<int:id>/edit/', views.post_edit, name = 'post_edit'),
    path('post/<int:id>/delete/', views.post_delete, name = 'post_delete')
    
]
