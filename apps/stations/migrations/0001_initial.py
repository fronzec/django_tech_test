# Generated by Django 2.1.2 on 2020-01-26 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=19)),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='StationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stations.LocationModel')),
            ],
        ),
    ]
