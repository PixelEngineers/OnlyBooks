from django.shortcuts import render

# Create your views here.
def landingPage(request):
    page = 'landing-page'
    return render(request,'app/landing_page.html', {
        "page": page
    })

def about(request):
    page = 'about'
    return render(request,'app/about.html', {
        "page": page
    })

def events(request):
    page = 'events'
    return render(request,'app/events.html', {
        "page": page
    })
