# views.py
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Count,Max
from .models import Board,Post
from .forms import *

def home(request): #view that returns a list of all the communities (Boards) present in the Website
    boards = Board.objects.all()
    return render(request, 'core/home.html', {'boards':boards})

def page404(request, exception):
    return render(request, 'core/error404.html', status=404)

def board_page_scroll(request, board_name):
    user_idcookie = request.COOKIES['idcookie']
    boards = Board.objects.all()
    board = Board.objects.get(name=board_name)
    threads = Post.objects.filter(board=board).order_by('-created_at')

    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.board = board  
            thread.idcookie = user_idcookie  
            content = form.cleaned_data.get('content') # Extract cleaned content, parse it, save it
            content = markdown_parser(content, board_name ,None)
            thread.content = content
            thread.save()
            thread_id = thread.id
            return redirect('single_thread', board_name=board_name, thread_id=thread_id)
    else:
        form = ThreadForm()

    context = {
        'boards': boards,
        'board': board,
        'threads': threads,
        'form': form,
        'user_idcookie': user_idcookie,
    }

    return render(request, 'core/board_page_scroll.html', context)

def board_page_catalog(request, board_name):
    user_idcookie = request.COOKIES['idcookie']
    boards = Board.objects.all()
    board = Board.objects.get(name=board_name)

    order_by = request.GET.get('order_by', 'creation_date')

    order_by_mapping = {
        'last_reply': '-last_reply_date',
        'reply_count': '-num_replies',
    }

    default_order_by = '-created_at'
    selected_order_by = order_by_mapping.get(order_by, default_order_by)

    threads = Post.objects.filter(board=board).annotate(
        num_replies=Count('replies'),
        num_images=Count('replies__file_uploaded', distinct=True),
        last_reply_date=Max('replies__created_at')
    ).order_by(selected_order_by)
    
    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.board = board  
            thread.idcookie = user_idcookie # Get the idcookie from the request's cookies
            content = form.cleaned_data.get('content') # Extract cleaned content, parse it, save it
            content = markdown_parser(content,board_name, None)
            thread.content = content
            thread.save()
            thread_id = thread.id
            return redirect('single_thread', board_name=board_name, thread_id=thread_id)
    else:
        form = ThreadForm()

    context = {
        'boards': boards,
        'board': board,
        'threads': threads,
        'form': form,
        'current_sort': order_by, 
        'user_idcookie': user_idcookie,
    }

    return render(request, 'core/board_page_catalog.html', context)

def single_thread(request, board_name ,thread_id):
    user_idcookie = request.COOKIES['idcookie']
    boards = Board.objects.all()
    board = Board.objects.get(name=board_name)
    thread = get_object_or_404(Post, id=thread_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            user_idcookie = request.COOKIES['idcookie']
            post.idcookie = user_idcookie
            content = form.cleaned_data.get('content') # Extract cleaned content, parse it, save it
            content = markdown_parser(content,board_name, thread_id)
            post.content = content
            post.save()
            return redirect('single_thread', board_name=board_name, thread_id=thread_id)
    else:
        form = PostForm()

    context = {
        'boards': boards,
        'board': board,
        'thread': thread,
        'form': form,
        'user_idcookie': user_idcookie,
    }
    return render(request,'core/board_page_single.html',context)

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.idcookie == post.idcookie:
        post.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
