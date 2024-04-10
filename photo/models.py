from django.db import models
from django.urls import reverse
from photo.fields import ThumbnailImageField

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('photo:album_detail', args=[self.id])
    

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField('Photo Description', blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/')
    upload_date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    def __str__(self):
        return self.title
