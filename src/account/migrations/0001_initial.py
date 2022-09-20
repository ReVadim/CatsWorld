# Generated by Django 4.1 on 2022-09-18 18:46

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import src.base.services


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatsOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_activated', models.BooleanField(db_index=True, default=True, verbose_name='is activated?')),
                ('send_message', models.BooleanField(default=True, verbose_name='send messages?')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True, verbose_name='country')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='city')),
                ('about', models.TextField(blank=True, max_length=2000, null=True)),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, max_length=30, null=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=src.base.services.get_path_upload_avatar, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg']), src.base.services.validate_size_image], verbose_name='avatar')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
