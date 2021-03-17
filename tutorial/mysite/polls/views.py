from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse
#from .apscheduler_handle import handle_scrapy_start,handle_scrapy_stop
from .apscheduler_handle import scrapy_scheduler

# Create your views here.

####### create scrapy scheduler object 
scheduler = scrapy_scheduler()

def run_background_app(request):
  context = {'header': 'My background app result'}
  #handle()
  scheduler.handle_scrapy_start()
  return render(request, 'background_app_result.html', context=context)

def run_background_app_stop(request):
  context = {'header': 'My background app result Stopped'}
  #handle()
  scheduler.handle_scrapy_stop()
  return render(request, 'background_app_result.html', context=context)
#######


def index_simple(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index_value(request):
  last_entries = Question.objects.all()
  return HttpResponse("Hello, world. You're at the polls index. %s" % len(last_entries))


def index(request):
  last_entries = Question.objects.all()
  context = {'last_entries': last_entries}
  return render(request, 'index.html', context=context)


class QuestionDetailView(generic.DetailView):
  model = Question
  template_name = 'detail.html'


class QuestionListView(generic.ListView):
  model = Question
  template_name = 'list.html'


class ChoiceListView(generic.ListView):
  model = Choice
  template_name = 'choice_list.html'


def detail(request, question_id):
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    '''
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #####    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">      POST['<name>] is <value>
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form. : render error message
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
      ##### save result
        ##### choice vote increment
        selected_choice.votes += 1
        selected_choice.save()
    ##### revese : call
        return HttpResponseRedirect(reverse('polls:result'), question_id)

        #return HttpResponse("You're voting on question %s." % question_id)
