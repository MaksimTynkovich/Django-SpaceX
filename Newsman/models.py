from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from slugify import slugify
import datetime
import random

date = datetime.datetime.today()
time = str(date.day) + '-' + str(date.month)

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['-time_create']
        
    def save(self, *args, **kwargs):
        if News.objects.filter(slug=slugify(self.title)).exists():
            self.slug = slugify(self.title) + str(time) + '-' + str(random.randint(0, 999))
            super().save(*args, **kwargs)
        else:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Имя категории")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)