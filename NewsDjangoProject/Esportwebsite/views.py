from django.shortcuts import render,redirect
from django.http import HttpResponse #1 เพือเอาไปแสดงหน้าเว็บ
from .models import tb_news #ฐานข้อมูล
from django.contrib.auth.models import User,auth #การเข้ารหัส
from django.contrib import messages #ทำ alert แจ้งเตื่อน
from django.contrib.auth.decorators import login_required,permission_required #decorators จัดการ Permission

# Create your views here.

def home(request): 
    content = tb_news.objects.all().order_by("-id")
    return render(request,'Esportwebsite/home.html',{'newsdata':content}) #7 render(request,'Esportwebsite/index.html',mydata) ส่งข้อมูลไปยัง html

def newsdetail(request):
    id = request.GET['id']
    result = tb_news.objects.filter(pk=id)
    return render(request,'Esportwebsite/newsdetail.html',{'newsdetail':result}) 

@login_required(login_url ='/login') #ต้องlogin ก่อนถึงมีสิทธิ
@permission_required('is_staff',login_url='/') #admin ต้องให้สิทธิก่อน

def addnews(request): # แสดงหน้า addnews
    return render(request,'Esportwebsite/addnew.html')

def addnewsdata(request): # บันทึก addnews
    news_title = request.POST['news_title']
    news_detail = request.POST['news_detail']
    news_photo = request.FILES['news_photo']
    
    content = tb_news(news_title=news_title,news_detail=news_detail,news_photo=news_photo)
    content.save()
    return redirect("/contentmanager") #เป็นชื่อฟังก์ชัน


@login_required(login_url ='/login') #ต้องlogin ก่อนถึงมีสิทธิ
@permission_required('is_staff',login_url='/')  #admin ต้องให้สิทธิก่อน

def contentmanager(request): # แสดงข่าวสารที่ได้บันทึก
    datanews = tb_news.objects.all()
    mydatanews = {'news':datanews}
    print(datanews)
    return render(request,'Esportwebsite/contentnewsmanager.html',mydatanews)

def contentedit(request): #แสดงหน้าข้อมูลที่ต้องการแก้ไขเมือกดปุ่มแก้ไข
    id = request.GET['id']
    result = tb_news.objects.filter(pk=id)
    return render(request,'Esportwebsite/contentnewsedit.html',{'result':result})

def contentupdate(request): #บันทึกข้อมูลที่ต้องการแก้ไข
    id = request.POST['id']
    news_title = request.POST['news_title']
    news_detail = request.POST['news_detail']
    try:
        news_photo = request.FILES['news_photo']
    except  KeyError:
        news_photo = None
     
    content = tb_news.objects.get(pk=id)
    content.news_title = news_title
    content.news_detail = news_detail
    if news_photo is not None:
        content.news_photo = news_photo

    content.save()
    
    return redirect("/contentmanager")
    

def contentdelete(request): #ลบข้อมูล
    id = request.POST['id']
    content = tb_news.objects.get(pk=id)
    content.delete()
    return redirect("/contentmanager")


# เกี่ยวกับระบบสมาชิก

def registeruser(request): #แสดงหน้า register
    return render(request,'Esportwebsite/registeruser.html')

def adduser(request): #บันทึกข้อมูล user
    fname = request.POST['fname']
    lname = request.POST['lname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']
    
    # ดัก validate
    if password == repassword :
        if User.objects.filter(username =username).exists():
            messages.error(request,"username มีคนใช้ไปแล้ว กรุณาลองใหม่อีกครั้ง !!")
            return redirect("/registeruser")
        elif User.objects.filter(email =email).exists():
            messages.error(request,"Email มีคนใช้ไปแล้ว กรุณาลองใหม่อีกครั้ง !!")
            return redirect("/registeruser")
        else:
                user = User.objects.create_user(
                    first_name =fname,
                    last_name = lname,
                    username= username,
                    email= email,
                    password = password
                )
                user.save()
                #messages.success(request,"บันทึกข้อมูลสำเร็จ!!")
                return redirect("/")
    
    else:
        messages.error(request,"Password ไม่ตรงกัน กรุณาตรวจสอบอีกครั้ง!!")
        return redirect("/registeruser")


def login(request): #แสดงหน้า login
    if request.user.is_authenticated :
        return redirect("/")
    return render(request,'Esportwebsite/login.html')

def logincheck(request): #login
    username = request.POST['username']
    password = request.POST['password']
    
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return redirect("/")
    else:
        messages.error(request,"username หรือ password ไม่ถูกต้อง")
        return redirect("/login")

def logoff(request): #logoff
    auth.logout(request)
    return redirect("/login")





def result(request): # HTTP POST #โยนข้อมูลไปหน้าบ้านจะต้องโยนเป็น dict เสมอ
    
    name = request.POST['name_news']
    detail = request.POST['detail_news']

    print(name)

    mydata ={
        'name_news' : name,
        'name_detail':detail,
    }
    return render(request,'Esportwebsite/result.html',mydata)