from django.shortcuts import render
# Create your views he
from .models import Student
from.models import QueryData
def home(request):

    return render(request,'app/home.html')

def base(request):
    guest="Guest"
    return render(request,'app/base.html',{'guest':guest})

def Signup(request):
    return render(request,'app/Signup.html')

def Login(request):
    return render(request,'app/Login.html')

def about(request):
    return render(request,'app/about.html')

def Contact(request):
    return render(request,'app/Contact.html')


def savedata(request):
    if request.method =='POST':
        name=request.POST['Name']
        email=request.POST['email']
        contact=request.POST['number']
        city=request.POST['city']
        password=request.POST['password']
        # cpassword = request.POST['cpassword']
          
        user = Student.objects.filter(email=email)

        if user: 
            message = "User already exist"
            return render(request,"app/Signup.html",{'msg':message})
        
        else:
            Student.objects.create(
            name=name,
            email=email,
            contact=contact,
            city=city,
            password=password
           )
            msg="user creation successfuly"
            return render(request, 'app/Login.html',{'data1':msg})

    else:
        msg="change method again post"
        return render(request, "app/Signup.html")

def Logindata(request):
     if request.method == "POST":
           email=request.POST['email']
           pwd=request.POST['password']

           user = Student.objects.filter(email=email)

           if user:
               data = Student.objects.get(email=email)
               if data.password == pwd:
                Name=data.name
                email=data.email
                number=data.contact
                city=data.city
               
                user={
                    'Name':Name,
                    'email':email,
                    'number':number,
                    'city':city,
                }

                return render(request,"app/dashboard.html",user)



def query(request):
    if request.method=='POST':
        qry_email=request.POST['email']
        qry_name=request.POST['Query']

        val=QueryData.objects.create(Query=qry_name, QueryEmail=qry_email)
        data = Student.objects.get(email=qry_email)
        Name=data.name
        email=data.email
        number=data.contact
        city=data.city
               
        user={
                    'Name':Name,
                    'email':email,
                    'number':number,
                    'city':city,
                }

        qnm=val.Query
        qel=val.QueryEmail

        print('Query',qnm)
        print('E-mail',qel)

        return render(request,'app/dashboard.html',user)
       

def showdata(request,pk):
    # print(pk)
    data=QueryData.objects.filter(QueryEmail=pk)
    return render(request,'app/showdata.html',{'key1':data})



def delete(request,pk):
    data=QueryData.objects.get(id=pk)
    email=data.QueryEmail
    data.delete()

    data=QueryData.objects.filter(QueryEmail=email)
    return render(request,'app/showdata.html',{'key1':data})


def edit(request,pk):
    data=QueryData.objects.get(id=pk)
    email=data.QueryEmail
    
    Signdata=Student.objects.get(email=email)
    Nm=Signdata.name,
    Eml=Signdata.email,
    cnt=Signdata.contact,
    pwd=Signdata.password

    Signdata={
        'name':Nm,
        'email':Eml,
        'contact':cnt,
        'password':pwd

    }
    all_data=Student.objects.filter(email=email)
    return render (request,'app/update.html',{'edit':data,'key1':all_data,'Signdata':Signdata})


def update(request,pk):
    updata=QueryData.objects.get(id=pk)
    updata.QueryEmail=request.POST['upEmail']
    updata.Query= request.POST['upQuery']
    updata.save()
    data2= Student.objects.get(email=updata.QueryEmail)

    Nm=data2.name,
    Eml=data2.email,
    cnt=data2.contact,
    pwd=data2.password

    Signdata={
        'name':Nm,
        'email':Eml,
        'contact':cnt,
        'password':pwd

    }
    all_data=QueryData.objects.filter(QueryEmail=updata.QueryEmail)
    return render (request,'app/showdata.html',{'key1':all_data,'Signdata':Signdata})