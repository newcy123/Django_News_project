from django.shortcuts import render,redirect
from django.http import HttpResponse #1 เพือเอาไปแสดงหน้าเว็บ
from .models import tb_news

# Create your views here.

def home(request): 
    return render(request,'Esportwebsite/home.html') #7 render(request,'Esportwebsite/index.html',mydata) ส่งข้อมูลไปยัง html

def addnews(request): # แสดงหน้า addnews
    return render(request,'Esportwebsite/addnew.html')

def addnewsdata(request): # บันทึก addnews
    news_title = request.POST['news_title']
    news_detail = request.POST['news_detail']
    news_photo = request.FILES['news_photo']
    
    content = tb_news(news_title=news_title,news_detail=news_detail,news_photo=news_photo)
    content.save()
    return redirect("/contentmanager") #เป็นชื่อฟังก์ชัน


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
    

def contentdelete(request):
    id = request.POST['id']
    content = tb_news.objects.get(pk=id)
    content.delete()
    return redirect("/contentmanager")


def result(request): # HTTP POST #โยนข้อมูลไปหน้าบ้านจะต้องโยนเป็น dict เสมอ
    
    name = request.POST['name_news']
    detail = request.POST['detail_news']

    print(name)

    mydata ={
        'name_news' : name,
        'name_detail':detail,
    }
    return render(request,'Esportwebsite/result.html',mydata)