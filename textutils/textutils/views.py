from email.policy import default
from ssl import Purpose
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render
from django.test import TestCase

# def cont_disp(request):
#     file = open('one.txt','r')
#     data=file.read()
#     return HttpResponse(data)

def index(request):
    return render (request, 'textutils/index.html')
    return HttpResponse('<h1>Home</h1> <h2><a href="http://127.0.0.1:8000/rempunc">Remove Punctuation</a> | <a href="http://127.0.0.1:8000/capfirst">Capitalize First</a> | <a href="http://127.0.0.1:8000/nlrem">Newline Remove</a> | <a href="http://127.0.0.1:8000/sprem">Space Remover</a> | <a href="http://127.0.0.1:8000/charcount">Character Counter</a></h2>')

def analyze(request):
    # Get the text
    text = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')
    
    # Check with checkbox is on 
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'textutils/analyze.html', params)
    
    elif(fullcaps == 'on'):
        analyzed = ''
        for char in text:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        return render(request, 'textutils/analyze.html', params)

    elif(newlineremover == 'on'):
        analyzed = ''
        for char in text:
            if char != '\n':
                analyzed = analyzed + char

        params = {'purpose': 'Newlines removed', 'analyzed_text': analyzed}
        return render(request, 'textutils/analyze.html', params)

    elif(extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(text):
            if text[index] == ' ' and text[index+1] == ' ':
                pass
            else:
                analyzed = analyzed +char

        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        return render(request, 'textutils/analyze.html', params)

    elif(charcounter =='on'):
        analyzed = str(len(text))

        params = {'purpose': 'Counted the chars', 'analyzed_text': analyzed}
        return render(request, 'textutils/analyze.html', params)


    else:
        return HttpResponse('Error')

# def capFirst(request):
#     return HttpResponse('<h1>Capitalize First</h1> <a href="http://127.0.0.1:8000/">Back</a>')

# def newlineRem(request):
#     return HttpResponse('<h1>Newline Remove</h1> <a href="http://127.0.0.1:8000/">Back</a>')

# def spaceRem(request):
#     return HttpResponse('<h1>Space Remover</h1> <a href="http://127.0.0.1:8000/">Back</a>')

# def charCount(request):
#     return HttpResponse('<h1>Character Counter</h1> <a href="http://127.0.0.1:8000/">Back</a>')