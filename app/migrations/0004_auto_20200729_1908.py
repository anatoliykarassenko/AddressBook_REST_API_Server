# Generated by Django 2.2.14 on 2020-07-29 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200729_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='email',
            name='mailtype',
            field=models.CharField(max_length=4, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='telephone',
            name='telenumber',
            field=models.CharField(max_length=12, verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='telephone',
            name='teletype',
            field=models.CharField(max_length=4, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=6, verbose_name='Gender'),
        ),
    ]
