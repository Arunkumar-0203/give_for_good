from django.urls import path
from charity.admin_views import IndexView,View_Volunteer,ApproveView,RejectView,View_Details,Benefactor_Approve, \
    Beneficiary_Approve, benefactor_ApproveView, benefactor_RejectView,beneficiary_ApproveView,beneficiary_RejectView,Benefactor_View,Beneficiary_View, \
    add_locationsView, view_feedback, ReportView, IndexViews

urlpatterns = [

    path('',IndexView.as_view()),
    path('j',IndexViews.as_view()),
    path('view_volunteer',View_Volunteer.as_view()),
    path('view_details',View_Details.as_view()),
    path('approve',ApproveView.as_view()),
    path('reject',RejectView.as_view()),
    path('bene_approve',Benefactor_Approve.as_view()),
    path('Beneficiary_Approve',Beneficiary_Approve.as_view()),
    path('benefactor_approve',benefactor_ApproveView.as_view()),
    path('benefactor_reject',benefactor_RejectView.as_view()),
    path('beneficiary_approve',beneficiary_ApproveView.as_view()),
    path('beneficiary_reject',beneficiary_RejectView.as_view()),
    path('benefactor_view',Benefactor_View.as_view()),
    path('beneficiary_view',Beneficiary_View.as_view()),
    path('add_loacation',add_locationsView.as_view()),
    path('view_feedback',view_feedback.as_view()),
    path('ReportView',ReportView.as_view())


    ]
def urls():
    return urlpatterns, 'admin', 'admin'