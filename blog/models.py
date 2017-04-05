from django.db import models

# Create your models here.
class bigsites(models.Model):
	bigsitesname=models.CharField(max_length=50,default="")

	def __str__(self):
		return self.bigsitesname

class sites(models.Model):
	siteid=models.IntegerField(default=0)
	sitename=models.CharField(max_length=50)
	bigsites=models.ForeignKey("bigsites",on_delete = models.CASCADE)

	def __str__(self):
		return self.sitename


class imageload(models.Model):
	imagename=models.CharField(max_length=50)
	image=models.ImageField(upload_to = "./uploads/",default="",max_length=100)
	imagetext=models.CharField(max_length=500)
	sites=models.ForeignKey("sites")

	def __str__(self):
		return self.imagename

class imagejudge(models.Model):
	username=models.CharField(max_length=50,default="")
	judge=models.CharField(max_length=50)
	imageload=models.ForeignKey("imageload")

	def __str__(self):
		return self.username
		
class judge(models.Model):
	username=models.CharField(max_length=50,default="")
	imageload=models.ForeignKey("imageload")
	judgecomment=models.CharField(max_length=10)
