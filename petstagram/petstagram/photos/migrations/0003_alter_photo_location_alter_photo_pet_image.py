# Generated by Django 4.2.1 on 2023-06-07 17:02

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_rename_date_of_publications_photo_date_of_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='photo',
            name='pet_image',
            field=models.ImageField(upload_to='', validators=[petstagram.photos.validators.image_size_validator_5mb]),
        ),
    ]