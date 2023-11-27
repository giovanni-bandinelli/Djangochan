# views.py
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Count,Q
from .models import Board,Thread,Post
from .forms import *

def home(request): #view that returns a list of all the communities (Boards) present in the Website
    boards = Board.objects.all()
    return render(request, 'core/home.html', {'boards':boards})

def board_page_scroll(request, board_name):
    boards = Board.objects.all()
    board = Board.objects.get(name=board_name)
    threads = Thread.objects.filter(board=board)

    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.board = board  
            thread.save()
            return redirect('board_page', board_name=board_name)
    else:
        form = ThreadForm()

    context = {
        'boards': boards,
        'board': board,
        'threads': threads,
        'form': form,
    }

    return render(request, 'core/board_page_scroll.html', context)

def board_page_catalog(request, board_name):
    boards = Board.objects.all()
    board = Board.objects.get(name=board_name)
    threads = Thread.objects.filter(board=board).annotate(
        num_replies=Count('post'),
        num_images=Count('post__file_uploaded', distinct=True)
    )

    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.board = board
            thread.save()
            return redirect('board_page', board_name=board_name)
    else:
        form = ThreadForm()

    context = {
        'boards': boards,
        'board': board,
        'threads': threads,
        'form': form,
    }

    return render(request, 'core/board_page_catalog.html', context)

def single_thread(request, board_name ,thread_id):
    boards = Board.objects.all()
    board = Board.objects.get(name=board_name)
    thread = get_object_or_404(Thread, id=thread_id)
    posts = Post.objects.filter(thread=thread)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('single_thread', board_name=board_name, thread_id=thread_id)
    else:
        form = PostForm()

    context = {
        'boards': boards,
        'board': board,
        'thread': thread,
        'posts': posts,
        'form': form,
    }
    return render(request,'core/board_page_single.html',context)