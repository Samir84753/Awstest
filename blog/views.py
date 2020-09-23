from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import sitemsg
# Create your views here.

def index(request):
    return render(request,'info.html')

def postmsg(request):
    user_name=request.POST.get('uname')
    user_email=request.POST.get('uemail')
    user_msg=request.POST.get('msg')
    s=sitemsg(user_name=user_name,user_email=user_email,user_msg=user_msg)
    s.save()
    return redirect('msgpage')

def viewmsg(request):
    messages=sitemsg.objects.all()
    ctx={'messages':messages}
    return render(request,'viewmsg.html',ctx)

def deletepost(request,user_id):
    delpost=sitemsg.objects.filter(user_id=user_id)
    delpost.delete()
    return redirect('msgpage')
def editpost(request,user_id):
    toupdate=sitemsg.objects.get(user_id=user_id)
    return render(request,'editpost.html',{'toupdate':toupdate})
def updatepost(request):
    print("updatepost")
    username=request.POST.get('uname')
    useremail=request.POST.get('uemail')
    usermsg=request.POST.get('msg')
    userid=request.POST.get('userid')
    post=sitemsg.objects.get(user_id=userid)
    post.user_name=username
    post.user_email=useremail
    post.user_msg=usermsg
    post.save()
    return redirect('msgpage')



