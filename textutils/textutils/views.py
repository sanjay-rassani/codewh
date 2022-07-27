from email.policy import default
from django.http import HttpResponse
from django.shortcuts import render

# def cont_disp(request):
#     file = open('one.txt','r')
#     data=file.read()
#     return HttpResponse(data)

def home(request):
    return render (request, 'textutils/index.html')
    return HttpResponse('<h1>Home</h1> <h2><a href="http://127.0.0.1:8000/rempunc">Remove Punctuation</a> | <a href="http://127.0.0.1:8000/capfirst">Capitalize First</a> | <a href="http://127.0.0.1:8000/nlrem">Newline Remove</a> | <a href="http://127.0.0.1:8000/sprem">Space Remover</a> | <a href="http://127.0.0.1:8000/charcount">Character Counter</a></h2>')

def remPunc(request):
    print(request.GET.get('text', 'default'))
    return HttpResponse("<h1>Remove Punc</h1> <a href='http://127.0.0.1:8000/'>Back</a>")

def capFirst(request):
    return HttpResponse('<h1>Capitalize First</h1> <a href="http://127.0.0.1:8000/">Back</a>')

def newlineRem(request):
    return HttpResponse('<h1>Newline Remove</h1> <a href="http://127.0.0.1:8000/">Back</a>')

def spaceRem(request):
    return HttpResponse('<h1>Space Remover</h1> <a href="http://127.0.0.1:8000/">Back</a>')

def charCount(request):
    return HttpResponse('<h1>Character Counter</h1> <a href="http://127.0.0.1:8000/">Back</a>')