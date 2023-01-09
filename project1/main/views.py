from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .forms import Image
from .db import *

# Create your views here.

def index(request):
    genre = 'All'
    return render(request, 'main\index.html', {'books': books, 'genres': genres, 'genre': genre, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def login(request):
    if request.method == 'POST':
        luser = request.POST

        for _user in users:
            if _user['login'] == luser['login'] and _user['password'] == luser['password']:
                global isLogin, isAdmin, user
                isLogin = True
                isAdmin = bool(_user['isAdmin'])
                user = _user
                
                return render(request, 'main\index.html', {'books': books, 'genres': genres, 'genre': genre, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
        return render(request, 'main/login.html', {'isFailed': True, 'genres': genres})
    else: return render(request, 'main/login.html', {'genres': genres})

def reg(request):
    if request.method == 'POST':
        ruser = request.POST
        form = Image(ruser, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = form.instance

            global users, user, isLogin, isAdmin

            for _user in users:
                if _user['login'] == ruser['login']:
                    return render(request, 'main/reg.html', {'form': Image, 'genres': genres})

            users.append({
                'login': ruser['login'],
                'password': ruser['password'],
                'isAdmin': False,
                'img': img_obj.image.url
            })

            isLogin = True
            isAdmin = False
            user = users[len(users) - 1]
            

            return render(request, 'main\index.html', {'books': books,  'genres': genres, 'genre': genre,  'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else: return render(request, 'main/reg.html', {'form': Image, 'genres': genres})

def Exit(request):
    global isAdmin, isLogin, user
    isAdmin = False
    isLogin = False
    user = None

    
    return render(request, 'main\index.html', {'books': books, 'genres': genres, 'genre': genre, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def Sort(request):
    global genre
    genre = request.POST['genre']
    
    return render(request, 'main\index.html', {'books': books, 'genres': genres, 'genre': genre, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    
def Search(request):
    resul = []

    for item in books:
        if str(item['genre']).lower() == request.POST['Search'].lower() or str(item['genre']).lower().__contains__(request.POST['Search'].lower()) or str(item['name']).lower() == request.POST['Search'].lower() or str(item['name']).lower().__contains__(request.POST['Search'].lower()):
            if genre != None and item['genre'] == genre:
                resul.append(item)
            else:
                resul.append(item)

    if len(resul) > 0:
        return render(request, 'main\index.html', {'books': resul, 'genres': genres, 'genre': genre, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:
        if genre == None:
            return render(request, "main\Error.html", {'error': "По запросу '" + request.POST['Search'] + "' ничего не найдено!"})
        else:
            return render(request, "main\Error.html", {'error': "В категории '" + genre + "' по запросу '" + request.POST['Search'] + "' ничего не найдено!"})

def Remove(request):
    name = request.POST['name']
    genre = request.POST['genre']

    _list = []

    for item in books:
        if item['name'] != name:
            _list.append(item)

    books.clear()
    for item in _list:
        books.append(item)

    CheckGeners()
    return render(request, 'main\index.html', {'books': books, 'genres': genres, 'genre': genre, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def About(request):
    if request.method == 'POST':
        pass
    else:
        book = GetBookByName(request.GET['name'])
        haveUserComment = False

        if user:
            for comment in book['comments']:
                if comment['user']['login'] == user['login']:
                    haveUserComment = True

        return render(request, 'main/about.html', {'user': user, 'isLogin': isLogin, 'haveUserComment': haveUserComment, 'genres': genres, 'book': book})

def Comment(request):
    if request.method == 'POST':
        for _book in books:
            if _book['name'] == request.POST['name']:
                _book['comments'].append({
                    'user': user,
                    'comment': request.POST['comment'],
                    'raiting': request.POST['raiting'],
                })
    
    book = GetBookByName(request.POST['name'])
    haveUserComment = False

    for comment in book['comments']:
        if comment['user']['login'] == user['login']:
            haveUserComment = True
    haveUserComment = False

    CheckRaiting()
    return render(request, 'main/about.html', {'user': user, 'isLogin': isLogin, 'haveUserComment': haveUserComment, 'genres': genres, 'book': book})


def Create(request):
    if request.method == 'POST':
        _book = request.POST

        if GetBookByName(_book['name']): 
            return render(request, 'main\index.html', {'books': books, 'genres': genres, 'genre': genre, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

        form = Image(_book, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = form.instance

            books.append({
                'name': _book['name'],
                'genre': _book['genre'],
                'author': _book['author'],
                'img': img_obj.image.url,
                'about': _book['about'],
                'comments': []
            })

        CheckGeners()
        return render(request, 'main\index.html', {'books': books, 'genres': genres, 'genre': genre, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:
        return render(request, 'main\create.html', {'genres': genres, 'form': Image, 'isLogin': isLogin, 'user': user})

def Change(request):
    if request.method == 'POST':
        _book = request.POST

        for book in books:
            if book['name'] == _book['oldName']:

                book['name'] = _book['name']
                book['author'] = _book['author']
                book['genre'] = _book['genre']
                book['img'] = _book['img']
                book['about'] = _book['about']

                break

        CheckGeners()
        return render(request, 'main\index.html', {'books': books, 'genres': genres, 'genre': genre, 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:
        for book in books:
            if book['name'] == request.GET['name']:
                return render(request, 'main\change.html', {'genres': genres, 'book': book, 'user': user, 'isLogin': isLogin})