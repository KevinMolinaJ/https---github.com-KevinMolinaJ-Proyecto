# Generated by Django 3.2.5 on 2021-07-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laRoja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(null=True, upload_to='noticias'),
        ),
    ]