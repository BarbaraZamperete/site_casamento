# Generated by Django 5.1.5 on 2025-01-29 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presente',
            name='image_path',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='presente',
            name='imagem',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
