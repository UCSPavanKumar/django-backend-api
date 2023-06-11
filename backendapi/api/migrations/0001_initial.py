# Generated by Django 4.0.4 on 2023-06-10 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentMaster',
            fields=[
                ('agent_id', models.AutoField(primary_key=True, serialize=False)),
                ('agent_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ClientMaster',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('voucher_id', models.AutoField(primary_key=True, serialize=False)),
                ('validity_date', models.DateField()),
                ('amount', models.BigIntegerField(max_length=10)),
                ('status', models.CharField(default='A', max_length=1)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clientmaster')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txn_date', models.DateField()),
                ('txn_amount', models.BigIntegerField(max_length=20)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.agentmaster')),
                ('voucher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.voucher')),
            ],
        ),
    ]
