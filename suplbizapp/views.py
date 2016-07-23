from django.core.context_processors import csrf

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, loader
from .models import Client
from .models import Provider
from .models import Region

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def company_p1(request):
    return render(request, 'company_p1.html', {})

def  search(request):	
	form = {}
	errors = []
	try:
		if request.method=='POST':
			form['client'] = request.POST.get('client')
			if not form['client']:
				errors.append('Errors')
			# print (form['client'])
			
			client = Client.objects.get(c_company_name=form['client']) #filter(company_name = form['client'])
			print (client.__unicode__())
			# print (client.c_regions.all())

			providers_list = set()
			providers_all = Provider.objects.all()
			for region in client.c_regions.all():
				for provider in providers_all:
					if provider.p_regions.filter(region_id=region.region_id):
						# print ("povider = ", provider)
						providers_list.add(provider)

			print (providers_list)
			

			template = loader.get_template('index.html')
			context = RequestContext(request, {'providers_list': providers_list,})
			return HttpResponse(template.render(context))
			return home(request)
	except Provider.DoesNotExist, Client.DoesNotExist:
	# 	return render(request, 'index.html', {})
		return home(request)
