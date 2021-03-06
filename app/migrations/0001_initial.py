# Generated by Django 3.2.5 on 2021-08-03 04:56

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
            name='StudentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=15, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('gender', models.CharField(max_length=10, null=True)),
                ('type', models.CharField(max_length=15, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=15, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('gender', models.CharField(max_length=10, null=True)),
                ('company', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=15, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=20)),
                ('image', models.FileField(null=True, upload_to='')),
                ('description', models.CharField(max_length=300)),
                ('experience', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=100)),
                ('creationdate', models.DateField()),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.recruiter')),
            ],
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(null=True, upload_to='')),
                ('applydate', models.DateField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.job')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.studentuser')),
            ],
        ),
    ]
