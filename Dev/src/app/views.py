from django.shortcuts import render
from .models import posts
from .forms import PostForm, RawPostForm
# Create your views here.

def post_create_view(request):
    form = RawPostForm()
    if request.method == "POST":
        form = RawPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # we pass ** to pass it as arguments to SAVE DATA
            posts.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "posts/post_create.html", context)


# def post_create_view(request):
#     context = {}
#     return render(request, "posts/post_create.html", context)


# def post_create_view(request):
#     form = PostForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#     context = {
#         'form': form
#     }
#     return render(request, "posts/post_create.html", context)



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