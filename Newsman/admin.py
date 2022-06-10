from unicodedata import category
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


from .models import *

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    # prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'category', 'author', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Предпросмотр"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    fields = ('title',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile)
# admin.site.register(Category, CategoryAdmin)