# views.py
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Count,Max
from .models import Board,Post
from .forms import *

def home(request): #view that returns a list of all the communities (Boards) present in the Website
    boards = Board.objects.all()
    return render(request, 'core/home.html', {'boards':boards})

def board_page_scroll(request, board_name):
    boards = Board.objects.all()
    board = Board.objects.get(name=board_name)
    threads = Post.objects.filter(board=board).order_by('-created_at')

    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.board = board  
            thread.idcookie = request.idcookie  # Get the idcookie from the request's cookies
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
    }

    return render(request, 'core/board_page_scroll.html', context)

def board_page_catalog(request, board_name):
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
            thread.idcookie = request.COOKIES['idcookie']  # Get the idcookie from the request's cookies
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
    }

    return render(request, 'core/board_page_catalog.html', context)

def single_thread(request, board_name ,thread_id):
    boards = Board.objects.all()
    board = Board.objects.get(name=board_name)
    thread = get_object_or_404(Post, id=thread_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.idcookie = request.idcookie 
            post.save()
            return redirect('single_thread', board_name=board_name, thread_id=thread_id)
    else:
        form = PostForm()

    context = {
        'boards': boards,
        'board': board,
        'thread': thread,
        'form': form,
    }
    return render(request,'core/board_page_single.html',context)
