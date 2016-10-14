from django.db import models
from django.utils import timezone
class Report(models.Model):
	report_date = models.DateField().primary_key=True
	last_report = models.FileField(upload_to='uploads/')
	GT11_0000 = models.DecimalField(max_digits=19, decimal_places=2)
	GT11_0700 = models.DecimalField(max_digits=19, decimal_places=2)
	GT11_1800 = models.DecimalField(max_digits=19, decimal_places=2)
	GT11_2400 = models.DecimalField(max_digits=19, decimal_places=2)
	UAT_0000 = models.DecimalField(max_digits=19, decimal_places=2)
	UAT_0700 = models.DecimalField(max_digits=19, decimal_places=2)
	UAT_1800 = models.DecimalField(max_digits=19, decimal_places=2)
	UAT_2400 = models.DecimalField(max_digits=19, decimal_places=2)
	SST_0000 = models.DecimalField(max_digits=19, decimal_places=2)
	SST_0700 = models.DecimalField(max_digits=19, decimal_places=2)
	SST_1800 = models.DecimalField(max_digits=19, decimal_places=2)
	SST_2400= models.DecimalField(max_digits=19, decimal_places=2)
	floweb_0000 = models.DecimalField(max_digits=19, decimal_places=2)
	floweb_2400 = models.DecimalField(max_digits=19, decimal_places=2)
	wbh_0000 = models.DecimalField(max_digits=19, decimal_places=2)
	wbh_2400 = models.DecimalField(max_digits=19, decimal_places=2)
	
	def save(self):
		self.save()
	

# Create your models here.
