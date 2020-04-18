from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Poetry(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'poetries'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('poetry-detail', args=[str(self.id)])




class Story(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'stories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('story-detail', args=[str(self.id)])



class Novel(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'novels'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('novel-detail', args=[str(self.id)])
