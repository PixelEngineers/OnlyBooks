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

def map_review(review):
    review["rating"] = '⭐' * review["rating"]
    user_id = review.get("user_id")
    if user_id is not None:
        review["user_link"] = f'/profile/{user_id}'
    book_id = review.get("book_id")
    if book_id is not None:
        review["book_link"] = f'/book/{book_id}'
    return review

def book(request, book_id):
    page = 'book'
    reviews = [{
        "message": "love this author's work",
        "rating": 5,
        "username": "Jerry Doe",
        "user_id": 1,
    }, {
        "message": "everything was amazing, but chapter 7 could have been better",
        "rating": 4,
        "username": "Jessi Doe",
        "user_id": 2,
    }]
    return render(request, 'app/book.html', {
        "page": page,
        "reviews": list(map(
            lambda review: map_review(review),
            reviews
        ))
    })

def profile(request, user_id):
    page = 'profile'
    reviews = [{
        "message": "best shit ever",
        "rating": 5,
        "book_name": "Baby Shark",
        "book_id": 0
    }, {
        "message": "what the hell is this",
        "rating": 1,
        "book_name": "Adult Shark",
        "book_id": 1
    }]
    username = "John Doe"
    return render(request, 'app/profile.html', {
        "page": page,
        "username": username,
        "reviews": list(map(
            lambda review: map_review(review),
            reviews
        ))
    })