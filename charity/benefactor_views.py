from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.conf import settings

from charity.models import Benefactorr, Request_Need, product_add, volunteer_reg, Location, feedback, Beneficiary


class IndexView(TemplateView):
    template_name = 'benefactor/benefactor_index.html'
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
    template_name = 'benefactor/benefactor_index.html'
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


class Logout(TemplateView):
    template_name = 'admin_index.html'

# class viewrequestedproduct_list(TemplateView):
#     template_name = 'benefactor/view_requestedproduct_list.html'
#     def get_context_data(self, **kwargs):
#         context =super(viewrequestedproduct_list,self).get_context_data(**kwargs)
#         id = User.objects.get(id=self.request.user.id)
#         vol=Benefactorr.objects.get(user_id=id)
#         request =Request_Need.objects.filter(location=vol.location,status=1)
#         print(request)
#         context['Requested_items'] = request
#         return context

class  AddproductView(TemplateView):
    template_name = 'benefactor/add_product.html'
    def post(self,request,*args,**kwargs):
        id = User.objects.get(id=self.request.user.id)
        vol=Benefactorr.objects.get(user_id=id)
        benefactor_id=id.id
        view_volun = volunteer_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1',location=vol.location)
        for i in view_volun:
          email = EmailMessage(
          vol.user.first_name,
          'product added',
          settings.EMAIL_HOST_USER,
          [i.user.email],
          )
          email.fail_silently = False
          email.send()
        product = request.POST.getlist('checks[]')
        members=request.POST['members']
        exp_date =request.POST['expiry_date']
        location= request.POST['location']
        products= product_add()
        products.benefactor_id=vol.id
        products.location=location
        products.members=members
        products.expiry_date=exp_date
        products.products=product
        products.save()
        return render(request,'benefactor/benefactor_index.html',{'message':"Add Product Successfully"})


    def get_context_data(self, **kwargs):
        context = super(AddproductView, self).get_context_data(**kwargs)
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



class View_Volunteer(TemplateView):
    template_name = 'benefactor/view_volunteer.html'
    def get_context_data(self, **kwargs):
        context = super(View_Volunteer,self).get_context_data(**kwargs)
        id = User.objects.get(id=self.request.user.id)
        vol=Benefactorr.objects.get(user_id=id)

        view_volun = volunteer_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1',location=vol.location)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        donate=product_add.objects.filter(status1=1).count()
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        context['view_volun'] = view_volun
        context['donate']=donate
        return context

class ProfileView(TemplateView):
    template_name = 'benefactor/benefactor_profile.html'
    def get_context_data(self, **kwargs):
        context =super(ProfileView,self).get_context_data(**kwargs)
        id = User.objects.get(id=self.request.user.id,last_name='1')
        profile=Benefactorr.objects.get(user_id=id,status=1)
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
        bene=Benefactorr.objects.get(user_id=user,status=1)
        user.first_name=name
        user.email=Email
        user.username=username

        user.save()
        bene.phone =phone
        bene.Home_Address = homename
        bene.City_Address = cityname
        bene.Street_Address = streetname
        bene.location= Location
        bene.type1 = type1

        bene.save()
        return render(request,'benefactor/benefactor_index.html',{'message':"Update Successfully"})

class productStatus(TemplateView):
    template_name = 'benefactor/product_status.html'
    def get_context_data(self, **kwargs):
        context =super(productStatus,self).get_context_data(**kwargs)
        id = User.objects.get(id=self.request.user.id,last_name='1')
        profile=Benefactorr.objects.get(user_id=id,status=1)
        print(profile)
        product= product_add.objects.filter(benefactor_id=profile.id)
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
    template_name = 'benefactor/feedback.html'
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
        return render(request,'benefactor/benefactor_index.html',{'message':"Add feedback Successfully"})
class ReportView(TemplateView):
    template_name = 'benefactor/report.html'
    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        id = User.objects.get(id=self.request.user.id,last_name='1')
        benefactor=Benefactorr.objects.get(user_id=id,status=1)
        request=product_add.objects.filter(status1=1,benefactor_id=benefactor.id)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        donate=product_add.objects.filter(status1=1).count()
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['request']=request
        context['donate']=donate
        return context
class donateView(TemplateView):
    template_name = 'benefactor/donate.html'
    def get_context_data(self, **kwargs):
        context = super(donateView, self).get_context_data(**kwargs)
        id = User.objects.get(id=self.request.user.id,last_name='1')
        benefactor=Benefactorr.objects.get(user_id=id,status=1)
        request=product_add.objects.filter(status1=1,benefactor_id=benefactor.id)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        donate=product_add.objects.filter(status1=1).count()
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['request']=request
        context['donate']=donate
        return context
