from django.shortcuts import render
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

class InterviewView(View):
    def get(self,request):
        return render(request, 'interview.html',{'form':InterviewForm})

    def post(self,request):
        my_form=InterviewForm(request.POST)
        if my_form.is_valid():
            print('OK')
            title=my_form.cleaned_data['title']
            date=my_form.cleaned_data['date']
            if title=="":
                messages.info(request, 'Title name shouldn\'t be empty')
            elif date=="":
                messages.info(request, 'Date name shouldn\'t be empty')
            else:
                my_form.save()
                return HttpResponseRedirect('/')
                
    


def interviewlist(request):
    all_list=InterviewModel.objects.all()
    return render(request, 'interviewlist.html',{'all_list':all_list})

class interviewEdit(View):
    def get(self,request,pk):
        inter_view=InterviewModel.objects.get(pk=pk)
        my_form=InterviewForm(instance=inter_view)
        return render(request, 'interviewedit.html',{'form':my_form})
    
    def post(self,request,pk):
        inter_view=InterviewModel.objects.get(pk=pk)
        my_form=InterviewForm(request.POST,request.FILES,instance=inter_view)
        if my_form.is_valid():
            title=my_form.cleaned_data['title']
            date=my_form.cleaned_data['date']
            if title=="":
                messages.info(request, 'Title name shouldn\'t be empty')
            elif date=="":
                messages.info(request, 'Date name shouldn\'t be empty')
            else:
                my_form.save()
                return HttpResponseRedirect('/')

def deleteInterview(request,pk):
    instance = InterviewModel.objects.get(pk=pk)
    instance.delete()
    messages.info(request, 'Sucessfully deleted')
    return HttpResponseRedirect('/')


def sessionlist(request):
    all_list=Session.objects.all()
    return render(request, 'sessionlist.html',{'all_list':all_list})


class AddSessionView(View):
    def get(self,request):
        return render(request, 'addsession.html',{'form':SessionForm})

    def post(self,request):
        my_form=SessionForm(request.POST)
        if my_form.is_valid():
            title=my_form.cleaned_data['title']
            date=my_form.cleaned_data['date']
            applicant=my_form.cleaned_data['aplicant']
            if title=="":
                messages.info(request, 'Title name shouldn\'t be empty')
            elif date=="":
                messages.info(request, 'Date name shouldn\'t be empty')
            else:
                my_form.save()
                return HttpResponseRedirect('/sessionlist')
                

class sessionEdit(View):
    def get(self,request,pk):
        inter_view=Session.objects.get(pk=pk)
        my_form=SessionForm(instance=inter_view)
        return render(request, 'sessionedit.html',{'form':my_form})
    
    def post(self,request,pk):
        inter_view=Session.objects.get(pk=pk)
        my_form=SessionForm(request.POST,request.FILES,instance=inter_view)
        if my_form.is_valid():
            title=my_form.cleaned_data['title']
            date=my_form.cleaned_data['date']
            if title=="":
                messages.info(request, 'Title name shouldn\'t be empty')
            elif date=="":
                messages.info(request, 'Date name shouldn\'t be empty')
            else:
                my_form.save()
                return HttpResponseRedirect('/sessionlist')

def deletesession(request,pk):
    instance = Session.objects.get(pk=pk)
    instance.delete()
    messages.info(request, 'Sucessfully deleted')
    return HttpResponseRedirect('/sessionlist')