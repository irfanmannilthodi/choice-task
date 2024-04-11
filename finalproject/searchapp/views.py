from django.shortcuts import render
from finalapp . models import Marvel,Dccomics,Monster

def search(request):
    if request.method=="POST":
         searched=request.POST['searched']
         movie=Marvel.objects.all()
    return render(request,'search.html',{'searched':searched,'movie':movie})
def search1(request):
    if request.method=="POST":
         searched=request.POST['searched']
         movie=Dccomics.objects.all()
    return render(request,'search.html',{'searched':searched,'movie':movie})
def search2(request):
    if request.method=="POST":
         searched=request.POST['searched']
         movie=Monster.objects.all()
    return render(request,'search.html',{'searched':searched,'movie':movie})










