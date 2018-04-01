from django.db import models
from django.contrib.auth.models import User

from .models_dbinspect import Comment, CommentStat, Region, Town

class DjangoUserComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)
	comment = models.ForeignKey('Comment', models.CASCADE, blank=True, null=True)