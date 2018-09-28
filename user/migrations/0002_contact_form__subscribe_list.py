# Generated by Django 2.1.1 on 2018-09-28 12:28

from django.db import migrations, models
import django.utils.timezone
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('message', models.TextField(verbose_name='message')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='SubscribeList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('token', models.CharField(default=user.models.gen_user_token, max_length=20, verbose_name='token')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('invited', models.BooleanField(default=False, verbose_name='invited')),
            ],
            options={
                'verbose_name_plural': 'Android wait list',
            },
        ),
        migrations.AlterUniqueTogether(
            name='subscribelist',
            unique_together={('email', 'token')},
        ),
    ]
