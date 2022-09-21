import base64
from re import template
import re, os
from django.shortcuts import render, get_object_or_404
from .models import Post, Links, AboutUs
from .forms import CommentForm
from pytube import YouTube
from instalooter.looters import PostLooter
from django.contrib import messages
import qrcode
from io import BytesIO


def indexView(request):
    post_list = Post.objects.filter(status=1).order_by("-created_on")
    links = Links.objects.all().first()
    about = AboutUs.objects.all().first()

    return render(
        request,
        "index.html",
        {"post_list": post_list, "links": links, "about":about},
    )


def post_detail(request, slug):
    links = Links.objects.all().first()
    all_post = Post.objects.all()
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(
        request,
        "post_details.html",
        {
            "post": post,
            "links":links,
            "all_post": all_post,
            "comments": comments,
            "new_comments": new_comment,
            "comment_form": comment_form,
        },
    )


def aboutUsView(request):
    about = AboutUs.objects.all().first()
    links = Links.objects.all().first()
    return render(request, "about.html", {"about": about, "links":links})


def qrcodeView(request):
    img = ''
    img_png = BytesIO()
    if request.method == 'POST':
        urlink = request.POST.get("site_link")
        qr = qrcode.QRCode(
            version = 1,
            box_size = 10,
            border = 2
        )

        # adding a link for the qr code to open

        data = urlink
        qr.add_data(data)
        qr.make(fit=True)

        # adding the color
        img = qr.make_image(fill = 'black', back_color = 'white')
        # img.save('qrcodelink.png')
        

        img.save(img_png, kind='PNG')

    return render(request, "bar&qrcode.html", {'img' : base64.b64encode(img_png.getvalue()).decode('utf-8')})


def downloadView(request):
    links = Links.objects.all().first()
    homedir = os.path.expanduser("~")
    dirs = homedir + '/downloads'
    you_length = None
    you_title = None
    you_thumbnail_url = None 
    youHdStream = None
    if request.method == 'GET':
        you_url = request.GET.get('you_url')
        if you_url:
            you_video = YouTube(you_url) 
            you_title = you_video.title
            you_length = you_video.length
            you_thumbnail_url = you_video.thumbnail_url
            youHdStream = you_video.streams.first()    
        return render(request, "download.html", {
            "you_title":you_title,
            "you_length":you_length,
            "thumbnail_url":you_thumbnail_url,
            "hdstream":youHdStream,
            "links":links
        })
        insta_url = request.POST.get('insta_url')
    about = AboutUs.objects.all().first()
    return render(request, "download.html", {})

def youtube(request):
    if request.method == "POST":
        you_url = request.POST.get('you_url')
    

def instagram(request):
    if request.method == "POST":
        insta_url = request.POST.get("insta_url")

def allPost(request):
    post_list = Post.objects.filter(status=1).order_by("-created_on")
    
    links = Links.objects.all().first()

    return render(
        request,
        "posts.html",
        {"post_list": post_list, "links": links},
    )


