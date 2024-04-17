# Generated by Django 4.2.4 on 2024-04-17 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0021_subcomponent'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamberloginfo',
            name='chamber_id',
            field=models.ForeignKey(db_column='chamber_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.chamber'),
        ),
        migrations.AddField(
            model_name='chamberloginfo',
            name='program_id',
            field=models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.program'),
        ),
        migrations.AddField(
            model_name='chamberloginfo',
            name='technician_id',
            field=models.ForeignKey(db_column='technician_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.technician'),
        ),
    ]
