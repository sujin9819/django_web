from django.conf import settings
from django.db import models

class SOP_list(models.Model):
	lang = models.CharField(max_length=5, default="en")
	SOP = models.CharField(max_length=20)
	category = models.CharField(max_length=30)
	title = models.CharField(max_length=80)
	#md_path = models.FileField(upload_to="") 깃허브에 마크다운 파일을 업로드하고 그 파일을 사용하는 거는 url vs file ??
	