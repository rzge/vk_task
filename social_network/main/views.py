from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return render(request, 'main/index.html')



def search_results(request):
    query = request.GET.get('query')
    if not query:
        query = ""
    results = User.objects.filter(username__icontains=query)
    print(results)
    return render(request, 'main/search_results.html', {'results': results, 'query':query})