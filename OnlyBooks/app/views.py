from django.shortcuts import render

# Create your views here.
def landingPage(request):
    page = 'landing-page'
    return render(request,'app/landing_page.html', {
        "page": page
    })

def About (request):
    return render(request,'app/about.html')