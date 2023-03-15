from django.shortcuts import render

# Create your views here.
def prathyu(request):
    d={'name':'perfect','dig':'intelligent'}
    return render(request,'prathyu.html',context=d)