from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .forms import NewCommentForm
from .models import Comment, Region, Town, CommentStat, DjangoUserComment
from django.http import HttpResponse

# Create your views here.
@login_required
def del_comment(request, comment_id):
	try:	
		comment = Comment.objects.get(pk=comment_id)
		django_user_comment = DjangoUserComment.objects.get(comment=comment)
		if (django_user_comment.user == request.user) or (request.user.is_staff):
			comment.visibility = False
			comment.save()

			dec_stat(comment.region, comment.town)

	except Exception as exc:
		print('Del comment error : {}'.format(exc))	

	return redirect('main')

def get_region_comment_status(region):
	counter = 0
	comment_stats = CommentStat.objects.filter(region=region)
	counter = sum([comment_stat.comment_num for comment_stat in comment_stats])
	return counter

def get_town_comment_status(town):
	counter = 0
	comment_stats = CommentStat.objects.filter(town=town)
	counter = sum([comment_stat.comment_num for comment_stat in comment_stats])
	return counter

@login_required
def get_towns_list(request):
	try:
		if request.method == 'GET':
			town_list = Town.objects.filter(region__id=request.GET['region_id'])
			html = ["<option value='{}'>{}</option>".format(town.id, town.name) for town in town_list]
			return HttpResponse(html, content_type='text/html')

		return HttpResponse('None', content_type='text/html')	
	except Exception as exc:
		print('unable to fetch towns list: {}'.format(exc))
		return HttpResponse('None', content_type='text/html')	

@staff_member_required
def towns_stat(request, region_id):
	try:
		towns = Town.objects.filter(region__id=region_id)
		towns_stats = []
		for town in towns:
			towns_stats.append((town, get_town_comment_status(town)))	

		return render(
            request,
            'towns_stat.html',
            { 
                'title' : 'Статистика Региона',
                'towns_stats'  : towns_stats,
            }
        )		

	except Exception as exc:
		print('towns stats error : {}'.format(exc))

@staff_member_required
def regions_stat(request):

	try:
		regions = Region.objects.all()
		region_stats = []
		region_stats_leaders = []
		for region in regions:
			com_num = get_region_comment_status(region)
			if com_num <=5:
				region_stats.append((region, com_num))
			else:
				region_stats_leaders.append((region, com_num))	

		return render(
            request,
            'regions_stat.html',
            { 
                'title' : 'Статистика',
                'region_stats'  : region_stats,
                'region_stats_leaders' : region_stats_leaders,
            }
        )		

	except Exception as exc:
		print('region stats error : {}'.format(exc))


@login_required
def main(request):

	comments = Comment.objects.filter(visibility=True)
	django_user_comments = DjangoUserComment.objects.all()
	user_comment_nums = [comment.id for comment in django_user_comments if comment.user == request.user ]
	return render(
            request,
            'main.html',
            { 
                'title' : 'Главная',
                'comments'  : comments,
                'user_comment_nums' : user_comment_nums,
            }
        )

def inc_stat(region, town):
	try:
		if not CommentStat.objects.filter(region=region, town=town).exists():
			comment_stat = CommentStat(
				region=region,
				town=town,
				comment_num=1
				)
			comment_stat.save()
		else:
			comment_stat = CommentStat.objects.get(region=region, town=town)
			comment_stat.comment_num += 1	
			comment_stat.save()

	except Exception as exc:
		print('inc_stat error : {}'.format(exc))

def dec_stat(region, town):
	try:
		if CommentStat.objects.filter(region=region, town=town).exists():
			comment_stat = CommentStat.objects.get(region=region, town=town)
			comment_stat.comment_num -= 1	
			if comment_stat.comment_num < 0:
				comment_stat.comment_num = 0
			comment_stat.save()

	except Exception as exc:
		print('inc_stat error : {}'.format(exc))		

@login_required
def new_comment(request):
	# if request.metgod == 

	# request.GET['user_name'] = request.user

	new_comment_form = NewCommentForm()
	new_comment_form.fields['user_name'].initial = request.user.first_name
	new_comment_form.fields['user_family_name'].initial = request.user.last_name
	new_comment_form.fields['email'].initial = request.user.email

	if request.method == 'POST':
		new_comment_form = NewCommentForm(request.POST)
		if new_comment_form.is_valid():
			try:
				try:
					region = Region.objects.get(pk=request.POST['region'])
				except Exception as exc:
					region = None 
				try:	
					town = Town.objects.get(pk=request.POST['town'])
				except Exception as exc:
					town = None	
				comment = Comment(
	    			user_name=request.POST['user_name'],
	    			user_family_name=request.POST['user_family_name'],
	    			email=request.POST['email'],
	    			region=region,
	    			town=town,
	    			patronomic=request.POST['patronomic'],
	    			phone=request.POST['phone'],
	    			comment=request.POST['comment'],
	    			# user = request.user,
	    			visibility = True,
	    			)
				comment.save()
				django_user_comment = DjangoUserComment(
					user = request.user,
					comment = comment,
 					)
				django_user_comment.save()



				inc_stat(region, town)

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