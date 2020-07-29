from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *

# Create your views here.

def error_404_page(request, exception):
    return render(request, "404.html")

def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse("About Response")

def add(request, a, b):     # Declare the parameter with respect to urls os this file
    return HttpResponse("add: {}".format(a+b))

def intro(request, name, age):
    # Json format must be a dictionary format
    mydictionary = {
        'name' : name,
        'age' : age
        }
    return JsonResponse(mydictionary)

def myfirstpage(request):
    return render(request, "index.html")

def mysecondpage(request):
    return render(request, "second.html")

def mythirdpage(request):
    var = "SuriyaJeyasuriya"
    greeting = "Welcome to the {}".format(var)
    names = ["suriya", "suresh", "soma", "siva"]
    dictionary = {
        "var":var,
        "greet" : greeting,
        "names" : names,
        }
    return render(request, "third.html", context=dictionary)

def myforthpage(request, num1, num2):
    ans = num1 > num2
    dictionary = {
        "ans" : ans,
        "num1": num1,
        "num2": num2,
        }
    return render(request, "fourth.html", context=dictionary)

def myimagepage(request):
    return render(request, "image.html")

def myimagepage2(request):
    return render(request, "image2.html")

def myimagepage3(request):
    return render(request, "image3.html")

def myimagepage4(request):
    return render(request, "image4.html")

def myimagepage5(request, name):
    myimagename = str(name)
    myimagename = myimagename.lower()
    print(myimagename)
    if myimagename == "django":
        var=True
    elif myimagename == "python":
        var=False
    mydictionary = {
        'var' : var
        }
    return render(request, "image5.html", context=mydictionary)

def myformpage_GET(request):
    return render(request, "form_GET.html")

def myformpage_POST(request):
    return render(request, "form_POST.html")

def mysubmitform_GET(request):
    mydictionary = {
        "var1": request.GET['mytext'],
        "var2":request.GET['mytextarea'],
        "method": request.method
        }
    return JsonResponse(mydictionary)

def mysubmitform_POST(request):
    mydictionary = {
        "var1": request.POST['mytext'],  #request.POST['name'] name=form input name
        "var2":request.POST['mytextarea'],
        "method": request.method
        }
    return JsonResponse(mydictionary)

def form2(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            mydictionary={
                'form':FeedbackForm()
                }
            errorflag = False
            Errors = []
            # for single error
            '''if title != title.upper():
                mydictionary["error"]=True
                mydictionary["errormes"]="Title should be Capital"
                return render(request, "form2.html", context=mydictionary)'''
            # for multiple errors
            if title != title.upper():
                errorflag = True
                errormes = "Title should be Capital"
                Errors.append(errormes)
            import re
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if not re.search(regex, email):
                errorflag = True
                errormes = "Invalid email id"
                Errors.append(errormes)
            if errorflag == False:
                mydictionary["success"] = True
                mydictionary["successmes"] = "Form Submitted"
            mydictionary['error'] = errorflag
            mydictionary['errors'] = Errors
            print(mydictionary)
            return render(request, "form2.html", context=mydictionary)
            
    if request.method == "GET":
        form = FeedbackForm()   #FeebackForm(None)
        mydictionary={
            'form':form
            }
        return render(request, "form2.html", context=mydictionary)
    
def form2_sub(request):
    mydictionary = {
        "var1": request.GET['title'],
        "var2":request.GET['subject'],
        "method": request.method
        }
    return JsonResponse(mydictionary)