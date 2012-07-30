from django.contrib import admin
from django.db import models
import datetime

#COMPANY MODEL
class Companie(models.Model): # 'Companie' because Django automatically adds an 's' to any class created
      companyName = models.CharField(max_length=100)
      companyIndex = models.CharField(max_length = 60)
      def __unicode__(self):
            return self.companyName
      

class CompanyAdmin(admin.ModelAdmin):
      list_display =('companyName','companyIndex')
      list_filter = ('companyName','companyIndex')
      search_fields = ('companyName','companyIndex')
      ordering = ('companyName','-companyIndex')


#ASSET MODEL   #want to relate this class to the company class but having troubles achieving it, since data is loader from gse.py 
class Asset(models.Model):
      volume_traded = models.BigIntegerField()
      price_per_share = models.FloatField()
      index_Name = models.CharField(max_length = 60)
      price_change_per_share =models.FloatField()
      #company_Name = models.OneToOneField(Companie, blank = 'True')
      def __unicode__(self):
            return self.index_Name

class AssetAdmin(admin.ModelAdmin):
      list_display =('index_Name','price_per_share','volume_traded','price_change_per_share')
      list_filter = ('index_Name','price_per_share')
      search_fields = ('index_Name','price_per_share')
      ordering = ('index_Name','-price_per_share')


'''
trying to get a class that would pick data from both asset and companie classes
class CompanyInfo(models.Model):
      Company_name =  models.ForeignKey(Companie)
      currentIndex = models.ForeignKey(Asset) 
      def __unicode__(self):
            return self.Company_name

class CompanyInfoAdmin(admin.ModelAdmin):
      list_display = ('Company_name','currentIndex')
      list_filter = ('Company_name','currentIndex')
      search_field = ('Company_name','currentIndex')
      ordering = ('Company_name','-currentIndex')
'''
'''     
will be used later
#ASSET TYPE MODEL
class AssetType (models.Model):
      forex = models.IntegerField()
      stock = models.FloatField()
      News = models.TextField()
  '''  

#Reporter Model
class Reporter(models.Model):
      full_name = models.CharField(max_length=70)
      def __unicode__(self):
		return self.full_name
#class ReporterAdmin

#Financial news model
class FinancialNew(models.Model):
      headline = models.CharField(max_length = 200)
      content   = models.TextField()
      pub_date = models.DateTimeField()
      reporter = models.ForeignKey(Reporter)
      def __unicode__(self):
		return self.headline
      def body_first_60(self):
		return self.content[:60]
      def get_absolute_url(self):
		return "/Stock/eureka/%i/true" % self.id
 

#model to post comments 
class View(models.Model):
	body = models.TextField()
	author = models.CharField(max_length=60)  
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)
	headline = models.ForeignKey(FinancialNew,related_name='comments')
        def __unicode__(self):
		return self.author
	def body_first_60(self):
		return self.body[:60]

class ViewAdmin(admin.ModelAdmin):
	list_display = ('author', 'body_first_60','date_created','date_updated')
	list_filter = ('date_created','author')
	

class ViewInline(admin.TabularInline):
	model = View

class FinancialNewsAdmin(admin.ModelAdmin):
	list_display = ('reporter','headline', 'content', 'pub_date')
	search_fields = ('reporter','headline')
	list_filter = ('reporter','pub_date')
	inlines = [ViewInline]

#admin.site.register(CompanyInfo,CompanyInfoAdmin)
admin.site.register(Reporter)
admin.site.register(Companie,CompanyAdmin)
admin.site.register(Asset,AssetAdmin)
admin.site.register(FinancialNew,FinancialNewsAdmin)
admin.site.register(View,ViewAdmin)

 

   
