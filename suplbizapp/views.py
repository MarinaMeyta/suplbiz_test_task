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

# def company_info(request, company_name):
def company_info(request, company_name):
	print (company_name)

	provider = Provider.objects.get(p_company_name=company_name)
 	regions = provider.p_regions.all()
	context = {
		'company_name': company_name,
		'regions': regions,
	}
	return render(request, 'company_info.html', context)
	
# 	print (company_name)
# 	provider = Provider.objects.get(p_company_name=company_name)
# 	regions = provider.p_regions.all()
# 	return render(request, 'company_template.html', {'regions': regions,}, {'company_name': company_name})

def  search(request):	
	form = {}
	errors = []
	
	try:
		if request.method=='POST':
			form['client'] = request.POST.get('client')
			if not form['client']:
				errors.append('Errors')
				print errors
				return home(request)
			

			client = Client.objects.get(c_company_name=form['client']) 
		

			print (client.__unicode__())


			providers_list = set()
			providers_all = Provider.objects.all()
			for region in client.c_regions.all():
				for provider in providers_all:
					if provider.p_regions.filter(region_id=region.region_id):
						print ("povider = ", provider)
						providers_list.add(provider)

			print (providers_list)
			
			template = loader.get_template('index.html')
			context = RequestContext(request, {'providers_list': providers_list,})
			return HttpResponse(template.render(context))
		return home(request)
		
	except Client.DoesNotExist:
		print ("omg")
		return home(request)
	# except Provider.DoesNotExist, Client.DoesNotExist:
	# 	print ('DoesNotExist')
	# 	# return render(request, 'index.html', {})
	# 	return HttpResponse(request, 'index.html', {})