from django.http import HttpResponse
from django.shortcuts import render

# def cont_disp(request):
#     file = open('one.txt','r')
#     data=file.read()
#     return HttpResponse(data)

def index(request):
    return render (request, 'textutils/index.html')
    return HttpResponse('<h1>Home</h1> <h2><a href="http://127.0.0.1:8000/rempunc">Remove Punctuation</a> | <a href="http://127.0.0.1:8000/capfirst">Capitalize First</a> | <a href="http://127.0.0.1:8000/nlrem">Newline Remove</a> | <a href="http://127.0.0.1:8000/sprem">Space Remover</a> | <a href="http://127.0.0.1:8000/charcount">Character Counter</a></h2>')

def analyze(request):
    # Get the text
    text = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    
    # Check with checkbox is on 
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        text = analyzed
        # return render(request, 'textutils/analyze.html', params)
    
    if(fullcaps == 'on'):
        analyzed = ''
        for char in text:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        text = analyzed
        # return render(request, 'textutils/analyze.html', params)

    if(newlineremover == 'on'):
        analyzed = ''
        for char in text:
            if char != '\n' and char!='\r':
                analyzed = analyzed + char

        params = {'purpose': 'Newlines removed', 'analyzed_text': analyzed}
        text = analyzed
        # return render(request, 'textutils/analyze.html', params)

    if(extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(text):
            if text[index] == ' ' and text[index+1] == ' ':
                pass
            else:
                analyzed = analyzed +char

        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        text = analyzed
        # return render(request, 'textutils/analyze.html', params)

    if(charcounter =='on'):
        analyzed = str(len(text))

        params = {'purpose': 'Counted the chars', 'analyzed_text': analyzed}
        
    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on' and charcounter!='on'):
        return HttpResponse('Error')
        
    # else:
    #     return HttpResponse('Error')

    return render(request, 'textutils/analyze.html', params)


# def capFirst(request):
#     return HttpResponse('<h1>Capitalize First</h1> <a href="http://127.0.0.1:8000/">Back</a>')

# def newlineRem(request):
#     return HttpResponse('<h1>Newline Remove</h1> <a href="http://127.0.0.1:8000/">Back</a>')

# def spaceRem(request):
#     return HttpResponse('<h1>Space Remover</h1> <a href="http://127.0.0.1:8000/">Back</a>')

# def charCount(request):
#     return HttpResponse('<h1>Character Counter</h1> <a href="http://127.0.0.1:8000/">Back</a>')