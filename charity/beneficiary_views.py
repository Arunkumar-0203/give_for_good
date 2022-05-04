from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from charity.models import Benefactorr, Beneficiary, Benefactor_Report, Request_Need, Beneficiary_Report, Location, \
    volunteer_reg, feedback, product_add


class IndexView(TemplateView):
    template_name = 'beneficiary/beneficiary_index.html'
    def get_context_data(self, **kwargs):
        context=super(IndexView,self).get_context_data(**kwargs)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        donate=product_add.objects.filter(status1=1).count()
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        context['donate']=donate
        return context

class IndexViews(TemplateView):
    template_name = 'beneficiary/beneficiary_index.html'
    def get_context_data(self, **kwargs):
        context=super(IndexViews,self).get_context_data(**kwargs)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        donate=product_add.objects.filter(status1=1).count()
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        context['donate']=donate
        return context

class add_requestView(TemplateView):
    template_name = 'beneficiary/add_request.html'
    def get_context_data(self, **kwargs):
        context = super(add_requestView, self).get_context_data(**kwargs)
        location = Location.objects.filter(status=1)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        donate=product_add.objects.filter(status1=1).count()
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        context['locations'] = location
        context['donate']=donate
        return context
    def post(self,request,*args,**kwargs):

        id = User.objects.get(id=self.request.user.id)
        vol=Beneficiary.objects.get(user_id=id)
        view_volun = volunteer_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1',location=vol.location)

        for i in view_volun:
          email = EmailMessage(
          vol.user.first_name,
          'requested for needs',
          settings.EMAIL_HOST_USER,
          [i.user.email],
          )
          email.fail_silently = False
          email.send()
        product = request.POST.getlist('checks[]')
        print(product)
        members=request.POST['members']
        print(members)
        location= request.POST['location']
        print(location)
        products= Request_Need()
        products.benfi_id_id=vol.id
        products.location=location
        products.members=members
        products.product_need=product
        products.save()
        return render(request,'beneficiary/beneficiary_index.html',{'message':"Add need Successfully"})



class beneficiaryProfile(TemplateView):
    template_name = 'beneficiary/beneficiary_profile.html'
    def get_context_data(self, **kwargs):
        context =super(beneficiaryProfile,self).get_context_data(**kwargs)
        id = User.objects.get(id=self.request.user.id,last_name='1')
        profile=Beneficiary.objects.get(user_id=id,status=1)
        location = Location.objects.filter(status=1)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        donate=product_add.objects.filter(status1=1).count()
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        context['locations'] = location
        context['profile'] = profile
        context['donate']=donate
        return context
    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        Email = request.POST['email']
        phone= request.POST['phone']
        homename = request.POST['home_name']
        cityname = request.POST['city_name']
        streetname = request.POST['street_name']
        Location = request.POST['location']
        type1 = request.POST['type1']
        username = request.POST['username']
        user = User.objects.get(id=self.request.user.id,last_name='1')
        bene=Beneficiary.objects.get(user_id=user,status=1)
        user.first_name=name
        user.email=Email
        user.username=username

        user.save()
        bene.phone =phone
        bene.home_Address = homename
        bene.city_Address = cityname
        bene.street_Address = streetname
        bene.location= Location
        bene.type1 = type1

        bene.save()
        return render(request,'beneficiary/beneficiary_index.html',{'message':"Update Successfully"})

class needStatus(TemplateView):
    template_name = 'beneficiary/need_status.html'
    def get_context_data(self, **kwargs):
        context =super(needStatus,self).get_context_data(**kwargs)
        id = User.objects.get(id=self.request.user.id,last_name='1')
        profile=Beneficiary.objects.get(user_id=id,status=1)
        print(profile)
        product= Request_Need.objects.filter(benfi_id=profile.id,location=profile.location)
        print(product)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        donate=product_add.objects.filter(status1=1).count()
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        context['product'] = product
        context['donate']=donate
        return context

class FEEDBACK(TemplateView):
    template_name = 'beneficiary/feedback.html'
    def get_context_data(self, **kwargs):
        context=super(FEEDBACK,self).get_context_data(**kwargs)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        donate=product_add.objects.filter(status1=1).count()
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        context['donate']=donate
        return context

    def post(self , request,*args,**kwargs):
        USER = User.objects.get(id=self.request.user.id)
        Feedbak =request.POST['feedback']
        feed=feedback()
        feed.user_id=USER.id
        feed.feedback=Feedbak
        feed.save()
        return render(request,'beneficiary/beneficiary_index.html',{'message':"Add feedback Successfully"})
