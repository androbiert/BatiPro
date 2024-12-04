# Generated by Django 5.1.2 on 2024-12-04 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BatiProApp', '0011_marketowner_join'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketMember',
            fields=[
                ('id_member', models.AutoField(primary_key=True, serialize=False)),
                ('adresse', models.CharField(max_length=255)),
                ('client', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='market_member', to='BatiProApp.client')),
                ('current_marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BatiProApp.marketplace')),
            ],
            options={
                'db_table': 'market_members',
            },
        ),
    ]
