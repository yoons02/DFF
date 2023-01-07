from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request, 'main/mainpage.html')

def showmentors(request):
    return render(request, 'main/mentor_list.html')

def showcontact(request):
    return render(request, 'main/contact.html')

def showrecruit(request):
    return render(request, 'main/recruit.html')