from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from zakai.models import Product, Catalog
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.simple import direct_to_template


def index(request):
    catalogs = Catalog.objects.filter(parent=None)
    return render_to_response('index.html', {'catalogs': catalogs}, context_instance = RequestContext(request))

def view_catalogs(request):
    return view_catalog(request)

def view_catalog(request, slug=None):
    if slug:
        try:
            catalog = Catalog.objects.select_related().get(slug=slug)
        except Catalog.DoesNotExist:
            raise Http404
        childs = catalog.get_children()
        return render_to_response('catalog.html', {'catalog': catalog, 'childs': childs}, context_instance = RequestContext(request))
    else:
        catalogs = Catalog.objects.filter(parent=None)
        return render_to_response('catalogs.html', {'catalogs': catalogs}, context_instance = RequestContext(request))

#def ProductsAll(request):
#    products = Product.objects.all().order_by('en_name')
#    context = {'products': products}
#    return render_to_response('productsall.html',
#        context, context_instance = RequestContext(request))
#
def view_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {'product': product}
        return render_to_response('product.html',
            context, context_instance=RequestContext(request))
    except Product.DoesNotExist:
        raise Http404