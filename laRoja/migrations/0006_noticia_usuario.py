# Generated by Django 3.2.5 on 2021-07-15 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laRoja', '0005_noticia_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='usuario',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
