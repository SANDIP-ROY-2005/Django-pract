from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request) :
   return render(request,'index.html')
    # return HttpResponse("this is homepage")
def about(request) :
    return HttpResponse("this is about")
def service(request) :
    return HttpResponse("this is service")