from django.urls import path
from . import views

# URLS
urlpatterns = [
    path('', views.home, name='posts'),
    path('about/', views.about, name='about'),
    path('post/create/', views.create_post, name='post-create'), # Creating  a post URL
    path('post/edit/<int:id>/', views.edit_post, name='post-edit'), #Editing  a post URL
    path('post/delete/<int:id>', views.delete_post, name='post-delete') #Deleting post  URL
    
]