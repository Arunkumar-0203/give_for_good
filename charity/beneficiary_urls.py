from django.urls import path
from charity.beneficiary_views  import IndexView,add_requestView, beneficiaryProfile, IndexViews, needStatus, FEEDBACK

urlpatterns = [

    path('',IndexView.as_view()),
    path('m',IndexViews.as_view()),
    path('add_requestView',add_requestView.as_view()),
    path('beneficiaryProfile',beneficiaryProfile.as_view()),
    path('needStatus',needStatus.as_view()),
    path('feedback',FEEDBACK.as_view())



    ]

def urls():
    return urlpatterns, 'benificiary', 'benificiary'