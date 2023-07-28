# Generated by Django 4.1 on 2022-10-26 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='CategoryImages/')),
                ('recorded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='CategoryImages/')),
                ('recorded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'ProductsCategories',
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='user name')),
                ('middle_name', models.CharField(max_length=100, verbose_name='middle name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('company_name', models.CharField(max_length=100, verbose_name='company name')),
                ('phone', models.CharField(default='+255', max_length=13, verbose_name='phone')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('hide_email', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=100)),
                ('ProductPrice', models.IntegerField(blank=True, null=True)),
                ('ProductDiscountPrice', models.IntegerField(blank=True, null=True)),
                ('ProductPackage', models.CharField(blank=True, max_length=100, null=True)),
                ('ProductQuantity', models.IntegerField(blank=True, null=True)),
                ('ProductStatus', models.CharField(blank=True, choices=[('New', 'New'), ('Old', 'Old')], max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ProductImages/')),
                ('D1', models.CharField(blank=True, default='Dimoso', max_length=100, null=True)),
                ('D2', models.CharField(blank=True, default='Shukuru', max_length=100, null=True)),
                ('D3', models.CharField(blank=True, default='Isaack', max_length=100, null=True)),
                ('D4', models.CharField(blank=True, default='Junior', max_length=100, null=True)),
                ('D5', models.CharField(blank=True, default='El Jr', max_length=100, null=True)),
                ('D1_place', models.CharField(blank=True, default='Magomeni', max_length=100, null=True)),
                ('D2_place', models.CharField(blank=True, default='Mbeya', max_length=100, null=True)),
                ('D3_place', models.CharField(blank=True, default='Arusha', max_length=100, null=True)),
                ('D4_place', models.CharField(blank=True, default='Mwanza', max_length=100, null=True)),
                ('D5_place', models.CharField(blank=True, default='Dodoma', max_length=100, null=True)),
                ('recorded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('ProductArchitecture', models.CharField(blank=True, max_length=100, null=True)),
                ('MemorySize', models.CharField(blank=True, max_length=100, null=True)),
                ('MaxFrequency', models.CharField(blank=True, max_length=100, null=True)),
                ('MemoryType', models.CharField(blank=True, max_length=100, null=True)),
                ('Peripherals', models.CharField(blank=True, max_length=500, null=True)),
                ('MaxSupplyVoltage', models.CharField(blank=True, max_length=100, null=True)),
                ('MinSupplyVoltage', models.CharField(blank=True, max_length=100, null=True)),
                ('AuthorizedDistributers', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.category')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.productscategory')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]