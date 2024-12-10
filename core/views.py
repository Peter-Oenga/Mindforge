from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def data_analytics(request):
    return render(request, 'data_analytics.html')

def data_visualization(request):
    return render(request, 'data-visualization.html')

def big_data(request):
    return render(request, 'big-data.html')

def economic_analysis(request):
    return render(request, 'economic-analysis.html')

def data_analysis(request):
    return render(request, 'data-analysis.html')