from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context={'1':2}
    return render(request, 'testpwp/index.html',context)