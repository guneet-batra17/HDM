from django.conf.urls import url
from manager import views

app_name='manager'

urlpatterns=[
            url(r'^$',views.index,name="index"),
                url(r'^manager/$',views.manager,name="managerindex"),
                url(r'^departmentcreate/$',views.departmentcreate,name="departmentcreate"),
                url(r'^departmentview/$',views.departmentview,name="departmentview"),
                url(r'^departmentdelete/$',views.departmentdelete,name="departmentdelete"),
                url(r'^departmentupdate/$',views.departmentupdate,name="departmentupdate"),
                url(r'^doctorcreate/$',views.doctorcreate,name="doctorcreate"),
                url(r'^doctorview/$',views.doctorview,name="doctorview"),
                url(r'^doctordelete/$',views.doctordelete,name="doctordelete"),
                url(r'^doctorupdate/$',views.doctorupdate,name="doctorupdate"),
                url(r'^staffcreate/$',views.staffcreate,name="staffcreate"),
                url(r'^staffview/$',views.staffview,name="staffview"),
                url(r'^staffdelete/$',views.staffdelete,name="staffdelete"),
                url(r'^staffupdate/$',views.staffupdate,name="staffupdate"),
                url(r'^logout/$',views.logout,name="logout"),
                url(r'^changepassword/$',views.changepassword,name="changepassword")



            ]
