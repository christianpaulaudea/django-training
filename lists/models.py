from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)

	def __str__(self):
		return "%s (by %s)" %(self.title, self.author)

class Movie(models.Model):
	genres = [
		(1, "Comedy"),
		(2, "Fantasy"),
		(3, "Action"),
		(4, "Romance"),
		(5, "Adventure"),
		(6, "Mystery"),
		(7, "Horror")
	]

	title = models.CharField(max_length=100)
	genre = models.IntegerField(choices=genres)

	def __str__(self):
		return "%s (%s)" %(self.title, self.get_genre_display())

class Holiday(models.Model):
	occasion = models.CharField(max_length=100)
	date = models.DateField()

	def __str__(self):
		return "%s (%s)" %(self.occasion, self.date)
