# Generated by Django 4.0.5 on 2022-06-21 06:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyticMethod',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('method', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Co2Allocation',
            fields=[
                ('pcces_encode', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('cradle_to_gate', models.FloatField(null=True)),
                ('factory_gate_to_site', models.FloatField(null=True)),
                ('total_carbon_footprint', models.FloatField(null=True)),
                ('unit', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DataQuality',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IndustrialCategory',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PccesEncode',
            fields=[
                ('pcces_encode', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('common_name', models.TextField(null=True)),
                ('chapter', models.TextField()),
                ('six_desc', models.TextField()),
                ('senven_desc', models.CharField(max_length=50)),
                ('eight_desc', models.CharField(max_length=50)),
                ('nine_desc', models.CharField(max_length=50)),
                ('ten_desc', models.CharField(max_length=30)),
                ('eleven_desc', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryCategory',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('category_id', models.CharField(max_length=30)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('industrial_category_desc', models.TextField()),
                ('pcces_encode', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('image', models.ImageField(upload_to='product_image/')),
                ('origin', models.CharField(max_length=50)),
                ('technology_desc', models.TextField()),
                ('lifecycle_category', models.CharField(max_length=30)),
                ('excluded_item', models.CharField(max_length=50)),
                ('data_generator', models.CharField(max_length=30, null=True)),
                ('emission_coefficient_source', models.CharField(max_length=30)),
                ('ISO_standard', models.CharField(max_length=30)),
                ('analysis_time_resource', models.CharField(max_length=30)),
                ('valid_time_span', models.CharField(max_length=20)),
                ('product_flow_image', models.ImageField(upload_to='product_flow_image/')),
                ('company_name', models.CharField(max_length=512)),
                ('company_phone', models.CharField(max_length=30)),
                ('company_address', models.TextField()),
                ('company_mail', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('reviewer_name', models.CharField(max_length=512)),
                ('reviewer_phone', models.CharField(max_length=50)),
                ('reviewer_address', models.TextField()),
                ('reviewer_mail', models.CharField(max_length=50)),
                ('review_date', models.DateTimeField(blank=True, null=True)),
                ('refresh_time', models.DateTimeField(default=datetime.datetime.now)),
                ('co2_allocation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carbon_footprint_web.co2allocation')),
                ('data_quality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carbon_footprint_web.dataquality')),
                ('industrial_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carbon_footprint_web.industrialcategory')),
                ('lifecycle_analytic_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carbon_footprint_web.analyticmethod')),
                ('primary_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carbon_footprint_web.primarycategory')),
            ],
        ),
        migrations.AddField(
            model_name='industrialcategory',
            name='primary_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary_categories', to='carbon_footprint_web.primarycategory'),
        ),
    ]
