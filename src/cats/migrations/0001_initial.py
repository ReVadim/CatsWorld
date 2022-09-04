# Generated by Django 4.1 on 2022-09-03 06:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import src.base.services


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('birthday', models.DateField()),
                ('color', models.CharField(max_length=150, verbose_name='color')),
                ('temperament', models.CharField(blank=True, max_length=35, null=True, verbose_name='temperament')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='description')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=src.base.services.get_path_upload_photo, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg']), src.base.services.validate_size_image], verbose_name='avatar')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'pet',
                'verbose_name_plural': 'pets',
            },
        ),
    ]
