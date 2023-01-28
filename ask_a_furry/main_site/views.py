from django.shortcuts import render
from django.http import HttpResponse


class Object:
    pass


def index(request):
    item = Object()
    item.header = "Как подоить змею?"
    item.pk = 1
    item.rating = 10
    item.full_text = "У меня есть змейка и я хочу ее подоить но не знаю как, помогите"
    item.author = "FurryLover"
    item.tags = ["snakes", "milk", "furry", "love", "milking", "scalie", "milk",
                 "furry", "love", "milking", "scalie", "milk", "furry", "love", "milking", "scalie"]
    best_tags = ["snakes", "milk", "furry", "love", "milking", "scalie"]
    best_members = ["Amon", "Kyra", "Monique"]
    return render(request, 'main_site/index.html', {"items": [item, item, item], "best_tags": best_tags, "best_members": best_members, "cur_page_num":1})

def question(request, id):
    item = Object()
    item.pk = 1
    item.rating = 10
    item.header = "Как подоить змею?"
    item.full_text = "У меня есть змейка и я хочу ее подоить но не знаю как, помогите"
    item.author = "FurryLover"
    item.tags = ["snakes", "milk", "furry", "love", "milking", "scalie", "milk",
                 "furry", "love", "milking", "scalie", "milk", "furry", "love", "milking", "scalie"]
    best_tags = ["snakes", "milk", "furry", "love", "milking", "scalie"]
    best_members = ["Amon", "Kyra", "Monique"]
    comment = Object()
    comment.pk=1
    comment.rating = 5
    comment.author = "Kyra"
    comment.full_text = "Просто бери и дои"
    return render(request, 'main_site/question.html', {"item":item, "answers":[comment, comment], "best_tags": best_tags, "best_members": best_members})

def ask(request):
    best_tags = ["snakes", "milk", "furry", "love", "milking", "scalie"]
    best_members = ["Amon", "Kyra", "Monique"]
    return render(request, 'main_site/ask.html', {"best_tags": best_tags, "best_members": best_members})

def tag(request, tag):
    item = Object()
    item.header = "Как подоить змею?"
    item.pk = 1
    item.rating = 10
    item.full_text = "У меня есть змейка и я хочу ее подоить но не знаю как, помогите"
    item.author = "FurryLover"
    item.tags = ["snakes", "milk", "furry", "love", "milking", "scalie", "milk",
                 "furry", "love", "milking", "scalie", "milk", "furry", "love", "milking", "scalie"]
    best_tags = ["snakes", "milk", "furry", "love", "milking", "scalie"]
    best_members = ["Amon", "Kyra", "Monique"]
    return render(request, 'main_site/tag.html', {"tag":tag, "items": [item, item], "best_tags": best_tags, "best_members": best_members, "cur_page_num":1})

def settings(request):
    best_tags = ["snakes", "milk", "furry", "love", "milking", "scalie"]
    best_members = ["Amon", "Kyra", "Monique"]
    return render(request, 'main_site/settings.html', {"best_tags": best_tags, "best_members": best_members})

def register(request):
    best_tags = ["snakes", "milk", "furry", "love", "milking", "scalie"]
    best_members = ["Amon", "Kyra", "Monique"]
    return render(request, 'main_site/register.html', {"best_tags": best_tags, "best_members": best_members})

def login(request):
    best_tags = ["snakes", "milk", "furry", "love", "milking", "scalie"]
    best_members = ["Amon", "Kyra", "Monique"]
    return render(request, 'main_site/login.html', {"best_tags": best_tags, "best_members": best_members})
