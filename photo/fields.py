from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
import os

class ThumbnailImageFieldFile(ImageFieldFile):
    def save(self, name, content, save=True):
        image = super().save(name, content, save)
        img = Image.open(image.path)
        size = (self.field.thumb_width, self.field.thumb_height)
        img.thumbnail(size)
        img.save(image.path)
        return image
    
    def _add_thumb(self):
        img = Image.open(self.path)
        size = (self.field.thumb_width, self.field.thumb_height)
        img.thumbnail(size)
        img.save(self.thumb_path, quality=85)

    @property
    def thumb_path(self):
        return self.path.replace('photos', 'thumbs')
    
    @property
    def thumb_url(self):
        return self.url.replace('photos', 'thumbs')
    
    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.unlink(self.thumb_path)
        super().delete(save)

class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.verbose_name = 'Thumbnail'
        self.help_text = 'Upload a thumbnail image for this photo.'


