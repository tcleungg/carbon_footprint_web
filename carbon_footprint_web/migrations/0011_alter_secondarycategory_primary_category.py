# Generated by Django 4.0.5 on 2022-06-16 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_footprint_web', '0010_alter_secondarycategory_primary_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondarycategory',
            name='primary_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary_categories', to='carbon_footprint_web.primarycategory'),
        ),
    ]
