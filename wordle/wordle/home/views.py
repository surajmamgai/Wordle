from django.shortcuts import render,redirect
from home import words

import random
chosen_word=[]
def split(word):
    return [char for char in word]
def index(request):
    item = random.choice(tuple(words.li))
    global chosen_word
    chosen_word=split(item)
    print(chosen_word)
    return render(request,'index.html')
def first(request):
    a=b=c=d=e=False
    if request.method=='POST':
        c1=request.POST.get('c1')
        if(c1==chosen_word[0]):
            a=True
        c2=request.POST.get('c2')
        if(c2==chosen_word[1]):
            b=True
        c3=request.POST.get('c3')
        if(c3==chosen_word[2]):
            c=True
        c4=request.POST.get('c4')
        if(c4==chosen_word[3]):
            d=True
        c5=request.POST.get('c5')
        if(c5==chosen_word[4]):
            e=True
        print(chosen_word)
        return render(request,'index.html',{'a':a,'c1':c1,'b':b,'c2':c2,'c':c,'c3':c3,'d':d,'c4':c4,'e':e,'c5':c5})

