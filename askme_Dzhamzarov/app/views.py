from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.db.models import Count

from app.models import Question, Answer, Tag


# Create your views here.

def paginate(object_list, request, per_page=10):
    page_num = request.GET.get('page', 1)
    try:
        if page_num is None:
            page_num = 1
        paginator = Paginator(object_list, per_page=per_page)
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

def index(request):
    questions = Question.objects.get_new()
    page = paginate(questions, request, 20)
    return render(
        request, template_name='index.html',
        context={'questions': page.object_list, 'page_obj': page}
    )

def hot(request):
    hot_questions = Question.objects.get_hot()
    page = paginate(hot_questions, request, 20)
    return render(
        request, template_name='hot_questions.html',
        context={'questions': page.object_list, 'page_obj': page}
    )

def question(request, question_id):
    quest = Question.objects.get_question(question_id)
    quest = quest.first()
    answer = Answer.objects.get_quest(question_id)
    page = paginate(answer, request, 30)
    return render(
        request, template_name='one_question.html',
        context={'item': quest, 'requestions' : page.object_list, 'page_obj': page}
    )

def ask(request):
    return render(request, template_name='ask.html')

def signup(request):
    return render(request, template_name='signup.html')

def login(request):
    return render(request, template_name='login.html')

def settings(request):
    return render(request, template_name='settings.html')

def tags(request, tag_id):
    questions = Question.objects.get_tag(tag_id)
    page = paginate(questions, request, 20)
    return render(
        request, template_name='tags.html',
        context={'questions': page.object_list, 'page_obj': page}
    )

