from django.db import models

# Create your models here.


class Post(models.Model):
   
    title=models.CharField(max_length=500)
    post=models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='img')
    post_created=models.DateTimeField(auto_now_add=True)
    post_updated=models.DateTimeField(auto_now=True)

    class Meta:
       ordering=["post_created"]


    def get_post(self):
        qs=Post.objects.all()
        my_post=[]
        for post in qs:
            my_post.append(post)
        return my_post
