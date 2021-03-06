# Generated by Django 4.0.2 on 2022-03-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0002_books_cond_books_exptp_books_resalen_books_yearofb'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.CharField(default='Cabc', max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.TextField(default='A1!b')),
                ('password2', models.TextField(default='A1!b')),
                ('phno', models.PositiveBigIntegerField()),
                ('col', models.TextField()),
                ('city', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='b_id',
            field=models.CharField(default='ABC', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='books',
            name='doi',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
