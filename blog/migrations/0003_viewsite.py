# Generated by Django 4.1.6 on 2023-02-16 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.TextField(max_length=400)),
                ('ip_address', models.TextField(max_length=400)),
            ],
        ),
    ]
