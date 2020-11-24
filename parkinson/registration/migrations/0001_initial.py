# Generated by Django 3.1.3 on 2020-11-24 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(choices=[('1', 'Mr'), ('2', 'Mrs'), ('3', 'Miss'), ('4', 'Dr'), ('5', 'Prof')], default=('1', 'Mr'), max_length=1)),
                ('Profession', models.CharField(blank=True, max_length=128)),
                ('Academic_Acreditation', models.CharField(blank=True, max_length=128)),
                ('Institution', models.CharField(blank=True, max_length=128)),
                ('Office_Phone', models.CharField(max_length=20, verbose_name='Office Phone')),
                ('Mobile_Phone', models.IntegerField(default=0, verbose_name='Mobile Phone')),
                ('Address', models.CharField(blank=True, max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
