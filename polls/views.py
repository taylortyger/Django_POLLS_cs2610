from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-pub_date')
    context = {
        'question_list': question_list,
    }
    return render(request, 'polls/index.html', context)
    
def detail(request, question_id):
    return HttpResponse("Well, you're looking at the details of question %s." % question_id)
    
def vote(request, question_id):
    return HttpResponse("You are voting on question: %s" % question_id)
    
def results(request, question_id):
    return HttpResponse("Here lies the results of question %s." % question_id)
    