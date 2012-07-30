
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Companie, Asset,FinancialNew,View 

#
def assets_list(request):
    assets = Asset.objects.all()
    t = loader.get_template('Stock/assets.html')
    c = Context({'assets':assets,'user': request.user})
    return HttpResponse(t.render(c))


def news_detail(request,id, showComments=False):
    news = Financial.objects.get(pk=id)


def year_archive(request, year):
    year_list = FinancialNew.objects.filter(pub_date__year=year)
    t = loader.get_template('Stock/year_archive.html')
    c = Context({'year_list':year_list,'user': request.user})
    return HttpResponse(t.render(c))

   # return render_to_response('Stock/year_archive.html', {'year': year, 'FinancialNew_list': a_list})


#@csrf_exempt	
def edit_comment(request,id):
   pass
'''
	comment = NewsComment.objects.get(pk=id)
	if request.user.username == '':
		return HttpResponseForbidden("You are logged out.<br/><a href='/reg/login'>CLICK TO LOGIN</a>")
	elif comment.author != request.user.username:
		return HttpResponseForbidden("You do not have permission to edit this comment<br/><a href='/blog/posts'>CLICK TO GET BLOGS</a>")
	if request.method == 'POST':
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(comment.post.get_absolute_url())
	else:
		form = CommentForm(instance=comment)
		
	return render_to_response('blog/edit_comment.html',{'comment':comment,'form':form,'user': request.user})
'''

#def update_database(request):
#	updateDatabase
'''
def import_data(request):
     import_dataa = get_ticker_data.objects.all()
     for data in import_dataa
     print data
'''
#def post_list(request):
    #post_list = Post.objects.all()
    #print type(post_list)
    #print post_list
    #return HttpResponse(post_list)

def post_detail(request, id, showComments=False):
    pass
    #posts = Post.objects.get(pk=id)
    #comments = posts.Comments.all()
    #return render_to_response('blog/post_detail.html',{'posts':posts,'comments':comments})
    
def post_search(request, term):
	if request.GET.get('search_item','') != '':
		term = request.GET.get('search_item','')
	news = Asset.objects.filter(index_Name__icontains=term) | Asset.objects.filter(index_Name__icontains=term)
	return render_to_response('Stock/post_search.html',{'news':news,'term':term,'user': request.user})

def home(request):
    return render_to_response('Stock/base.html',{'user': request.user})
