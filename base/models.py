from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True, default='')
    description = models.CharField(max_length=100)


class Category(models.Model):
    subject = models.CharField(max_length=50)


class Post(models.Model):
	title = models.CharField(max_length=100, unique=True)
	url = models.CharField(max_length= 1000, null=True)
	board = models.ForeignKey(Board, on_delete=models.CASCADE)
	content = models.TextField(max_length=4000)
	category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='posts')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	list_filter = ['title','created_at', 'created_by']


class Subscriber(models.Model):
	email = models.CharField(max_length=100, unique=True)
	pw = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	login_at = models.DateTimeField(null=True)