from django.shortcuts import render


def consolefun(request):
    return render(request, 'index_templates/index.html')

def new2fun(request):
    return render(request, 'index_templates/new2.html')

def domfun(request):
    return render(request, 'index_templates/DOM.html')

def calfun(request):
    return render(request, 'index_templates/calculator.html')

def todofun(request):
    return render(request, 'index_templates/todo.html')

def tod_insertcellfun(request):
    return render(request, 'index_templates/todousinginsertcell.html')

def productListfun(request):
    return render(request, 'index_templates/productlist.html')

def jqueryfun(request):
    return render(request, 'index_templates/jquery.html')

def jquery2fun(request):
    return render(request, 'index_templates/jquery2.html')

def formfun(request):
    return render(request, 'index_templates/formValidation.html')

def listfun(request):
    return render(request, 'index_templates/list.html')
   
def arrayfun(request):
    return render(request, 'index_templates/array.html')
# Create your views here.
