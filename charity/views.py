import re

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from django.contrib.auth import login, authenticate

# Create your views here.
from charity.models import Location, volunteer_reg, UserType, Beneficiary, Benefactorr


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context=super(IndexView,self).get_context_data(**kwargs)
        location = Location.objects.filter(status=1)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        context['locations'] = location
        return context

class Volunteer_Reg(TemplateView):
    template_name = 'volunteer_reg.html'
    def get_context_data(self, **kwargs):
        context = super(Volunteer_Reg, self).get_context_data(**kwargs)
        location = Location.objects.filter(status=1)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        context['locations'] = location
        return context
    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        homename = request.POST['home_name']
        cityname = request.POST['city_name']
        streetname = request.POST['street_name']
        image=request.FILES['image']
        fi=FileSystemStorage()
        filess=fi.save(image.name,image)
        proof=request.FILES['proof']
        fiii=FileSystemStorage()
        files=fiii.save(proof.name,proof)
        email= request.POST['email']
        qualification = request.POST['qualification']
        phone = request.POST['phone']
        Location = request.POST['location']
        # username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects._create_user(username=email,password=password,first_name=name,email=email,is_staff='0',last_name='0')
            user.save()
            Volunteer = volunteer_reg()
            Volunteer.user = user
            Volunteer.Home_Address=homename
            Volunteer.Street_Address=streetname
            Volunteer.City_Address=cityname
            Volunteer.image =filess
            Volunteer.password=password
            Volunteer.proof = files
            Volunteer.qualification= qualification
            Volunteer.phone = phone
            Volunteer.location = Location
            Volunteer.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "volunteer"
            usertype.save()
            # return redirect('warden_reg')
            return render(request,'index.html',{'message':"Registration Successfully"})
        except:
            messages = "Enter Another Username"
            return render(request, 'volunteer_reg.html', {'messages': messages})

class Benefactor_Reg(TemplateView):
    template_name = 'benefactor_reg.html'
    def get_context_data(self, **kwargs):
        context = super(Benefactor_Reg, self).get_context_data(**kwargs)
        location = Location.objects.filter(status=1)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        context['locations'] = location
        return context


    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        email = request.POST['email']
        PHONE= request.POST['phone']
        homename = request.POST['home_name']
        cityname = request.POST['city_name']
        streetname = request.POST['street_name']
        Location = request.POST['location']
        type1 = request.POST['type1']
        # username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects._create_user(username=email,password=password,email=email,first_name=name,is_staff='0',last_name='0')
            user.save()
            bene = Benefactorr()
            bene.user = user
            print(PHONE)
            bene.phone=PHONE
            bene.Home_Address = homename
            bene.City_Address = cityname
            bene.Street_Address = streetname
            bene.location= Location
            bene.type1 = type1
            bene.password=password
            bene.save()
            usertype = UserType()

            usertype.user = user
            usertype.type = "benefactor"
            usertype.save()
            return render(request,'index.html',{'message':"Registration Successfully"})
        except:
            messages = "Enter Another Username"
            return render(request, 'benefactor_reg.html', {'messages': messages})

class Beneficiary_Reg(TemplateView):
    template_name = 'beneficiary_reg.html'

    def get_context_data(self, **kwargs):
        context = super(Beneficiary_Reg, self).get_context_data(**kwargs)
        location = Location.objects.filter(status=1)
        context['locations'] = location
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        return context

    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        email = request.POST['email']
        homename = request.POST['home_name']
        cityname = request.POST['city_name']
        streetname = request.POST['street_name']
        phone= request.POST['phone']
        Location = request.POST['location']
        type1 = request.POST['type1']
        # username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects._create_user(username=email,password=password,email=email,first_name=name,is_staff='0',last_name='0')
            user.save()
            b = Beneficiary()
            b.user = user
            b.city_Address=cityname
            b.home_Address=homename
            b.street_Address=streetname
            b.phone =phone
            b.password=password
            b.location= Location
            b.type1 = type1
            b.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "beneficiary"
            usertype.save()
            return render(request,'index.html',{'message':"Registration Successfully"})
        except:

            messages = "Enter Another Username"
            return render(request, 'beneficiary_reg.html', {'messages': messages})
def isValid(s):
    Pattern = re.compile("^[7-9][0-9]{9}$")
    return Pattern.match(s)

class Login(TemplateView):
    template_name = 'login.html'
    def get_context_data(self, **kwargs):
        context=super(Login,self).get_context_data(**kwargs)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        return context

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        print(email)
        password= request.POST['password']
        print()
        user = authenticate(username=email,password=password)
        # det = User.objects.get(id=18)
        # det.last_name=1
        # det.save()

        if user is not None:

            login(request,user)
            if user.last_name == '1':

                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "volunteer":
                    return redirect('/volunteer')
                elif UserType.objects.get(user_id=user.id).type == "benefactor":
                    return redirect('/benefactor')
                else:
                    return redirect('/beneficiary')

            else:

                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:

            return render(request,'login.html',{'message':"Invalid Username or Password"})

class FrogotpasswordView1(TemplateView):
    template_name = 'forgot_password.html'
    def get_context_data(self, **kwargs):
        context=super(FrogotpasswordView1,self).get_context_data(**kwargs)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        admin=User.objects.get(is_superuser='1')
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['admin']=admin
        return context
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        print(name)

        email= request.POST['email']
        print(email)
        user_id=self.request.user.id
        if User.objects.filter(last_name='1',first_name=name,email=email):
           user=User.objects.get(last_name='1',first_name=name,email=email)
           Type=UserType.objects.get(user_id=user.id)
           if Type.type=='benefactor':
              benefactor=Benefactorr.objects.get(user_id=user.id)
              Password=benefactor.password
              email = EmailMessage(
              Password,
              'Your password',
              settings.EMAIL_HOST_USER,
              [user.email],
              )
              email.fail_silently = False
              email.send()
              return render(request,'index.html',{'message':"Send mail successfully"})
           elif Type.type=='beneficiary':

              beneficiary=Beneficiary.objects.get(user_id=user.id)
              print(user)
              email = EmailMessage(
              beneficiary.password,
              'Your password',
              settings.EMAIL_HOST_USER,
              [user.email],
               )
              email.fail_silently = False
              email.send()
              return render(request,'index.html',{'message':"Send mail successfully"})
           elif Type.type=='volunteer':

              volunteer=volunteer_reg.objects.get(user_id=user.id)
              print(user)
              email = EmailMessage(
              volunteer.password,
              'Your password',
              settings.EMAIL_HOST_USER,
              [user.email],
               )
              email.fail_silently = False
              email.send()
              return render(request,'index.html',{'message':"Send mail successfully"})

        else:
           return render(request,'index.html',{'message':"Tis User Is Not Exist"})













