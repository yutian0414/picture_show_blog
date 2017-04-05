from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.forms import addform,loadimage
from blog.models import imageload,sites,bigsites

def index(request):
	if request.method=="POST":
		form=addform(request.POST)
		if form.is_valid() and form.cleaned_data["a"]!=None:
			a=form.cleaned_data["a"]
			b=form.cleaned_data["b"]
			return HttpResponse(str(int(a)+int(b)))
	else:
		form=addform()
	return render(request,"home.html",{"form":form})

def home(request):
	return render(request,"pictureshow.html")

def refresh(request,setsid="100001"):
	setsidget=sites.objects.get(siteid=setsid)
	imageitems=setsidget.imageload_set.all()

	sitesitems=sites.objects.all()
	bigsitesitems=bigsites.objects.all()
	return render(request,"pictureshow.html",{"imageitems":imageitems,"sitesitems":sitesitems,"bigsitesitems":bigsitesitems} )
