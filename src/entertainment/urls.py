from django.urls import path
from . import views



urlpatterns = [


    path('movies/', views.MovieListView.as_view(), name='movies'),
    path('movie/<int:pk>', views.MovieDetailView.as_view(), name='movie-detail'),

    path('dramas/', views.DramaListView.as_view(), name='dramas'),
    path('drama/<int:pk>', views.DramaDetailView.as_view(), name='drama-detail'),

    path('musics/', views.MusicListView.as_view(), name='musics'),
    path('music/<int:pk>', views.MusicDetailView.as_view(), name='music-detail'),

]
