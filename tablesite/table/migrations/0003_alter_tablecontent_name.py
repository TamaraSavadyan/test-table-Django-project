# Generated by Django 4.0.4 on 2022-04-23 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_tablecontent_amount_tablecontent_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablecontent',
            name='name',
            field=models.CharField(default='...', max_length=200),
        ),
    ]