from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('title',)
    list_filter = ('title',)
    search_fields = ('title', 'description')
    ordering = ('title',)

@admin.register(Pasport_book)
class PassportBookAdmin(admin.ModelAdmin):
    list_display = ('article', 'features', 'book')
    list_display_links = ('article',)
    list_filter = ('article', 'features')
    search_fields = ('article', 'features')
    ordering = ('article',)

@admin.register(Publishing_house)
class Publishing_houseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'agent_name', 'agent_secondname', 'agent_surname', 'telephone')
    list_display_links = ('title',)
    list_filter = ('title', 'agent_name')
    search_fields = ('title', 'agent_name', 'agent_secondname', 'agent_surname', 'telephone')
    ordering = ('title',)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'exists', 'publisher', 'author')
    list_display_links = ('name',)
    search_fields = ('name', 'price', 'publisher__title', 'author__name_author')
    list_editable = ('price', 'exists')
    list_filter = ('exists', 'publisher', 'author')
    ordering = ('name', '-price')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_author', 'second_name', 'author_surname')
    list_display_links = ('name_author',)
    list_filter = ('name_author', 'second_name')
    search_fields = ('name_author', 'second_name', 'author_surname')
    ordering = ('name_author',)
