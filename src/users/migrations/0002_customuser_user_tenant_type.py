# Generated by Django 3.2 on 2023-02-02 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo_tenant', '0003_remove_tenantuser_tenant_user_name'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_tenant_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='demo_tenant.tenantuser'),
        ),
    ]