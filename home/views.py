from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("This is the Home Page!")
    context={
        "variable":"This is the value of the variable!",
        "variable1":"This is the value of the second variable!"
    }
    return render(request, 'home.html',context)


def about(request):
    #return HttpResponse("This is the About Page!")
    return render(request,'aboutus.html')

def contact(request):
    #return HttpResponse("This is the Contact Us Page!")
    return render(request,'contactus.html')