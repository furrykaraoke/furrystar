from django.urls import path, re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', views.home, name='home'),
    path('rate/<int:song_id>/', views.rate_song, name='rate_song'),
    path('increment/<int:song_id>/', views.increment_play_count, name='increment_play_count'),
    path('dynamic_search_songs/', views.dynamic_search_songs, name='dynamic_search_songs'),
    path('piosenka/<int:song_id>/', views.piosenka, name='piosenka'),
    path('top-songs/', views.top_songs, name='top_songs'),
    path('dodaj-piosenki/', views.dodaj_piosenki_z_pliku, name='dodaj_piosenki_z_pliku'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('piojs/', views.piosjs, name='piojs'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
