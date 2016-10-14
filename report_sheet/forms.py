from django import forms
from . models import Report

#class ReportForm(forms.ModelForm):
#	class Meta:
#		model = Report
	#	fields = ('last_report','GT11_0000','GT11_0700','GT11_1800','GT11_2400','UAT_0000','UAT_0700','UAT_1800','UAT_2400','SST_0000','SST_0700','SST_1800','SST_2400','floweb_0000','floweb_2400','wbh_0000','wbh_2400')
		
class ReportForm(forms.Form):
	last_report = forms.FileField()
	GT11_0000 = forms.DecimalField( initial ='0098',disabled =True, label= 'GT11 0000', max_digits=19, decimal_places=2)
	GT11_0700 = forms.DecimalField(max_digits=19, decimal_places=2, help_text = 'Kindly insert energy reading at 00:00 hours',)
	GT11_1800= forms.DecimalField(max_digits=19, decimal_places=2)
	GT11_2400 = forms.DecimalField(max_digits=19, decimal_places=2)
	UAT_0000 = forms.DecimalField(max_digits=19, decimal_places=2)
	UAT_0700 = forms.DecimalField(max_digits=19, decimal_places=2)
	UAT_1800= forms.DecimalField(max_digits=19, decimal_places=2)
	UAT_2400 = forms.DecimalField(max_digits=19, decimal_places=2)
	SST_0000 =forms.DecimalField(max_digits=19, decimal_places=2)
	SST_0700 = forms.DecimalField(max_digits=19, decimal_places=2)
	SST_1800 = forms.DecimalField(max_digits=19, decimal_places=2)
	SST_2400 = forms.DecimalField(max_digits=19, decimal_places=2)
	floweb_0000 = forms.DecimalField(max_digits=19, decimal_places=2)
	floweb_2400 = forms.DecimalField(max_digits=19, decimal_places=2)
	wbh_0000 = forms.DecimalField(max_digits=19, decimal_places=2)
	wbh_2400 = forms.DecimalField(max_digits=19, decimal_places=2)
	