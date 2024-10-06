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
        "cover_link": "https://fastly.picsum.photos/id/83/300/500.jpg?hmac=xBw_i32ezzCcXFdm7P9L6RLda43HLOfcC-2K-xyl4Sk",
        "title": "Dumb ways to die",
        "author": "John Doe",
        "pages": 420,
        "tags": ["romance"],
        "book_id": 4,
    }] * 14
    return render(request,'app/books.html', {
        "page": page,
        "books": list(map(
             lambda book_data: map_ids(book_data),
             books_data
        ))
    })

def map_ids(data):
    rating = data.get("rating")
    if rating is not None:
        data["rating"] = [0] * rating # used to iterate in jinja
    user_id = data.get("user_id")
    if user_id is not None:
        data["user_link"] = f'/profile/{user_id}'
    book_id = data.get("book_id")
    if book_id is not None:
        data["book_link"] = f'/book/{book_id}'
    return data

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
    book_data = {
        "cover_link": "https://fastly.picsum.photos/id/83/300/500.jpg?hmac=xBw_i32ezzCcXFdm7P9L6RLda43HLOfcC-2K-xyl4Sk",
        "title": "Dumb ways to die",
        "author": "John Doe",
        "pages": 420,
        "tags": ["romance"]
    }
    return render(request, 'app/book.html', {
        "page": page,
        "book": book_data,
        "reviews": list(map(
            lambda review: map_ids(review),
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
    user_data = {
        "name": "John Doe",
        "favourite_tags": ["sci-fi", "romance"],
        "wishlisted_books": [{
            "link": 'book/0',
            "name": "Baby Shark"
        }, {
            "link": 'book/2',
            "name": "Mary had a little lamb"
        }]
    }
    return render(request, 'app/profile.html', {
        "page": page,
        "user_data": user_data,
        "reviews": list(map(
            lambda review: map_ids(review),
            reviews
        ))
    })