# views.py
from django.shortcuts import render
from .models import Board,Thread,Post

def home(request): #view that returns a list of all the communities (Boards) present in the Website
    boards = Board.objects.all()
    return render(request, 'core/home.html', {'boards':boards})

def board_page(request, board_name): #view to access a boards's content
    board = Board.objects.get(name=board_name)
    threads = Thread.objects.filter(board=board)
    context = {
        'board': board,
        'threads': threads,
    }
    return render(request, 'core/board_page.html', context)

def single_thread(request, thread_id): #view page with single thread (used for catalog mode)
    thread = Thread.objects.get(id=thread_id)
    posts = Post.objects.get(thread=thread)


