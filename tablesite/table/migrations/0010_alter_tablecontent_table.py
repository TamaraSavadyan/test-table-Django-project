# Generated by Django 4.0.3 on 2022-05-18 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0009_alter_tablecontent_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tablecontent',
            table='"public"."market_data"',
        ),
    ]