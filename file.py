import random 
### reading from files###
def generate_questions(url):
    with open(url,'r') as file:
        sentences=[line.strip() for line in file.readlines()]
    random_sentences=random.sample(sentences,6)
    sentences_parts=[]
    for sentence in random_sentences:
        parts=sentence.strip().split(',')
        sentences_parts.append(parts)
    return sentences_parts
def arrange_question(url): 
    with open(url,'r') as file:
        sentences=[line.strip() for line in file.readlines()]
    random_sentences=random.sample(sentences,2)
    sentences_parts=[]
    for sentence in random_sentences:
        parts=sentence.strip().split()
        random.shuffle(parts)
        s=" / ".join(parts)
        sentences_parts.append(s)
        
    return {'split_sen':sentences_parts,'order_sen':random_sentences}
def convert_tense(url):
    with open(url,'r') as file:
        sentences=[line.strip() for line in file.readlines()]
    random_sentences=random.sample(sentences,2)
    return random_sentences
def select_tense(url):
    with open(url,'r') as file:
        sentences=[line.strip() for line in file.readlines()]
    random_sentences=random.sample(sentences,4)
    return random_sentences

###############grammer####################
verbs_dic={
         'go':['goes','going','went','gone'],
         'eat':['eats','eating','ate','eaten'],
         'write':['writes','writting','wrote','written'],
         'see':['sees','seeing','saw','seen'],
         'give':['gives','giving','gave','given'],
         'take':['takes','taking','took','taken'],
         'do':['does','doing','did','done'],
         'make':['makes','making','made','made'],
         'tell':['tells','telling','told','told'],
         'find':['finds','finding','found','found'],
         'have':['has','having','had','had'],
         'send':['sends','sending','sent','sent'],
         'speak':['speaks','speaking','spoke','spoken'],
         'learn':['learns','learning','learnt','learnt'],
         'feel':['feels','feeling','felt','felt'],
         'sleep':['sleeps','sleeping','slept','slept'],
         'meet':['meets','meeting','met','met'],
         'think':['thinks','thinking','thought','thought'],
         'lose':['loses','losing','lost','lost'],
         'forget':['forgets','forgetting','forgot','forgotten'],
         'get':['gets','getting','got','got'],
         'ride':['rides','ridding','rode','ridden'],
         'drink':['drinks','drinking','drank','drunk'],
         'play':['plays','playing','played','played'],
         'buy':['buys','buying','bought','bought'],
         'study':['studies','studying','studied','studied'],
         'work':['works','working','worked','worked'],
         'arrive':['arrives','arriving','arrived','arrived'],
         'visit':['visits','visiting','visited','visited'],
         'win':['wins','winning','won','won'],
         'read':['reads','reading','read','read'],
         'watch':['watches','watching','watched','watched'],
         'help':['helps','helping','helped','helped'],
         'live':['lives','living','lived','lived'],
         'finish':['finishes','finishing','finished','finished'],
         'cook':['cooks','cooking','cooked','cooked'],
         'travel':['travels','travelling','travelled','travelled'],
         'complete':['completes','completing','completed','completed'],
         'start':['starts','starting','started','started']
         }

past_simple = ["yesterday", "last", "ago"]
past_continuous = ["when", "while", "all"]
past_perfect = ["before", "after", "already"]
present_simple = ["always", "often", "every"]
present_continuous = ["now", "moment", "currently"]
present_perfect = ["recently", "lately"]
future_simple = ["tomorrow", "next", "soon"]
pro=["he","she","it","He","She","It"]
tobe=['am','is','are']
pro_cont=["he","she","it","He","She","It","I","i"]
thr_pro=['I','i','They','they','We','we','You','you']
import nltk 


def fill_blank(sen1,sen2,answer,verb):
    check_pointer=False
    link=0
    space=" "
    Q=1
    return_answer=sen1,space,answer,space,sen2
    answer1=answer.lower()
    sentence=sen1+space+sen2
    list_word=nltk.word_tokenize(sentence)
    for w in list_word:
        if w in present_simple:
            if list_word[0] in pro :
                if answer1 == verbs_dic.get(verb)[0]:
                    check_pointer=True
                    message=sen1,answer1,sen2
                else:
                    message=sen1+space+verbs_dic.get(verb)[0]+space+sen2
                    link=1
            elif ( 'and' not in sen1 ) and ( list_word[0] not in thr_pro ):
                if answer1 == verbs_dic.get(verb)[0]:
                    check_pointer=True
                    message=sen1,answer1,sen2
                else:
                    message=sen1+space+verbs_dic.get(verb)[0]+space+sen2
                    link=1
            elif list_word[0] in thr_pro :
                if answer1 == verb:
                    message=sen1,answer1,sen2
                    check_pointer=True
                else:
                    message=sen1+space+verb+space+sen2
                    link=1
            elif 'and' in sen1 :
                if answer1 == verb:
                    message=sen1,answer1,sen2
                    check_pointer=True
                else:
                    message=+sen1+space+verb+space+sen2
                    link=1
        elif w in past_simple:
            if answer1 == verbs_dic.get(verb)[2]:
                check_pointer=True
                message=sen1,answer1,sen2
            else:
                message=sen1+space+verbs_dic.get(verb)[2]+space+sen2
                link=4
        elif w in present_continuous:
            if answer1 == verbs_dic.get(verb)[1]:
                check_pointer=True
                message=sen1,answer1,sen2
            else:
                message=sen1+space+verbs_dic.get(verb)[1]+space+sen2
                link=2
    if answer == "":
        link=10
    result={"message":message,"check_pointer":check_pointer,'link':link,'return_answer':return_answer,"q":Q}
    return result

def choose_answer(sen1,sen2,answer):
    link=0
    check_pointer=False
    space=" "
    Q=2
    return_answer=sen1,space,answer,space,sen2
    sentence=sen1+space+sen2
    list_word=nltk.word_tokenize(sentence)
    sen1_token=nltk.word_tokenize(sen1)
    for w in list_word:
        if w in future_simple:
            if answer=='going to' :
                if list_word[1] in tobe:
                    check_pointer=True
                    message=sen1,answer,sen2
                else:
                    message=sen1,"will",sen2 
                    link=7
            elif answer=='will':
                if list_word[1] not in tobe:
                    check_pointer=True
                    message=sen1,answer,sen2
                else:
                    message=sen1,"going to",sen2
                    link=7
        elif w in past_continuous:
            if answer=='was':
                if list_word[0] in pro_cont:
                    check_pointer=True
                    message=sen1,answer,sen2
                else:
                    message=sen1,"were",sen2
                    link=5
            elif answer=='were':
                if list_word[0] not in pro_cont:
                    check_pointer=True
                    message=sen1,answer,sen2
                else:
                    message=sen1,"was",sen2
                    link=5
        elif w in present_perfect:
            if answer=='has':
                if list_word[0] in pro:
                    check_pointer=True
                    message=sen1,answer,sen2
                else:
                    message=sen1,"have",sen2 
                    link=3
            elif answer=='have':
                if list_word[0] not in pro:
                    check_pointer=True
                    message=sen1,answer,sen2
                else:
                    message=sen1,"has",sen2
                    link=3  
    if answer is None:
        link=20
        message='You have to select one choice at least'
    result={"message":message,"check_pointer":check_pointer,'link':link,'return_answer':return_answer,"q":Q}
    return result
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer

def choose_tense(sentence,answer):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    verb_index = -1  # Initialize the verb index to -1
    check_pointer=False
    link=0
    Q=3
    for i, (word, tag) in enumerate(tagged_words):
        if tag.startswith('V') or tag.startswith('JJ'):
            verb_index = i  # Set the verb index to the current index if a verb is found
            break
    
    if verb_index < 0:
        message="No verb found in the sentence."
        return
    
    verb = words[verb_index]  # Get the verb from the words list using the verb index

    
    
    if verb_index >= 0:
        verb = words[verb_index]  # Get the verb from the words list using the verb index
    
    # Get the previous word (if there is one)
        if verb_index > 0:
            prev_word = words[verb_index - 1]
        else:
            prev_word = None
    
    # Get the next word (if there is one)
        if verb_index < len(words) - 1:
            next_word = words[verb_index + 1]
        else:
            next_word = None
    
    # Print the verb and its surrounding words
        print("Verb: ", verb)
        print("Previous word: ", prev_word)
        print("Next word: ", next_word)
    else:
        print("No verb found in the sentence.")

    
    
    for word_future, tag in tagged_words:
        if tag.startswith('MD'):
            print(word_future)
            break
    

    pre_cont=['am','AM','is','IS','are','ARE']
    past_cont=['was','WAS','were','WERE']
    pre_perf=['has','HAS','have','HAVE']
    future=['will','WILL','going','GOING']

    

    #get the sourec of the verb or zero tense of it
    wordnet_lemmatizer = WordNetLemmatizer()    
    base_form = wordnet_lemmatizer.lemmatize(verb, pos="v")
    base_form_next = wordnet_lemmatizer.lemmatize(next_word, pos="v")

    
    
    
    
    #******************All Present Perfect State***************
    #----------------------------------------------------------
    #if the prevois word of the verb in list ['he','she','it'] or not
    if verb in pre_perf and (tagged_words[i+1][1].startswith('V') or tagged_words[i+1][1].startswith('JJ') )and next_word==verbs_dic.get(base_form_next)[3] :
        if answer == 'present perfect' :
            check_pointer=True
            message="True, it's present perfect"
        elif answer == 'Open this select menu':
            message='present perfect'
            link=10    
        else:
            link=3
            message='present perfect'

    #******************Past Perfect State***************
    elif 'had' in verb and next_word == verbs_dic.get(base_form_next)[3] :
        if answer == 'past perfect':
            check_pointer=True
            message="true, it's past perfect"
        elif answer == 'Open this select menu':
            message='past perfect'
            link=10
        else:
            link=6
            message='past perfect'
    #******************Future Simple State***************
    elif word_future in future or ( word in pre_cont and 'going' in next_word ):
        if verb == 'future simple':
            check_pointer=True
            message="true, it's future simple"
        elif answer == 'Open this select menu':
            message='future simple'
            link=10
        else:
            message='future simple'
            link=7
    #******************Present Continuous State***************
    elif verb in pre_cont and next_word==verbs_dic.get(base_form_next)[1]:
        if answer == 'present continuous' :
            check_pointer=True
            message="true, it's present continuous"
        elif answer == 'Open this select menu':
            message='present continuous'
            link=10
        else:
            link=2
            message='present continuous'
    
    
    #******************Past Continuous State***************
    elif verb in past_cont and next_word==verbs_dic.get(base_form_next)[1]:
        if answer == 'past continuous' :
            message="true, it's past continuous"
            check_pointer=True
        elif answer == 'Open this select menu':
            message='past continuous'
            link=10
        else:
            link=5
            message='past continuous'
    
    #******************Present Simple State***************
    #if the prevois word of the verb in list ['he','she','it'] or not
    elif base_form in list(verbs_dic.keys()):
        if verb ==verbs_dic.get(base_form)[0] or verb == base_form:
            if answer == 'present simple':
                check_pointer=True
                message="true, it's present simple"
            elif answer == 'Open this select menu':
                message='present simple'
                link=10
            else:
                link=1
                message='present simple'
    
    #******************Past Simple State********************
    elif base_form in list(verbs_dic.keys()):
        if verb == verbs_dic.get(base_form)[2]:
            if answer == 'past simple' :
                message="true, it's past simple"
                check_pointer=True
            elif answer == 'Open this select menu':
                message='past simple '
                link=10
            else:
                link=4
                message='past simple'
                
    # if answer == "Open this select menu":
    #     link=10
    result={"message":message,"check_pointer":check_pointer,'link':link,'return_answer':answer,"q":Q}
    return result


def sentense_order(sentence,answer):
    link=0
    check_pointer=False
    answer1=answer.lower()
    sentence1=sentence.lower()
    Q=4
    
    # Initialize variable to count differences
    num_diff = 0
    ans1=nltk.word_tokenize(answer1)
    sen1=nltk.word_tokenize(sentence1)
    for i in range(max(len(sen1), len(ans1))):
        if len(sen1) != len(ans1):
            num_diff +=2
        elif sen1[i]!=ans1[i]:
            num_diff+=1
            
    if num_diff == 0:
        check_pointer=True
        message=answer
    elif num_diff == 1:
        link=11
        message=sentence
    else:
        message=sentence
        link=6   
    
    if answer == "":
        link=10
    result={"message":message,"check_pointer":check_pointer,'link':link,'return_answer':answer,"q":Q}
    return result




from nltk.tokenize import word_tokenize as wt
from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()





def verb_to_wordnet(verb_tag):
    if verb_tag.startswith('V') or verb_tag.startswith('JJ'):
        return 'v'

    
    
    
    
def correct_singular_plural(cont_sent_tag, cont_sent_lem):
    
    index = 0

    for i in range(len(cont_sent_lem)):
        if cont_sent_lem[i]=='be':
            index = i

    if 'not' in cont_sent_lem:
        pos_neg = 'neg'
    else:
        pos_neg = 'pos'
        

    if cont_sent_tag[index-1][1] == 'NN' or cont_sent_tag[index-1][1] == 'NNP' or cont_sent_tag[index-1][1] == 'JJ' or cont_sent_tag[index-1][0].capitalize() == 'He' or cont_sent_tag[index-1][0].capitalize() == 'She' or cont_sent_tag[index-1][0].capitalize() == 'It':
    
        if pos_neg == 'pos':
        
            if cont_sent_lem[index+1][-1] == 'o' or cont_sent_lem[index+1][-1] == 's' or cont_sent_lem[index+1][-1] == 'z' or cont_sent_lem[index+1][-2:] == 'ch' or cont_sent_lem[index+1][-2:] == 'sh' or cont_sent_lem[index+1][-1] == 'x':
                cont_sent_lem[index+1]+='es'
        
            elif cont_sent_lem[index+1][-1] == 'y':
                if cont_sent_lem[index+1][-2] == 'a' or cont_sent_lem[index+1][-2] == 'e' or cont_sent_lem[index+1][-2] == 'i' or cont_sent_lem[index+1][-2] == 'o' or cont_sent_lem[index+1][-2] == 'u':
                    cont_sent_lem[index+1]+='s'
                else:
                    cont_sent_lem[index+1] = cont_sent_lem[index+1].replace(cont_sent_lem[index+1][-1],'ies')
        
            elif cont_sent_lem[index+1] == 'have':
                cont_sent_lem[index+1] = cont_sent_lem[index+1].replace('have','has')
        
            else:
                cont_sent_lem[index+1]+='s'
            
            cont_sent_lem.remove('be')
    
        else:
        
            cont_sent_lem = ['does' if word == 'be' else word for word in cont_sent_lem]
        
    else:
        if pos_neg == 'pos':
            cont_sent_lem.remove('be')
        else:
            cont_sent_lem = ['do' if word == 'be' else word for word in cont_sent_lem]
            
    return cont_sent_lem
def prescont_to_simpress(prescont,answer):
    link=0
    check_pointer=False
    Q=5
    answer1=answer.lower()
    # Tokenizing
    cont_sent_token = wt(prescont)
    cont_sent_tag = nltk.pos_tag(cont_sent_token)
    
    # Lemmatizing
    cont_sent_lem = []

    for i in cont_sent_tag:
        wordnet_verb = verb_to_wordnet(i[1])
    
        if wordnet_verb is not None:
            cont_sent_lem.append(lem.lemmatize(i[0], wordnet_verb))
        else:
            cont_sent_lem.append(i[0])
       
    # Correcting singular and plural
    cont_sent_lem = correct_singular_plural(cont_sent_tag, cont_sent_lem)
    
    # Simple present tense form
    correct_answer=' '.join(cont_sent_lem)
    corr_ans=correct_answer.lower()
    if corr_ans==answer1:
        check_pointer=True
        message=answer
    else:
        link=1
        message=correct_answer
    if answer == "":
        link=10
    result={"message":message,"check_pointer":check_pointer,'link':link,'return_answer':answer,"q":Q}
    return result
    
