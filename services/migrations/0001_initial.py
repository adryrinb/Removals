# Generated by Django 4.0.7 on 2022-08-21 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        ('clients', '0001_initial'),
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Move_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Move type')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Move types',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickUp', models.CharField(max_length=100, verbose_name='Pick-up')),
                ('pickUpComment', models.TextField(blank=True, null=True, verbose_name='Pick-up Comments')),
                ('dropOff', models.CharField(max_length=100, verbose_name='Drop-off')),
                ('dropOffComment', models.TextField(blank=True, null=True, verbose_name='Drop-off Comments')),
                ('date', models.DateField(verbose_name='Moving Date')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Service Comments')),
                ('price', models.IntegerField(null=True, verbose_name='Service Price')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('clientId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.client', verbose_name='Client')),
            ],
            options={
                'verbose_name_plural': 'Services',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Service_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Service Type')),
                ('condition', models.TextField(blank=True, null=True, verbose_name='Service Type Conditiions')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Service Types',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Service_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Qty')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.furniture_item')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.service')),
            ],
            options={
                'verbose_name_plural': 'Service Items',
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='service',
            name='furniture_item',
            field=models.ManyToManyField(related_name='furniture_items', through='services.Service_item', to='inventory.furniture_item', verbose_name='Furniture Item'),
        ),
        migrations.AddField(
            model_name='service',
            name='move',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.move_type', verbose_name='Move type'),
        ),
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.service_type', verbose_name='Service type'),
        ),
        migrations.AddField(
            model_name='service',
            name='vehicle',
            field=models.ManyToManyField(related_name='vehicles', to='vehicles.vehicle', verbose_name='Vehicle'),
        ),
    ]
