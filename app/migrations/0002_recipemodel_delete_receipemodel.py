# Generated by Django 5.0.6 on 2024-06-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='recipeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='app')),
            ],
            options={
                'db_table': 'recipe',
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='ReceipeModel',
        ),
    ]