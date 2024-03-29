# Generated by Django 4.0.2 on 2023-04-09 20:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(choices=[('Science', 'Science'), ('History', 'History'), ('Religions', 'Religions'), ('Politics', 'Politics'), ('Psychology', 'Psychology'), ('Philosophy', 'Philosophy'), ('Islamic Sciences', 'Islamic Sciences'), ('Personal Growth', 'Personal Growth'), ('Business', 'Business'), ('Technology', 'Technology'), ('Computer Science', 'Computer Science'), ('Software Engineering', 'Software Engineering'), ('Mobile Development', 'Mobile Dev'), ('Web Development', 'Web Dev'), ('Coding Interviews', 'Coding Interviews')], max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book_cover', models.ImageField(blank=True, null=True, upload_to='book_covers/')),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('review_count', models.IntegerField(blank=True, default=0, null=True)),
                ('categories', models.ManyToManyField(blank=True, to='base.Category')),
            ],
            options={
                'verbose_name_plural': 'Summaries',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_premium', models.BooleanField(default=False)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('ended_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='community.profile')),
            ],
        ),
    ]
