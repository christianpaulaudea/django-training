from django.shortcuts				import render, redirect, get_object_or_404
from django.contrib.auth.decorators	import login_required
from django.db.models				import Q
from django.utils					import timezone
from .models	import Book, Movie, Holiday
from .forms		import BookForm, MovieForm, HolidayForm


@login_required
def index(request):
	return render(request, 'lists/index.html', {})





def books(request):
	if request.method == "POST":
		key = request.POST["search-key"]
		items = Book.objects.filter(Q(title__contains=key) | Q(author__contains=key)).order_by('title')
	else: items = Book.objects.order_by('title')
	return render(request, 'lists/list.html', dict(title="Books", url="books/", list=items, add_url="new_book", edit_url="edit_book", delete_url="delete_book"))

@login_required
def new_book(request):
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('books')
	else: form = BookForm()
	return render(request, 'lists/form.html', dict(title="New Book", form=form))

@login_required
def edit_book(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == "POST":
		form = BookForm(request.POST, instance=book)
		if form.is_valid():
			form.save()
			return redirect('books')
	else: form = BookForm(instance=book)
	return render(request, 'lists/form.html', dict(title="Edit Book", form=form))

@login_required
def delete_book(request, pk):
	book = get_object_or_404(Book, pk=pk)
	book.delete()
	return redirect('books')





def movies(request):
	if request.method == "POST":
		key = request.POST["search-key"].lower()
		genres = [a[0] for a in Movie.genres if key in a[1].lower()]
		items = Movie.objects.filter(Q(title__contains=key) | Q(genre__in=genres)).order_by('title')
	else: items = Movie.objects.order_by('title')
	return render(request, 'lists/list.html', dict(title="Movies", url="movies/", list=items, add_url="new_movie", edit_url="edit_movie", delete_url="delete_movie"))

@login_required
def new_movie(request):
	if request.method == "POST":
		form = MovieForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('movies')
	else: form = MovieForm()
	return render(request, 'lists/form.html', dict(title="New Movie", form=form))

@login_required
def edit_movie(request, pk):
	movie = get_object_or_404(Movie, pk=pk)
	if request.method == "POST":
		form = MovieForm(request.POST, instance=movie)
		if form.is_valid():
			form.save()
			return redirect('movies')
	else: form = MovieForm(instance=movie)
	return render(request, 'lists/form.html', dict(title="Edit Movie", form=form))

@login_required
def delete_movie(request, pk):
	movie = get_object_or_404(Movie, pk=pk)
	movie.delete()
	return redirect('movies')





def holidays(request):
	if request.method == "POST":
		key = request.POST["search-key"]
		items = Holiday.objects.filter(occasion__contains=key, date__gte=timezone.now()).order_by('date')
	else: items = Holiday.objects.filter(date__gte=timezone.now()).order_by('date')
	return render(request, 'lists/list.html', dict(title="Holidays", url="holidays/", list=items, add_url="new_holiday", edit_url="edit_holiday", delete_url="delete_holiday"))

@login_required
def new_holiday(request):
	if request.method == "POST":
		form = HolidayForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('holidays')
	else: form = HolidayForm()
	return render(request, 'lists/form.html', dict(title="New Holiday", form=form))

@login_required
def edit_holiday(request, pk):
	holiday = get_object_or_404(Holiday, pk=pk)
	if request.method == "POST":
		form = HolidayForm(request.POST, instance=holiday)
		if form.is_valid():
			form.save()
			return redirect('holidays')
	else: form = HolidayForm(instance=holiday)
	return render(request, 'lists/form.html', dict(title="Edit Holiday", form=form))

@login_required
def delete_holiday(request, pk):
	holiday = get_object_or_404(Holiday, pk=pk)
	holiday.delete()
	return redirect('holidays')
