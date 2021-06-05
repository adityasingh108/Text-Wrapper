# Created By me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def anlyze(request):
    # Get the text from user with the help of  method of Get
    user_text = request.POST.get('text', 'default')

    # chek Chekbox vlaue
    user_chek_punc = request.POST.get('removepunc', 'off')
    user_chek_upper = request.POST.get('upper_text', 'off')
    user_chek_newline = request.POST.get('newline', 'off')
    user_chek_spaceremover = request.POST.get('space_remover', 'off')

    # if  chekbox value is on

    if user_chek_punc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in user_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        user_text = analyzed
        

    if user_chek_upper == "on":
        analyzed = ""
        for char in user_text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Convert to Upper Case','analyzed_text': analyzed}
        user_text = analyzed
        

    if user_chek_newline == "on":
        analyzed = ""
        for char in user_text:
            if char != '\n' and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remove', 'analyzed_text': analyzed}
        user_text = analyzed

    if user_chek_spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(user_text):
            # It is for if a extraspace is in the last of the string
            if char == user_text[-1]:
                    if not(user_text[index] == " "):
                        analyzed = analyzed + char

            elif not(user_text[index] == " " and user_text[index+1]==" "):                        
                analyzed = analyzed + char
                
        params = {'purpose': 'New Line Remove', 'analyzed_text': analyzed}
        user_text = analyzed
    if user_chek_punc != "on" and user_chek_upper != "on" and user_chek_newline != "on" and user_chek_spaceremover != "on":
        return render(request, 'error.html')

    return render(request, 'analyze.html', params)



