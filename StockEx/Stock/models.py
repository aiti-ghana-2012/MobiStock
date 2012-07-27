from django.db import models
from django.contrib import admin
#import gse
import datetime

# Create your models here.
#class stock_data(models.Model):
#	company_name = models.CharField(max_length=60)
#	index_name = models.CharField(max_length=15,blank=True)
#	volume_traded = models.IntegerField(blank=True)
#	price_per_share = models.FloatField(blank=True)
#	price_change_per_share= models.FloatField(blank=True)
		
#	def __unicode__(self):
#		return self.company_name

#admin.site.register(stock_data)

#COMPANY MODEL
class Companie(models.Model):
      companyName = models.CharField(max_length=100)
      companyIndex = models.CharField(max_length=60)
      #lowForYear = models.FloatField()
      #highForYear = models.FloatField()
      #dateCreated = models.DateField(auto_now = True)
      #dateUpdated = models.DateField(auto_now_add = True)
      def __unicode__(self):
            return self.companyName
      

class CompanyAdmin(admin.ModelAdmin):
      list_display =('companyName','companyIndex')
      list_filter = ('companyName','companyIndex')
      search_fields = ('companyName','companyIndex')
      ordering = ('companyName','-companyIndex')


#ASSET MODEL
class Asset(models.Model):
      volume_traded = models.BigIntegerField()
      price_per_share = models.FloatField()
      index_Name = models.CharField(max_length = 60)
      price_change_per_share =models.FloatField()
    
      def __unicode__(self):
            return self.symbol

class AssetAdmin(admin.ModelAdmin):
      list_display =('index_Name','price_per_share','volume_traded','price_change_per_share')
      list_filter = ('index_Name','price_per_share')
      search_fields = ('index_Name','price_per_share')
      ordering = ('index_Name','-price_per_share')
'''     
will be used later
#ASSET TYPE MODEL
class AssetType (models.Model):
      forex = models.IntegerField()
      stock = models.FloatField()
      News = models.TextField()
  '''  

admin.site.register(Companie,CompanyAdmin)
admin.site.register(Asset,AssetAdmin) 


