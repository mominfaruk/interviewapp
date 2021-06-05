from django.shortcuts import render
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.template.loader import render_to_string
from django.template import RequestContext, context
import json
# Create your views here.


class InterviewView(View):

    def post(self,request):
        message=[]
        my_form=InterviewForm(request.POST or None)
        if my_form.is_valid():
            title=my_form.cleaned_data['title']
            date=my_form.cleaned_data['date']
            if title=="":
                message.append('Title name shouldn\'t be empty')
            elif date=="":
                message.append('Date name shouldn\'t be empty')
            else:
                my_form.save()
                message.append('Interview added sucessfully')
                msg = render_to_string('messages.html', {'messages':message})
                all_list=InterviewModel.objects.all().order_by('-id')
                interviewlist=render_to_string('interview/interviewlistTbody.html', {'all_list':all_list})
                context={'msg':msg,'interviewlist':interviewlist}
                context=json.dumps(context)
                return HttpResponse(context,content_type='application/json')
    


def interviewlist(request):
    all_list=InterviewModel.objects.all().order_by('-id')
    return render(request, 'interview/interviewlist.html',{'all_list':all_list,'form':InterviewForm})

class interviewEdit(View):
    def get(self,request,pk):
        inter_view=InterviewModel.objects.get(pk=pk)
        my_form=InterviewForm(instance=inter_view)
        data=render_to_string('interview/interviewedit.html',{'form':my_form,'id':inter_view.id},request=request)
        #data={'id':inter_view.id,'title':inter_view.title,'date':inter_view.date}
        #return JsonResponse(data)
        return HttpResponse(data)
    
    def post(self,request,pk):
        message=[]
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
                message.append('Interview edited sucessfully')
                msg = render_to_string('messages.html', {'messages':message})
                row=render_to_string('interview/tablerow.html',{'list':inter_view},request=request)
                context={'msg':msg,'row':row}
                context=json.dumps(context)
                return HttpResponse(context,content_type='application/json')

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
            messages.info(request, 'Title name shouldn\'t be empty')
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