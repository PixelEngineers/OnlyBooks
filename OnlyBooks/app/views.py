import datetime

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
    events_data = [{
        "name": "Samuhik Sambhog",
        "description": "20 girls from E hostel + 5 boys from J hostel",
        "date": datetime.date(2024, 10, 6),
        "location": "Nirvana"
    }] * 3
    return render(request,'app/events.html', {
        "page": page,
        "events": events_data
    })

def books(request):
    page = 'books'
    books_data = [{
        "name": "John Doe's Biography",
        "author": "John Doe",
        "description": "John Doe's life history",
        "pages": 100,
        "tags": ["fiction", "sci-fi", "romance"]
    }] * 3
    return render(request,'app/books.html', {
        "page": page,
        "books": books_data
    })

def book(request, book_id):
    page = 'book'
    reviews = [{
        "message": "love this author's work",
        "rating": 5,
    }, {
        "message": "everything was amazing, but chapter 7 could have been better",
        "rating": 4,
    }]
    return render(request, 'app/book.html', {
        "page": page,
        "reviews": reviews
    })

def profile(request):
    page = 'profile'
    reviews = [{
        "message": "best shit ever",
        "rating": 5
    }, {
        "message": "what the hell is this",
        "rating": 1
    }]
    return render(request, 'app/profile.html', {
        "page": page,
        "reviews": reviews
    })