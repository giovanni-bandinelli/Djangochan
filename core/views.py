# views.py
from django.shortcuts import render,redirect
from .models import Board,Thread,Post
from .forms import ThreadForm

def home(request): #view that returns a list of all the communities (Boards) present in the Website
    boards = Board.objects.all()
    return render(request, 'core/home.html', {'boards':boards})

def board_page(request, board_name):
    boards = Board.objects.all()
    board = Board.objects.get(name=board_name)
    threads = Thread.objects.filter(board=board)

    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.board = board  # Assign the current board to the thread
            thread.save()
            return redirect('board_page', board_name=board_name)
    else:
        form = ThreadForm()

    context = {
        'boards': boards,
        'board': board,
        'threads': threads,
        'form': form,
        'form_errors': form.errors,
    }

    return render(request, 'core/default_board_page.html', context)


def single_thread(request, thread_id): #view page with single thread (used for catalog mode)
    thread = Thread.objects.get(id=thread_id)
    posts = Post.objects.get(thread=thread)