from django.shortcuts import render
from .models import Report
from . forms import ReportForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import openpyxl
import os

posts=Report.objects.all().order_by('wbh_0000')
def data_list(request):
	return render(request, 'report_sheet/data_list.html',{'posts':posts})
def report_new(request):
	if request.method =="POST":
		form = ReportForm(request.POST, request.FILES)
		if form.is_valid():
			a = form.cleaned_data['GT11_0000']
			b = form.cleaned_data['GT11_2400']
			c = form.cleaned_data['GT11_1800']
			f = form.cleaned_data['last_report']
			
			f2 = openpyxl.load_workbook(f)
			f3 = f2['DATA']
			
			fh=open('nm.txt','w')
			
			fh.write("%s %s \n %s %s \n %s %s \n %s %s" %(a, "GT11_0000",b,"GT11_1800",c,"GT11_2400",f3['C7'].value,"Data"))
           
			return render(request,'report_sheet/report_edit.html',{'form':form})
		#else:
			#return render(request,'report_sheet/report_new.html',{'form':form})
	
	else:

		form = ReportForm()
		context_data = {'form':form}
		
		return render(request,'report_sheet/report_edit.html',{'form':form})

# Create your views here.
