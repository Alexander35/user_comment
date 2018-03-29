from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
	path('', RedirectView.as_view(url='main/')),
	path('main/', views.main, name="main"),
	path('comment/', views.new_comment, name="new_comment"),
	path('del_comment/<comment_id>', views.del_comment, name="del_comment"),

]