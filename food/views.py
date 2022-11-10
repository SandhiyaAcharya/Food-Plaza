from django.shortcuts import render,HttpResponse,redirect
from . import forms
from .models import Food,Customer,Admin,cart,Orders
from django.db import connection,transaction
from django.http import JsonResponse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

cursor=connection.cursor()

# Create your views here.
def home(request):
    return render(request,'base.html')

def addfood(request):
    form=forms.Foodform()
    if request.method=="POST":
        form=forms.Foodform(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save(commit=True)
                return redirect("/menu")
                print("saved")
            except:
                return HttpResponse("Error")
        else:
            food=forms.Foodform()
    return render(request,'addfood.html',{"form":form})

def addcustomer(request):
    cust=forms.Customerform()
    if request.method=="POST":
        cust=forms.Customerform(request.POST,request.FILES)
        if cust.is_valid():
            try:
                cust.save(commit=True)
                return redirect("/customer")
                print("saved")
            except:
                return HttpResponse("Error")
        else:
            cust=forms.Customerform()
    return render(request,'addcustomer.html',{"cust":cust})

def menu(request):
    mainmenu=Food.objects.all()
    return render(request, "menu.html", {"menu":mainmenu})

def customer(request):
    allcustomer=Customer.objects.all()
    return render(request, "customer.html", {"cust":allcustomer})

def update(request,id):
    data=Food.objects.get(foodId=id)
    if request.method == "POST":
        data=forms.Foodform(request.POST,request.FILES, instance=data)
        if data.is_valid():
            data.save()
            return redirect("/menu")
    return render(request,"update.html",{"data":data})

def updatecust(request,custid):
    custdata = Customer.objects.get(customerId=custid)
    if request.method == "POST":
        cdata = forms.Customerform(request.POST,instance=custdata)
        print(cdata)
        if cdata.is_valid():
            print("hello")
            cdata.save()
            return redirect("/customer")
    return render(request, "updatecust.html", {"cust": custdata})

def delete(request,id):
    data=Food.objects.get(foodId=id)
    data.delete()
    return redirect("/menu")

def deletecust(request,custid):
    custdata=Customer.objects.get(customerId=custid)
    custdata.delete()
    return redirect("/customer")

def login(request):
    return render(request,'login.html')

def doLogin(request):
    if request.method=="POST":
        userId=request.POST.get('userId','')
        passwd=request.POST.get('password','')
        utype=request.POST.get('type','')
        print("user=",userId,"pass=",passwd)
        if utype=="user":
            print("helloworld")
            for c in Customer.objects.raw('select * from Customer where customerName="%s" and customerPassword="%s"'%(userId,passwd)):
                print("helloworld")
                if c.customerName==userId:
                    print(c)
                    request.session['userId']=userId
                    return render(request, 'index.html',{'success':'Welcome'+c.customerName})
            else:
                return render(request,'login.html',{'failure':'login failed!! try again'})
        elif utype=="admin":
            for a in Admin.objects.raw('select * from Admin where adminName="%s" and adminPass="%s" ' %(userId,passwd)):
                a=Admin.objects.get(adminName=userId)
                if a.adminName==userId:
                    request.session['adminId']=userId
                    return render(request,'index.html',{'success':'login done'})
            else:
                return render(request,'login.html',{'failure':'login failed !! try again'})
    else:
        return render(request,'login.html')
         


def addtocart(request):
    fid =int(request.GET.get('foodId', ''))
    print(fid)
    data = Food.objects.get(foodId=fid)
    foodPrice = data.foodPrice
    sql='insert into cart(custEmail,fid,foodQty,total) values("%s","%d","%d","%d")'%(request.session['userId'],fid,1,foodPrice)
    cursor.execute(sql)
    transaction.commit()
    return JsonResponse({'done': 'true'})

def showcart(request):
    data=cart.objects.raw('select cartId,foodName,foodPrice,foodQty,total from Food as f inner join cart as c on f.foodId=c.fid where custEmail="%s"' % request.session['userId'])
    print(data)
    return render(request,'cart.html',{'mycart':data})

def updatequantity(request):
    id=int(request.POST['id'])
    q=int(request.POST.get('q'))
    p=int(request.POST.get('p'))
    print("id",id,"q",q,"p",p)
    s="update cart set foodQuantity='%d',total='%d' where cartId='%d'" % (q,p,id)
    cursor.execute(s)
    transaction.commit()
    return JsonResponse({'status': True})

def deletecart(request,id):
    data=cart.objects.get(cartId=id)
    data.delete()
    return redirect("/showcart")

def order(request):
    orderr = Orders()
    if request.method == "POST":
        price = request.POST.get('totalperprice')
        q = request.POST.get('foodQuantity')
        total = request.POST.get('Totalbill', '')
        date = datetime.datetime.now()
        print(total, "total")
        sql = "insert into Orders(custemail,date,totalbill) values('%s','%s','%s')" %(request.session['userId'],str(date),str(total))
        cursor.execute(sql)
        sql1 = "delete from Cart where custEmail='%s'" %(request.session['userId'])
        cursor.execute(sql1)
        transaction.commit()
        if price is '' and q is '':
            return render(request, "base.html", {'success': 'Cart is empty'})
        else:
            for o in Orders.objects.raw("select * from Orders where custemail='%s' and date='%s'" %(request.session['userId'], str(date))):
                orderr = o
    return render(request, "base.html", {'success':'order has been placed your orderid is "%d" and bill "%s"' %(orderr.orderid, orderr.totalbill)})

def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request,'index.html',{"success":'Logged out successfully..!!!'})

def changepass(request):
    if request.method == "POST":
        oldpass = request.POST.get("old")
        newpass = request.POST.get("new")
        print("user", request.session.keys())
        if request.session['userId']:
            sql = "update Customer set customerPassword='%s' where customerPassword='%s'" % (newpass, oldpass)
            cursor.execute(sql)
            transaction.commit()
            return redirect("/login")
        elif request.session['adminId']:
            sql = "update Admin set customerPassword='%s' where customerPassword='%s'" % (newpass, oldpass)
            cursor.execute(sql)
            transaction.commit()
            return redirect("/login")
    return render(request, "changepass.html")

def myorders(request):
    orders = Orders.objects.raw("select orderid, foodname, foodquant, foodprice, date, price from Food as f inner join orderSummary as o on f.foodId=o.foodId inner join Orders as o1 on o.ordId=o1.orderid where custemail='%s'" %(request.session['userId']))
    print(orders)
    return render(request,"myorder.html",{'orders':orders})

def graphs(request):
    food=Food.objects.all().count()
    cust=Customer.objects.all().count()
    order=Orders.objects.all().count()
    amount=Orders.objects.all().values_list('totalbill')
    '''
    totalam=0
    for i in amount:
        for j in i:
            totalam=totalam + j
            print(totalam)
    return render(request,"figure.html",{'food':food,'cust':cust,'order':order,'totalam':totalam})
    '''
    return render(request,"figure.html")


def graphone(request):
    orderall = "select orderid,custemail,totalbill,date from Orders"
    i = cursor.execute(orderall)
    df = pd.DataFrame(i, columns=["id", "email", "bill", "date"])
    cust = df.groupby('email').count().sort_values(by=['email'])
    plt.xticks(rotation=70)
    plt.plot(cust.index, cust['id'])
    plt.show()
    return render(request, "figure.html")

def graphtwo(request):
    customerall = "select customerAddress from Customer"
    i = cursor.execute(customerall)
    df = pd.DataFrame(i, columns=["address"])
    data=df.groupby("address")['address'].count()
    plt.pie(data,labels=data.index,autopct='%1.1f%%')
    plt.show()
    return render(request, "figure.html")

def graphthree(request):
    foodall = "select foodCat from Food"
    i = cursor.execute(foodall)
    df = pd.DataFrame(i, columns=["foodCat"])
    data=df.groupby("foodCat")['foodCat'].count()
    plt.bar(data.index,data)
    plt.show()
    return render(request, "figure.html")

def graphfour(request):
    orderall = "select totalbill,date from Orders"
    i = cursor.execute(orderall)
    df = pd.DataFrame(i, columns=["totalbill", "date"])
    data = df.groupby('date')['totalbill'].sum()
    plt.xticks(rotation=7)
    plt.plot(data.index,data)
    plt.title("Date Per Totalbill Plot")
    plt.xlabel("Date")
    plt.ylabel("Totalbill")
    plt.show()
    return render(request,"figure.html")











    


                    