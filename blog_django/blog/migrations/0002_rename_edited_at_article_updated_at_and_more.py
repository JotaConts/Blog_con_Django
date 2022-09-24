# Generated by Django 4.0.6 on 2022-08-23 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='edited_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.category', verbose_name='Categorías'),
        ),
    ]
