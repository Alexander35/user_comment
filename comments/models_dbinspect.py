# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Comment(models.Model):
    user_name = models.CharField(max_length=100, blank=True, null=True)
    user_family_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region', blank=True, null=True)
    town = models.ForeignKey('Town', models.DO_NOTHING, db_column='town', blank=True, null=True)
    patronomic = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    visibility = models.NullBooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'comment'

    def __str__(self):
        return '{} :: {} :: {}'.format(self.comment, self.user_name, self.created_at)        


class CommentStat(models.Model):
    region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region', blank=True, null=True)
    town = models.ForeignKey('Town', models.DO_NOTHING, db_column='town', blank=True, null=True)
    comment_num = models.IntegerField()
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'comment_stat'

    def __str__(self):
        return '{}'.format(self.name)       


class Region(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'region'

    def __str__(self):
        return '{}'.format(self.name)           


class Town(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    region = models.ForeignKey(Region, models.DO_NOTHING, db_column='region', blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'town'

    def __str__(self):
        return '{}'.format(self.name)