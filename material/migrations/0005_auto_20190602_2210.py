# Generated by Django 2.1.2 on 2019-06-03 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0004_auto_20190602_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='archivo',
            field=models.FileField(upload_to='material/'),
        ),
    ]
