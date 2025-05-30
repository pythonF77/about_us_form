from django.contrib import admin
from .models import author,Genre,Post
# Register your models here.
admin.site.register(author)
admin.site.register(Genre)
admin.site.register(Post)