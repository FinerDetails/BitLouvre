from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)

    #alla oleva koodi on tutoriaalista ja tutkinnan alla, etta olisko hyöty siita
    #def publish(self):
        #self.published_date = timezone.now()
        #self.save()
