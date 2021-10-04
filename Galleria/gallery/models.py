from django.db import models
#ei tarvita varmaa
from PIL import Image
from django.conf import settings
from stdimage import StdImageField, JPEGField
# Create your models here.

class Post(models.Model):
    #Meillä on neljä kuvaa StdImagen avulla yhdesä. Kaikki kuuluu samaan juttun
    image = StdImageField(upload_to='images/', blank=True, variations={
        'large':(800, 600),
        'thumbnail':(300, 300, True),
        'medium':(400,600),}, delete_orphans=True)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

