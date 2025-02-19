# Generated by Django 5.0.1 on 2024-04-17 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www_app', '0004_rename_id_member_m_id_rename_id_portaladmin_pa_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='www_app.property')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='www_app.propertyseeker')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.DeleteModel(
            name='PortalAdmin',
        ),
    ]
