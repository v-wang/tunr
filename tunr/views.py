from django.shortcuts import render, redirect
from .models import Artist, Song
from .forms import ArtistForm, SongForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# This will determine which template to render
def artist_list(request):
  artists = Artist.objects.all()
  return render(request, 'tunr/artist_list.html', {'artists': artists})

def artist_detail(request, pk):
  artist = Artist.objects.get(id=pk)
  # on request, it will render the artist_detail.html template
  # will render what the response gives (the specific artist object)
  return render(request, 'tunr/artist_detail.html',{'artist': artist})

# Condensing both the GET and POST in one function
# First time, 'else' will catch and an ArtistForm is instantiated
# When user submits, artist_create is called again and 'if' statement catches
# form saves and redirects to the artist that was created by taking it's pk(id) and going to the artist_detail path
@login_required
def artist_create(request):
  if request.method == 'POST':
    form = ArtistForm(request.POST)
    if form.is_valid():
      artist = form.save()
      return redirect('artist_detail', pk=artist.pk)
  else:
    form = ArtistForm()
  return render(request, 'tunr/artist_form.html', {'form': form})

@login_required
def artist_edit(request, pk):
    artist = Artist.objects.get(id=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'tunr/artist_form.html', {'form': form , 'pk': artist.pk})

@login_required
def artist_delete(request, pk):
  Artist.objects.get(id=pk).delete()
  return redirect('artists')


def song_list(request):
  songs = Song.objects.all()
  return render(request, 'tunr/song_list.html', {'songs': songs})

def song_detail(request, pk):
  song = Song.objects.get(id=pk)
  return render(request, 'tunr/song_detail.html', {'song': song})

@login_required
def song_create(request):
  if request.method == 'POST':
    form = SongForm(request.POST)
    if form.is_valid():
      song = form.save()
      return redirect('song_detail', pk=song.pk)
  else:
    form = SongForm()
  return render(request, 'tunr/song_form.html', {'form': form})

@login_required
def song_edit(request, pk):
  song = Song.objects.get(id=pk)
  if request.method == 'POST':
    form = SongForm(request.POST, instance=song)
    if form.is_valid():
      song = form.save()
      return redirect('song_detail', pk=song.pk)
  else:
    form = SongForm(instance=song)
  return render(request, 'tunr/song_form.html', 
    {'form': form ,'pk': song.pk}
  )

@login_required
def song_delete(request, pk):
  Song.objects.get(id=pk).delete()
  return redirect('song')