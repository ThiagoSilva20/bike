# Generated by Django 4.0.4 on 2022-05-23 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo',
            name='value',
            field=models.FloatField(default=0.0, verbose_name='value'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='marca',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='image',
            field=models.URLField(default='', verbose_name='URL for image'),
        ),
    ]
