# Generated by Django 3.2.9 on 2022-01-25 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SoftDesk', '0003_alter_contributor_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributors', related_query_name='contributors', to='SoftDesk.project'),
        ),
    ]
