# Generated by Django 4.0.4 on 2022-11-18 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_size_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категория'},
        ),
        migrations.AlterModelOptions(
            name='categorybrand',
            options={'verbose_name': 'Бренд', 'verbose_name_plural': 'Бренд'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'Грамм', 'verbose_name_plural': 'Грамм'},
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='size',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Граммы'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('old_price', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('rating', models.FloatField(default=0)),
                ('mini_description', models.TextField(blank=True)),
                ('logo', models.ImageField(blank=True, upload_to='upload')),
                ('logo2', models.ImageField(blank=True, upload_to='upload')),
                ('logo3', models.ImageField(blank=True, upload_to='upload')),
                ('logo4', models.ImageField(blank=True, upload_to='upload')),
                ('logo5', models.ImageField(blank=True, upload_to='upload')),
                ('logo6', models.ImageField(blank=True, upload_to='upload')),
                ('description1', models.TextField(blank=True)),
                ('description2', models.TextField(blank=True)),
                ('is_new', models.BooleanField(default=False)),
                ('is_main', models.BooleanField(default=False)),
                ('is_popular', models.BooleanField(default=False)),
                ('is_discount', models.BooleanField(default=False)),
                ('stock', models.IntegerField(blank=True, default=0)),
                ('discount', models.IntegerField(blank=True, default=0)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.categorybrand')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('size', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.size')),
            ],
        ),
    ]