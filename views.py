from django.shortcuts import render
from . import file

# Create your views here.
def index(request):
    return render(request,'pages/index.html')
def present_simple(request):
    return render(request,'pages/present-simple.html')
def present_perfect(request):
    return render(request,'pages/present-perfect.html')
def present_continuous(request):
    return render(request,'pages/present-continuous.html')
def past_simple(request):
    return render(request,'pages/past-simple.html')
def past_perfect(request):
    return render(request,'pages/past-perfect.html')
def past_continuous(request):
    return render(request,'pages/past-continuous.html')
def future_simple(request):
    return render(request,'pages/future-simple.html')
def exercices(request):
    global complete_sen
    global choices_sen
    global arrange_sen
    global convert_tense
    global select_tense
    complete_sen=file.generate_questions('/Users/user/Desktop/files/sentence.txt')
    choices_sen=file.generate_questions('/Users/user/Desktop/files/choices.txt')
    arrange_sen=file.arrange_question('/Users/user/Desktop/files/arrange.txt')
    convert_tense=file.convert_tense('/Users/user/Desktop/files/convert.txt')
    select_tense=file.select_tense('/Users/user/Desktop/files/select.txt')
    print(select_tense)
    return render(request,'pages/exercises.html',{'sen':{'s':complete_sen,'c':choices_sen,'a':arrange_sen['split_sen'],'r':convert_tense,'t':select_tense}})
def check(req):
    dic_complete={}
    dic_choice={}
    ch_list=[]
    y=-1
    x=-1
    for sen in complete_sen:
        y=y+1
        for ii in sen :
            dic_complete.update({y:{"pre":sen[0],"aff":sen[1],"suff":sen[2]}})
    for sen in choices_sen:
        x=x+1
        for ii in sen :
            dic_choice.update({x:{"pre":sen[0],"suff":sen[1]}})      
    dic_fillblank={}
    dic_chooseanswer={}
    ch_list=[]
    complete_word=req.POST.getlist("complete_list")
    for l in choices_sen:
        c=req.POST.get(l[4])
        ch_list.append(c)
    arrange_list=req.POST.getlist("arrange_sen")
    print(arrange_list)
    change_list=req.POST.getlist("change_sen")
    print(change_list)
    select_list=req.POST.getlist("tense")
    print(select_list)
    for k,v in dic_complete.items():
        dic_fillblank.update({k:[dic_complete[k]["pre"],dic_complete[k]["suff"],complete_word[k],dic_complete[k]["aff"]]})  
    for k,v in dic_choice.items():
        dic_chooseanswer.update({k:[dic_choice[k]["pre"],dic_choice[k]["suff"],ch_list[k]]})  
    
    ## fill blank first question ##
    a=file.fill_blank(dic_fillblank[0][0],dic_fillblank[0][1],dic_fillblank[0][2],dic_fillblank[0][3])
    b=file.fill_blank(dic_fillblank[1][0],dic_fillblank[1][1],dic_fillblank[1][2],dic_fillblank[1][3])
    c=file.fill_blank(dic_fillblank[2][0],dic_fillblank[2][1],dic_fillblank[2][2],dic_fillblank[2][3])
    d=file.fill_blank(dic_fillblank[3][0],dic_fillblank[3][1],dic_fillblank[3][2],dic_fillblank[3][3])
    e=file.fill_blank(dic_fillblank[4][0],dic_fillblank[4][1],dic_fillblank[4][2],dic_fillblank[4][3])
    f=file.fill_blank(dic_fillblank[5][0],dic_fillblank[5][1],dic_fillblank[5][2],dic_fillblank[5][3])
    ## choose answer second question ##
    g=file.choose_answer(dic_chooseanswer[0][0],dic_chooseanswer[0][1],dic_chooseanswer[0][2])
    h=file.choose_answer(dic_chooseanswer[1][0],dic_chooseanswer[1][1],dic_chooseanswer[1][2])
    ii=file.choose_answer(dic_chooseanswer[2][0],dic_chooseanswer[2][1],dic_chooseanswer[2][2])
    j=file.choose_answer(dic_chooseanswer[3][0],dic_chooseanswer[3][1],dic_chooseanswer[3][2])
    k=file.choose_answer(dic_chooseanswer[4][0],dic_chooseanswer[4][1],dic_chooseanswer[4][2])
    l=file.choose_answer(dic_chooseanswer[5][0],dic_chooseanswer[5][1],dic_chooseanswer[5][2])
    ##choose the correct tense third question ##
    m=file.choose_tense(select_tense[0],select_list[0])
    n=file.choose_tense(select_tense[1],select_list[1])
    o=file.choose_tense(select_tense[2],select_list[2])
    p=file.choose_tense(select_tense[3],select_list[3])
    ## arrange the word fourth question ##
    q=file.sentense_order(arrange_sen['order_sen'][0],arrange_list[0])
    r=file.sentense_order(arrange_sen['order_sen'][1],arrange_list[1])
    ## transform the tense fifth question ##
    s=file.prescont_to_simpress(convert_tense[0],change_list[0])
    t=file.prescont_to_simpress(convert_tense[1],change_list[1])
    array=[a,b,c,d,e,f,g,h,ii,j,k,l,m,n,o,p,q,r,s,t]
    counter=0
    for i in array:
        if i['check_pointer'] :
            counter=counter+1
        elif i['link'] == 11:
            counter=counter+0.5
    score=round((counter/20)*100)
    return render(req,'pages/check.html',{'result':[a,b,c,d,e,f,g,h,ii,j,k,l,m,n,o,p,q,r,s,t],'counter':counter,'score':score})
