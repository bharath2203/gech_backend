# Generated by Django 2.1 on 2018-09-16 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('glue', '0002_coremember'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlueBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_no', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('blog_content', models.TextField()),
                ('attendence', models.IntegerField()),
                ('session_date', models.DateField()),
                ('session_time', models.TimeField()),
                ('documenter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Docs', to='glue.CoreMember')),
                ('speakers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='glue.CoreMember')),
            ],
        ),
    ]