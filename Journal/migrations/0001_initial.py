# Generated by Django 4.0.4 on 2022-10-31 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Student', '0001_initial'),
        ('Subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolJournal',
            fields=[
                ('journal_name', models.CharField(help_text='journal4a-t1-2021', max_length=200, primary_key=True, serialize=False)),
                ('class_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Student.madarasa')),
                ('class_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredJournal1',
            fields=[
                ('journal_id', models.CharField(help_text='journ-4a-2022-07-12', max_length=40, primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('day', models.CharField(help_text='monday', max_length=10)),
                ('journal_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Journal.schooljournal')),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredJournal',
            fields=[
                ('journal_id', models.CharField(help_text='journ-4a-2022-07-12', max_length=40, primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('day', models.CharField(help_text='monday', max_length=10)),
                ('journal_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Journal.schooljournal')),
            ],
        ),
        migrations.CreateModel(
            name='JournalDailyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_period_taught', models.CharField(max_length=200)),
                ('number_periods_nottaught', models.CharField(max_length=200)),
                ('reason_nottaught', models.CharField(blank=True, max_length=200, null=True)),
                ('cl_comment', models.CharField(blank=True, max_length=200, null=True)),
                ('ct_comment', models.CharField(blank=True, max_length=200, null=True)),
                ('am_comment', models.CharField(blank=True, max_length=200, null=True)),
                ('hs_comment', models.CharField(blank=True, max_length=200, null=True)),
                ('class_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('j_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Journal.registeredjournal1')),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(blank=True, choices=[('session1', '8:00-8:40'), ('session2', '8:40-9:20'), ('session3', '9:20-10:0'), ('session4', '10:00-10:40'), ('session5', '10:40-11:20'), ('session6', '11:40-12:20'), ('session7', '12:20-01:00'), ('session8', '01:00-01:40'), ('session9', '01:40-02:20'), ('session10', '03:00-04:00')], default='8:00-8:40', max_length=20)),
                ('period', models.CharField(blank=True, help_text='1,2,3...', max_length=2, null=True)),
                ('concept_covered', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_teachers_comment', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_teachers_name', models.CharField(blank=True, max_length=200, null=True)),
                ('class_leaders_comment', models.CharField(blank=True, max_length=200, null=True)),
                ('class_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('j_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Journal.registeredjournal1')),
                ('subject_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Subjects.masomo')),
            ],
        ),
    ]
