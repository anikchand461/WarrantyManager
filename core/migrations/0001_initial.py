# Generated by Django 5.1.4 on 2025-04-13 06:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_image', models.ImageField(upload_to='bills/')),
                ('shop_name', models.CharField(max_length=255)),
                ('contact_number', models.CharField(blank=True, max_length=20)),
                ('bill_date', models.DateField()),
                ('total_amount', models.FloatField()),
                ('items', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WarrantyCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warranty_image', models.ImageField(blank=True, null=True, upload_to='warranties/')),
                ('warranty_period_years', models.IntegerField(default=0)),
                ('warranty_end_date', models.DateField(blank=True, null=True)),
                ('bill', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.bill')),
            ],
        ),
        migrations.CreateModel(
            name='SharedWarranty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shared_text', models.TextField()),
                ('shared_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('warranty_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.warrantycard')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('warranty_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.warrantycard')),
            ],
        ),
    ]
