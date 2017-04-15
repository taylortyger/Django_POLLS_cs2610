from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-pub_date')
    context = {
        'question_list': question_list,
    }
    return render(request, 'polls/index.html', context)
    
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    
def vote(request, question_id):
    return HttpResponse("You are voting on question: %s" % question_id)
    
def results(request, question_id):
    return HttpResponse("Here lies the results of question %s." % question_id)
    