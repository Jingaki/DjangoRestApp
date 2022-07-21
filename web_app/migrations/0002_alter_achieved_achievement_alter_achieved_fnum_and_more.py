# Generated by Django 4.0.4 on 2022-06-01 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achieved',
            name='achievement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achieved', to='web_app.achievements'),
        ),
        migrations.AlterField(
            model_name='achieved',
            name='fnum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achieved', to='web_app.students'),
        ),
        migrations.AlterField(
            model_name='achieved',
            name='signature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achieved', to='web_app.courses'),
        ),
        migrations.AlterField(
            model_name='actions',
            name='fnum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='web_app.students'),
        ),
        migrations.AlterField(
            model_name='actions',
            name='signature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='web_app.courses'),
        ),
        migrations.AlterField(
            model_name='enrollments',
            name='fnum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='web_app.students'),
        ),
        migrations.AlterField(
            model_name='enrollments',
            name='signature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='web_app.courses'),
        ),
        migrations.AlterField(
            model_name='qrcodes',
            name='fnum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qrcodes', to='web_app.students'),
        ),
    ]