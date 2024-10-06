import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password


# Create your views here.
def landingPage(request):
    page = 'landing-page'
    books_data = [{
        "cover_link": "https://fastly.picsum.photos/id/83/300/500.jpg?hmac=xBw_i32ezzCcXFdm7P9L6RLda43HLOfcC-2K-xyl4Sk",
        "title": "Dumb ways to die",
        "author": "John Doe",
        "pages": 420,
        "tags": ["romance"],
        "book_id": 4,
    }] * 6
    return render(request, 'app/landing_page.html', {
        "page": page,
        "books": books_data,
    })


def about(request):
    page = 'about'
    return render(request, 'app/about.html', {
        "page": page
    })


def events(request):
    page = 'events'
    events_data = [{
        "name": "Author Meet and Greet",
        "description": "Meet Dr. John Doe for meet and greet session",
        "date": datetime.date(2024, 10, 7),
        "location": "Tan Building"
    }, {
        "name": "Speaker session by Dr. Phil",
        "description": "Join for an inspiring speaker session by Dr. Phil",
        "date": datetime.date(2024, 10, 8),
        "location": "LT-101"
    }, {
        "name": "Book Nerds hang out",
        "description": "Calling all book nerds, join us for a casual and fun hangout",
        "date": datetime.date(2024, 10, 9),
        "location": "OAT"
    }]
    return render(request, 'app/events.html', {
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
    }] * 6
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
        "name": "Ojesh Srivastav",
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


def login_view(request):
    if request.method != 'POST':
        return JsonResponse({})
    username = request.POST['username']
    password = request.POST['password']

    # Authenticate the user
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # Log in the user
        login(request, user)
        messages.success(request, "Login successful!")
    else:
        messages.error(request, "Invalid username or password.")
    return redirect('landing-page')

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('landing-page')

def signup_view(request):
    if request.method != 'POST':
        return JsonResponse({})
    username = request.POST['username']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    # Validate password match
    if password != confirm_password:
        messages.error(request, "Passwords do not match.")
        return redirect('signup')

    # Check if the username is already taken
    if User.objects.filter(username=username).exists():
        messages.error(request, "Username is already taken.")
        return redirect('signup')

    # Create and authenticate the user
    user = User.objects.create_user(username=username, password=password)
    user.save()

    # Automatically log in the user after signup
    login(request, user)
    messages.success(request, "Signup successful! You are now logged in.")
    return redirect('landing-page')  # Redirect to a relevant page after signup

def auth_view(request):
    if request.method != 'POST':
        return JsonResponse({})
    print(request.POST)
    if request.POST.get('confirm_password') is not None:
        return signup_view(request)
    return login_view(request)
