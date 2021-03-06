# Generated by Django 2.1 on 2018-08-23 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(choices=[('CS', 'COMPUTER SCIENCE & ENGG'), ('ENC', 'ELECTRONICS AND COMMUNICATION & ENGG'), ('CV', 'CIVIL ENGG'), ('ME', 'MECHANICAL ENGG')], max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='notification',
            name='type',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ug_program',
        ),
        migrations.AddField(
            model_name='department',
            name='notifications',
            field=models.ManyToManyField(to='student.Notification'),
        ),
        migrations.AddField(
            model_name='department',
            name='students',
            field=models.ManyToManyField(to='student.Student'),
        ),
        migrations.AddField(
            model_name='notification',
            name='belongs_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Department'),
        ),
        migrations.AddField(
            model_name='student',
            name='department_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Department'),
        ),
    ]
