# Generated by Django 2.1.2 on 2019-06-03 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0003_document_archivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='archivo',
            field=models.FileField(blank=True, upload_to='material/'),
        ),
    ]
