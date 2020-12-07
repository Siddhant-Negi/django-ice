# Generated by Django 3.1.3 on 2020-12-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zipp', models.CharField(max_length=10)),
                ('Flavour', models.CharField(max_length=20)),
                ('Price', models.CharField(max_length=3)),
                ('Qty', models.CharField(max_length=3)),
                ('Amount', models.CharField(max_length=4)),
                ('Payment', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
