from django.shortcuts import render
from django.http import HttpResponse #1 เพือเอาไปแสดงหน้าเว็บ

# Create your views here.
#5 render(request,'Esportwebsite/index.html') ใช้ render แทน HttpResponse

def home(request): #โยนข้อมูลจะต้องโยนเป็น dict เสมอ
    return render(request,'Esportwebsite/index.html') #7 render(request,'Esportwebsite/index.html',mydata) ส่งข้อมูลไปยัง html

def addnews(request):
    return render(request,'Esportwebsite/addnew.html')

def result(request): # HTTP POST
    
    name = request.POST['name_news']
    detail = request.POST['detail_news']
    
    mydata ={
        'name_news' : name,
        'name_detail':detail,
    }

    return render(request,'Esportwebsite/result.html',mydata)