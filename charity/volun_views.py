from django.contrib.auth.models import User
from django.views.generic import TemplateView
from charity.models import Benefactorr,Benefactor_Report,volunteer_reg,Beneficiary,Beneficiary_Report, Request_Need, \
    Location,feedback, product_add
from django.shortcuts import redirect, render


class IndexView(TemplateView):
    template_name = 'volunteer/volunteer_index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        request=product_add.objects.filter(status1=1)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        donate=product_add.objects.filter(status1=1).count()
        admin=User.objects.get(is_superuser='1')
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        context['request']=request
        context['donate']=donate
        return context

class LogoutView(TemplateView):
    template_name = 'volunteer/volunteer_index.html'
    def get_context_data(self, **kwargs):
        context = super(LogoutView, self).get_context_data(**kwargs)
        request=product_add.objects.filter(status1=1)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        donate=product_add.objects.filter(status1=1).count()
        admin=User.objects.get(is_superuser='1')
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        context['request']=request
        context['donate']=donate
        return context

class Benefactor_View(TemplateView):
    template_name = 'volunteer/benefactor_view.html'

    def get_context_data(self, **kwargs):
        context = super(Benefactor_View,self).get_context_data(**kwargs)
        volun_id = User.objects.get(id=self.request.user.id)
        vol_location = volunteer_reg.objects.filter(user_id=volun_id)
        print(vol_location)
        context=super(Benefactor_View,self).get_context_data(**kwargs)
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
        for loc in  vol_location :
           bene_view = Benefactorr.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1',location=loc.location,status=0)
           print(bene_view)
           context['bene_view'] = bene_view
        return context

    def post(self,request,*args,**kwargs):
        volun_id = User.objects.get(id=self.request.user.id)
        vol_id =volunteer_reg.objects.get(user_id=volun_id.id)
        print(volun_id.id)
        reply = request.POST['reply']
        benefactor_id = request.POST['benefactor_id']
        print(benefactor_id)
        print(reply)
        benefactor = Benefactorr.objects.get(id=benefactor_id)
        benefactor.status=1
        benefactor.save()

        report = Benefactor_Report()
        report.benefactor_id_id = benefactor_id
        report.location =benefactor.location




        report.reply = reply

        report.save()
        return redirect(request.META['HTTP_REFERER'])


class Benefactor_list(TemplateView):
    template_name = 'volunteer/benefactor_list.html'
    def get_context_data(self, **kwargs):
        context = super(Benefactor_list,self).get_context_data(**kwargs)
        volun_id = User.objects.get(id=self.request.user.id)
        vol_location = volunteer_reg.objects.filter(user_id=volun_id)
        print(vol_location)
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

        for loc in  vol_location :
           location=loc.location
           print(location)
           bene_view = Benefactorr.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1',location=loc.location,status=1)

           print(bene_view)
           context['bene_view'] = bene_view
        return context

class Beneficiary_View(TemplateView):
    template_name = 'volunteer/beneficiary_view.html'
    def get_context_data(self, **kwargs):
        context = super(Beneficiary_View,self).get_context_data(**kwargs)
        volun_id = User.objects.get(id=self.request.user.id)
        vol_location = volunteer_reg.objects.filter(user_id=volun_id)
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
        for loc in  vol_location :
          bene_view = Beneficiary.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1',location=loc.location,status=0)
          print(bene_view)
          context['benefi_view'] = bene_view
        return context

    def post(self,request,*args,**kwargs):
        volun_id = User.objects.get(id=self.request.user.id)
        vol_id =volunteer_reg.objects.get(user_id=volun_id.id)
        print(volun_id.id)
        reply = request.POST['reply']
        beneficiary_id = request.POST['beneficiary_id']
        # print(benefactor_id)
        # print(reply)
        beneficiary = Beneficiary.objects.get(id=beneficiary_id)
        beneficiary.status=1

        beneficiary.save()

        report = Beneficiary_Report()
        report.beneficiary_id_id = beneficiary_id
        report.location =beneficiary.location


        report.reply = reply

        report.save()
        return redirect(request.META['HTTP_REFERER'])

class Beneficiary_list(TemplateView):
    template_name = 'volunteer/beneficiary_list.html'
    def get_context_data(self, **kwargs):
        context = super(Beneficiary_list,self).get_context_data(**kwargs)
        volun_id = User.objects.get(id=self.request.user.id)
        vol_location = volunteer_reg.objects.filter(user_id=volun_id)
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
        for loc in  vol_location :
          bene_view = Beneficiary.objects.filter(user__is_staff='0',user__is_active='1',location=loc.location,status=1)
          print(bene_view)
          context['benefi_view'] = bene_view
        return context

class view_requestedproduct_list(TemplateView):
    template_name = 'volunteer/view_requestedproduct_list.html'
    def get_context_data(self, **kwargs):
        context =super(view_requestedproduct_list,self).get_context_data(**kwargs)
        id = User.objects.get(id=self.request.user.id)
        vol=volunteer_reg.objects.get(user_id=id)
        reques =Request_Need.objects.filter(location=vol.location,status='0',need_status='apply')
        print(reques)
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
        context['Requested_items'] = reques
        return context
    def post(self , request,*args,**kwargs):
        product_id = request.POST['id']
        reply = request.POST['reply']
        id = User.objects.get(id=self.request.user.id)
        vol=volunteer_reg.objects.get(user_id=id)
        reques =Request_Need.objects.get(location=vol.location,status='0',id=product_id)
        reques.need_status=reply
        reques.volunteer_id=vol.id
        reques.save()
        return render(request,'volunteer/volunteer_index.html',{'message':"Successfully"})



class viewVolunteer(TemplateView):
    template_name = 'volunteer/view_volunteer.html'
    def get_context_data(self, **kwargs):
        context = super(viewVolunteer,self).get_context_data(**kwargs)
        id = User.objects.get(id=self.request.user.id)
        vol=volunteer_reg.objects.get(user_id=id)
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
        view_volun = volunteer_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1',location=vol.location)

        context['view_volun'] = view_volun
        return context

class viewProfile(TemplateView):
    template_name = 'volunteer/profile_view.html'
    def get_context_data(self, **kwargs):
        context = super(viewProfile,self).get_context_data(**kwargs)
        id = User.objects.get(id=self.request.user.id)
        vol=volunteer_reg.objects.get(user_id=id)
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
        context['donate']=donate
        context['locations'] = location

        # volunteer = volunteer_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1',location=vol.location)
        context['volunteer'] = vol
        return context

    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        homename = request.POST['home_name']
        cityname = request.POST['city_name']
        streetname = request.POST['street_name']
        Email= request.POST['email']
        qualification = request.POST['qualification']
        phone = request.POST['phone']
        Location = request.POST['location']
        # username = request.POST['username']
        user = User.objects.get(id=self.request.user.id,last_name='1')
        volunt=volunteer_reg.objects.get(user_id=user)
        user.first_name=name
        user.email=Email
        volunt.username=Email
        user.save()
        volunt.phone =phone
        volunt.Home_Address = homename
        volunt.City_Address = cityname
        volunt.Street_Address = streetname
        volunt.location= Location
        volunt.qualification=qualification
        volunt.save()
        return render(request,'volunteer/volunteer_index.html',{'message':"Update Successfully"})


class accepted_list(TemplateView):
    template_name = 'volunteer/Accepted_list.html'
    def get_context_data(self, **kwargs):
        context =super(accepted_list,self).get_context_data(**kwargs)
        id = User.objects.get(id=self.request.user.id)
        vol=volunteer_reg.objects.get(user_id=id)
        reques =Request_Need.objects.filter(location=vol.location,status='0',need_status='Accept')
        print(reques)
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
        context['Requested_items'] = reques
        return context

class donated_items(TemplateView):
    template_name = 'volunteer/donated_items.html'
    def get_context_data(self, **kwargs):
        context = super(donated_items, self).get_context_data(**kwargs)
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
        context['donate']=donate
        context['locations'] = location
        return context
class FEEDBACK(TemplateView):
    template_name = 'volunteer/feedback.html'
    def get_context_data(self, **kwargs):
        context = super(FEEDBACK, self).get_context_data(**kwargs)
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
        context['donate']=donate
        context['locations'] = location
        context['donate'] = donate
        return context
    def post(self , request,*args,**kwargs):
        USER = User.objects.get(id=self.request.user.id)
        Feedbak =request.POST['feedback']
        feed=feedback()
        feed.user_id=USER.id
        feed.feedback=Feedbak
        feed.save()
        return render(request,'volunteer/volunteer_index.html',{'message':"Add feedback Successfully"})

class ResourcesView(TemplateView):
    template_name = 'volunteer/resource_list.html'
    def get_context_data(self, **kwargs):
        context = super(ResourcesView, self).get_context_data(**kwargs)
        request=product_add.objects.filter(status=0)
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
        context['request']=request
        context['donate']=donate
        return context
    def post(self,request,*args,**kwargs):
        id = User.objects.get(id=self.request.user.id)
        vol=volunteer_reg.objects.get(user_id=id)
        status=request.POST['reply']
        Product=request.POST['product_id']
        Date=request.POST['date']
        product=product_add.objects.get(id=Product)
        product.status=status
        product.volunteer_id=vol.id
        product.collected_date=Date
        product.status1=1
        product.save()
        return render(request,'volunteer/volunteer_index.html',{'message':"Resource Accepted"})


class Acceptedresources(TemplateView):
    template_name = 'volunteer/accepted_resources.html'
    def get_context_data(self, **kwargs):
        context = super(Acceptedresources, self).get_context_data(**kwargs)
        request=product_add.objects.filter(status1=1)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        donate=product_add.objects.filter(status1=1).count()
        admin=User.objects.get(is_superuser='1')
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        context['request']=request
        context['donate']=donate
        return context