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

def  search(request):	
	form = {}
	errors = []
	if request.method=='POST':
			form['client'] = request.POST.get('client')
			if not form['client']:
				errors.append('Errors')
	# print (form['client'])
			client = Client.objects.get(c_company_name=form['client']) #filter(company_name = form['client'])
			print (client.__unicode__())

			print (client.c_regions.all())

			try:
				providers_list = Provider.objects.all()

			# c_regions = client.objects.filter(client_id__region_id__isnull=False)
			# print (c_regions)

			# providers = Provider.objects.filter(p_regions__c_regions__isnull=False)

			# regions_search = Provider.objects.filter(p_regions=client_regions) 

				template = loader.get_template('index.html')
				context = RequestContext(request, {'providers_list': providers_list,})
				return HttpResponse(template.render(context))
			except Provider.DoesNotExist:
				return HttpResponseRedirect(request, 'home.html')