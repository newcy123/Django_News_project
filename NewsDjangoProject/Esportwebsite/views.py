from django.shortcuts import render,redirect
from django.http import HttpResponse #1 เพือเอาไปแสดงหน้าเว็บ
from .models import tb_news

# Create your views here.
#5 render(request,'Esportwebsite/index.html') ใช้ render แทน HttpResponse

def home(request): #โยนข้อมูลจะต้องโยนเป็น dict เสมอ
    return render(request,'Esportwebsite/home.html') #7 render(request,'Esportwebsite/index.html',mydata) ส่งข้อมูลไปยัง html

def addnews(request):
    return render(request,'Esportwebsite/addnew.html')

def addnewsdata(request):
    news_title = request.POST['news_title']
    news_detail = request.POST['news_detail']
    news_photo = request.FILES['news_photo']
    
    content = tb_news(news_title=news_title,news_detail=news_detail,news_photo=news_photo)
    content.save()
    return redirect("/contentmanager") #เป็นชื่อฟังก์ชัน
    #return HttpResponse("บันทึกแล้ววว!!")

def contentmanager(request):
    datanews = tb_news.objects.all()
    
    mydatanews = {'news':datanews}
    print(datanews)
    return render(request,'Esportwebsite/contentnewsmanager.html',mydatanews)

def result(request): # HTTP POST
    
    name = request.POST['name_news']
    detail = request.POST['detail_news']

    print(name)

    mydata ={
        'name_news' : name,
        'name_detail':detail,
    }
    return render(request,'Esportwebsite/result.html',mydata)