from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('branch_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('branch_detail', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'aboutus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appo_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('appo_date', models.DateField(blank=True, null=True)),
                ('appo_time', models.DateField()),
            ],
            options={
                'db_table': 'appointment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cus_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cus_name', models.CharField(max_length=100)),
                ('cus_gender', models.CharField(max_length=10)),
                ('cus_contact', models.CharField(max_length=10)),
                ('cus_address', models.CharField(max_length=200)),
                ('cus_birth', models.DateField(blank=True, null=True)),
                ('cus_reward', models.CharField(max_length=10)),
                ('somsi_coin', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_gender', models.CharField(max_length=10)),
                ('emp_contact', models.CharField(max_length=10)),
                ('emp_address', models.CharField(max_length=200)),
                ('emp_position', models.CharField(max_length=100)),
                ('emp_salary', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notifies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noti_course', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'notifies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('prod_qty', models.IntegerField()),
                ('prod_price', models.FloatField(blank=True, null=True)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('ship_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('payment_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100, null=True)),
                ('remark', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'payment_method',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prod_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=100)),
                ('prod_cost', models.FloatField(blank=True, null=True)),
                ('prod_price', models.FloatField(blank=True, null=True)),
                ('prod_qty_stock', models.IntegerField(null=True)),
                ('prod_date', models.DateField(blank=True, null=True)),
                ('prod_detail', models.JSONField()),
                ('prod_description', models.JSONField()),
                ('prod_review', models.JSONField()),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('promo_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('noti_promo', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'promotion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('receipt_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('receipt_date', models.DateField(blank=True, null=True)),
                ('total_price', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'receipt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('reward', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('rew_level', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'reward',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=100)),
                ('service_cost', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('key', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
    ]