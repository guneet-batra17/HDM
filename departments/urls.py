from django.conf.urls import url
from departments import views

app_name='departments'

urlpatterns=[
            url(r'^$',views.index,name="index"),
            url(r'^departmentcreate/$',views.departmentcreate,name="departmentcreate")]
