# Generated by Django 2.2.10 on 2020-07-30 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200730_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
            ],
        ),
    ]