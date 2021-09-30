from django.db import models
from django.utils import timezone
from PIL import Image
from django.conf import settings
# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)
