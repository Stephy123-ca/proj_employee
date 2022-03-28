# Generated by Django 4.0.2 on 2022-03-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0003_book_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_name', models.CharField(max_length=120, unique=True)),
                ('Email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('photo', models.ImageField(null=True, upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]