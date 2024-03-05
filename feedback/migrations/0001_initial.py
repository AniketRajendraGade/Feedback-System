# Generated by Django 4.1.3 on 2024-03-02 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=50)),
                ('Phone_number', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Visit_First_Time', models.BooleanField(default=False)),
                ('Food_You_liked', models.CharField(max_length=20)),
                ('Time_slot', models.CharField(max_length=20)),
                ('Upload_Photo', models.ImageField(upload_to='img/')),
            ],
        ),
    ]