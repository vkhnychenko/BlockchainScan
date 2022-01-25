# Generated by Django 3.2.5 on 2021-08-05 15:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_address', models.CharField(max_length=100)),
                ('chain', models.CharField(choices=[('eth', 'eth'), ('bsc', 'bsc'), ('polygon', 'polygon')], max_length=50)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('symbol', models.CharField(blank=True, max_length=50, null=True)),
                ('decimals', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'unique_together': {('token_address', 'chain')},
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('chain', models.CharField(choices=[('eth', 'eth'), ('bsc', 'bsc'), ('polygon', 'polygon')], max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_tx_timestamp', models.IntegerField()),
                ('last_tx_block_number', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallets', to='users.userbot')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('native', 'native'), ('token', 'token'), ('nft', 'nft')], max_length=50)),
                ('hash', models.CharField(blank=True, max_length=100, null=True)),
                ('to_address', models.CharField(blank=True, max_length=100, null=True)),
                ('from_address', models.CharField(blank=True, max_length=100, null=True)),
                ('tx_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('value', models.CharField(blank=True, max_length=100, null=True)),
                ('native_price', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('token_price', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('token_contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wallets.tokencontract')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='wallets.wallet')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('date_start', models.DateTimeField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filters', to='wallets.wallet')),
            ],
            options={
                'ordering': ('-created_at',),
                'unique_together': {('address', 'wallet')},
            },
        ),
    ]