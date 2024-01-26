from django.shortcuts import render,redirect
from django.contrib import messages
from . models import Post

# Create your views here.
def index(request):
    return render(request,'post/index.html')

def create_post(request):
    return render(request,'post/createpost.html')


def create_post_handler(request):
    title=request.POST['title']
    print(title)
    description=request.POST['description']
    if (len(title)==0):
        messages.info(request,'title field cannot be empy')
        return redirect('create')
    elif (len(description)==0):
        messages.info(request,'description field cannot be empy')
        return redirect('create')
    else:
        post=Post.objects.create(title=title,description=description)
        post.save()
        return redirect('create')
    
