# Generated by Django 4.0.4 on 2022-10-31 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolAttendance',
            fields=[
                ('attendance_name', models.CharField(help_text='form-4a-2022-att', max_length=100, primary_key=True, serialize=False)),
                ('class_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Student.madarasa')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('present', 'present'), ('absent', 'absent'), ('sick', 'sick')], default='absent', max_length=30, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('attendance_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Attendance.schoolattendance')),
                ('student_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Student.mwanafunzi')),
            ],
        ),
    ]
