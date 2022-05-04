"""give_for_good URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from charity.views import IndexView,Volunteer_Reg,Login,Benefactor_Reg,Beneficiary_Reg, FrogotpasswordView1
from django.conf.urls.static import static
from give_for_good import settings
from charity import admin_urls,volun_urls,benefactor_urls,beneficiary_urls

urlpatterns = [
    path('admin/',admin_urls.urls()),
    path('volunteer/',volun_urls.urls()),
    path('benefactor/',benefactor_urls.urls()),
    path('beneficiary/',beneficiary_urls.urls()),
    path('', IndexView.as_view()),
    path('volunteer_reg',Volunteer_Reg.as_view()),
    path('login',Login.as_view()),
    path('benefactor_reg',Benefactor_Reg.as_view()),
    path('beneficiary_reg',Beneficiary_Reg.as_view()),
    path('FrogotpasswordView1',FrogotpasswordView1.as_view())

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
