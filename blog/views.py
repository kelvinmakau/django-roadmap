from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


# Create your views here.

# View posts view
def home(request):
    posts = Post.objects.all() #Get all posts from database
    context = {
        'title': 'Django Developent',
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

# Create post view
@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request,'blog/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            form.save()
            messages.success(request, 'The form has been created successfully')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct errors:')
            return render(request, 'blog/post_form.html', {'form':form})
        

# Edit post view
@login_required
def edit_post(request, id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(Post, pk=id)

    #Show the forms with edit option
    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'id': id}
        return render(request, 'blog/post_form.html', context)
    
    # Handle posting of edited data
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The form has been updated successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Input the data correctly or check for errors')
            return render(request, 'blog/post_form.html', {'form': form})
        
# Deleting a post view
@login_required
def delete_post(request, id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, pk=id)
    post = get_object_or_404(Post, pk=id)

    context = {'post': post}

    if request.method == 'GET':
        return render(request, 'blog/post_confirm_delete.html', context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request, 'The Post has been deleted successfully.')
        return redirect('posts')