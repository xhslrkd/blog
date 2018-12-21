from django.contrib import admin
from .models import Board, Category, Post



class PostAdmin(admin.ModelAdmin):
	model = Post
	list_display = ['title', 'board_name', 'created_at', ]
	def board_name(self, obj):
		return obj.board.name

class BoardAdmin(admin.ModelAdmin):
	model = Board
	list_display = ['name', 'description']
	def get_name(self, obj):
		return obj.name
class CategoryAdmin(admin.ModelAdmin):
	model = Category
	list_display = ['subject']
	def get_name(self, obj):
		return obj.subject
	
admin.site.register(Board, BoardAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)