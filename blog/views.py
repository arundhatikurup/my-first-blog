
from django.shortcuts import render

from .models import Post

# Create your views here.

def post_list(request):    
    d = {
     'posts': Post.objects.all(),
    }



    return render(request, 'post_list.html', d)
