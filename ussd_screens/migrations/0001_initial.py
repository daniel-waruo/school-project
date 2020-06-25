# Generated by Django 3.0.7 on 2020-06-24 07:49

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USSDState',
            fields=[
                ('session_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=200, null=True)),
                ('data', jsonfield.fields.JSONField(null=True)),
            ],
        ),
    ]