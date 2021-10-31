from django.shortcuts import render,HttpResponse
from home.models import Contact,requestblog
# Create your views here.
def home(request):
    return render(request,'home.html')
def blog(request):
    if request.method=='POST':
        topic = request.POST['topic']
        desc = request.POST['desc']
        # inss = requestblog(topic=topic,desc=desc)
        # inss.save()
        print(topic,desc)

    return render(request,'blog.html')
def blogpost(request,slug):
    return HttpResponse(f'Hii this is my {slug}')
def contact(request):
    if request.method=='POST':
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        queries = request.POST['queries']

        # ins = Contact(first=first,last=last,email=email,queries= queries)
        # ins.save()
        print(first ,last,email,queries)

    return render(request,'contact.html')
def winter(request):
    return render(request,'winter.html')
def jungle(request):
    return render(request,'jungle.html')
def oxygen(request):
    return render(request,'oxygen.html')

