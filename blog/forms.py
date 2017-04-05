#-*- coding:utf-8 -*-
from django import forms
class addform(forms.Form):
	a=forms.IntegerField()
	b=forms.IntegerField()
	
class loadimage(forms.Form):
	imagename=forms.CharField()
	image=forms.FileField()
	imagetext=forms.CharField()
