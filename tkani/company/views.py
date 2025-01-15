from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'company/about.html')


def delivery(request):
    return render(request, 'company/delivery.html')


def sewing(request):
    return render(request, 'company/sewing.html')