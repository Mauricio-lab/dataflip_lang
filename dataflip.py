import json
import time
import nltk
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from googletrans import Translator
import googletrans

app = Flask(__name__)

translator = Translator()
jezici=googletrans.LANGUAGES
#probaj
HR={}


def vrati_jezik(sadržaj):
    #print(jezici)
    jezik=translator.detect(sadržaj)
    #gdje=str(jezik.lang).find('lang=')
    #kratica=str(jezik)[gdje+5:gdje+7]
    
    koji_je=jezici[str(jezik.lang.lower())]

    return str(koji_je)
    

def prevedi(text_sentence):
    prijevod=translator.translate(text_sentence, dest='hr')
    return str(prijevod.text)

def prevedi_2(list_sentences):
    LOCAL_LIST=[]
    for sentence in list_sentences:
        prijevod=translator.translate(sentence, dest='hr')
        #print(sentence)
        HR[prijevod.text]=str(sentence)
        LOCAL_LIST.append(prijevod.text)
        #print(prijevod.text)
        #print('__________')
        #print(LOCAL_LIST)
    return LOCAL_LIST

nltk.download('punkt')

INPUT={}
n=0
fp_input=open('BAZA_JSON.txt','r', encoding='utf-8')
while n < 700000:
    n+=1
    linija=fp_input.readline()
    linija=linija.replace('\n','')
    word_rijec=linija[:linija.find('{')]
    json_rest=linija[linija.find('{'):]
    #print(word_rijec)
    #print(json_rest)
    if 'XXX' in linija:
        break
    INPUT[word_rijec]=json_rest

    #time.sleep(1)

fp_input.close()

@app.route('/process/<ticker>', methods =["GET", "POST"])
def process(ticker):
    #url = "https://www.index.hr/vijesti/clanak/maja-djerek-nije-zvizdacica-kaze-sud-evo-sto-ona-kaze/2454556.aspx"
    #https:||www.index.hr|vijesti|clanak|macron-biti-saveznik-sada-ne-znaci-biti-njegov-vazal|2454561.aspx
    #https:||www.index.hr|vijesti|clanak|krece-velika-promjena-vremena-izdana-upozorenja-za-cijelu-zemlju|2454590.aspx?index_ref=naslovnica_vijesti_prva_d
    #https:||www.index.hr|vijesti|clanak|americka-organizacija-na-twitteru-o-skejinim-brcicima-zapanjujuce|2454646.aspx?index_ref=clanak_procitaj_jos_d
    #https:||www.index.hr|vijesti|clanak|velika-ruska-promjena-u-bahmutu-pogledajte-kako-izgledaju-ulice-nakon-mjeseci-rata|2455599.aspx
    url=ticker.replace('|','/')
    #print('____________________________________________')
    #print('____________________________________________')
    #print(url)
    #print('____________________________________________')
    #print('____________________________________________')
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    text_link=''
    els = soup.find_all("p")
    for el in els:
        text_link=text_link+el.text
    #print(el.text)
    start_time = time.time()
    TEXT=[]
    #nltk_sentences = nltk.sent_tokenize(text_link)
    nltk_sentences = nltk.sent_tokenize(text_link)
    
    nltk_sentences_hr = prevedi_2(nltk_sentences)
    #print(len(nltk_sentences))
    #print(len(nltk_sentences_hr))

    language_used=vrati_jezik(text_link)
    
    #print('_______________________________________________')
    #nltk_riječi = nltk.word_tokenize(text_link)
    nr_words_checked=0

    BIJES=0
    LJUTNJA=0
    ODVAŽNOST=0

    BUDNOST=0
    OČEKIVANJE=0
    INTERES=0

    GNUŠANJE=0
    GAĐENJE=0
    AVERZIJA=0

    TEROR=0
    STRAH=0
    BOJAZAN=0

    EKSTAZA=0
    SREĆA=0
    SPOKOJ=0

    PATNJA=0
    TUGA=0
    SJETA=0

    ZAPANJENOST=0
    IZNENAĐENJE=0
    DISTRAKCIJA=0

    DIVLJENJE=0
    POVJERENJE=0
    PRIHVAĆANJE=0
    #step_on=len(nltk_riječi)/200
    #print(len(nltk_riječi))
    #print(str(int(step_on)))
    rrr=''
    tut=''
    count=0
    #input('h')
    TEXT.append('{"language":"'+'%s' % language_used+'"}')

    for loop_over_sentence in nltk_sentences_hr:
        #print('████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████')
        #print('*************************************************')
        #print(loop_over_sentence)
        #print('_________________________________________________')
        #print(HR[loop_over_sentence])
        #print('*************************************************')
        nltk_words = nltk.word_tokenize(loop_over_sentence)
        words=[word.lower() for word in nltk_words if word.isalpha()]
        rečenica=words
        prijateljstvo=0
        ljubav=0
        obožavanje=0

        #____primarne____
        bijes=0
        ljutnja=0
        odvažnost=0

        budnost=0
        očekivanje=0
        interes=0

        gnušanje=0
        gađenje=0
        averzija=0

        teror=0
        strah=0
        bojazan=0

        ekstaza=0
        sreća=0
        spokoj=0

        patnja=0
        tuga=0
        sjeta=0

        zapanjenost=0
        iznenađenje=0
        distrakcija=0

        divljenje=0
        povjerenje=0
        prihvaćanje=0
        #---------end primarne------------
        
        #_____________secondary
        očaj_int_1=0
        očaj_int_2=0
        očaj_int_3=0
        neodobravanje_int_1=0
        neodobravanje_int_2=0
        razočaranje=0
        nevjerica_int_1=0
        nevjerica_int_2=0
        šok=0
        žaljenje_int_1=0
        žaljenje_int_2=0
        nesretan=0
        strahopoštovanje_int_1=0
        strahopoštovanje_int_2=0
        strahopoštovanje_int_3=0
        podređenost_int_1=0
        podređenost_int_2=0
        podređenost_int_3=0
        zadovoljstvo_int_1=0
        zadovoljstvo_int_2=0
        zadovoljstvo_int_3=0
        znatiželja_int_1=0
        znatiželja_int_2=0
        znatiželja_int_3=0
        sentimentalnost_int_1=0
        sentimentalnost_int_2=0
        sentimentalnost_int_3=0
        ponos_int_1=0
        ponos_int_2=0
        pobjeda=0
        optimizam_int_1=0
        optimizam_int_2=0
        hrabrost=0
        nada_int_1=0
        nada_int_2=0
        nada_int_3=0
        krivnja_int_1=0
        krivnja_int_2=0
        uzbuđenje=0
        sram_int_1=0
        sram_int_2=0
        bezobraština=0
        prezir_int_1=0
        prezir_int_2=0
        bez_poštovanja=0
        zavist_int_1=0
        zavist_int_2=0
        neugoda=0
        dominacija_int_1=0
        dominacija_int_2=0
        dominacija_int_3=0
        agresija_int_1=0
        agresija_int_2=0
        agresija_int_3=0
        uvreda_int_1=0
        uvreda_int_2=0
        mržnja=0
        pesimizam_int_1=0
        pesimizam_int_2=0
        nepovjerenje=0
        anksioznost_int_1=0
        anksioznost_int_2=0
        zabrinutost=0
        morbidnost_int_1=0
        morbidnost_int_2=0
        ismijavanje=0
        cinizam_int_1=0
        cinizam_int_2=0
        cinizam_int_3=0
        prijateljstvo=0
        ljubav=0
        obožavanje=0
        #---------end sekundarne------------
        """     

        zamjenica > zamjenica > glagol
                > glagol  
        prilog > imenica
            > prilog
            > glagol
        pridjev > imenica
                > prilog

        ?prijedlog > 

        glagol  > glagol > prijedlog > imenica
                        > imenica
                        > glagol
                > zamjenica > glagol > prilog
                            > prilog > glagol
                > prilog > imenica
        imenica 

        """
        korak=0
        NEGACIJA_AKTIVNA=False
        #print(rečenia.index('kuću'))
        #print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        #print(rečenica)
        for i in rečenica:
            #i=i.lower()
            count=count+1
            nr_words_checked=nr_words_checked+1
            #if count>int(step_on):
            #    rrr=rrr+'█'
            #    tut=tut+' '
            #    print(rrr+" {:2}".format(nr_words_checked),end='\r')
                #print(tut+'<█>',end='\r')
            #    time.sleep(.005)
            #    count=0
            #print(rrr +'Y',end='\x1b[2K\r')
            try:
                y=json.loads(INPUT[i.lower()])
                #print(i+'   '+INPUT[i.lower()])
                #print(i+INPUT[i.lower()])
                if 'niječni' in y["vrsta"]:
                    #print('Neg.___> ' + i)
                    lokacija_negacije=rečenica.index(str(i))
                    #print(str(lokacija_negacije))
                    try:
                        riječ_poz1=rečenica[lokacija_negacije+1]
                        riječ1_json=json.loads(INPUT[riječ_poz1.lower()])
                    except:pass
                    try:
                        riječ_poz2=rečenica[lokacija_negacije+2]
                        riječ2_json=json.loads(INPUT[riječ_poz2.lower()])
                    except:pass
                    try:
                        riječ_poz3=rečenica[lokacija_negacije+3]
                        riječ3_json=json.loads(INPUT[riječ_poz3.lower()])
                    except:pass
                    try:
                        riječ_poz4=rečenica[lokacija_negacije+4]
                        riječ4_json=json.loads(INPUT[riječ_poz4.lower()])
                    except:pass
                    try:
                        riječ_poz5=rečenica[lokacija_negacije+5]
                        riječ5_json=json.loads(INPUT[riječ_poz5.lower()])
                    except:pass

                    if 'glagol' in riječ1_json["vrsta"]:
                        korak=1
                        NEGACIJA_AKTIVNA=True
                        #print('Jedan')
                        if 'imenica' in riječ2_json["vrsta"]:
                            NEGACIJA_AKTIVNA=True
                            korak=2
                        if 'glagol' in riječ2_json["vrsta"]:
                            NEGACIJA_AKTIVNA=True
                            korak=2
                            if 'prijedlog' in riječ3_json["vrsta"]:
                                NEGACIJA_AKTIVNA=True
                                korak=3
                                if 'imenica' in riječ4_json["vrsta"]:
                                    NEGACIJA_AKTIVNA=True
                                    korak=4
                            if 'imenica' in riječ3_json["vrsta"]:
                                NEGACIJA_AKTIVNA=True
                                korak=3
                            if 'glagol' in riječ3_json["vrsta"]:
                                NEGACIJA_AKTIVNA=True
                                korak=3
                        if 'zamjenica' in riječ2_json["vrsta"]:
                            NEGACIJA_AKTIVNA=True
                            korak=2
                            if 'glagol' in riječ3_json["vrsta"]:
                                NEGACIJA_AKTIVNA=True
                                korak=3
                                if 'prilog' in riječ4_json["vrsta"]:
                                    NEGACIJA_AKTIVNA=True
                                    korak=4
                            if 'prilog' in riječ3_json["vrsta"]:
                                NEGACIJA_AKTIVNA=True
                                korak=3
                                if 'glagol' in riječ4_json["vrsta"]:
                                    NEGACIJA_AKTIVNA=True
                                    korak=4
                        if 'prilog' in riječ2_json["vrsta"]:
                            NEGACIJA_AKTIVNA=True
                            korak=2
                            #print('Dva')
                            if 'pomoćni' in riječ3_json["vrsta"]:
                                NEGACIJA_AKTIVNA=True
                                korak=3
                                if 'pridjev' in riječ4_json["vrsta"]:
                                    NEGACIJA_AKTIVNA=True
                                    korak=4
                                    if 'imenica' in riječ5_json["vrsta"]:
                                        NEGACIJA_AKTIVNA=True
                                        korak=5
                            #if 'imenica' in riječ3_json["vrsta"]:
                            #    NEGACIJA_AKTIVNA=True
                            #    korak=3
                            #    print('Tri')
                            #if 'pridjev' in riječ3_json["vrsta"]:
                            #    NEGACIJA_AKTIVNA=True
                            #    korak=3
                            #    print('Tri')
                            #    if 'imenica' in riječ4_json["vrsta"]:
                            #        NEGACIJA_AKTIVNA=True
                            #        korak=3
                            #        print('Četiri')
        
                    if 'pril.(čest.)' in riječ1_json["vrsta"]:
                        NEGACIJA_AKTIVNA=True
                        korak=1
                        #print('JEDAN')
                        if 'pridjev' in riječ2_json["vrsta"]:
                            NEGACIJA_AKTIVNA=True
                            korak=2
                            #print('DVA')
                            if 'prijedlog' in riječ3_json["vrsta"]:
                                NEGACIJA_AKTIVNA=True
                                korak=3
                                #print('TRI')
                                if 'imenica' in riječ4_json["vrsta"]:
                                    NEGACIJA_AKTIVNA=True
                                    korak=4
                                    #print('ČETIRI')
                                if 'zamjenica' in riječ4_json["vrsta"]:
                                    NEGACIJA_AKTIVNA=True
                                    korak=4
                                    if 'imenica' in riječ5_json["vrsta"]:
                                        NEGACIJA_AKTIVNA=True
                                        korak=5
                                        #print('PET')
                    if 'imenica' in riječ1_json["vrsta"]:
                        NEGACIJA_AKTIVNA=True
                        korak=1
 
            except:
                pass
            
            try:
                y=json.loads(INPUT[i.lower()])
                try:
                    if y["bijes"]:
                        if NEGACIJA_AKTIVNA:
                            teror=teror+1
                            TEROR=TEROR+1
                        if not NEGACIJA_AKTIVNA:
                            bijes=bijes+1
                            BIJES=BIJES+1
                except:
                    pass
                try:
                    if y["ljutnja"]:
                        if NEGACIJA_AKTIVNA:
                            strah=strah+1
                            STRAH=STRAH+1
                        if not NEGACIJA_AKTIVNA:
                            ljutnja=ljutnja+1
                            LJUTNJA=LJUTNJA+1
                except:
                    pass
                try:
                    if y["odvažnost"]:
                        if NEGACIJA_AKTIVNA:
                            bojazan=bojazan+1
                            BOJAZAN=BOJAZAN+1
                        if not NEGACIJA_AKTIVNA:
                            odvažnost=odvažnost+1
                            ODVAŽNOST=ODVAŽNOST+1
                except:
                    pass
                try:
                    if y["budnost"]:
                        if NEGACIJA_AKTIVNA:
                            zapanjenost=zapanjenost+1
                            ZAPANJENOST=ZAPANJENOST+1
                        if not NEGACIJA_AKTIVNA:
                            budnost=budnost+1
                            BUDNOST=BUDNOST+1
                        
                except:
                    pass
                try:
                    if y["očekivanje"]:
                        if NEGACIJA_AKTIVNA:
                            iznenađenje=iznenađenje+1
                            IZNENAĐENJE=IZNENAĐENJE+1
                        if not NEGACIJA_AKTIVNA:
                            očekivanje=očekivanje+1
                            OČEKIVANJE=OČEKIVANJE+1
                except:
                    pass
                try:
                    if y["interes"]:
                        if NEGACIJA_AKTIVNA:
                            distrakcija=distrakcija+1
                            DISTRAKCIJA=DISTRAKCIJA+1
                        if not NEGACIJA_AKTIVNA:
                            interes=interes+1
                            INTERES=INTERES+1
                except:
                    pass

                try:
                    if y["gnušanje"]:
                        if NEGACIJA_AKTIVNA:
                            divljenje=divljenje+1
                            DIVLJENJE=DIVLJENJE+1
                        if not NEGACIJA_AKTIVNA:
                            gnušanje=gnušanje+1
                            GNUŠANJE=GNUŠANJE+1
                except:
                    pass
                
                try:
                    if y["gađenje"]:
                        if NEGACIJA_AKTIVNA:
                            povjerenje=povjerenje+1
                            POVJERENJE=POVJERENJE+1
                        if not NEGACIJA_AKTIVNA:
                            gađenje=gađenje+1
                            GAĐENJE=GAĐENJE+1
                except:
                    pass
                
                try:
                    if y["averzija"]:
                        if NEGACIJA_AKTIVNA:
                            prihvaćanje=prihvaćanje+1
                            PRIHVAĆANJE=PRIHVAĆANJE+1
                        if not NEGACIJA_AKTIVNA:
                            averzija=averzija+1
                            AVERZIJA=AVERZIJA+1
                except:
                    pass

                try:
                    if y["teror"]:
                        if NEGACIJA_AKTIVNA:
                            bijes=bijes+1
                            BIJES=BIJES+1
                        if not NEGACIJA_AKTIVNA:
                            teror=teror+1
                            TEROR=TEROR+1
                except:
                    pass
                
                try:
                    if y["strah"]:
                        if NEGACIJA_AKTIVNA:
                            ljutnja=ljutnja+1
                            LJUTNJA=LJUTNJA+1
                        if not NEGACIJA_AKTIVNA:
                            strah=strah+1
                            STRAH=STRAH+1
                except:
                    pass
                
                try:
                    if y["bojazan"]:
                        if NEGACIJA_AKTIVNA:
                            odvažnost=odvažnost+1
                            ODVAŽNOST=ODVAŽNOST+1
                        if not NEGACIJA_AKTIVNA:
                            bojazan=bojazan+1
                            BOJAZAN=BOJAZAN+1
                except:
                    pass

                try:
                    if y["ekstaza"]:
                        if NEGACIJA_AKTIVNA:
                            patnja=patnja+1
                            PATNJA=PATNJA+1
                        if not NEGACIJA_AKTIVNA:
                            ekstaza=ekstaza+1
                            EKSTAZA=EKSTAZA+1
                except:
                    pass
                
                try:
                    if y["sreća"]:
                        if NEGACIJA_AKTIVNA:
                            tuga=tuga+1
                            TUGA=TUGA+1
                        if not NEGACIJA_AKTIVNA:
                            sreća=sreća+1
                            SREĆA=SREĆA+1
                except:
                    pass

                try:
                    if y["spokoj"]:
                        if NEGACIJA_AKTIVNA:
                            sjeta=sjeta+1
                            SJETA=SJETA+1
                        if not NEGACIJA_AKTIVNA:
                            spokoj=spokoj+1
                            SPOKOJ=SPOKOJ+1
                except:
                    pass

                try:
                    if y["patnja"]:
                        if NEGACIJA_AKTIVNA:
                            ekstaza=ekstaza+1
                            EKSTAZA=EKSTAZA+1
                        if not NEGACIJA_AKTIVNA:
                            patnja=patnja+1
                except:
                    pass
                
                try:
                    if y["tuga"]:
                        if NEGACIJA_AKTIVNA:
                            sreća=sreća+1
                            SREĆA=SREĆA+1
                        if not NEGACIJA_AKTIVNA:
                            tuga=tuga+1
                            TUGA=TUGA+1
                except:
                    pass
                
                try:
                    if y["sjeta"]:
                        if NEGACIJA_AKTIVNA:
                            spokoj=spokoj+1
                            SPOKOJ=SPOKOJ+1
                        if not NEGACIJA_AKTIVNA:
                            sjeta=sjeta+1
                            SJETA=SJETA+1
                except:
                    pass

                try:
                    if y["zapanjenost"]:
                        if NEGACIJA_AKTIVNA:
                            budnost=budnost+1
                            BUDNOST=BUDNOST+1
                        if not NEGACIJA_AKTIVNA:
                            zapanjenost=zapanjenost+1
                            ZAPANJENOST=ZAPANJENOST+1
                except:
                    pass
                
                try:
                    if y["iznenađenje"]:
                        if NEGACIJA_AKTIVNA:
                            očekivanje=očekivanje+1
                            OČEKIVANJE=OČEKIVANJE+1
                        if not NEGACIJA_AKTIVNA:
                            iznenađenje=iznenađenje+1
                            IZNENAĐENJE=IZNENAĐENJE+1
                except:
                    pass
                
                try:
                    if y["distrakcija"]:
                        if NEGACIJA_AKTIVNA:
                            interes=interes+1
                            INTERES=INTERES+1
                        if not NEGACIJA_AKTIVNA:
                            distrakcija=distrakcija+1
                            DISTRAKCIJA=DISTRAKCIJA+1
                except:
                    pass

                try:
                    if y["divljenje"]:
                        if NEGACIJA_AKTIVNA:
                            gnušanje=gnušanje+1
                            GNUŠANJE=GNUŠANJE+1
                        if not NEGACIJA_AKTIVNA:
                            divljenje=divljenje+1
                            DIVLJENJE=DIVLJENJE+1
                except:
                    pass
                
                try:
                    if y["povjerenje"]:
                        if NEGACIJA_AKTIVNA:
                            gađenje=gađenje+1
                            GAĐENJE=GAĐENJE+1
                        if not NEGACIJA_AKTIVNA:
                            povjerenje=povjerenje+1
                            POVJERENJE=POVJERENJE+1
                except:
                    pass
                
                try:
                    if y["prihvaćanje"]:
                        if NEGACIJA_AKTIVNA:
                            averzija=averzija+1
                            AVERZIJA=AVERZIJA+1
                        if not NEGACIJA_AKTIVNA:
                            prihvaćanje=prihvaćanje+1
                            PRIHVAĆANJE=PRIHVAĆANJE+1
                except:
                    pass
        #__________________________SEKUNDANRE_____________________________
                try:
                    if y["očaj_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            ponos_int_1=ponos_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            očaj_int_1=očaj_int_1+1
                except:
                    pass
                try:
                    if y["očaj_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            ponos_int_2=ponos_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            očaj_int_2=očaj_int_2+1
                except:
                    pass
                try:
                    if y["očaj_int_3"]:
                        if NEGACIJA_AKTIVNA:
                            pobjeda=pobjeda+1
                        if not NEGACIJA_AKTIVNA:
                            očaj_int_3=očaj_int_3+1
                except:
                    pass
                try:
                    if y["neodobravanje_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            optimizam_int_1=optimizam_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            neodobravanje_int_1=neodobravanje_int_1+1
                except:
                    pass
                try:
                    if y["neodobravanje_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            optimizam_int_2=optimizam_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            neodobravanje_int_2=neodobravanje_int_2+1
                except:
                    pass
                try:
                    if y["razočaranje"]:
                        if NEGACIJA_AKTIVNA:
                            hrabrost=hrabrost+1
                        if not NEGACIJA_AKTIVNA:
                            razočaranje=razočaranje+1
                except:
                    pass
                try:
                    if y["nevjerica_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            nada_int_1=nada_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            nevjerica_int_1=nevjerica_int_1+1
                except:
                    pass
                try:
                    if y["nevjerica_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            nada_int_2=nada_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            nevjerica_int_2=nevjerica_int_2+1
                except:
                    pass
                try:
                    if y["šok"]:
                        if NEGACIJA_AKTIVNA:
                            nada_int_3=nada_int_3+1
                        if not NEGACIJA_AKTIVNA:
                            šok=šok+1
                except:
                    pass
                try:
                    if y["žaljenje_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            prijateljstvo=prijateljstvo+1
                        if not NEGACIJA_AKTIVNA:
                            žaljenje_int_1=žaljenje_int_1+1
                except:
                    pass
                try:
                    if y["žaljenje_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            ljubav=ljubav+1
                        if not NEGACIJA_AKTIVNA:
                            žaljenje_int_2=žaljenje_int_2+1
                except:
                    pass
                try:
                    if y["nesretan"]:
                        if NEGACIJA_AKTIVNA:
                            obožavanje=obožavanje+1
                        if not NEGACIJA_AKTIVNA:
                            nesretan=nesretan+1
                except:
                    pass
                try:
                    if y["strahopoštovanje_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            agresija_int_1=agresija_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            strahopoštovanje_int_1=strahopoštovanje_int_1+1
                except:
                    pass
                try:
                    if y["strahopoštovanje_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            agresija_int_2=agresija_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            strahopoštovanje_int_2=strahopoštovanje_int_2+1
                except:
                    pass
                try:
                    if y["strahopoštovanje_int_3"]:
                        if NEGACIJA_AKTIVNA:
                            agresija_int_3=agresija_int_3+1
                        if not NEGACIJA_AKTIVNA:
                            strahopoštovanje_int_3=strahopoštovanje_int_3+1
                except:
                    pass
                try:
                    if y["podređenost_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            prezir_int_1=prezir_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            podređenost_int_1=podređenost_int_1+1
                except:
                    pass
                try:
                    if y["podređenost_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            prezir_int_2=prezir_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            podređenost_int_2=podređenost_int_2+1
                except:
                    pass
                try:
                    if y["podređenost_int_3"]:
                        if NEGACIJA_AKTIVNA:
                            bez_poštovanja=bez_poštovanja+1
                        if not NEGACIJA_AKTIVNA:
                            podređenost_int_3=podređenost_int_3+1
                except:
                    pass
                try:
                    if y["zadovoljstvo_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            pesimizam_int_1=pesimizam_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            zadovoljstvo_int_1=zadovoljstvo_int_1+1
                except:
                    pass
                try:
                    if y["zadovoljstvo_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            pesimizam_int_2=pesimizam_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            zadovoljstvo_int_2=zadovoljstvo_int_2+1
                except:
                    pass
                try:
                    if y["zadovoljstvo_int_3"]:
                        if NEGACIJA_AKTIVNA:
                            nepovjerenje=nepovjerenje+1
                        if not NEGACIJA_AKTIVNA:
                            zadovoljstvo_int_3=zadovoljstvo_int_3+1
                except:
                    pass
                try:
                    if y["znatiželja_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            cinizam_int_1=cinizam_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            znatiželja_int_1=znatiželja_int_1+1
                except:
                    pass
                try:
                    if y["znatiželja_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            cinizam_int_2=cinizam_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            znatiželja_int_2=znatiželja_int_2+1
                except:
                    pass
                try:
                    if y["znatiželja_int_3"]:
                        if NEGACIJA_AKTIVNA:
                            cinizam_int_3=cinizam_int_3+1
                        if not NEGACIJA_AKTIVNA:
                            znatiželja_int_3=znatiželja_int_3+1
                except:
                    pass
                try:
                    if y["sentimentalnost_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            morbidnost_int_1=morbidnost_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            sentimentalnost_int_1=sentimentalnost_int_1+1
                except:
                    pass
                try:
                    if y["sentimentalnost_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            morbidnost_int_2=morbidnost_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            sentimentalnost_int_2=sentimentalnost_int_2+1
                except:
                    pass
                try:
                    if y["sentimentalnost_int_3"]:
                        if NEGACIJA_AKTIVNA:
                            ismijavanje=ismijavanje+1
                        if not NEGACIJA_AKTIVNA:
                            sentimentalnost_int_3=sentimentalnost_int_3+1
                except:
                    pass
                try:
                    if y["ponos_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            očaj_int_1=očaj_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            ponos_int_1=ponos_int_1+1
                except:
                    pass
                try:
                    if y["ponos_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            očaj_int_2=očaj_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            ponos_int_2=ponos_int_2+1
                except:
                    pass
                try:
                    if y["pobjeda"]:
                        if NEGACIJA_AKTIVNA:
                            očaj_int_3=očaj_int_3+1
                        if not NEGACIJA_AKTIVNA:
                            pobjeda=pobjeda+1
                except:
                    pass
                try:
                    if y["optimizam_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            neodobravanje_int_1=neodobravanje_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            optimizam_int_1=optimizam_int_1+1
                except:
                    pass
                try:
                    if y["optimizam_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            neodobravanje_int_2=neodobravanje_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            optimizam_int_2=optimizam_int_2+1
                except:
                    pass
                try:
                    if y["hrabrost"]:
                        if NEGACIJA_AKTIVNA:
                            razočaranje=razočaranje+1
                        if not NEGACIJA_AKTIVNA:
                            hrabrost=hrabrost+1
                except:
                    pass
                try:
                    if y["nada_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            nevjerica_int_1=nevjerica_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            nada_int_1=nada_int_1+1
                except:
                    pass
                try:
                    if y["nada_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            nevjerica_int_2=nevjerica_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            nada_int_2=nada_int_2+1
                except:
                    pass
                try:
                    if y["nada_int_3"]:
                        if NEGACIJA_AKTIVNA:
                            šok=šok+1
                        if not NEGACIJA_AKTIVNA:
                            nada_int_3=nada_int_3+1
                except:
                    pass
                try:
                    if y["krivnja_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            zavist_int_1=zavist_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            krivnja_int_1=krivnja_int_1+1
                except:
                    pass
                try:
                    if y["krivnja_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            zavist_int_2=zavist_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            krivnja_int_2=krivnja_int_2+1
                except:
                    pass
                try:
                    if y["uzbuđenje"]:
                        if NEGACIJA_AKTIVNA:
                            neugoda=neugoda+1
                        if not NEGACIJA_AKTIVNA:
                            uzbuđenje=uzbuđenje+1
                except:
                    pass
                try:
                    if y["sram_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            dominacija_int_1=dominacija_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            sram_int_1=sram_int_1+1
                except:
                    pass
                try:
                    if y["sram_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            dominacija_int_2=dominacija_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            sram_int_2=sram_int_2+1
                except:
                    pass
                try:
                    if y["bezobraština"]:
                        if NEGACIJA_AKTIVNA:
                            dominacija_int_3=dominacija_int_3+1
                        if not NEGACIJA_AKTIVNA:
                            bezobraština=bezobraština+1
                except:
                    pass
                try:
                    if y["prezir_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            podređenost_int_1=podređenost_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            prezir_int_1=prezir_int_1+1
                except:
                    pass
                try:
                    if y["prezir_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            podređenost_int_2=podređenost_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            prezir_int_2=prezir_int_2+1
                except:
                    pass
                try:
                    if y["bez_poštovanja"]:
                        if NEGACIJA_AKTIVNA:
                            podređenost_int_3=podređenost_int_3+1
                        if not NEGACIJA_AKTIVNA:
                            bez_poštovanja=bez_poštovanja+1
                except:
                    pass
                try:
                    if y["zavist_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            krivnja_int_1=krivnja_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            zavist_int_1=zavist_int_1+1
                except:
                    pass
                try:
                    if y["zavist_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            krivnja_int_2=krivnja_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            zavist_int_2=zavist_int_2+1
                except:
                    pass
                try:
                    if y["neugoda"]:
                        if NEGACIJA_AKTIVNA:
                            uzbuđenje=uzbuđenje+1
                        if not NEGACIJA_AKTIVNA:
                            neugoda=neugoda+1
                except:
                    pass
                try:
                    if y["dominacija_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            sram_int_1=sram_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            dominacija_int_1=dominacija_int_1+1
                except:
                    pass
                try:
                    if y["dominacija_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            sram_int_2=sram_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            dominacija_int_2=dominacija_int_2+1
                except:
                    pass
                try:
                    if y["dominacija_int_3"]:
                        if NEGACIJA_AKTIVNA:
                            bezobraština=bezobraština+1
                        if not NEGACIJA_AKTIVNA:
                            dominacija_int_3=dominacija_int_3+1
                except:
                    pass
                try:
                    if y["agresija_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            strahopoštovanje_int_1=strahopoštovanje_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            agresija_int_1=agresija_int_1+1
                except:
                    pass
                try:
                    if y["agresija_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            strahopoštovanje_int_2=strahopoštovanje_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            agresija_int_2=agresija_int_2+1
                except:
                    pass
                try:
                    if y["agresija_int_3"]:
                        if NEGACIJA_AKTIVNA:
                            strahopoštovanje_int_3=strahopoštovanje_int_3+1
                        if not NEGACIJA_AKTIVNA:
                            agresija_int_3=agresija_int_3+1
                except:
                    pass
                try:
                    if y["uvreda_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            anksioznost_int_1=anksioznost_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            uvreda_int_1=uvreda_int_1+1
                except:
                    pass
                try:
                    if y["uvreda_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            anksioznost_int_2=anksioznost_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            uvreda_int_2=uvreda_int_2+1
                except:
                    pass
                try:
                    if y["mržnja"]:
                        if NEGACIJA_AKTIVNA:
                            zabrinutost=zabrinutost+1
                        if not NEGACIJA_AKTIVNA:
                            mržnja=mržnja+1
                except:
                    pass
                try:
                    if y["pesimizam_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            zadovoljstvo_int_1=zadovoljstvo_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            pesimizam_int_1=pesimizam_int_1+1
                except:
                    pass
                try:
                    if y["pesimizam_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            zadovoljstvo_int_2=zadovoljstvo_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            pesimizam_int_2=pesimizam_int_2+1
                except:
                    pass
                try:
                    if y["nepovjerenje"]:
                        if NEGACIJA_AKTIVNA:
                            zadovoljstvo_int_3=zadovoljstvo_int_3+1
                        if not NEGACIJA_AKTIVNA:
                            nepovjerenje=nepovjerenje+1
                except:
                    pass
                try:
                    if y["anksioznost_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            uvreda_int_1=uvreda_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            anksioznost_int_1=anksioznost_int_1+1
                except:
                    pass
                try:
                    if y["anksioznost_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            uvreda_int_2=uvreda_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            anksioznost_int_2=anksioznost_int_2+1
                except:
                    pass
                try:
                    if y["zabrinutost"]:
                        if NEGACIJA_AKTIVNA:
                            mržnja=mržnja+1
                        if not NEGACIJA_AKTIVNA:
                            zabrinutost=zabrinutost+1
                except:
                    pass
                try:
                    if y["morbidnost_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            sentimentalnost_int_1=sentimentalnost_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            morbidnost_int_1=morbidnost_int_1+1
                except:
                    pass
                try:
                    if y["morbidnost_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            sentimentalnost_int_2=sentimentalnost_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            morbidnost_int_2=morbidnost_int_2+1
                except:
                    pass
                try:
                    if y["ismijavanje"]:
                        if NEGACIJA_AKTIVNA:
                            sentimentalnost_int_3=sentimentalnost_int_3+1
                        if not NEGACIJA_AKTIVNA:
                            ismijavanje=ismijavanje+1
                except:
                    pass
                try:
                    if y["cinizam_int_1"]:
                        if NEGACIJA_AKTIVNA:
                            znatiželja_int_1=znatiželja_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            cinizam_int_1=cinizam_int_1+1
                except:
                    pass
                try:
                    if y["cinizam_int_2"]:
                        if NEGACIJA_AKTIVNA:
                            znatiželja_int_2=znatiželja_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            cinizam_int_2=cinizam_int_2+1
                except:
                    pass
                try:
                    if y["cinizam_int_3"]:
                        if NEGACIJA_AKTIVNA:
                            znatiželja_int_3=znatiželja_int_3+1
                        if not NEGACIJA_AKTIVNA:
                            cinizam_int_3=cinizam_int_3+1
                except:
                    pass
                try:
                    if y["prijateljstvo"]:
                        if NEGACIJA_AKTIVNA:
                            žaljenje_int_1=žaljenje_int_1+1
                        if not NEGACIJA_AKTIVNA:
                            prijateljstvo=prijateljstvo+1
                except:
                    pass
                try:
                    if y["ljubav"]:
                        if NEGACIJA_AKTIVNA:
                            žaljenje_int_2=žaljenje_int_2+1
                        if not NEGACIJA_AKTIVNA:
                            ljubav=ljubav+1
                except:
                    pass
                try:
                    if y["obožavanje"]:
                        if NEGACIJA_AKTIVNA:
                            nesretan=nesretan+1
                        if not NEGACIJA_AKTIVNA:
                            obožavanje=obožavanje+1
                except:
                    pass
            except:
                pass
    #PRIMARNE            

    #SURPRISE		ANTICIPATION
    #ANTICIPATION		SURPRISE
    #TRUST			DISGUST
    #DISGUST			TRUST
    #ANGER			FEAR
    #FEAR			ANGER
    #JOY			SADNESS#
    #SADNESS			JOY

    # SEKUNDARNE 

    #PODREĐENOST        #PREZIR
    #LJUBAV             #ŽALJENJE (kajanje)
    #OPTIMIZAM          #NEODOBRAVANJE
    #NADA               #NEVJERICA (horror) šok
    #KRIVNJA            #ZAVIST
    #ZNATIŽELJA         #CINIZAM
    #PONOS              #OČAJ
    #DOMINACIJA         #SRAM
    #SENTIMENTALNOST    #MORBIDNOST
    #ZADOVOLJSTVO       #PESIMIZAM
    #ANKSIOZNOST        #UVREDA
#https:||www.jutarnji.hr|dobrahrana|pricetrenutak-iskrenosti-davida-skoke-frapirao-sve-u-rovinju-sve-sto-radimo-je-krivo-ovo-je-katastrofa-15326312
            if (NEGACIJA_AKTIVNA==True) and ('niječni' not in y["vrsta"]):

                korak=korak-1
                if korak==0:
                    NEGACIJA_AKTIVNA=False
                
        #finale = '{"rečenica":"'+HR[loop_over_sentence].replace('"','')+'", '

        #if bijes!=0: finale=finale+'"bijes":'+str(bijes)+', '
        #if ljutnja!=0: finale=finale+'"ljutnja":'+str(ljutnja)+', ' 
        #if odvažnost!=0: finale=finale+'"odvažnost":'+str(odvažnost)+', '

        #if budnost!=0: finale=finale+'"budnost":'+str(budnost)+', '
        #if očekivanje!=0: finale=finale+'"očekivanje":'+str(očekivanje)+', '
        #if interes!=0: finale=finale+'"interes":'+str(interes)+', '

        #if gnušanje!=0: finale=finale+'"gnušanje":'+str(gnušanje)+', '
        #if gađenje!=0: finale=finale+'"gađenje":'+str(gađenje)+', '
        #if averzija!=0: finale=finale+'"averzija":'+str(averzija)+', '

        #if teror!=0: finale=finale+'"teror":'+str(teror)+', '
        #if strah!=0: finale=finale+'"strah":'+str(strah)+', '
        #if bojazan!=0: finale=finale+'"bojazan":'+str(bojazan)+', '

        #if ekstaza!=0: finale=finale+'"ekstaza":'+str(ekstaza)+', '
        #if sreća!=0: finale=finale+'"sreća":'+str(sreća)+', '
        #if spokoj!=0: finale=finale+'"spokoj":'+str(spokoj)+', '

        #if patnja!=0: finale=finale+'"patnja":'+str(patnja)+', '
        #if tuga!=0: finale=finale+'"tuga":'+str(tuga)+', '
        #if sjeta!=0: finale=finale+'"sjeta":'+str(sjeta)+', '

        #if zapanjenost!=0: finale=finale+'"zapanjenost":'+str(zapanjenost)+', '
        #if iznenađenje!=0: finale=finale+'"iznenađenje":'+str(iznenađenje)+', '
        #if distrakcija!=0: finale=finale+'"distrakcija":'+str(distrakcija)+', '

        #if divljenje!=0: finale=finale+'"divljenje":'+str(divljenje)+', '
        #if povjerenje!=0: finale=finale+'"povjerenje":'+str(povjerenje)+', '
        #if prihvaćanje!=0: finale=finale+'"prihvaćanje":'+str(prihvaćanje)+', '
        
        #_________________________________SEKUNDARNE________________
        #if očaj_int_1!=0: finale=finale+'"očaj_int_1":'+str(očaj_int_1)+', '
        #if očaj_int_2!=0: finale=finale+'"očaj_int_2":'+str(očaj_int_2)+', '
        #if očaj_int_3!=0: finale=finale+'"očaj_int_3":'+str(očaj_int_3)+', '
        #if neodobravanje_int_1!=0: finale=finale+'"neodobravanje_int_1":'+str(neodobravanje_int_1)+', '
        #if neodobravanje_int_2!=0: finale=finale+'"neodobravanje_int_2":'+str(neodobravanje_int_2)+', '
        #if razočaranje!=0: finale=finale+'"razočaranje":'+str(razočaranje)+', '
        #if nevjerica_int_1!=0: finale=finale+'"nevjerica_int_1":'+str(nevjerica_int_1)+', '
        #if nevjerica_int_2!=0: finale=finale+'"nevjerica_int_2":'+str(nevjerica_int_2)+', '
        #if šok!=0: finale=finale+'"šok":'+str(šok)+', '
        #if žaljenje_int_1!=0: finale=finale+'"žaljenje_int_1":'+str(žaljenje_int_1)+', '
        #if žaljenje_int_2!=0: finale=finale+'"žaljenje_int_2":'+str(žaljenje_int_2)+', '
        #if nesretan!=0: finale=finale+'"nesretan":'+str(nesretan)+', '
        #if strahopoštovanje_int_1!=0: finale=finale+'"strahopoštovanje_int_1":'+str(strahopoštovanje_int_1)+', '
        #if strahopoštovanje_int_2!=0: finale=finale+'"strahopoštovanje_int_2":'+str(strahopoštovanje_int_2)+', '
        #if strahopoštovanje_int_3!=0: finale=finale+'"strahopoštovanje_int_3":'+str(strahopoštovanje_int_3)+', '
        #if podređenost_int_1!=0: finale=finale+'"podređenost_int_1":'+str(podređenost_int_1)+', '
        #if podređenost_int_2!=0: finale=finale+'"podređenost_int_2":'+str(podređenost_int_2)+', '
        #if podređenost_int_3!=0: finale=finale+'"podređenost_int_3":'+str(podređenost_int_3)+', '
        #if zadovoljstvo_int_1!=0: finale=finale+'"zadovoljstvo_int_1":'+str(zadovoljstvo_int_1)+', '
        #if zadovoljstvo_int_2!=0: finale=finale+'"zadovoljstvo_int_2":'+str(zadovoljstvo_int_2)+', '
        #if zadovoljstvo_int_3!=0: finale=finale+'"zadovoljstvo_int_3":'+str(zadovoljstvo_int_3)+', '
        #if znatiželja_int_1!=0: finale=finale+'"znatiželja_int_1":'+str(znatiželja_int_1)+', '
        #if znatiželja_int_2!=0: finale=finale+'"znatiželja_int_2":'+str(znatiželja_int_2)+', '
        #if znatiželja_int_3!=0: finale=finale+'"znatiželja_int_3":'+str(znatiželja_int_3)+', '
        #if sentimentalnost_int_1!=0: finale=finale+'"sentimentalnost_int_1":'+str(sentimentalnost_int_1)+', '
        #if sentimentalnost_int_2!=0: finale=finale+'"sentimentalnost_int_2":'+str(sentimentalnost_int_2)+', '
        #if sentimentalnost_int_3!=0: finale=finale+'"sentimentalnost_int_3":'+str(sentimentalnost_int_3)+', '
        #if ponos_int_1!=0: finale=finale+'"ponos_int_1":'+str(ponos_int_1)+', '
        #if ponos_int_2!=0: finale=finale+'"ponos_int_2":'+str(ponos_int_2)+', '
        #if pobjeda!=0: finale=finale+'"pobjeda":'+str(pobjeda)+', '
        #if optimizam_int_1!=0: finale=finale+'"optimizam_int_1":'+str(optimizam_int_1)+', '
        #if optimizam_int_2!=0: finale=finale+'"optimizam_int_2":'+str(optimizam_int_2)+', '
        #if hrabrost!=0: finale=finale+'"hrabrost":'+str(hrabrost)+', '
        #if nada_int_1!=0: finale=finale+'"nada_int_1":'+str(nada_int_1)+', '
        #if nada_int_2!=0: finale=finale+'"nada_int_2":'+str(nada_int_2)+', '
        #if nada_int_3!=0: finale=finale+'"nada_int_3":'+str(nada_int_3)+', '
        #if krivnja_int_1!=0: finale=finale+'"krivnja_int_1":'+str(krivnja_int_1)+', '
        #if krivnja_int_2!=0: finale=finale+'"krivnja_int_2":'+str(krivnja_int_2)+', '
        #if uzbuđenje!=0: finale=finale+'"uzbuđenje":'+str(uzbuđenje)+', '
        #if sram_int_1!=0: finale=finale+'"sram_int_1":'+str(sram_int_1)+', '
        #if sram_int_2!=0: finale=finale+'"sram_int_2":'+str(sram_int_2)+', '
        #if bezobraština!=0: finale=finale+'"bezobraština":'+str(bezobraština)+', '
        #if prezir_int_1!=0: finale=finale+'"prezir_int_1":'+str(prezir_int_1)+', '
        #if prezir_int_2!=0: finale=finale+'"prezir_int_2":'+str(prezir_int_2)+', '
        #if bez_poštovanja!=0: finale=finale+'"bez_poštovanjabijes":'+str(bez_poštovanja)+', '
        #if zavist_int_1!=0: finale=finale+'"zavist_int_1":'+str(zavist_int_1)+', '
        #if zavist_int_2!=0: finale=finale+'"zavist_int_2":'+str(zavist_int_2)+', '
        #if neugoda!=0: finale=finale+'"neugoda":'+str(neugoda)+', '
        #if dominacija_int_1!=0: finale=finale+'"dominacija_int_1":'+str(dominacija_int_1)+', '
        #if dominacija_int_2!=0: finale=finale+'"dominacija_int_2":'+str(dominacija_int_2)+', '
        #if dominacija_int_3!=0: finale=finale+'"dominacija_int_3":'+str(dominacija_int_3)+', '
        #if agresija_int_1!=0: finale=finale+'"agresija_int_1":'+str(agresija_int_1)+', '
        #if agresija_int_2!=0: finale=finale+'"agresija_int_2":'+str(agresija_int_2)+', '
        #if agresija_int_3!=0: finale=finale+'"agresija_int_3":'+str(agresija_int_3)+', '
        #if uvreda_int_1!=0: finale=finale+'"uvreda_int_1":'+str(uvreda_int_1)+', '
        #if uvreda_int_2!=0: finale=finale+'"uvreda_int_2":'+str(uvreda_int_2)+', '
        #if mržnja!=0: finale=finale+'"mržnja":'+str(mržnja)+', '
        #if pesimizam_int_1!=0: finale=finale+'"pesimizam_int_1":'+str(pesimizam_int_1)+', '
        #if pesimizam_int_2!=0: finale=finale+'"pesimizam_int_2":'+str(pesimizam_int_2)+', '
        #if nepovjerenje!=0: finale=finale+'"nepovjerenje":'+str(nepovjerenje)+', '
        #if anksioznost_int_1!=0: finale=finale+'"anksioznost_int_1":'+str(anksioznost_int_1)+', '
        #if anksioznost_int_2!=0: finale=finale+'"anksioznost_int_2":'+str(anksioznost_int_2)+', '
        #if zabrinutost!=0: finale=finale+'"zabrinutost":'+str(zabrinutost)+', '
        #if morbidnost_int_1!=0: finale=finale+'"morbidnost_int_1":'+str(morbidnost_int_1)+', '
        #if morbidnost_int_2!=0: finale=finale+'"morbidnost_int_2":'+str(morbidnost_int_2)+', '
        #if ismijavanje!=0: finale=finale+'"ismijavanje":'+str(ismijavanje)+', '
        #if cinizam_int_1!=0: finale=finale+'"cinizam_int_1":'+str(cinizam_int_1)+', '
        #if cinizam_int_2!=0: finale=finale+'"cinizam_int_2":'+str(cinizam_int_2)+', '
        #if cinizam_int_3!=0: finale=finale+'"cinizam_int_3":'+str(cinizam_int_3)+', '
        #if prijateljstvo!=0: finale=finale+'"prijateljstvo":'+str(prijateljstvo)+', '
        #if ljubav!=0: finale=finale+'"ljubav":'+str(ljubav)+', '
        #if obožavanje!=0: finale=finale+'"obožavanje":'+str(obožavanje)+', '

        CLEAN_LINE='{"rečenica":"'+HR[loop_over_sentence].replace('"','').replace("'",'*')+'", '

    #SURPRISE		ANTICIPATION
        if budnost>zapanjenost:
            CLEAN_LINE=CLEAN_LINE+'"budnost":'+str(abs(budnost-zapanjenost))+', '
        if budnost<zapanjenost:
            CLEAN_LINE=CLEAN_LINE+'"zapanjenost":'+str(abs(budnost-zapanjenost))+', '
        if budnost==zapanjenost:
            pass
        if očekivanje>iznenađenje:
            CLEAN_LINE=CLEAN_LINE+'"očekivanje":'+str(abs(očekivanje-iznenađenje))+', '
        if očekivanje<iznenađenje:
            CLEAN_LINE=CLEAN_LINE+'"iznenađenje":'+str(abs(očekivanje-iznenađenje))+', '
        if očekivanje==iznenađenje:
            pass
        if interes>distrakcija:
            CLEAN_LINE=CLEAN_LINE+'"interes":'+str(abs(interes-distrakcija))+', '
        if interes<distrakcija:
            CLEAN_LINE=CLEAN_LINE+'"distrakcija":'+str(abs(interes-distrakcija))+', '
        if interes==distrakcija:
            pass
    #ANGER		FEAR
        if bijes>teror:
            CLEAN_LINE=CLEAN_LINE+'"bijes":'+str(abs(bijes-teror))+', '
        if bijes<teror:
            CLEAN_LINE=CLEAN_LINE+'"teror":'+str(abs(bijes-teror))+', '
        if bijes==teror:
            pass
        if ljutnja>strah:
            CLEAN_LINE=CLEAN_LINE+'"ljutnja":'+str(abs(ljutnja-strah))+', '
        if ljutnja<strah:
            CLEAN_LINE=CLEAN_LINE+'"strah":'+str(abs(ljutnja-strah))+', '
        if ljutnja==strah:
            pass
        if odvažnost>bojazan:
            CLEAN_LINE=CLEAN_LINE+'"odvažnost":'+str(abs(odvažnost-bojazan))+', '
        if odvažnost<bojazan:
            CLEAN_LINE=CLEAN_LINE+'"bojazan":'+str(abs(odvažnost-bojazan))+', '
        if odvažnost==bojazan:
            pass
    #TRUST			DISGUST
        if divljenje>gnušanje:
            CLEAN_LINE=CLEAN_LINE+'"divljenje":'+str(abs(divljenje-gnušanje))+', '
        if divljenje<gnušanje:
            CLEAN_LINE=CLEAN_LINE+'"gnušanje":'+str(abs(divljenje-gnušanje))+', '
        if divljenje==gnušanje:
            pass
        if povjerenje>gađenje:
            CLEAN_LINE=CLEAN_LINE+'"povjerenje":'+str(abs(povjerenje-gađenje))+', '
        if povjerenje<gađenje:
            CLEAN_LINE=CLEAN_LINE+'"gađenje":'+str(abs(povjerenje-gađenje))+', '
        if povjerenje==gađenje:
            pass
        if prihvaćanje>averzija:
            CLEAN_LINE=CLEAN_LINE+'"prihvaćanje":'+str(abs(prihvaćanje-averzija))+', '
        if prihvaćanje<averzija:
            CLEAN_LINE=CLEAN_LINE+'"averzija":'+str(abs(prihvaćanje-averzija))+', '
        if prihvaćanje==averzija:
            pass

    #JOY			SADNESS#
        if ekstaza>patnja:
            CLEAN_LINE=CLEAN_LINE+'"ekstaza":'+str(abs(ekstaza-patnja))+', '
        if ekstaza<patnja:
            CLEAN_LINE=CLEAN_LINE+'"patnja":'+str(abs(ekstaza-patnja))+', '
        if ekstaza==patnja:
            pass
        if sreća>tuga:
            CLEAN_LINE=CLEAN_LINE+'"sreća":'+str(abs(sreća-tuga))+', '
        if sreća<tuga:
            CLEAN_LINE=CLEAN_LINE+'"tuga":'+str(abs(sreća-tuga))+', '
        if sreća==tuga:
            pass
        if spokoj>sjeta:
            CLEAN_LINE=CLEAN_LINE+'"spokoj":'+str(abs(spokoj-sjeta))+', '
        if spokoj<sjeta:
            CLEAN_LINE=CLEAN_LINE+'"sjeta":'+str(abs(spokoj-sjeta))+', '
        if spokoj==sjeta:
            pass
        #-------------SEKUNDARNE
    #PODREĐENOST        #PREZIR
        if podređenost_int_1>prezir_int_1:
            CLEAN_LINE=CLEAN_LINE+'"podređenost_int_1":'+str(abs(podređenost_int_1-prezir_int_1))+', '
        if podređenost_int_1<prezir_int_1:
            CLEAN_LINE=CLEAN_LINE+'"prezir_int_1":'+str(abs(podređenost_int_1-prezir_int_1))+', '
        if podređenost_int_1==prezir_int_1:
            pass
        if podređenost_int_2>prezir_int_2:
            CLEAN_LINE=CLEAN_LINE+'"podređenost_int_2":'+str(abs(podređenost_int_2-prezir_int_2))+', '
        if podređenost_int_2<prezir_int_2:
            CLEAN_LINE=CLEAN_LINE+'"prezir_int_2":'+str(abs(podređenost_int_2-prezir_int_2))+', '
        if podređenost_int_2==prezir_int_2:
            pass
        if podređenost_int_3>bez_poštovanja:
            CLEAN_LINE=CLEAN_LINE+'"podređenost_int_3":'+str(abs(podređenost_int_3-bez_poštovanja))+', '
        if podređenost_int_3<bez_poštovanja:
            CLEAN_LINE=CLEAN_LINE+'"bez_poštovanja":'+str(abs(podređenost_int_3-bez_poštovanja))+', '
        if podređenost_int_3==bez_poštovanja:
            pass

    #LJUBAV             #ŽALJENJE (kajanje)
        if prijateljstvo>žaljenje_int_1:
            CLEAN_LINE=CLEAN_LINE+'"prijateljstvo":'+str(abs(prijateljstvo-žaljenje_int_1))+', '
        if prijateljstvo<žaljenje_int_1:
            CLEAN_LINE=CLEAN_LINE+'"žaljenje_int_1":'+str(abs(prijateljstvo-žaljenje_int_1))+', '
        if prijateljstvo==žaljenje_int_1:
            pass
        if ljubav>žaljenje_int_2:
            CLEAN_LINE=CLEAN_LINE+'"ljubav":'+str(abs(ljubav-žaljenje_int_2))+', '
        if ljubav<žaljenje_int_2:
            CLEAN_LINE=CLEAN_LINE+'"žaljenje_int_2":'+str(abs(ljubav-žaljenje_int_2))+', '
        if ljubav==žaljenje_int_2:
            pass
        if obožavanje>nesretan:
            CLEAN_LINE=CLEAN_LINE+'"obožavanje":'+str(abs(obožavanje-nesretan))+', '
        if obožavanje<nesretan:
            CLEAN_LINE=CLEAN_LINE+'"nesretan":'+str(abs(obožavanje-nesretan))+', '
        if obožavanje==nesretan:
            pass
    #OPTIMIZAM          #NEODOBRAVANJE
        if optimizam_int_1>neodobravanje_int_1:
            CLEAN_LINE=CLEAN_LINE+'"optimizam_int_1":'+str(abs(optimizam_int_1-neodobravanje_int_1))+', '
        if optimizam_int_1<neodobravanje_int_1:
            CLEAN_LINE=CLEAN_LINE+'"neodobravanje_int_1":'+str(abs(optimizam_int_1-neodobravanje_int_1))+', '
        if optimizam_int_1==neodobravanje_int_1:
            pass
        if optimizam_int_2>neodobravanje_int_2:
            CLEAN_LINE=CLEAN_LINE+'"optimizam_int_2":'+str(abs(optimizam_int_2-neodobravanje_int_2))+', '
        if optimizam_int_2<neodobravanje_int_2:
            CLEAN_LINE=CLEAN_LINE+'"neodobravanje_int_2":'+str(abs(optimizam_int_2-neodobravanje_int_2))+', '
        if optimizam_int_2==neodobravanje_int_2:
            pass
        if hrabrost>razočaranje:
            CLEAN_LINE=CLEAN_LINE+'"hrabrost":'+str(abs(hrabrost-razočaranje))+', '
        if hrabrost<razočaranje:
            CLEAN_LINE=CLEAN_LINE+'"razočaranje":'+str(abs(hrabrost-razočaranje))+', '
        if hrabrost==razočaranje:
            pass
    #NADA               #NEVJERICA (horror) šok
        if nada_int_1>nevjerica_int_1:
            CLEAN_LINE=CLEAN_LINE+'"nada_int_1":'+str(abs(nada_int_1-nevjerica_int_1))+', '
        if nada_int_1<nevjerica_int_1:
            CLEAN_LINE=CLEAN_LINE+'"nevjerica_int_1":'+str(abs(nada_int_1-nevjerica_int_1))+', '
        if nada_int_1==nevjerica_int_1:
            pass
        if nada_int_2>nevjerica_int_2:
            CLEAN_LINE=CLEAN_LINE+'"nada_int_2":'+str(abs(nada_int_2-nevjerica_int_2))+', '
        if nada_int_2<nevjerica_int_2:
            CLEAN_LINE=CLEAN_LINE+'"nevjerica_int_2":'+str(abs(nada_int_2-nevjerica_int_2))+', '
        if nada_int_2==nevjerica_int_2:
            pass
        if nada_int_3>šok:
            CLEAN_LINE=CLEAN_LINE+'"nada_int_3":'+str(abs(nada_int_3-šok))+', '
        if nada_int_3<šok:
            CLEAN_LINE=CLEAN_LINE+'"šok":'+str(abs(nada_int_3-šok))+', '
        if nada_int_3==šok:
            pass
    #KRIVNJA            #ZAVIST
        if krivnja_int_1>zavist_int_1:
            CLEAN_LINE=CLEAN_LINE+'"krivnja_int_1":'+str(abs(krivnja_int_1-zavist_int_1))+', '
        if krivnja_int_1<zavist_int_1:
            CLEAN_LINE=CLEAN_LINE+'"zavist_int_1":'+str(abs(krivnja_int_1-zavist_int_1))+', '
        if krivnja_int_1==zavist_int_1:
            pass
        if krivnja_int_2>zavist_int_2:
            CLEAN_LINE=CLEAN_LINE+'"krivnja_int_2":'+str(abs(krivnja_int_2-zavist_int_2))+', '
        if krivnja_int_2<zavist_int_2:
            CLEAN_LINE=CLEAN_LINE+'"zavist_int_2":'+str(abs(krivnja_int_2-zavist_int_2))+', '
        if krivnja_int_2==zavist_int_2:
            pass
        if uzbuđenje>neugoda:
            CLEAN_LINE=CLEAN_LINE+'"nauzbuđenjeda_int_3":'+str(abs(uzbuđenje-neugoda))+', '
        if uzbuđenje<neugoda:
            CLEAN_LINE=CLEAN_LINE+'"neugoda":'+str(abs(uzbuđenje-neugoda))+', '
        if uzbuđenje==neugoda:
            pass
    #ZNATIŽELJA         #CINIZAM
        if znatiželja_int_1>cinizam_int_1:
            CLEAN_LINE=CLEAN_LINE+'"znatiželja_int_1":'+str(abs(znatiželja_int_1-cinizam_int_1))+', '
        if znatiželja_int_1<cinizam_int_1:
            CLEAN_LINE=CLEAN_LINE+'"cinizam_int_1":'+str(abs(znatiželja_int_1-cinizam_int_1))+', '
        if znatiželja_int_1==cinizam_int_1:
            pass
        if znatiželja_int_2>cinizam_int_2:
            CLEAN_LINE=CLEAN_LINE+'"znatiželja_int_2":'+str(abs(znatiželja_int_2-cinizam_int_2))+', '
        if znatiželja_int_2<cinizam_int_2:
            CLEAN_LINE=CLEAN_LINE+'"cinizam_int_2":'+str(abs(znatiželja_int_2-cinizam_int_2))+', '
        if znatiželja_int_2==cinizam_int_2:
            pass
        if znatiželja_int_3>cinizam_int_3:
            CLEAN_LINE=CLEAN_LINE+'"znatiželja_int_3":'+str(abs(znatiželja_int_3-cinizam_int_3))+', '
        if znatiželja_int_3<cinizam_int_3:
            CLEAN_LINE=CLEAN_LINE+'"cinizam_int_3":'+str(abs(znatiželja_int_3-cinizam_int_3))+', '
        if znatiželja_int_3==cinizam_int_3:
            pass
    #PONOS              #OČAJ
        if ponos_int_1>očaj_int_1:
            CLEAN_LINE=CLEAN_LINE+'"ponos_int_1":'+str(abs(ponos_int_1-očaj_int_1))+', '
        if ponos_int_1<očaj_int_1:
            CLEAN_LINE=CLEAN_LINE+'"očaj_int_1":'+str(abs(ponos_int_1-očaj_int_1))+', '
        if ponos_int_1==očaj_int_1:
            pass
        if ponos_int_2>očaj_int_2:
            CLEAN_LINE=CLEAN_LINE+'"ponos_int_2":'+str(abs(ponos_int_2-očaj_int_2))+', '
        if ponos_int_2<očaj_int_2:
            CLEAN_LINE=CLEAN_LINE+'"očaj_int_2":'+str(abs(ponos_int_2-očaj_int_2))+', '
        if ponos_int_2==očaj_int_2:
            pass
        if pobjeda>očaj_int_3:
            CLEAN_LINE=CLEAN_LINE+'"pobjeda":'+str(abs(pobjeda-očaj_int_3))+', '
        if pobjeda<očaj_int_3:
            CLEAN_LINE=CLEAN_LINE+'"očaj_int_3":'+str(abs(pobjeda-očaj_int_3))+', '
        if pobjeda==očaj_int_3:
            pass
    #DOMINACIJA         #SRAM
        if dominacija_int_1>sram_int_1:
            CLEAN_LINE=CLEAN_LINE+'"dominacija_int_1":'+str(abs(dominacija_int_1-sram_int_1))+', '
        if dominacija_int_1<sram_int_1:
            CLEAN_LINE=CLEAN_LINE+'"sram_int_1":'+str(abs(dominacija_int_1-sram_int_1))+', '
        if dominacija_int_1==sram_int_1:
            pass
        if dominacija_int_2>sram_int_2:
            CLEAN_LINE=CLEAN_LINE+'"dominacija_int_2":'+str(abs(dominacija_int_2-sram_int_2))+', '
        if dominacija_int_2<sram_int_2:
            CLEAN_LINE=CLEAN_LINE+'"sram_int_2":'+str(abs(dominacija_int_2-sram_int_2))+', '
        if dominacija_int_2==sram_int_2:
            pass
        if dominacija_int_3>bezobraština:
            CLEAN_LINE=CLEAN_LINE+'"dominacija_int_3":'+str(abs(dominacija_int_3-bezobraština))+', '
        if dominacija_int_3<bezobraština:
            CLEAN_LINE=CLEAN_LINE+'"bezobraština":'+str(abs(dominacija_int_3-bezobraština))+', '
        if dominacija_int_3==bezobraština:
            pass

    #SENTIMENTALNOST    #MORBIDNOST
        if sentimentalnost_int_1>morbidnost_int_1:
            CLEAN_LINE=CLEAN_LINE+'"sentimentalnost_int_1":'+str(abs(sentimentalnost_int_1-morbidnost_int_1))+', '
        if sentimentalnost_int_1<morbidnost_int_1:
            CLEAN_LINE=CLEAN_LINE+'"morbidnost_int_1":'+str(abs(sentimentalnost_int_1-morbidnost_int_1))+', '
        if sentimentalnost_int_1==morbidnost_int_1:
            pass
        if sentimentalnost_int_2>morbidnost_int_2:
            CLEAN_LINE=CLEAN_LINE+'"sentimentalnost_int_2":'+str(abs(sentimentalnost_int_2-morbidnost_int_2))+', '
        if sentimentalnost_int_2<morbidnost_int_2:
            CLEAN_LINE=CLEAN_LINE+'"morbidnost_int_2":'+str(abs(sentimentalnost_int_2-morbidnost_int_2))+', '
        if sentimentalnost_int_2==morbidnost_int_2:
            pass
        if sentimentalnost_int_3>ismijavanje:
            CLEAN_LINE=CLEAN_LINE+'"sentimentalnost_int_3":'+str(abs(sentimentalnost_int_3-ismijavanje))+', '
        if sentimentalnost_int_3<ismijavanje:
            CLEAN_LINE=CLEAN_LINE+'"ismijavanje":'+str(abs(sentimentalnost_int_3-ismijavanje))+', '
        if sentimentalnost_int_3==ismijavanje:
            pass

    #ZADOVOLJSTVO       #PESIMIZAM
        if zadovoljstvo_int_1>pesimizam_int_1:
            CLEAN_LINE=CLEAN_LINE+'"zadovoljstvo_int_1":'+str(abs(zadovoljstvo_int_1-pesimizam_int_1))+', '
        if zadovoljstvo_int_1<pesimizam_int_1:
            CLEAN_LINE=CLEAN_LINE+'"pesimizam_int_1":'+str(abs(zadovoljstvo_int_1-pesimizam_int_1))+', '
        if zadovoljstvo_int_1==pesimizam_int_1:
            pass
        if zadovoljstvo_int_2>pesimizam_int_2:
            CLEAN_LINE=CLEAN_LINE+'"zadovoljstvo_int_2":'+str(abs(zadovoljstvo_int_2-pesimizam_int_2))+', '
        if zadovoljstvo_int_2<pesimizam_int_2:
            CLEAN_LINE=CLEAN_LINE+'"pesimizam_int_2":'+str(abs(zadovoljstvo_int_2-pesimizam_int_2))+', '
        if zadovoljstvo_int_2==pesimizam_int_2:
            pass
        if zadovoljstvo_int_3>nepovjerenje:
            CLEAN_LINE=CLEAN_LINE+'"zadovoljstvo_int_3":'+str(abs(zadovoljstvo_int_3-nepovjerenje))+', '
        if zadovoljstvo_int_3<nepovjerenje:
            CLEAN_LINE=CLEAN_LINE+'"nepovjerenje":'+str(abs(zadovoljstvo_int_3-nepovjerenje))+', '
        if zadovoljstvo_int_3==nepovjerenje:
            pass

    #ANKSIOZNOST        #UVREDA
        if anksioznost_int_1>uvreda_int_1:
            CLEAN_LINE=CLEAN_LINE+'"anksioznost_int_1":'+str(abs(anksioznost_int_1-uvreda_int_1))+', '
        if anksioznost_int_1<uvreda_int_1:
            CLEAN_LINE=CLEAN_LINE+'"uvreda_int_1":'+str(abs(anksioznost_int_1-uvreda_int_1))+', '
        if anksioznost_int_1==uvreda_int_1:
            pass
        if anksioznost_int_2>uvreda_int_2:
            CLEAN_LINE=CLEAN_LINE+'"anksioznost_int_2":'+str(abs(anksioznost_int_2-uvreda_int_2))+', '
        if anksioznost_int_2<uvreda_int_2:
            CLEAN_LINE=CLEAN_LINE+'"uvreda_int_2":'+str(abs(anksioznost_int_2-uvreda_int_2))+', '
        if anksioznost_int_2==uvreda_int_2:
            pass
        if zabrinutost>mržnja:
            CLEAN_LINE=CLEAN_LINE+'"zabrinutost":'+str(abs(zabrinutost-mržnja))+', '
        if zabrinutost<mržnja:
            CLEAN_LINE=CLEAN_LINE+'"mržnja":'+str(abs(zabrinutost-mržnja))+', '
        if zabrinutost==mržnja:
            pass


        CLEAN_LINE=CLEAN_LINE[:-2]
        CLEAN_LINE=CLEAN_LINE+'}'

        #
#        finale=finale[:-2]
#        finale=finale+'}'
        #zzz=clean(finale)
        #print('******************************')
        #print(finale)
        #print(CLEAN_LINE)
        #print('******************************')
        TEXT.append(CLEAN_LINE)
        #TEXT.append(finale)


    #print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    #print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    #print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    #print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    #____________________KUMULATIVNE
    #finale_kumulativne = '{'

    #if BIJES!=0: finale_kumulativne=finale_kumulativne+'"BIJES":'+str(BIJES)+', '
    #if LJUTNJA!=0: finale_kumulativne=finale_kumulativne+'"LJUTNJA":'+str(LJUTNJA)+', ' 
    #if ODVAŽNOST!=0: finale_kumulativne=finale_kumulativne+'"ODVAŽNOST":'+str(ODVAŽNOST)+', '

    #if BUDNOST!=0: finale_kumulativne=finale_kumulativne+'"BUDNOST":'+str(BUDNOST)+', '
    #if OČEKIVANJE!=0: finale_kumulativne=finale_kumulativne+'"OČEKIVANJE":'+str(OČEKIVANJE)+', '
    #if INTERES!=0: finale_kumulativne=finale_kumulativne+'"INTERES":'+str(INTERES)+', '

    #if GNUŠANJE!=0: finale_kumulativne=finale_kumulativne+'"GNUŠANJE":'+str(GNUŠANJE)+', '
    #if GAĐENJE!=0: finale_kumulativne=finale_kumulativne+'"GAĐENJE":'+str(GAĐENJE)+', '
    #if AVERZIJA!=0: finale_kumulativne=finale_kumulativne+'"AVERZIJA":'+str(AVERZIJA)+', '

    #if TEROR!=0: finale_kumulativne=finale_kumulativne+'"TEROR":'+str(TEROR)+', '
    #if STRAH!=0: finale_kumulativne=finale_kumulativne+'"STRAH":'+str(STRAH)+', '
    #if BOJAZAN!=0: finale_kumulativne=finale_kumulativne+'"BOJAZAN":'+str(BOJAZAN)+', '

    #if EKSTAZA!=0: finale_kumulativne=finale_kumulativne+'"EKSTAZA":'+str(EKSTAZA)+', '
    #if SREĆA!=0: finale_kumulativne=finale_kumulativne+'"SREĆA":'+str(SREĆA)+', '
    #if SPOKOJ!=0: finale_kumulativne=finale_kumulativne+'"SPOKOJ":'+str(SPOKOJ)+', '

    #if PATNJA!=0: finale_kumulativne=finale_kumulativne+'"PATNJA":'+str(PATNJA)+', '
    #if TUGA!=0: finale_kumulativne=finale_kumulativne+'"TUGA":'+str(TUGA)+', '
    #if SJETA!=0: finale_kumulativne=finale_kumulativne+'"SJETA":'+str(SJETA)+', '

    #if ZAPANJENOST!=0: finale_kumulativne=finale_kumulativne+'"ZAPANJENOST":'+str(ZAPANJENOST)+', '
    #if IZNENAĐENJE!=0: finale_kumulativne=finale_kumulativne+'"IZNENAĐENJE":'+str(IZNENAĐENJE)+', '
    #if DISTRAKCIJA!=0: finale_kumulativne=finale_kumulativne+'"DISTRAKCIJA":'+str(DISTRAKCIJA)+', '

    #if DIVLJENJE!=0: finale_kumulativne=finale_kumulativne+'"DIVLJENJE":'+str(DIVLJENJE)+', '
    #if POVJERENJE!=0: finale_kumulativne=finale_kumulativne+'"POVJERENJE":'+str(POVJERENJE)+', '
    #if PRIHVAĆANJE!=0: finale_kumulativne=finale_kumulativne+'"PRIHVAĆANJE":'+str(PRIHVAĆANJE)+', '

    #finale_kumulativne=finale_kumulativne[:-2]
    #finale_kumulativne=finale_kumulativne+'}'

    CLEAN_LINE_kumulativne='{"url":"'+url+'", '

    #SURPRISE		ANTICIPATION
    if BUDNOST>ZAPANJENOST:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"BUDNOST":'+str(abs(BUDNOST-ZAPANJENOST))+', '
    if BUDNOST<ZAPANJENOST:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"ZAPANJENOST":'+str(abs(BUDNOST-ZAPANJENOST))+', '
    if BUDNOST==ZAPANJENOST:
        pass
    if OČEKIVANJE>IZNENAĐENJE:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"OČEKIVANJE":'+str(abs(OČEKIVANJE-IZNENAĐENJE))+', '
    if OČEKIVANJE<IZNENAĐENJE:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"IZNENAĐENJE":'+str(abs(OČEKIVANJE-IZNENAĐENJE))+', '
    if OČEKIVANJE==IZNENAĐENJE:
        pass
    if INTERES>DISTRAKCIJA:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"INTERES":'+str(abs(INTERES-DISTRAKCIJA))+', '
    if INTERES<DISTRAKCIJA:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"DISTRAKCIJA":'+str(abs(INTERES-DISTRAKCIJA))+', '
    if INTERES==DISTRAKCIJA:
        pass
    #ANGER		FEAR
    if BIJES>TEROR:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"BIJES":'+str(abs(BIJES-TEROR))+', '
    if BIJES<TEROR:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"TEROR":'+str(abs(BIJES-TEROR))+', '
    if BIJES==TEROR:
        pass
    if LJUTNJA>STRAH:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"LJUTNJA":'+str(abs(LJUTNJA-STRAH))+', '
    if LJUTNJA<STRAH:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"STRAH":'+str(abs(LJUTNJA-STRAH))+', '
    if LJUTNJA==STRAH:
        pass
    if ODVAŽNOST>BOJAZAN:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"ODVAŽNOST":'+str(abs(ODVAŽNOST-BOJAZAN))+', '
    if ODVAŽNOST<BOJAZAN:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"BOJAZAN":'+str(abs(ODVAŽNOST-BOJAZAN))+', '
    if ODVAŽNOST==BOJAZAN:
        pass
    #TRUST			DISGUST
    if DIVLJENJE>GNUŠANJE:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"DIVLJENJE":'+str(abs(DIVLJENJE-GNUŠANJE))+', '
    if DIVLJENJE<GNUŠANJE:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"GNUŠANJE":'+str(abs(DIVLJENJE-GNUŠANJE))+', '
    if DIVLJENJE==GNUŠANJE:
        pass
    if POVJERENJE>GAĐENJE:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"POVJERENJE":'+str(abs(POVJERENJE-GAĐENJE))+', '
    if POVJERENJE<GAĐENJE:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"GAĐENJE":'+str(abs(POVJERENJE-GAĐENJE))+', '
    if POVJERENJE==GAĐENJE:
        pass
    if PRIHVAĆANJE>AVERZIJA:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"PRIHVAĆANJE":'+str(abs(PRIHVAĆANJE-AVERZIJA))+', '
    if PRIHVAĆANJE<AVERZIJA:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"AVERZIJA":'+str(abs(PRIHVAĆANJE-AVERZIJA))+', '
    if PRIHVAĆANJE==AVERZIJA:
        pass

    #JOY			SADNESS#
    if EKSTAZA>PATNJA:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"EKSTAZA":'+str(abs(EKSTAZA-PATNJA))+', '
    if EKSTAZA<PATNJA:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"PATNJA":'+str(abs(EKSTAZA-PATNJA))+', '
    if EKSTAZA==PATNJA:
        pass
    if SREĆA>TUGA:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"SREĆA":'+str(abs(SREĆA-TUGA))+', '
    if SREĆA<TUGA:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"TUGA":'+str(abs(SREĆA-TUGA))+', '
    if SREĆA==TUGA:
        pass
    if SPOKOJ>SJETA:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"SPOKOJ":'+str(abs(SPOKOJ-SJETA))+', '
    if SPOKOJ<SJETA:
        CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'"SJETA":'+str(abs(SPOKOJ-SJETA))+', '
    if SPOKOJ==SJETA:
        pass


    CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne[:-2]
    CLEAN_LINE_kumulativne=CLEAN_LINE_kumulativne+'}'


    TEXT.append(CLEAN_LINE_kumulativne)
    UKUPAN_TEXT_ZA_HTML=''
    #print(CLEAN_LINE_kumulativne)
    #print('__________________________')
    process_speed='{"time[s]":'+'%s' % round((time.time() - start_time),4)+"}"
    print(process_speed)
    TEXT.append(process_speed)
    for rezultat in TEXT:
        #print('======================================================')
        UKUPAN_TEXT_ZA_HTML=UKUPAN_TEXT_ZA_HTML+rezultat
        print(rezultat)
    print('######################################################')
    print(UKUPAN_TEXT_ZA_HTML)
    #print("--- %s seconds ---" % (time.time() - start_time))
    print('--- %s words processed ---' % nr_words_checked )
    return render_template('stock_quote.html',text1=TEXT)
    return 0
