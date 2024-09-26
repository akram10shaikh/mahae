from django.shortcuts import render,redirect
from .models import Person_Detail, Document_ready
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import random

# Create your views here.
def home(request):
    return render(request,'index.html')

def person_detail(request):
    return render(request,'person.html')

def save_detail(request):
    '''Saving the record of the person'''
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        education = request.POST.get('education')
        university_name = request.POST.get('university_name')
        date_of_addmission = request.POST.get('date_of_addmission')
        date_of_leaving = request.POST.get('date_of_leaving')
        father_name = request.POST.get('father_name')
        aadhar_no = request.POST.get('aadhar')
        pan_no = request.POST.get('pan')
        photo = request.FILES['photo']
        user = request.user
        residential = request.POST.get('doc')
        data = Person_Detail.objects.create(first_name=first_name,second_name=second_name,last_name=last_name,father_name=father_name,date_of_birth=date_of_birth,gender=gender,phone_no=phone_no,address=address,city=city,state=state,pincode=pincode,education=education,university_name=university_name,date_of_addmission=date_of_addmission,date_of_leaving=date_of_leaving,aadhar_no=aadhar_no,pan_no=pan_no,photo=photo,user=user,doc_for=residential)
        data.save()
        request.session['person_id'] = data.no
        message = "Date is saved successfully"
        return render(request,'document.html',{'message':message})

def doc_detail(request):
    '''Sending the id of the person and detail'''
    id = request.session.get('person_id')
    person = Person_Detail.objects.get(no=id)
    if not person:
        return redirect('person_detail')
    return render(request,'document.html',{'message':id,'person':person})

def doc_save(request):
    '''Saving the documnets of the Persons'''
    id = request.session.get('person_id')
    person = Person_Detail.objects.get(no=id)
    if not person:
        return redirect('person_detail')
    if request.method == "POST":
        doc_aadhar = request.FILES['doc_aadhar']
        doc_pan = request.FILES['doc_pan']
        doc_tc = request.FILES['doc_tc']
        doc_election = request.FILES['doc_election']


        id = request.session.get('person_id')
        person = Person_Detail.objects.get(no=id)
        person.doc_aadhar = doc_aadhar
        person.doc_pan = doc_pan
        person.doc_tc = doc_tc
        person.doc_election = doc_election
        person.save()
        return redirect(doc_display)

def doc_display(request):
    '''Displying the documents of the persons'''
    id = request.session.get('person_id')
    files = Person_Detail.objects.get(no=id)

    return render(request,'display.html',{'file':files})


def login_user(request):
    '''Login User'''
    if request.method == "POST":
        username = request.POST.get('user')
        password = request.POST.get('password')

        use = authenticate(request,username=username,password=password)
        if use is not None:
            login(request,use)
            return render(request,'dashboard.html')
        else:
            message = "Wrong Username or Password"
            return render(request,"index.html",{'message':message})

def logout_user(request):
    '''Logout user'''
    logout(request)
    return render(request,'index.html')

def profile_detail(request):
    '''Profile detail to display'''
    return render(request,'profile.html')

def services(request):
    '''Serviece which is providing'''
    return render(request,'services.html')

def work(request):
    '''Work complated by the user'''
    user = request.user
    data = Person_Detail.objects.filter(user=user)
    return render(request,'work.html',{'data':data})

def check_work(request):
    '''Creating the work detail'''
    id = request.session['person_id']
    person = Person_Detail.objects.get(no=id)
    user = request.user
    Document_ready.objects.create(user=user,person=person)
    del request.session['person_id']
    data = Person_Detail.objects.filter(user=user)
    date = Document_ready.objects.filter(user=user)
    return render(request,'work.html',{'data':data,'date':date})

def nationality(request):
    '''Creating Nationality form'''
    return render(request,'nationality.html')


def print_n(request,id):
    '''Printing the Nationality'''
    data = Person_Detail.objects.get(no=id)
    serial = random.randint(999999,9999999)

    return render(request,'print_nationality.html',{'data':data,'serial':serial})

def print_residential(request,id):
    '''Printing the Residential Certificate'''
    data = Person_Detail.objects.get(no=id)
    serial = random.randint(999999,9999999)
    return render(request,'print_residential.html',{'data':data,'serial':serial})
