from django.shortcuts import render
from .models import Post

# Create your views here.
 
def post_view(request,):
    post=Post.objects.all()
    my_post=Post.get_post(Post)
    context={ 'my_post':my_post,'post':post}
    return render(request,'post.html',context)
