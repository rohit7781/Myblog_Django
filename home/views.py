from django.shortcuts import render,HttpResponse
from home.models import Contact,requestblog,Blog
# Create your views here.
def home(request):
    return render(request,'home.html')
def blog(request):
    blogs = Blog.objects.all()
    # context3={'blogs':blogs} 
    context2 = {'successful':False,'blogs': blogs}
    if request.method=='POST':
        topic = request.POST['topic']
        desc = request.POST['desc']
        inss = requestblog(topic=topic,desc=desc)
        inss.save()
        context2 = {'successful':True}
        # print(topic,desc)

    return render(request,'blog.html',context2)
def blogpost(request,slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}
    # return HttpResponse(f'you are viewing {slug}')
    return render(request,'blogpost.html',context)


def contact(request):
    context = {'success':False}
    if request.method=='POST':
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        queries = request.POST['queries']
        context = {'success':True}
        ins = Contact(first=first,last=last,email=email,queries= queries)
        ins.save()
        # print(first ,last,email,queries)

    return render(request,'contact.html',context)
def winter(request):
    return render(request,'winter.html')
def jungle(request):
    return render(request,'jungle.html')
def oxygen(request):
    return render(request,'oxygen.html')

