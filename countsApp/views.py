# Create your views here.

from django.http import HttpResponse

def index(request):
    """

    :param request:
    :return:
    """
    return HttpResponse("Hello, world. You're at the poll index.")