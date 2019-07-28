# Generated by Django 2.2.3 on 2019-07-28 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='name')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('draft', 'draft')], db_index=True, default='draft', max_length=16, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('title', models.CharField(max_length=1024, verbose_name='title')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('content', models.TextField(verbose_name='content')),
                ('published', models.DateTimeField(db_index=True, verbose_name='published')),
                ('tags', models.ManyToManyField(blank=True, to='posts.Tag')),
            ],
            options={
                'ordering': ('published', 'id'),
            },
        ),
    ]
