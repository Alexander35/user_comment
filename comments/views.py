from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewCommentForm

# Create your views here.


@login_required
def main(request):

	# project = Project.objects.get(pk=project_id)

	

	return render(
            request,
            'main.html',
            { 
                'title' : 'Main',
            }
        )

@login_required
def new_comment(request):

	# project = Project.objects.get(pk=project_id)

	new_comment_form = NewCommentForm()

	return render(
            request,
            'new_comment.html',
            { 
                'title' : 'Создать Комент',
                'new_comment_form' : new_comment_form,        
            }
        )	