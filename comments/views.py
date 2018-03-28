from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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