from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import UploadForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.

#app/urls viittaa nimet tänne ja miten ne toimii

def display_images(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'gallery/index.html', {'posts' : posts})

@login_required
def image_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.submitter = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('gallery:display_images')
    else:
        form = UploadForm()
    return render(request, 'gallery/upload.html', {'form' : form})


#kuvan poisto form
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/gallery/'
