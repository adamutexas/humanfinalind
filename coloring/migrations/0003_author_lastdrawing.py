# Generated by Django 3.1.5 on 2022-04-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coloring', '0002_drawingmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='lastDrawing',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]