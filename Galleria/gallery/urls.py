from django.urls import path
from . views import *

#path(request osa ja url, nimi jolla me viitataan views.pyssä, viitataan html/views?)
#gallery:functio sivuun johon haluaan
app_name = 'gallery'
urlpatterns = [
    #index
    path('', display_images, name = 'display_images'),
    #upload sivu
    path('image_upload', image_upload, name = 'image_upload'),
    #Delete id perusteella
    path('<pk>/delete/', PostDeleteView.as_view()),
]
