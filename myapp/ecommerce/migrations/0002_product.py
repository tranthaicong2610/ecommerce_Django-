# Generated by Django 4.0.3 on 2022-03-11 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('sale_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('description', models.TextField()),
                ('image_list', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.category')),
            ],
        ),
    ]
