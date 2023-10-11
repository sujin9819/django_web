# Generated by Django 3.2.22 on 2023-10-11 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneCount',
            fields=[
                ('Gene_index', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Gene_symbol', models.CharField(max_length=50)),
                ('Gene_description', models.TextField()),
                ('COG', models.CharField(max_length=50)),
                ('COG_category', models.CharField(max_length=50)),
                ('KEGG_KO', models.CharField(max_length=50)),
                ('KEGG_module', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GeneData',
            fields=[
                ('Gene_index', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Gene_symbol', models.CharField(max_length=50)),
                ('Gene_description', models.TextField()),
                ('COG', models.CharField(max_length=10)),
                ('COG_category', models.CharField(max_length=10)),
                ('KEGG_KO', models.CharField(max_length=50)),
                ('KEGG_module', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MAGdata',
            fields=[
                ('MAG_index', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Taxon', models.TextField()),
                ('Genome_size', models.IntegerField()),
                ('N50', models.IntegerField()),
                ('Contamination_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Completeness_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('GC', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='sample',
            fields=[
                ('sample_ID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Sex', models.TextField()),
                ('Age', models.IntegerField()),
                ('HC', models.CharField(max_length=50)),
                ('BMI', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Allergy', models.CharField(max_length=50)),
                ('Smoking', models.CharField(max_length=50)),
                ('COVID', models.CharField(max_length=50)),
                ('WBCcount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Hemoglobin', models.DecimalField(decimal_places=2, max_digits=5)),
                ('HCT', models.IntegerField()),
                ('PLTcount', models.IntegerField()),
                ('ESR', models.DecimalField(decimal_places=2, max_digits=5)),
                ('CRP', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Albumin', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
