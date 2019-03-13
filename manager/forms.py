from django import forms
from manager.models import Department,Doctor,Staff,UserData

class DepartmentForm(forms.ModelForm):
    class Meta():
        model=Department
        exclude=["department_id","department_name","department_strength","department_location","department_head"]
class DoctorForm(forms.ModelForm):
    class Meta():
        model=Doctor
        exclude=["role_id","doctor_id","doctor_first_name","doctor_address","doctor_email","doctor_photo","doctor_phone","doctor_department","doctor_gender","doctor_dob","doctor_password",'doctor_last_name']
class StaffForm(forms.ModelForm):
    class Meta():
        model=Staff
        exclude=["role_id",'member_id','member_first_name','member_last_name','member_address','member_phone','member_image','member_email','member_gender','member_status','member_dob',"member_password"]
class MemberForm(forms.ModelForm):
    class Meta():
        model=UserData
        exclude=["role_id",'member_id','member_first_name','member_last_name','member_address','member_phone','member_image','member_email','member_gender','member_status','member_dob',"member_password"]
