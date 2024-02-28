from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.
# from .middlewares import auth
#View for Register Page
def RegisterPage(request):
    return render(request,"app/register.html")

# View for user registration
def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        # First we will validate that user already exist
        user = User.objects.filter(Email=email)

        if user: 
            message = "User already exist"
            return render(request,"app/register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = User.objects.create(Firstname=fname,Lastname=lname,Email=email
                                    ,Contact=contact,Password=password)
                message = "User register Successfully"
                return render(request,"app/login.html",{'msg':message})
            else:
                message = "Password and Confirm Password Does not Match"
                return render(request,"app/register.html",{'msg':message})

#Login VIew
def LoginPage(request):
    return render(request,"app/login.html")

# Login User

def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Checking the emailid with database
        user = User.objects.filter(Email=email)
        if user:
            data = User.objects.get(Email=email)
            if data.Password == password:
                fname = data.Firstname
                lname = data.Lastname
                email = data.Email
                contact = data.Contact
                password = data.Password
                user={
                    'fname':fname,
                    'lname':lname,
                    'email':email,
                    'contact':contact,
                    'password':password,
                }
                return render(request,"app/home.html",{'user':user})
            else:
                message = "Password does not match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"app/register.html",{'msg':message})

def query(request,pk):
    # Data come from HTML to View
    email = request.POST['email']
    query = request.POST['query']
    Query.objects.create(Email=email,Query=query)
    
    data = User.objects.get(Email=pk)
    fname = data.Firstname
    lname = data.Lastname
    email = data.Email
    contact = data.Contact
    password = data.Password
    user={
        'fname':fname,
        'lname':lname,
        'email':email,
        'contact':contact,
        'password':password,
    }
    all_data=Query.objects.filter(Email=pk)
    return render(request,'app/home.html',{'key1':all_data,'user':user})
    # After Insert render on Show.html
    return render(request,"app/home.html")

def showdata(request,pk):
    #select * from tablename
    #for fetching all the data of the table
    data = User.objects.get(Email=pk)
    fname = data.Firstname
    lname = data.Lastname
    email = data.Email
    contact = data.Contact
    password = data.Password
    user={
        'fname':fname,
        'lname':lname,
        'email':email,
        'contact':contact,
        'password':password,
    }
    all_data=Query.objects.filter(Email=pk)
    return render(request,'app/home.html',{'key1':all_data,'user':user})


#Edit page view
def deleteData(request,pk):
    data = Query.objects.get(id=pk)
    email = data.Email
    data.delete()
    data = User.objects.get(Email=email)
    fname = data.Firstname
    lname = data.Lastname
    email = data.Email
    contact = data.Contact
    password = data.Password
    user={
        'fname':fname,
        'lname':lname,
        'email':email,
        'contact':contact,
        'password':password,
    }
    all_data=Query.objects.filter(Email=email)
    return render(request,'app/home.html',{'key1':all_data,'user':user})

def editPage(request,pk):
    #fetching the data of perticular ID
    data1=Query.objects.get(id=pk)
    email = data1.Email
    data = User.objects.get(Email=email)
    fname = data.Firstname
    lname = data.Lastname
    email = data.Email
    contact = data.Contact
    password = data.Password
    user={
        'fname':fname,
        'lname':lname,
        'email':email,
        'contact':contact,
        'password':password,
    }
    all_data=Query.objects.filter(Email=email)
    return render(request,'app/home.html',{'key1':all_data,'user':user,'key2':data1})

def updateData(request,pk):
    udata=Query.objects.get(id=pk)
    udata.Email=request.POST['email']
    udata.Query=request.POST['query']
    #Query for update
    udata.save()
    data = User.objects.get(Email=udata.Email)
    fname = data.Firstname
    lname = data.Lastname
    email = data.Email
    contact = data.Contact
    password = data.Password
    user={
        'fname':fname,
        'lname':lname,
        'email':email,
        'contact':contact,
        'password':password,
    }
    all_data=Query.objects.filter(Email=udata.Email)
    return render(request,'app/home.html',{'key1':all_data,'user':user})

def search(request,pk):
    print(pk)
    if request.method=="POST":
        search=request.POST['search']
        data = User.objects.get(Email=pk)
        fname = data.Firstname
        lname = data.Lastname
        email = data.Email
        contact = data.Contact
        password = data.Password
        user={
            'fname':fname,
            'lname':lname,
            'email':email,
            'contact':contact,
            'password':password,
        }
        # all_data=Query.objects.filter(Q(Email=email) & (Q(Query__contains=search) | Q(Email=search)))
        all_data=Query.objects.filter(Q(Email__contains=search) | Q(Query__contains=search) | Q(id=int(search)))
        return render(request,'app/home.html',{'key1':all_data,'user':user})


def logout(request):
    return render(request,'app/login.html')