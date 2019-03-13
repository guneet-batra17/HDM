from django.conf.urls import url
from doctor import views

app_name='doctor'

urlpatterns=[
            url(r'^doctorindex$',views.doctorindex,name="doctorindex"),]
