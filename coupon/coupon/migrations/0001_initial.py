# Generated by Django 4.2 on 2023-09-03 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100)),
                ('translatedCategoryName', models.CharField(max_length=100)),
                ('parentPath', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('translatedDescription', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('pageTitle', models.CharField(max_length=100)),
                ('metaDescription', models.CharField(max_length=100)),
                ('metaKeyword', models.CharField(max_length=100)),
                ('mpu', models.CharField(max_length=100)),
                ('cssClass', models.CharField(max_length=100)),
                ('categoryIcon', models.ImageField(blank=True, upload_to='product_image')),
            ],
        ),
    ]
