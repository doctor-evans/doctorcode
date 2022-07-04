from operator import mod
import profile
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    # meta description is for search engines like google
    meta_description = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to="images", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)


class Links(models.Model):
    twitter = models.URLField(null=True, blank=True, default="")
    facebook = models.URLField(null=True, blank=True, default="")
    youtube = models.URLField(null=True, blank=True, default="")
    instagram = models.URLField(null=True, blank=True, default="")
    linkedin = models.URLField(null=True, blank=True, default="")




class AboutUs(models.Model):
    name = models.CharField(max_length=250, default="Admin")
    title = models.CharField(max_length=250, default="Admin")
    aboutAdmin = models.TextField()
    who_are_we = models.TextField()
    profilePic = models.ImageField(upload_to="images", blank=False)
    email = models.EmailField(default="gainwealth@mail.com")

    def __str__(self):
        return self.name
