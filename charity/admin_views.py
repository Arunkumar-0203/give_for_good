from django.views.generic import TemplateView
from charity.models import volunteer_reg, Benefactor_Report, Beneficiary_Report, Location, feedback, UserType, \
    Benefactorr, product_add, Beneficiary
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.base import View


class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        product=product_add.objects.filter(status1=1).count()
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['product']=product
        return context

class IndexViews(TemplateView):
    template_name = 'admin/admin_index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexViews, self).get_context_data(**kwargs)
        benefactor=Benefactorr.objects.filter(user__last_name='1').count()
        volunteer =volunteer_reg.objects.filter(user__last_name='1').count()
        beneficiary=Beneficiary.objects.filter(user__last_name='1').count()
        product=product_add.objects.filter(status1=1).count()
        context['benefactor'] = benefactor
        context['volunteer'] = volunteer
        context['beneficiary'] = beneficiary
        context['product']=product
        return context


class View_Volunteer(TemplateView):
    template_name = 'admin/view_volunteer.html'
    def get_context_data(self, **kwargs):
        context = super(View_Volunteer,self).get_context_data(**kwargs)

        view_volun = volunteer_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['view_volun'] = view_volun
        return context

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)

        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})

class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class View_Details(TemplateView):
    template_name = 'admin/volun_details.html'
    def get_context_data(self, **kwargs):
        context = super(View_Details,self).get_context_data(**kwargs)

        view_details = volunteer_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['view_details'] = view_details
        return context

class Benefactor_Approve(TemplateView):
    template_name = 'admin/benefactor_approve.html'
    def get_context_data(self, **kwargs):
        context =super(Benefactor_Approve, self).get_context_data(**kwargs)
        approve_view= Benefactor_Report.objects.filter(status=0,reply='Accept')
        print(approve_view)
        context['approve_details']=approve_view
        return context

class Beneficiary_Approve(TemplateView):
    template_name = 'admin/beneficiary_approve.html'
    def get_context_data(self, **kwargs):
        context =super(Beneficiary_Approve, self).get_context_data(**kwargs)
        approve_view= Beneficiary_Report.objects.filter(status=0,reply='Accept')
        print(approve_view)
        context['approve_details']=approve_view
        return context





class benefactor_ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        Benefactor =Benefactor_Report.objects.get(benefactor_id__user__id=id)
        Benefactor.status=1
        user.last_name='1'
        user.save()
        Benefactor.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})

class benefactor_RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='0'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class beneficiary_ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        Beneficiary =Beneficiary_Report.objects.get(beneficiary_id__user__id=id)
        Beneficiary.status=1
        user.last_name='1'
        user.save()
        Beneficiary.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})

class beneficiary_RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='0'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class Benefactor_View(TemplateView):
    template_name = 'admin/benefactor_view.html'
    def get_context_data(self, **kwargs):
        context =super(Benefactor_View, self).get_context_data(**kwargs)
        approve_view= Benefactor_Report.objects.filter(status=1)
        print(approve_view)
        context['approve_view']=approve_view
        return context

class Beneficiary_View(TemplateView):
    template_name = 'admin/beneficiary_view.html'
    def get_context_data(self, **kwargs):
        context =super(Beneficiary_View, self).get_context_data(**kwargs)
        view_benefi_details= Beneficiary_Report.objects.filter(status=1)
        print(view_benefi_details)
        context['view_benefi_details']=view_benefi_details
        return context

class add_locationsView(TemplateView):
    template_name = 'admin/add_locations.html'
    def post(self,request,*args,**kwargs):
        loc = request.POST['location']
        L=Location()
        L.location=loc
        L.save()
        return redirect(request.META['HTTP_REFERER'])
    def get_context_data(self, **kwargs):
        context =super(add_locationsView, self).get_context_data(**kwargs)
        loc= Location.objects.filter(status=1)
        context['location']=loc
        return context

class view_feedback(TemplateView):
    template_name = 'admin/view_feedback.html'
    def get_context_data(self, **kwargs):
        context =super(view_feedback, self).get_context_data(**kwargs)
        feed= feedback.objects.all()
        for i in feed:
            TYPE=UserType.objects.all()
            for j in TYPE:
               TYPE=UserType.objects.get(user_id=j.user_id)
               id=TYPE.user_id
               Type=i.user_id
               if id==Type:
                 TYPE=UserType.objects.get(user_id=id)
                 fd=TYPE.type
                 context['type']=fd
        context['feedback']=feed
        return context

class ReportView(TemplateView):
    template_name = 'admin/report.html'
    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        report=product_add.objects.filter(status1=1)
        context['report']=report
        print(report)
        return context