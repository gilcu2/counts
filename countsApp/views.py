# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

from countsApp.models import Count

def index(request):
    """

    :param request:
    :return:
    """
    latest_count_list = Count.objects.order_by('-last_update')[:5]
    template = loader.get_template('countsApp/index.html')
    context = RequestContext(request, {
        'latest_count_list': latest_count_list,
    })
    return HttpResponse(template.render(context))

def detail(request, count_id):
    return HttpResponse("You're looking at counts %s." % count_id)