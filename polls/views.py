from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import F
from .models import Question, Choice


#---------------------------------------------------------------------
#   index view
#       -front/main page of the app. 
#       -template: polls/index.html
#       -lists poll questions by publication date.
#---------------------------------------------------------------------
def index(request):
    question_list = Question.objects.order_by('-pub_date')
    return render(request, 'polls/index.html', {'question_list': question_list})


#---------------------------------------------------------------------
#   detail view
#       shows a poll question's details and provides an html form, 
#       allowing users to select a choice and vote.
#       template: polls/detail.html
#
#---------------------------------------------------------------------
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


#---------------------------------------------------------------------
#   vote view
#       Processes a vote sent by the voting form from the detail view.
#       Redirects to the results page for the poll when finished.
#---------------------------------------------------------------------    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # If the choice selected does not exists, return the user to the 
        # poll form with an appropriate error message.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Please select a valid choice.",
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


#-------------------------------------------------------------------
#   results view
#       View for displaying the results for a poll.
#       template: polls/results.html
#-------------------------------------------------------------------
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    