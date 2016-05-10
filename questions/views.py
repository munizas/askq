from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Question

def categories(request):
	return render(request, 'categories.html')

def question(request, category="Travel"):
	questions = Question.objects.filter(category__name=category)
	question = random.choice(questions)
	context = {'content': question}
	return render(request, 'question.html', context)
