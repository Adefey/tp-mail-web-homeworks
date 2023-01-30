from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import AskForm
from .models import *

best_tags = ["snakes", "milk", "furry", "love", "milking", "scalie"]
best_members = ["Amon", "Kyra", "Monique"]

def paginate(model_class, page_num, per_page=3):
    items = model_class.objects.filter(id__in=range((page_num-1)*per_page, page_num*per_page+1))
    return items

def index(request):
    return HttpResponseRedirect('/1')

def show_questions(request, id):
    items = paginate(Question, id)
    return render(request, 'main_site/index.html', {"items": items, "best_tags": best_tags, "best_members": best_members, "cur_page_num": id})

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
    comment.pk = 1
    comment.rating = 5
    comment.author = "Kyra"
    comment.full_text = "Просто бери и дои"
    return render(request, 'main_site/question.html', {"item": item, "answers": [comment, comment], "best_tags": best_tags, "best_members": best_members})


def ask(request):
    form = AskForm()
    return render(request, 'main_site/ask.html', {"best_tags": best_tags, "best_members": best_members, "form":form})


def tag(request, tag):
    item = Object()
    item.header = "Как подоить змею?"
    item.pk = 1
    item.rating = 10
    item.full_text = "У меня есть змейка и я хочу ее подоить но не знаю как, помогите"
    item.author = "FurryLover"
    item.tags = ["snakes", "milk", "furry", "love", "milking", "scalie", "milk",
                 "furry", "love", "milking", "scalie", "milk", "furry", "love", "milking", "scalie"]

    return render(request, 'main_site/tag.html', {"tag": tag, "items": [item, item], "best_tags": best_tags, "best_members": best_members, "cur_page_num": 1})


def settings(request):

    return render(request, 'main_site/settings.html', {"best_tags": best_tags, "best_members": best_members})


def register(request):
    return render(request, 'main_site/register.html', {"best_tags": best_tags, "best_members": best_members})


def login(request):
    return render(request, 'main_site/login.html', {"best_tags": best_tags, "best_members": best_members})

def send_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            header = form.cleaned_data['header']
            full_text = form.cleaned_data['full_text']
            tags = form.cleaned_data['tags']
            tags = tags.split(', ')
            user = User.create("avoknelok@mail.ru", "Anon", "14565")
            user.save()
            question = Question.create(header, full_text, user, tags)
            question.save()
    return HttpResponseRedirect('/')

