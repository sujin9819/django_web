from django.conf import settings
from django.db import models

class sample(models.Model):
    sample_ID = models.CharField(max_length=50,primary_key=True)
    Sex = models.TextField()
    Age = models.IntegerField()
    HC = models.CharField(max_length=50)
    BMI = models.DecimalField(max_digits=5,decimal_places=2)
    Allergy = models.CharField(max_length=50)
    Smoking = models.CharField(max_length=50)
    COVID = models.CharField(max_length=50)
    WBCcount = models.DecimalField(max_digits=5,decimal_places=2)
    Hemoglobin = models.DecimalField(max_digits=5,decimal_places=2)
    HCT = models.IntegerField()
    PLTcount = models.IntegerField()
    ESR = models.DecimalField(max_digits=5,decimal_places=2)
    CRP = models.DecimalField(max_digits=5,decimal_places=2)
    Albumin = models.DecimalField(max_digits=5,decimal_places=2)

class MAGdata(models.Model):
    MAG_index = models.CharField(max_length=10,primary_key=True)
    Taxon = models.TextField()
    Genome_size = models.IntegerField()
    N50 = models.IntegerField()
    Contamination_score = models.DecimalField(max_digits=5,decimal_places=2)
    Completeness_score = models.DecimalField(max_digits=5,decimal_places=2)
    GC = models.DecimalField(max_digits=5,decimal_places=2)
    fasta = models.FilePathField(blank=True, path="/media/fasta",match="*.fa")
    DNAcount = models.IntegerField(default=0)
    RNAcount = models.IntegerField(default=0)
    Ribocount = models.IntegerField(default=0)
    sample = models.CharField(max_length=10,blank=True)

class GeneData(models.Model):
    MAG = models.CharField(max_length=10,blank=True)
    Gene_index = models.CharField(max_length=50,primary_key=True)
    Gene_symbol = models.CharField(max_length=50)
    Gene_description = models.TextField()
    COG = models.CharField(max_length=10)
    KEGG_KO = models.CharField(max_length=50)
    KEGG_module = models.CharField(max_length=50)
    RNAcount = models.IntegerField(default=0)
    Ribocount = models.IntegerField(default=0)


