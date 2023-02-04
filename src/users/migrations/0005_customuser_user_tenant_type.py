# Generated by Django 3.2 on 2023-02-02 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo_shared', '0001_initial'),
        ('users', '0004_remove_customuser_user_tenant_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_tenant_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='demo_shared.tenanttype'),
        ),
    ]