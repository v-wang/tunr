from django import forms
from .models import Artist, Song

# Creating a form that follows the Artist model
# The fields will capture name, photo_url and nationality
# Not adding ID because that's going to be created when we add a new artist
class ArtistForm(forms.ModelForm):
  class Meta:
    model = Artist
    # fields will determine what shows up on the form
    fields = ('name', 'photo_url', 
    'nationality')

class SongForm(forms.ModelForm):
  class Meta:
    model = Song
    fields = ('title', 'artist', 'album', 'preview_url')