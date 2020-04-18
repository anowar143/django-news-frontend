from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Cricket(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'crickets'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('cricket-detail', args=[str(self.id)])




class Football(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'footballs'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('football-detail', args=[str(self.id)])



class Tennis(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'tennises'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('tennis-detail', args=[str(self.id)])



class Swimming(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'swimmings'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('swimming-detail', args=[str(self.id)])




class Hockey(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'hockies'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('hockey-detail', args=[str(self.id)])
