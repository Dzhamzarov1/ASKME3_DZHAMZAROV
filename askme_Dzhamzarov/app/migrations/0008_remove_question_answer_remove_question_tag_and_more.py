# Generated by Django 5.1.3 on 2024-11-06 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='avatar',
            new_name='user_avatar',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='data_register',
            new_name='user_data_register',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='rating',
            new_name='user_rating',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='name_tag',
        ),
        migrations.CreateModel(
            name='Requestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_text', models.CharField(max_length=255)),
                ('request_date_created', models.DateTimeField(auto_now_add=True)),
                ('request_correct', models.CharField(choices=[('T', 'Correct'), ('N', 'NotCorrect')], max_length=10)),
                ('request_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest_title', models.CharField(max_length=255)),
                ('quest_text', models.CharField(max_length=255)),
                ('quest_date_created', models.DateTimeField(auto_now_add=True)),
                ('quest_rating', models.IntegerField()),
                ('quest_tag', models.ManyToManyField(to='app.tag')),
                ('quest_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
                ('quest_request', models.ManyToManyField(blank=True, null=True, to='app.requestions')),
            ],
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
