from django.db.models import Avg
from django.shortcuts import render, get_object_or_404, redirect
from .models import Song, Rating
from .forms import RatingForm, DodajPiosenkiForm
from django.http import JsonResponse
from .decorators import admin_required
#import json
#from django.core import serializers

def home(request):
    #paginacja
    songs = Song.objects.prefetch_related('ratings').annotate(avarage_rating=Avg('ratings__value'))[:30]

    return render(request, 's_home.html', {'songs': songs})


def piosenka(request, song_id):
    songs = Song.objects.filter(pk=song_id).prefetch_related('ratings').annotate(avarage_rating=Avg('ratings__value')).first()
    return render(request, 's_single.html', {'song': songs, 'ratings': songs.ratings.all()})


def rate_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            rating_value = form.cleaned_data['rating']
            nick_value = form.cleaned_data['nick']
            Rating.objects.create(song=song, value=rating_value, nick=nick_value)
            song.play_count += 1
            song.save(update_fields=['play_count'])

            return redirect('piosenka', song_id)
    else:
        form = RatingForm()

    return render(request, 'rate_song.html', {'form': form, 'song': song})


def increment_play_count(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    song.play_count += 1
    song.save(update_fields=['play_count'])
    return JsonResponse({'message': 'Licznik odtworzeń został zwiększony'})


def dynamic_search_songs(request):
    query = request.GET.get('query', '')
    songs = list(Song.objects.filter(title__icontains=query).values('id', 'title')[:10])
    return JsonResponse({'results': songs})

def top_songs(request):
    # Pobierz 10 piosenek o największej liczbie odtworzeń (play_count)
    top_songs = Song.objects.filter(play_count__gt=0).order_by('-play_count')[:20]

    context = {'top_songs': top_songs}
    return render(request, 'top_songs.html', context)

@admin_required
#def dodaj_piosenki_z_pliku(request):
#    if request.method == 'POST':
#        form = DodajPiosenkiForm(request.POST, request.FILES)
#        if form.is_valid():
#            plik_tekstowy = form.cleaned_data['plik_tekstowy']
#            # Odczytaj zawartość pliku i podziel na linie
#            linie = plik_tekstowy.read().decode().splitlines()

            # Dodaj każdą piosenkę do bazy danych
#           for linia in linie:
#                nazwa_utworu = linia.strip()  # Pobierz nazwę utworu z linii
#                # Sprawdź, czy piosenka o danej nazwie już istnieje w bazie
#                if not Song.objects.filter(title=nazwa_utworu).exists():
#                    song = Song(title=nazwa_utworu)
#                    song.save()

#            return redirect('home')  # Przekieruj użytkownika na stronę główną lub inaczej

#    else:
#        form = DodajPiosenkiForm()
#
#    return render(request, 'dodaj_piosenki.html', {'form': form})

def dodaj_piosenki_z_pliku(request):
    if request.method == 'POST':
        form = DodajPiosenkiForm(request.POST, request.FILES)
        if form.is_valid():
            plik_tekstowy = form.cleaned_data['plik_tekstowy']
            kategoria = form.cleaned_data['jezyk']  # Pobierz kategorię z formularza
            linie = plik_tekstowy.read().decode().splitlines()

            for linia in linie:
                nazwa_utworu = linia.strip()
                if not Song.objects.filter(title=nazwa_utworu).exists():
                    song = Song(title=nazwa_utworu, jezyk=kategoria)  # Przypisz kategorię do utworu
                    song.save()

            return redirect('home')

    else:
        form = DodajPiosenkiForm()

    return render(request, 'dodaj_piosenki.html', {'form': form})
def piosjs(request):
    songs_json = Song.objects.all().order_by('title')
    for song in songs_json:
        ratings = Rating.objects.filter(song=song)
        total_rating = sum([rating.value for rating in ratings]) if ratings else 0
        average_rating = total_rating / len(ratings) if ratings else 0
        song.rating = int(average_rating)
#    lista_piosenek = [item for item in serializers.serialize('python', songs_json)]
#    json_string = json.dumps(lista_piosenek)
    piosenki_list = [{'id': p.id, 'tytul': p.title, 'play_count':p.play_count, 'rating':p.rating, 'jezyk':p.jezyk } for p in songs_json]
#    piosenki_list = piosenki_list.replace("[","")
#    piosenki_list = piosenki_list.replace("]","")
    response_data = {'rows': piosenki_list}
    return JsonResponse(response_data, safe=False)
