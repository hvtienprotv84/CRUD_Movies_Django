from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('add_movies',views.add_movies,name='add_movies'),
    path('view_movies',views.view_movies,name='view_movies'),
    path('update_movies/<int:id>',views.update_movies,name='update_movies'),
    path('delete_movies/<int:id>',views.delete_movies,name='delete_movies'),
]