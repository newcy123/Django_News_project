# เว็บไซต์จัดการข่าวสารเกี่ยวกับวงการ Esport

http://newcy123.pythonanywhere.com/

## **เทคโนโลยีที่ใช้พัฒนา**
```
python 3.8
Django Framework
Bootstrap
MySQL

```


## **การติดตั้งโปรเจคเริ่มต้น**
```
mkvirtualenv (ชื่อ env)
workon (ชื่อ env ที่มีการสร้าง)
pip install django
pip install mysqlclient
pip install pillow
django-admin startproject ชื่อโปรเจค
python manage.py startapp ชื่อapp
```


## **ติดตั้ง module เสริม เกี่ยวกับ texteditor**
```
pip install django-wysiwyg
pip install django-ckeditor
```


## **จัดการ Data base**
  - ใช้คำสั้งนี้ทุกครั้งเมือมีการ update database(models)
```
python manage.py makemigrations
python manage.py migrate
```


## **Run server**
  - เข้า virtaulenv ที่สร้างก่อนรัน server ทุกครั้ง ด้วยคำสั่ง
```
workon (ชื่อ env ที่มีการสร้าง)
python manage.py runserver
```
