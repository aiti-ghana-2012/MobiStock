# Create your views here.
#from django.template import Context, loader
from django.http import HttpResponse
from models import stock_data
from gse import get_ticker_data
from StockEx.models import stock_data
from StockEx.gse import get_ticker_data
	

#def update_database(request):
#	updateDatabase
