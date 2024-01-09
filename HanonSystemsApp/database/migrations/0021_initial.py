# Generated by Django 4.2.4 on 2024-01-04 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('database', '0020_remove_product_program_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('lab_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=15, null=True)),
                ('supervisor', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('program_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('status', models.SmallIntegerField(null=True)),
                ('phase', models.SmallIntegerField(null=True)),
                ('enterproj_id', models.IntegerField(null=True)),
                ('wbs_number', models.CharField(max_length=30, null=True)),
                ('oem', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill', models.CharField(max_length=25, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('technician_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('lab_name', models.ForeignKey(db_column='lab_name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.lab')),
            ],
        ),
        migrations.CreateModel(
            name='TestMap',
            fields=[
                ('map_name', models.CharField(max_length=30, null=True)),
                ('tr', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('program_name', models.ForeignKey(db_column='program_name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.program')),
            ],
        ),
        migrations.CreateModel(
            name='Technician_Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ForeignKey(db_column='skill', on_delete=django.db.models.deletion.CASCADE, to='database.skill')),
                ('technician_name', models.ForeignKey(db_column='technician_name', on_delete=django.db.models.deletion.CASCADE, to='database.technician')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_family', models.CharField(max_length=10, null=True)),
                ('platform', models.CharField(max_length=15, null=True)),
                ('communication_protocol', models.CharField(max_length=15, null=True)),
                ('voltage', models.CharField(max_length=3, null=True)),
                ('variant', models.CharField(max_length=30, null=True)),
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('program_name', models.ForeignKey(db_column='program_name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.program')),
            ],
        ),
        migrations.CreateModel(
            name='DUT',
            fields=[
                ('dut_name', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('received_date', models.DateField(null=True)),
                ('storage_date', models.DateField(null=True)),
                ('storage_bin', models.CharField(max_length=20, null=True)),
                ('product_id', models.ForeignKey(db_column='product_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.product')),
            ],
        ),
    ]
