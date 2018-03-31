from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
	path('', RedirectView.as_view(url='view/')),
	path('view/', views.main, name="main"),
	path('comment/', views.new_comment, name="new_comment"),
	path('del_comment/<comment_id>', views.del_comment, name="del_comment"),
	path('stat/', views.regions_stat, name="regions_stat"),
	path('stat/<region_id>/', views.towns_stat, name="towns_stat"),
	path('get_towns_list/', views.get_towns_list, name="get_towns_list"),

]