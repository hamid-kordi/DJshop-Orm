from typing import Iterable
from django.db import models
import hashlib


# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(width_field=10, height_field=10, upload_to="images/")
    width = models.IntegerField(editable=False)
    height = models.IntegerField(editable=False)

    file_hash = models.CharField(max_length=40, db_index=True, editable=False)
    fiel_size = models.PositiveIntegerField(null=True, editable=False)

    focal_point_x = models.PositiveIntegerField(null=True, blank=True)
    focal_point_y = models.PositiveIntegerField(null=True, blank=True)
    focal_point_width = models.PositiveIntegerField(null=True, blank=True)
    focal_point_height = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.image.file.closed:
            self.file_size = self.image.size

            hasher = hashlib.sha1()
            for chunk in self.image.file.chunks():
                hasher.update(chunk)

            self.file_hash = hasher.hexdigest()
        super().save(*args, **kwargs)
