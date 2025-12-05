from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Board
from django.contrib.auth.models import User
from .models import Topic,Post
from .forms import NewTopicForm

# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})
def about (request):
    return HttpResponse(request)
def board_topics(request,board_id):
    #board = Board.objects.get(pk=board_id)
    board = get_object_or_404(Board,pk=board_id)
    return render(request,'topics.html',{'board':board})
def new_topic(request,board_id):
    board = get_object_or_404(Board,pk=board_id)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                created_by=user,
                topic=topic
            )
            return redirect('board_topics',board_id=board_id)
    else:
        form = NewTopicForm()
    # if request.method == 'POST':
    #     subject = request.POST['subject']
    #     message = request.POST['message']
    #     user = User.objects.first()
    #     topic = Topic.objects.create(
    #         subject = subject,
    #         board = board,
    #         created_by = user
    #     )
    #     post = Post.objects.create(
    #         message = message,
    #         topic = topic,
    #         created_by = user
    #     )
    #     return redirect('board_topics',board_id=board.pk)
    return render(request,'new_topic.html',{'board': board,'form':form})