# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
#from models import stock_data
from gse import get_ticker_data()
from django.shortcuts import render_to_response
#from models import Post, Comment 
#import datetime	

#def update_database(request):
#	updateDatabase

def import_data(request):
     import_dataa = get_ticker_data.objects.all()
     for data in import_dataa
     print data

#def post_list(request):
    #post_list = Post.objects.all()
    #print type(post_list)
    #print post_list
    #return HttpResponse(post_list)

#def post_detail(request, id, showComments=False):
    #posts = Post.objects.get(pk=id)
    #comments = posts.Comments.all()
    #return render_to_response('blog/post_detail.html',{'posts':posts,'comments':comments})
    
#def post_search(request, term):
    #posts = Post.objects.filter(title__contains=term)
    #return render_to_response('blog/post_search.html',{'posts':posts,'term':term})
    

'''
def post_search(request,term):
    word = str(term)+ ' NOT FOUND'
    return HttpResponse(word)
'''
#def home(request):
    #return render_to_response('blog/base.html',{})
