# -*- encoding:utf-8 -*-
#  Create your views here.

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views import generic

from .models import Question,Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """return the last  eight published questions;"""
        return Question.objects.order_by('-pub_date')[:8]


class DetailView(generic.ListView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.ListView):
    model = Question
    template_name = 'polls/results.html'


def vote(request,question_id):
    p = get_object_or_404(Question,pk=question_id)
    try:
        select_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':p,
            'error_message':"you didn't select a choice.",
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))



'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request,{
        'latest_question_list':latest_question_list,
    })
    return render(request,'polls/index.html',context)
    # # return HttpResponse(template.render(context))
    #output = ','.join([p.question_text for p in latest_question_list])
    # return HttpResponse("Hello,world. you're at the polls index.")
    #return HttpResponse(output)


def detail(request,question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #    raise Http404
    # return HttpResponse("you're looking at question %s "% question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    # response = "You're looking at the results of question %s ."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request,question_id):
    p = get_object_or_404(Question,pk=question_id)
    try:
        select_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':p,
            'error_message':"you didn't select a choice.",
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
'''





