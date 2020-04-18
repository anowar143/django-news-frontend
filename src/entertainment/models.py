from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Movie(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'movies'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('movie-detail', args=[str(self.id)])




class Drama(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'dramas'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('drama-detail', args=[str(self.id)])



class Music(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'musics'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('music-detail', args=[str(self.id)])
