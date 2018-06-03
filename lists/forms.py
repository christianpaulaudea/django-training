from django import forms
from .models import Book, Movie, Holiday


class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('title', 'author')

class MovieForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = ('title', 'genre')

class HolidayForm(forms.ModelForm):
	class Meta:
		model = Holiday
		fields = ('occasion', 'date')
