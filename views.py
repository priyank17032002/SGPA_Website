# this file is created by me 
from django.http import HttpResponse
from django.shortcuts import render
## addition of link on webpage 
# def index(request):
#     return HttpResponse('''<h1>song playlist</h1><a href="https://www.youtube.com/playlist?list=PLCULndnUE-_rtFzK-8rBKDjOqrNuDBvFO"> song playlist</a> ''')
# ###################################################
# ### adding a new url 
# def about(request):
#     return HttpResponse("About")
# #####################################################
# # reading a file 
# def read_file(request):
#     with open("t1.txt", "r") as f:    # Opening the file in read mode, we don't use r+ because file already exists, r+ is used when file doesn't exists then assigning it a variable named f
#         content = f.read()    # Reading the contents of the file and storing it in a variable, we use read instead of readlines because readlines gives each line as a list element
#     return HttpResponse(content)


###############################################################################
############  code after video 7
def index1(request):
    
    return render(request,'index.html')
# def index(request):
#     return HttpResponse('''<a href="http://127.0.0.1:8000/removepunc">remove_punctuation</a>
#                         <br>
#                         <a href="http://127.0.0.1:8000/capfirst">cap_fisrt</a>
#                         <br>
#                         <a href="http://127.0.0.1:8000/newlineremove">newlineremove</a>
#                         <br>
#                         <a href="http://127.0.0.1:8000/spaceremove">space_remover</a>
#                         <br>
#                         <a href="http://127.0.0.1:8000/charcount">char_counter</a>
#                         <br>''')
def analyze(request):
    # getting the text 
    djtext=request.POST.get('text','default')
    # print(djtext)
    
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')
    grades=request.POST.get('grades','off')
    # print(removepunc)
    #analysing the text 
    # analyzed=djtext
    
    if grades=="on":
        g={"A+":10,"A":9,"B+":8,"B":7,"C+":6,"C":5,"F":0}
        sgpa=0
        listg=djtext.split(" ")
        finallist=[]
        credit_score=0
        for i in range(0,len(listg)-1,2):
            finallist.append([listg[i],listg[i+1]])
        print(finallist)
        for gra in range(len(finallist)):
            print(g[finallist[gra][0]],finallist[gra][1])
            sgpa+=(g[finallist[gra][0]] * float(finallist[gra][1]))
            credit_score+=float(finallist[gra][1])
        print(credit_score)
        print(sgpa)
        x=sgpa/credit_score
        analyzed=str(x)
        params={'purpose': 'sgpa','analyzed_text':analyzed}
        return render(request,'sgpa.html',params)
    

    elif removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char 

        params={'purpose':'remove punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params={'purpose':'full capitalised text ','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char

        params={'purpose':'newline remover','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif spaceremover=="on":
        analyzed=""
        for char in djtext:
            if char==" ":
                continue 
            else:
                analyzed=analyzed+char

        params={'purpose':'space removed','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif charcount=="on":
        analyzed=0
        for char in djtext:
            analyzed+=1

        params={'purpose':'No. of charcter ','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")
def about(request):
    return HttpResponse("i am here ")
def contactus(request):
    return HttpResponse("8398915565 ,tpriyank@gmail.com")
# def capfirst(request):
#     return HttpResponse("capitalize first<br><a href='http://127.0.0.1:8000/'>back</a>")
# def newlineremove(request):
#     return HttpResponse("newline remover<br><a href='http://127.0.0.1:8000/'>back</a>")
# def spaceremove(request):
#     return HttpResponse("space remover<br><a href='http://127.0.0.1:8000/'>back</a>")
# def charcount(request):
#     return HttpResponse("char count<br><a href='http://127.0.0.1:8000/'>back</a>")