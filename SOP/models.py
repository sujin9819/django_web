from django.conf import settings
from django.db import models

class SOP_list(models.Model):
	lang = models.CharField(max_length=5, default="en")
	SOP = models.CharField(max_length=20)
	title = models.CharField(max_length=80)
	md_path = models.URLField(default="") 
	