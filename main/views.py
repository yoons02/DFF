from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
def showmain(request):
    return render(request, 'main/mainpage.html')

def showmentors(request):
    return render(request, 'main/mentor_list.html')

def showcontact(request):
    return render(request, 'main/contact.html')

def showrecruit(request):
    return render(request, 'main/recruit.html')

def showdff(request):
    return render(request, 'main/dff.html')

def showannounce(request):
    return render(request, 'main/announce.html')

def showmessage(request):
    blogs = Blog.objects.all()
    return render(request, 'main/message.html',{'blogs':blogs})

def showdreamer(request):
    return render(request, 'main/dreamer.html')

def showtoMentor(request):
    return render(request, 'main/toMentor.html')

def showNew(request):
    if request.method == "GET":
        return render(request, 'main/new.html')

def showcomplete(request):
    return render(request, 'main/complete.html')
        
def showForyou(request):
    return render(request, 'main/foryou.html') 

def create(request):
    new_blog = Blog()
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('main:showcomplete')

def delete(request, id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('main:showmessage')
