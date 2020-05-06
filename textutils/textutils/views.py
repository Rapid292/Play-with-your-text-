# # I have created this file - Rishabh


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):

    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newremoveline = request.POST.get('newremoveline', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'is given below', 'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newremoveline == 'on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'After line removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char
        params = {'purpose': 'Extra spaces are removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc == 'on' or fullcaps == 'on' or newremoveline == 'on' or extraspaceremover == 'on'):
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("error")

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')