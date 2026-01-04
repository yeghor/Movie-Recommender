from django.contrib import admin
from .models import HistorySearchFilm, FilmSearches

# Register your models here.

admin.site.register(HistorySearchFilm)
admin.site.register(FilmSearches)
