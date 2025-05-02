from django.shortcuts import render,redirect,get_object_or_404
from .models import Insert,Update,Delete
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
def index(request):
    users_count = Insert.objects.count()
    update_count = Update.objects.count()
    del_count = Delete.objects.count()
    # print(users_count)
    return render(request,'Apps/index.html',{"users_count" :users_count,'updated_count':update_count,'del_count':del_count})


def insert(request):
    print('1')
    if request.method == 'POST':
        print('2')
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        
        if not username or not email or not password or not confirmpassword:
            print('3')
            messages.error(request, "Please fill All Requirements")
            return render(request,'Apps/insert.html')
        if password != confirmpassword:
            print('4')
            messages.error(request,"Password is Not Matching")
            return render(request,'Apps/insert.html')
        if Insert.objects.filter(email=email).exists() or Insert.objects.filter(username=username).exists():
            messages.error(request,"Your Email or User name already registered")
            return render(request,'Apps/insert.html')
        try:
            print('5')
            user = Insert()
            user.create_user(username=username,email=email,password=password)
            print('6')
            user.save()
            return redirect('/')
            # print(user)
            print('7')
             
           
              
        except Exception as error:
            # print('8')
            return render(request, 'Apps/insert.html',{'error': error})
   

    
    
    return render(request,'Apps/insert.html')

def update(request,user_id):
    # user = get_object_or_404(Insert,id=user_id)
    user = Insert.objects.get(id=user_id)

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        user.username = username
        user.save()
       
        up_users = Update()
        up_users.username = username
        up_users.email = email
        
        up_users.save()
        return redirect('/')
        

        
    
    return render(request,'Apps/update.html',{'user':user})

def updated(request):
    users = Insert.objects.all()
    updated = Update.objects.all()
    return render(request,'Apps/updated.html',{'users':users,'updated' : updated})    
    
    
    
def delete(request,user_id):
    user = get_object_or_404(Insert,id=user_id)
    if request.method == 'POST':
        del_user = Delete()
        del_user.save()
        user.delete()
        return redirect('/')
    
    return render(request,'Apps/delete.html',{'user':user})

def display(request):
    # print("1")
    users = Insert.objects.all()
    up = Update.objects.all()
   
    # print("2")
    # print(users)
    
    return render(request,'Apps/display.html',{'users' :users,'up' : up})
@login_required(login_url='/login/')
def home(request):
    return render(request, 'Apps/home.html')
