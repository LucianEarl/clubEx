# Generated by Django 3.0.10 on 2020-11-23 22:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=30)),
                ('videofile', models.FileField(upload_to='videos/', verbose_name='')),
                ('views', models.PositiveIntegerField(default=0)),
                ('length', models.CharField(blank=True, max_length=12)),
                ('likes', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('category', models.ForeignKey(max_length=25, on_delete=django.db.models.deletion.CASCADE, to='clubEx.Category')),
            ],
            options={
                'verbose_name': 'Exercise',
                'verbose_name_plural': 'Exercises',
            },
        ),
        migrations.CreateModel(
            name='UserVidWatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specific_views', models.PositiveIntegerField(default=0)),
                ('joined_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('joined_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubEx.Exercise')),
            ],
        ),
    ]
