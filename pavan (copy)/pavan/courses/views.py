from django.shortcuts import render

from django.http import HttpResponse

from .models import Question
# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, template_name='index.html', context=context)