# Generated by Django 3.2.6 on 2021-08-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saveTextApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_title',
            field=models.CharField(max_length=150),
        ),
    ]
