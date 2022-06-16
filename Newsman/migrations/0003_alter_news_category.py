# Generated by Django 4.0.2 on 2022-06-14 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Newsman', '0002_news_author_news_author_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Newsman.category', verbose_name='Категория'),
        ),
    ]
