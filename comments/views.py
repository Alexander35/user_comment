from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewCommentForm
from .models import Comment, Region, Town

# Create your views here.
@login_required
def del_comment(request, comment_id):
	try:	
		comment = Comment.objects.get(pk=comment_id)
		if (comment.user == request.user) or (request.user.is_staff):
			comment.visibility = False
			comment.save()
	except Exception as exc:
		print('Del comment error : {}'.format(exc))	

	return redirect('main')


@login_required
def main(request):

	comments = Comment.objects.filter(visibility=True)

	return render(
            request,
            'main.html',
            { 
                'title' : 'Main',
                'comments'  : comments,
            }
        )

@login_required
def new_comment(request):

	new_comment_form = NewCommentForm()

	if request.method == 'POST':
		new_comment_form = NewCommentForm(request.POST)
		if new_comment_form.is_valid():
			try:
				region = Region.objects.get(pk=request.POST['region'])
				town = Town.objects.get(pk=request.POST['town'])
				comment = Comment(
	    			user_name=request.POST['user_name'],
	    			user_family_name=request.POST['user_family_name'],
	    			email=request.POST['email'],
	    			region=region,
	    			town=town,
	    			patronomic=request.POST['patronomic'],
	    			phone=request.POST['phone'],
	    			comment=request.POST['comment'],
	    			user = request.user,
	    			)
				comment.save()
				return redirect('main')
			except Exception as exc:
				new_comment_form.add_error(None, exc)
				print('Save comment error : {}'.format(exc))			

	return render(
            request,
            'new_comment.html',
            { 
                'title' : 'Создать Комент',
                'new_comment_form' : new_comment_form,        
            }
        )	