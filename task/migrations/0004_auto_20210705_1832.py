# Generated by Django 3.2.5 on 2021-07-05 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0003_alter_task_complete_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('complete_date', models.DateField()),
                ('assign_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assign_to', to=settings.AUTH_USER_MODEL)),
                ('task_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]