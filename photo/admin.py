from django.contrib import admin
from .models import Album, Photo

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1

# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_per_page = 25

admin.site.register(Album, AlbumAdmin)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'album','upload_date')
    search_fields = ('title', 'album__name')
    list_per_page = 25

admin.site.register(Photo, PhotoAdmin)

