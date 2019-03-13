from django.shortcuts import render, HttpResponse,redirect
from manager.forms import DepartmentForm,DoctorForm,StaffForm
from manager.models import Department,Doctor,Staff,UserRole
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.hashers import PBKDF2SHA1PasswordHasher


def index(request):
    if request.method=="POST":
        uemail=request.POST['uemail']
        try:
            doctor=Doctor.objects.get(doctor_email=uemail)
            mail=doctor.doctor_email
            if(len(mail)>0):
                pass1=request.POST['upassword']
                pass2=doctor.doctor_password
                if(pass1==pass2):
                    request.session['email']=doctor.doctor_email
                    request.session['authenticated']=True
                    request.session['roleid']=doctor.role_id_id
                    return render(request,"doctorindex.html",{'name':doctor.doctor_first_name})
                else:
                    return render(request,"index.html",{'wrngpass':True})
            else:
                staff=Staff.objects.get(member_email=uemail)
                pass1=request.POST['upassword']
                pass2=staff.member_password
                if(pass1==pass2):
                    request.session['email']=staff.member_email
                    request.session['authenticated']=True
                    request.seesion['roleid']=staff.role_id_id
                    return render(request,"index.html",{'name':staff.member_first_name})
                else:
                    return render(request,"index.html",{'wrngpass':True})
        except:
            return render(request,"index.html",{'wrnguname':True})
    return render(request,"index.html")
def logout(request):
    request.session['authenticated']=False
    return redirect("/")
def changepassword(request):
    if request.method=="POST":
        if(request.session['roleid']==1):
            email=request.session['email']
            doctor=Doctor.objects.get(doctor_email=email)
            id=doctor.doctor_id
            password=doctor.doctor_password
            oldpassword=request.POST['oldpassword']
            if(password==oldpassword):
                newpassword=request.POST['newpassword']
                confirmpassword=request.POST['confirmpassword']
                if(newpassword==confirmpassword):
                    update=Doctor(doctor_id=id,doctor_password=newpassword)
                    update.save(update_fields=['doctor_password'])
                    name=doctor.doctor_first_name
                    return render(request,"changepassword.html",{'success':True,'name':name})
                else:
                    return render(request,"changepassword.html",{'wrngpass':True})
            else:
                return render(request,"changepassword.html",{'failed':True})
        else:
            email=request.session['email']
            staff=Staff.objects.get(member_email=email)
            id=staff.staff_id
            password=staff.member_password
            oldpassword=request.POST['oldpassword']
            if(password==oldpassword):
                newpassword=request.POST['newpassword']
                confirmpassword=request.POST['confirmpassword']
                if(newpassword==confirmpassword):
                    update=Staff(member_id=id,member_password=newpassword)
                    update.save(update_fields=['member_password'])
                    name=staff.member_first_name
                    return render(request,"changepassword.html",{'success':True,'name':name})
                else:
                    return render(request,"changepassword.html",{'wrngpass':True})
            else:
                return render(request,"changepassword.html",{'failed':True})
    return render(request,"changepassword.html")
def manager(request):
    return render(request,"managerindex.html")
def departmentcreate(request):
    if request.method=="POST":
        form=DepartmentForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.department_name=request.POST['department_name']
            f.department_strength=request.POST['department_strength']
            f.department_location=request.POST['department_location']
            f.department_head=request.POST['department_head']
            f.save()
            return render(request,"departmentcreate.html")
    return render(request,"departmentcreate.html")
def departmentview(request):
    department=Department.objects.all()
    return render(request,"departmentview.html",{'department':department})
def departmentdelete(request):
    id=request.GET['id']
    data=Department.objects.get(department_id=id)
    data.delete()
    return redirect("/departmentview/")
def departmentupdate(request):
    id=request.GET['id']
    ddata=Department.objects.get(department_id=id)
    if request.method=="POST":
        dname=request.POST['department_name']
        dstrength=request.POST['department_strength']
        dlocation=request.POST['department_location']
        dhead=request.POST['department_head']
        update=Department(department_id=id,department_name=dname,department_strength=dstrength,department_location=dlocation,department_head=dhead)
        update.save(update_fields=['department_name','department_strength','department_location','department_head'])
        return redirect("/departmentview/")
    return render(request,"departmentupdate.html",{'ddata':ddata})
def choosedoctordeparmtent(request):
    data=Department.objects.all()
    return render(request,"choosedoctordepartment.html",{'data':data})
def doctorcreate(request):
    data=Department.objects.all()
    if request.method=="POST":
        doctorimage=None
        if request.FILES:
            myfile = request.FILES['doctor_photo']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name,myfile)
            doctorimage=fs.url(filename)
            doctorimage=myfile.name
        form=DoctorForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            name=request.POST['doctor_last_name']
            name1=request.POST['doctor_first_name']
            address=request.POST['doctor_address']
            doctor=UserRole()
            doctor.role_id=1
            length=str(len(address))+str(len(name))+str(len(name1))
            password=str(name)+str(length)
            f.doctor_photo=doctorimage
            f.doctor_first_name=request.POST['doctor_first_name']
            f.doctor_last_name=request.POST['doctor_last_name']
            f.doctor_address=request.POST['doctor_address']
            f.doctor_phone=request.POST['doctor_phone']
            f.doctor_dob=request.POST['doctor_dob']
            f.doctor_email=request.POST['doctor_email']
            f.doctor_department_id=request.POST['doctor_department']
            f.doctor_gender=request.POST['doctor_gender']
            f.role_id=doctor
            f.doctor_password=password
            f.save()
            return render(request,"doctorcreate.html",{'data':data,'success':True})
        else:
             return render(request,"doctorcreate.html",{'data':data,'invalid':True})
    return render(request,"doctorcreate.html",{'data':data})

def doctorview(request):
    data=Doctor.objects.all()
    return render(request,"doctorview.html",{'data':data})
def doctordelete(request):
    id=request.GET['id']
    data=Doctor.objects.get(doctor_id=id)
    data.delete()
    return redirect("/doctorview/")
def doctorupdate(request):
    id=request.GET['id']
    doctordata=Doctor.objects.get(doctor_id=id)
    departmentdata=Department.objects.all()
    if request.method=="POST":
        doctor_photo=doctordata.doctor_photo
        if request.FILES:
            newfile=request.FILES['doctor_photo']
            fs=FileSystemStorage()
            filename=fs.save(newfile.name,newfile)
            doctor_photo=fs.url(filename)
            doctor_photo=newfile.name
        dname=request.POST['doctor_first_name']
        dlname=request.POST['doctor_last_name']
        daddress=request.POST['doctor_address']
        dphone=request.POST['doctor_phone']
        dgender=request.POST['doctor_gender']
        dimage=doctor_photo
        ddepartment=request.POST['doctor_department']
        update=Doctor(doctor_id=id,doctor_first_name=dname,doctor_last_name=dlname,doctor_address=daddress,doctor_gender=dgender,doctor_phone=dphone,doctor_photo=dimage,doctor_department_id=ddepartment)
        update.save(update_fields=['doctor_first_name','doctor_last_name','doctor_address','doctor_gender','doctor_phone','doctor_department_id','doctor_photo'])
        return redirect("/doctorview/")
    return render(request,"doctorupdate.html",{'data':departmentdata,'docdata':doctordata})
def staffcreate(request):
    if request.method=="POST":
        memberimage=None
        if request.FILES:
            myfile = request.FILES['member_image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name,myfile)
            memberimage=fs.url(filename)
            memberimage=myfile.name
        form=StaffForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            name=request.POST['member_first_name']
            name1=request.POST['member_last_name']
            address=request.POST['member_address']
            staff=UserRole()
            staff.role_id=2
            length=str(len(name))+str(len(name1))+str(len(address))
            password=str(name1)+str(length)
            f.member_image=memberimage
            f.member_first_name=request.POST['member_first_name']
            f.member_last_name=request.POST['member_last_name']
            f.member_address=request.POST['member_address']
            f.member_phone=request.POST['member_phone']
            f.member_email=request.POST['member_email']
            f.member_dob=request.POST['member_dob']
            f.member_gender=request.POST['member_gender']
            f.member_status=True
            f.role_id=staff
            f.member_password=password
            f.save()
            return render(request,"staffcreate.html",{'success':True})
        else:
            return render(request,"staffcreate.html",{'failed':True})
    return render(request,"staffcreate.html")

def staffview(request):
    mdata=Staff.objects.all()
    return render(request,"staffview.html",{'mdata':mdata})
def staffdelete(request):
    id=request.GET['id']
    data=Staff.objects.get(member_id=id)
    data.delete()
    return redirect("/staffview/")
def staffupdate(request):
    id=request.GET['id']
    mdata=Staff.objects.get(member_id=id)
    if request.method=="POST":
        member_image=mdata.member_image
        if request.FILES:
            newfile=request.POST['member_image']
            fs=FileSystemStorage()
            filename=fs.save(newfile.name,newfile)
            member_image=fs.url(filename)
            member_image=newfile.name
        mname=request.POST['member_name']
        mimage=member_image
        maddress=request.POST['member_address']
        mphone=request.POST['member_phone']
        mdob=request.POST['member_dob']
        mgender=request.POST['member_gender']
        update=Staff(member_id=id,member_name=mname,member_image=mimage,member_address=maddress,member_phone=mphone,member_dob=mdob,member_gender=mgender)
        update.save(update_fields=['member_name','member_image','member_address','member_phone','member_dob','member_gender'])
        return redirect("/staffview/")
    return render(request,"staffupdate.html",{'mdata':mdata})
def membercreate(request):
    if request.method=="POST":
        memberimage=None
        if request.FILES:
            myfile = request.FILES['member_image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name,myfile)
            memberimage=fs.url(filename)
            memberimage=myfile.name
        form=StaffForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            name=request.POST['member_first_name']
            name1=request.POST['member_last_name']
            address=request.POST['member_address']
            staff=UserRole()
            staff.role_id=2
            length=str(len(name))+str(len(name1))+str(len(address))
            password=str(name1)+str(length)
            f.member_image=memberimage
            f.member_first_name=request.POST['member_first_name']
            f.member_last_name=request.POST['member_last_name']
            f.member_address=request.POST['member_address']
            f.member_phone=request.POST['member_phone']
            f.member_email=request.POST['member_email']
            f.member_dob=request.POST['member_dob']
            f.member_gender=request.POST['member_gender']
            f.member_status=True
            f.role_id=staff
            f.member_password=password
            f.save()
            return render(request,"staffcreate.html",{'success':True})
        else:
            return render(request,"staffcreate.html",{'failed':True})
    return render(request,"staffcreate.html")
