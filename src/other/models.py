from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Ramadan(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'ramadans'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('ramadan-detail', args=[str(self.id)])




class Feature(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'features'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('feature-detail', args=[str(self.id)])

