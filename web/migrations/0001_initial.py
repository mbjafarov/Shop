# Generated by Django 3.2.8 on 2021-10-28 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('group', models.CharField(choices=[('smartphone', 'smartphone'), ('pc', 'pc'), ('accessories', 'accessories'), ('laptop', 'laptop')], default='smartphone', max_length=20)),
                ('img', models.ImageField(default='no_image.jpg', upload_to='product_image')),
            ],
        ),
    ]