# Generated by Django 4.0 on 2021-12-26 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_image_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser'),
        ),
    ]
