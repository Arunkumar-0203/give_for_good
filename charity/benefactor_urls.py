from django.urls import path

from charity.benefactor_views import IndexView,  Logout, AddproductView, View_Volunteer, \
    ProfileView, IndexViews, productStatus, FEEDBACK, ReportView, donateView

urlpatterns = [

    path('',IndexView.as_view()),
    path('i',IndexViews.as_view()),
    # path('viewrequestedproduct_list',viewrequestedproduct_list.as_view()),
    path('AddproductView',AddproductView.as_view()),
    path('View_Volunteer',View_Volunteer.as_view()),
    path('ProfileView',ProfileView.as_view()),
    path('productStatus',productStatus.as_view()),
    path('feedback',FEEDBACK.as_view()),
    path('ReportView',ReportView.as_view()),
    path('donateView',donateView.as_view())


    ]

def urls():
    return urlpatterns, 'benefactor', 'benefactor'