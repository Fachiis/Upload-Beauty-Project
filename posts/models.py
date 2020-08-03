from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None)

    def __str__(self):
        return self.title



