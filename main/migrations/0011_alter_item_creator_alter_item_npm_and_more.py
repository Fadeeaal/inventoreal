# Generated by Django 4.2.5 on 2023-09-12 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_item_npm_alter_item_pbpclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='creator',
            field=models.CharField(default='Rakha Fadil Atmojo', max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='npm',
            field=models.CharField(default='2206082985', max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='pbpclass',
            field=models.CharField(default='PBP C', max_length=255),
        ),
    ]
