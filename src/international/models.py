from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Subcontinent(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'subcontinents'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('subcontinent-detail', args=[str(self.id)])




class Asia(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'asias'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('asia-detail', args=[str(self.id)])



class MiddleEast(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'middleeasts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('middleeast-detail', args=[str(self.id)])




class UnitedState(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'unitedstates'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('unitedstate-detail', args=[str(self.id)])




class Europe(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'europes'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('europe-detail', args=[str(self.id)])



class InternationalOrganization(models.Model):

    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to='images/', )
    summary = models.TextField(max_length=50000, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        db_table = 'internationalorganizations'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this news."""
        return reverse('internationalorganization-detail', args=[str(self.id)])
