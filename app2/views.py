from django.shortcuts import render

# Create your views here.
def geeta_a2(request):
    d={'name':'geeta','digi':'silent'}
    return render(request,'geeta_a2.html',context=d)
