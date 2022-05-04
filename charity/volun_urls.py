from django.urls import path
from charity.volun_views import IndexView,Benefactor_View,Beneficiary_View, Benefactor_list, Beneficiary_list, \
    LogoutView, view_requestedproduct_list, viewVolunteer,  viewProfile, accepted_list, donated_items, feedback, \
    FEEDBACK, ResourcesView, Acceptedresources

urlpatterns = [

    path('',IndexView.as_view()),
    path('benefactor_view',Benefactor_View.as_view()),
    path('beneficiary_view',Beneficiary_View.as_view()),
    path('Benefactor_list',Benefactor_list.as_view()),
    path('Beneficiary_list',Beneficiary_list.as_view()),
    path('L',LogoutView.as_view()),
    path('view_requestedt',view_requestedproduct_list.as_view()),
    path('viewVolunteer',viewVolunteer.as_view()),
    path('viewProfile',viewProfile.as_view()),
    path('accepted_list',accepted_list.as_view()),
    path('donated_items',donated_items.as_view()),
    path('feedback',FEEDBACK.as_view()),
    path('ResourseView',ResourcesView.as_view()),
    path('Acceptedresources',Acceptedresources.as_view())



    ]
def urls():
    return urlpatterns, 'volunteer', 'volunteer'