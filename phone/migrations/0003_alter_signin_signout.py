# Generated by Django 4.0.2 on 2022-02-28 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0002_signin_signedin_alter_signin_signout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='signout',
            field=models.DateField(null=True),
        ),
    ]
