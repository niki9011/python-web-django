from django.db import models
from petstagram.photos.models import Photo


class Comment(models.Model):
    comment_text = models.TextField(max_length=300, blank=False, null=False)
    # optional
    data_time_of_publication = models.DateField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

