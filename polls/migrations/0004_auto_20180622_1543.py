# Generated by Django 2.0.6 on 2018-06-22 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180621_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Question_text',
            new_name='question_text',
        ),
    ]
