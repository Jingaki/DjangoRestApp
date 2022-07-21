# Generated by Django 4.0.4 on 2022-05-31 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('signature', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('fnum', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='QRCodes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=7)),
                ('week', models.IntegerField()),
                ('signature', models.CharField(max_length=16)),
                ('sent', models.BooleanField(null=True)),
                ('fnum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.students')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tyear', models.IntegerField()),
                ('semester', models.CharField(max_length=10)),
                ('test_1_grade', models.FloatField(null=True)),
                ('test_2_grade', models.FloatField(null=True)),
                ('test_3_grade', models.FloatField(null=True)),
                ('final_exam_grade', models.FloatField(null=True)),
                ('project_grade', models.FloatField(null=True)),
                ('attendance1', models.BooleanField(null=True)),
                ('attendance2', models.BooleanField(null=True)),
                ('attendance3', models.BooleanField(null=True)),
                ('attendance4', models.BooleanField(null=True)),
                ('attendance5', models.BooleanField(null=True)),
                ('attendance6', models.BooleanField(null=True)),
                ('attendance7', models.BooleanField(null=True)),
                ('attendance8', models.BooleanField(null=True)),
                ('attendance9', models.BooleanField(null=True)),
                ('attendance10', models.BooleanField(null=True)),
                ('attendance11', models.BooleanField(null=True)),
                ('attendance12', models.BooleanField(null=True)),
                ('attendance13', models.BooleanField(null=True)),
                ('attendance14', models.BooleanField(null=True)),
                ('attendance15', models.BooleanField(null=True)),
                ('fnum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.students')),
                ('signature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('evaluation', models.FloatField(null=True)),
                ('fnum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.students')),
                ('signature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Achieved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achieve_date', models.DateField(null=True)),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.achievements')),
                ('fnum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.students')),
                ('signature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.courses')),
            ],
        ),
        migrations.AddConstraint(
            model_name='enrollments',
            constraint=models.UniqueConstraint(fields=('fnum', 'signature', 'tyear', 'semester'), name='id_enrollments'),
        ),
        migrations.AddConstraint(
            model_name='actions',
            constraint=models.UniqueConstraint(fields=('fnum', 'name', 'signature'), name='id_actions'),
        ),
        migrations.AddConstraint(
            model_name='achieved',
            constraint=models.UniqueConstraint(fields=('fnum', 'signature', 'achievement'), name='id_achieved'),
        ),
    ]