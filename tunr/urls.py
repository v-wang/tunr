from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
  # linking the path that we go to in URL to the view that will be rendered
  path('', views.artist_list, name='artists'),
  # you can determine what variable type it will be
  # it's an integer here (the ID of the artist)
  # same as ('/artist/:id') in express
  path('artists/<int:pk>', views.artist_detail, name='artist_detail'),
  path('artists/<int:pk>/edit', views.artist_edit, name='artist_edit'),
  path('artists/new', views.artist_create, name='artist_create' ),
  path('artists/<int:pk>/delete', views.artist_delete, name='artist_delete'),
  path('songs/', views.song_list, name='song'),
  path('songs/<int:pk>', views.song_detail, name='song_detail'),
  path('songs/<int:pk>/edit', views.song_edit, name='song_edit'),
  path('songs/new', views.song_create, name='song_create'),
  path('songs/<int:pk>/delete', views.song_delete, name='song_delete')
]