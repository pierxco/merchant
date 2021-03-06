# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonFPSResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('buyerEmail', models.EmailField(max_length=254)),
                ('buyerName', models.CharField(max_length=75)),
                ('callerReference', models.CharField(max_length=100)),
                ('notificationType', models.CharField(max_length=50)),
                ('operation', models.CharField(max_length=20)),
                ('paymentMethod', models.CharField(max_length=5)),
                ('recipientEmail', models.EmailField(max_length=254)),
                ('recipientName', models.CharField(max_length=75)),
                ('statusCode', models.CharField(max_length=50)),
                ('statusMessage', models.TextField()),
                ('transactionAmount', models.CharField(max_length=20)),
                ('transactionDate', models.DateTimeField()),
                ('transactionId', models.CharField(max_length=50, db_index=True)),
                ('transactionStatus', models.CharField(max_length=50)),
                ('customerEmail', models.EmailField(max_length=254, null=True, blank=True)),
                ('customerName', models.CharField(max_length=75, null=True, blank=True)),
                ('addressFullName', models.CharField(max_length=100, null=True, blank=True)),
                ('addressLine1', models.CharField(max_length=100, null=True, blank=True)),
                ('addressLine2', models.CharField(max_length=100, null=True, blank=True)),
                ('addressState', models.CharField(max_length=50, null=True, blank=True)),
                ('addressZip', models.CharField(max_length=25, null=True, blank=True)),
                ('addressCountry', models.CharField(max_length=25, null=True, blank=True)),
                ('addressPhone', models.CharField(max_length=25, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorizeAIMResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('response_code', models.IntegerField(choices=[(1, b'Approved'), (2, b'Declined'), (3, b'Error'), (4, b'Held for Review')])),
                ('response_reason_code', models.IntegerField(blank=True)),
                ('response_reason_text', models.TextField(blank=True)),
                ('authorization_code', models.CharField(max_length=8)),
                ('address_verification_response', models.CharField(max_length=b'8', choices=[(b'A', b'Address(Street) matches,ZIP does not'), (b'B', b'Address information not provided for AVS check'), (b'E', b'AVS error'), (b'G', b'Non-U.S. Card Issuing Bank'), (b'N', b'No match on Address(Street) or ZIP'), (b'P', b'AVS not applicable for this transactions'), (b'R', b'Retry-System unavailable or timed out'), (b'S', b'Service not supported by issuer'), (b'U', b'Address information is unavailable'), (b'W', b'Nine digit Zip matches, Address(Street) does not'), (b'X', b'Address(Street) and nine digit ZIP match'), (b'Y', b'Address(Street) and five digit ZIP match'), (b'Z', b'Five digit Zip matches, Address(Street) does not')])),
                ('transaction_id', models.CharField(max_length=64)),
                ('invoice_number', models.CharField(max_length=64, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('amount', models.DecimalField(max_digits=16, decimal_places=2)),
                ('method', models.CharField(max_length=255, blank=True)),
                ('transaction_type', models.CharField(max_length=255, blank=True)),
                ('customer_id', models.CharField(max_length=64, blank=True)),
                ('first_name', models.CharField(max_length=64, blank=True)),
                ('last_name', models.CharField(max_length=64, blank=True)),
                ('company', models.CharField(max_length=64, blank=True)),
                ('address', models.CharField(max_length=64, blank=True)),
                ('city', models.CharField(max_length=64, blank=True)),
                ('state', models.CharField(max_length=64, blank=True)),
                ('zip_code', models.CharField(max_length=64, blank=True)),
                ('country', models.CharField(max_length=64, blank=True)),
                ('phone', models.CharField(max_length=64, blank=True)),
                ('fax', models.CharField(max_length=64, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('shipping_first_name', models.CharField(max_length=64, blank=True)),
                ('shipping_last_name', models.CharField(max_length=64, blank=True)),
                ('shipping_company', models.CharField(max_length=64, blank=True)),
                ('shipping_address', models.CharField(max_length=64, blank=True)),
                ('shipping_city', models.CharField(max_length=64, blank=True)),
                ('shipping_state', models.CharField(max_length=64, blank=True)),
                ('shipping_zip_code', models.CharField(max_length=64, blank=True)),
                ('shipping_country', models.CharField(max_length=64, blank=True)),
                ('card_code_response', models.CharField(help_text='Card Code Verification response', max_length=b'8', choices=[(b'', b''), (b'M', b'Match'), (b'N', b'No Match'), (b'P', b'Not Processed'), (b'S', b'Should have been present'), (b'U', b'Issuer unable to process request')])),
            ],
        ),
        migrations.CreateModel(
            name='EwayResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='GCNewOrderNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notify_type', models.CharField(max_length=255, blank=True)),
                ('serial_number', models.CharField(max_length=255)),
                ('google_order_number', models.CharField(max_length=255)),
                ('buyer_id', models.CharField(max_length=255)),
                ('private_data', models.CharField(max_length=255, blank=True)),
                ('shipping_contact_name', models.CharField(max_length=255, blank=True)),
                ('shipping_address1', models.CharField(max_length=255, blank=True)),
                ('shipping_address2', models.CharField(max_length=255, blank=True)),
                ('shipping_city', models.CharField(max_length=255, blank=True)),
                ('shipping_postal_code', models.CharField(max_length=255, blank=True)),
                ('shipping_region', models.CharField(max_length=255, blank=True)),
                ('shipping_country_code', models.CharField(max_length=255, blank=True)),
                ('shipping_email', models.EmailField(max_length=254)),
                ('shipping_company_name', models.CharField(max_length=255, blank=True)),
                ('shipping_fax', models.CharField(max_length=255, blank=True)),
                ('shipping_phone', models.CharField(max_length=255, blank=True)),
                ('billing_contact_name', models.CharField(max_length=255, blank=True)),
                ('billing_address1', models.CharField(max_length=255, blank=True)),
                ('billing_address2', models.CharField(max_length=255, blank=True)),
                ('billing_city', models.CharField(max_length=255, blank=True)),
                ('billing_postal_code', models.CharField(max_length=255, blank=True)),
                ('billing_region', models.CharField(max_length=255, blank=True)),
                ('billing_country_code', models.CharField(max_length=255, blank=True)),
                ('billing_email', models.EmailField(max_length=254)),
                ('billing_company_name', models.CharField(max_length=255, blank=True)),
                ('billing_fax', models.CharField(max_length=255, blank=True)),
                ('billing_phone', models.CharField(max_length=255, blank=True)),
                ('marketing_email_allowed', models.BooleanField(default=False)),
                ('num_cart_items', models.IntegerField()),
                ('cart_items', models.TextField()),
                ('total_tax', models.DecimalField(null=True, max_digits=16, decimal_places=2, blank=True)),
                ('total_tax_currency', models.CharField(max_length=255, blank=True)),
                ('adjustment_total', models.DecimalField(null=True, max_digits=16, decimal_places=2, blank=True)),
                ('adjustment_total_currency', models.CharField(max_length=255, blank=True)),
                ('order_total', models.DecimalField(null=True, max_digits=16, decimal_places=2, blank=True)),
                ('order_total_currency', models.CharField(max_length=255, blank=True)),
                ('financial_order_state', models.CharField(max_length=255, blank=True)),
                ('fulfillment_order_state', models.CharField(max_length=255, blank=True)),
                ('timestamp', models.CharField(max_length=64, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaylaneAuthorization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sale_authorization_id', models.BigIntegerField(db_index=True)),
                ('first_authorization', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PaylaneTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_email', models.CharField(max_length=200)),
                ('product', models.CharField(max_length=200)),
                ('success', models.BooleanField(default=False)),
                ('error_code', models.IntegerField(default=0)),
                ('error_description', models.CharField(max_length=300, blank=True)),
                ('acquirer_error', models.CharField(max_length=40, blank=True)),
                ('acquirer_description', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PinCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=32, editable=False, db_index=True)),
                ('display_number', models.CharField(max_length=20, editable=False)),
                ('expiry_month', models.PositiveSmallIntegerField()),
                ('expiry_year', models.PositiveSmallIntegerField()),
                ('scheme', models.CharField(max_length=20, editable=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(max_length=255, blank=True)),
                ('address_city', models.CharField(max_length=255)),
                ('address_postcode', models.CharField(max_length=20)),
                ('address_state', models.CharField(max_length=255)),
                ('address_country', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='pin_cards', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PinCharge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(unique=True, max_length=32, editable=False)),
                ('success', models.BooleanField()),
                ('amount', models.DecimalField(max_digits=16, decimal_places=2)),
                ('currency', models.CharField(max_length=3)),
                ('description', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('ip_address', models.IPAddressField()),
                ('created_at', models.DateTimeField()),
                ('status_message', models.CharField(max_length=255)),
                ('error_message', models.CharField(max_length=255, null=True, blank=True)),
                ('card', models.ForeignKey(related_name='charges', editable=False, to='billing.PinCard')),
            ],
        ),
        migrations.CreateModel(
            name='PinCustomer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(unique=True, max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField()),
                ('card', models.ForeignKey(related_name='customers', to='billing.PinCard')),
                ('user', models.OneToOneField(related_name='pin_customer', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PinRefund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(unique=True, max_length=32)),
                ('success', models.BooleanField()),
                ('amount', models.DecimalField(max_digits=16, decimal_places=2)),
                ('currency', models.CharField(max_length=3)),
                ('created_at', models.DateTimeField()),
                ('status_message', models.CharField(max_length=255)),
                ('error_message', models.CharField(max_length=255, null=True, blank=True)),
                ('charge', models.ForeignKey(related_name='refunds', to='billing.PinCharge')),
                ('user', models.ForeignKey(related_name='pin_refunds', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorldPayResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('installation_id', models.CharField(max_length=64)),
                ('company_name', models.CharField(max_length=255, null=True, blank=True)),
                ('cart_id', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('amount', models.DecimalField(max_digits=16, decimal_places=2)),
                ('currency', models.CharField(max_length=64)),
                ('amount_string', models.CharField(max_length=64)),
                ('auth_mode', models.CharField(max_length=64)),
                ('test_mode', models.CharField(max_length=64)),
                ('transaction_id', models.CharField(max_length=64)),
                ('transaction_status', models.CharField(max_length=64)),
                ('transaction_time', models.CharField(max_length=64)),
                ('auth_amount', models.DecimalField(max_digits=16, decimal_places=2)),
                ('auth_currency', models.CharField(max_length=64)),
                ('auth_amount_string', models.CharField(max_length=64)),
                ('raw_auth_message', models.CharField(max_length=255)),
                ('raw_auth_code', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('post_code', models.CharField(max_length=64)),
                ('country_code', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=64, verbose_name='Phone number', blank=True)),
                ('fax', models.CharField(max_length=64, verbose_name='Fax number', blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('future_pay_id', models.CharField(max_length=64, blank=True)),
                ('card_type', models.CharField(max_length=64, blank=True)),
                ('ip_address', models.IPAddressField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='pincharge',
            name='customer',
            field=models.ForeignKey(related_name='customers', blank=True, editable=False, to='billing.PinCustomer', null=True),
        ),
        migrations.AddField(
            model_name='pincharge',
            name='user',
            field=models.ForeignKey(related_name='pin_charges', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='paylaneauthorization',
            name='transaction',
            field=models.OneToOneField(to='billing.PaylaneTransaction'),
        ),
    ]
