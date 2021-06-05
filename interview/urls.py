from django.urls import path
from .views import *
urlpatterns = [
    path('interview/',InterviewView.as_view(),name='interview'),
    path('',interviewlist,name='interviewlist'),
    path('interviewedit/<int:pk>/',interviewEdit.as_view(),name='interviewEdit'),
    path('interviewdelete/<int:pk>/',deleteInterview,name='interview_delete'),

    path('sessionlist/',sessionlist,name='session_list'),
    path('addsession/',AddSessionView.as_view(),name='session_add'),
    path('sessionwedit/<int:pk>/',sessionEdit.as_view(),name='sessionEdit'),
    path('sessiondelete/<int:pk>',deletesession,name='session_delete'),

]