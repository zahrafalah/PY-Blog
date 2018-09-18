from django.shortcuts import render
from .models import posts
# Create your views here.

def posts_detail_view(request):
    obj = posts.objects.get(id=1)
    # context = {
    #     'Author': obj.author,
    #     'Title': obj.title,
    #     'Text' : obj.bodytext,
    #     'Time' : obj.timestamp,

    # }

    context = {
        'object': obj
    }
    
    return render(request, "posts/detail.html", context)