from django.shortcuts import render

# Create your views here.
#create a fucntion then call the function for urls
def home (request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')