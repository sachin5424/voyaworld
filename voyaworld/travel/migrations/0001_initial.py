# Generated by Django 3.1 on 2020-08-19 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Devloper_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D_image', models.ImageField(null=True, upload_to='')),
                ('D_name', models.CharField(max_length=100)),
                ('D_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PackagaesCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PackagaesState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('Country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.packagaescountry')),
            ],
        ),
        migrations.CreateModel(
            name='PackagesAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_place', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('package_Day', models.IntegerField()),
                ('package_Night', models.IntegerField()),
                ('package_price', models.IntegerField()),
                ('dis', models.TextField()),
                ('State', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travel.packagaesstate')),
            ],
        ),
        migrations.CreateModel(
            name='tranding_package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tranding_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.packagesadd')),
            ],
        ),
        migrations.CreateModel(
            name='special_package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.packagesadd')),
            ],
        ),
    ]
