from django.contrib import admin

# Register your models here.
from .models import Book

#データベースに登録されているものを表示
admin.site.register(Book)
