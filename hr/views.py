from django.shortcuts import render

# Create your views here.

def hrHome(request):
    return render(request, 'hr/hrdashboard.html')

def post_job(request):
    return render(request, 'hr/postjob.html')