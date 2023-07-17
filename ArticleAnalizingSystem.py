# [코드 설명]
# 1. BBCsport에 팀별 소식을 정리한 page를 crawling하여 매체별로 작성한 이적설을 가져온다
# 2. 가져온 기사를 고안한 법칙에 의해 어떤 선수가 어떤 팀으로 이적하는지 분석하고 list에 저장한다
# 3. 실제 이적한 선수 명단과 분석한 list를 비교하여 매체별로 적확도를 분석한다.


## data base[1] ## - excel파일로부터 data base 구축(excel파일이 완성되지 않아 실행을 위해 주석 처리 후 data base[2] 참고)

# 1.팀별 선수 명단 list
# 선수명단 excel (2223SpringRosterExample.xlsx) 로부터 팀별 선수명단 list 생성

# import pandas as pd
# file_name = '2223SpringRosterExample.xlsx'
# player_df = pd.read_excel(file_name,sheet_name=['ManCity','Arsenal','Tottenham','Chelsea','Barcelona'])

# class Team:
#     def __init__(self,team):
#         self.player_df = player_df['%s'%(team)]

#         i = 0
#         for j in self.player_df.iloc[:,0]:
#             i += 1
#         list1 = []
#         for j in range(i):
#            list1.append(self.player_df.iloc[j,0])       

#         self.player_list = list1

# Arsenal = Team("Arsenal").player_list
# ManCity = Team("ManCity").player_list
# Tottenham = Team("Tottenham").player_list
# Chelsea = Team("Chelsea").player_list
# Barcelona = Team("Barcelona").player_list

# # 2.분석 대상 팀 list
# Teams = ["Arsenal","ManCity","Tottenham","Chelsea","Barcelona"]

# # 3.전체 선수 명단 list
# Players = [Arsenal,ManCity,Tottenham,Chelsea,Barcelona]

# # 4.실제 이적 명단 list
# # 명단변화 excel (2223SummerVariationExample.xlsx) 로부터 list 생성

# file_name = '2223SummerVariationExample.xlsx'
# transferdf = pd.read_excel(file_name,sheet_name=['Transfer'])

# i = 0
# for j in transferdf.iloc[:,0]:
#     i += 1
# num = len(transferdf.columns)
# RealTransfer = []
# for j in range(i):
#     listinlist = []
#     listinlist.append(transferdf.iloc[j,0])
#     listinlist.append(transferdf.iloc[j,2])
#     RealTransfer.append(listinlist)      

# # 5.분석 대상 미디어 list
# MediaList = ["(Sun)","Sun","(Times - subscription required)","Times - subscription required","(Mail)","Mail","(Telegraph - subscription required)","Telegraph - subscription required","(Mirror)","Mirror"]

# RumorList_before = []
# RumorList = []



## data base[2] ## - 실행 예시를 위해 일부만 직접 작성하여 data base 구축 

# 1.팀별 선수명단 list
ManchesterCity = ["Ederson","Ortega","Steffen","Carson","Ruben Dias","Ake","Stones","Laporte","Akanji","Sergio Gomez","Walker","Rico Lewis","Rodri","Philips","Gundogan","De Bruyne","Bernardo Silva","Palmer","Foden","Grealish","Mahrez","Haaland","Julian Alvarez","Cancelo","Yangel Herrera","Kabore","Couto","Bustos"]
Arsenal = ["Ramsdale","Turner","Saliba","Magalhaes","Trusty","Holding","Zinchenko","Tierney","Ben White","Tomiyasu","Partey","Elneny","Xhaka","Lokonga","Odegaard","Smith Rowe","Fabio Vieira","Martinelli","Saka","Marquinhos","Reiss Nelson","Jesus","Nketiah","Balogun","Nicolas Pepe","Tavares","Soares","Runarsson"]
ManUtd = ["Henderson","Gea","Heaton","Lisandro","Varane","Maguire","Lindelof","Tuanzebe","Phil Jones","Mengi","Shaw","Malacia","Brandon Williams","Alvaro Fernandez","Dalot","Bissaka","Casemiro","Tominay","Eriksen","Fred","Beek","Bruno Fernandes","Hannibal","Rashford","Sancho","Elanga","Garnacho","Antony","Diallo","Shoretire","Pellistri","Martial"]
Newcastle = ["Pope","Dubravka","Karius","Darlow","Gillespie","Botman","Schar","Lascelles","Jonjo Shelvey","Ciaran Clark","Kell Watts","Targett","Dan Burn","Jamal Lewis","Dummett","Trippier","Krafth","Manquillo","Guimaraes","Hayden","Willock","Sean Longstaff","Hendrick","Matty Longstaff","Ritchie","Joelinton","Elliot Anderson","Maximin","Fraser","Almiron","Murphy","Garang Kuol","Isak","Callun Wilon"]
Liverpool = ["Alisson","Kelleher","Adrian","Dijk","Konate","Joe Gomez","Matip","Phillips","Rhys Williams","Rovertson","Tsimikas","Arnold","Calvin Ramsay","Fabinho","Bajcetic","Thiago","Keita","Curtis Jones","Berg","Henderson","Chamberlain","Milner","Elliott","Carvalho","Luis Diaz","Diogo Jota","Salah","Numez","Firmino"]
Brighton = ["Trossard","Sanchez","Steele","McGill","Dunk","Hecke","Haydon Roberts","Estupinan","Lamptey","Veltman","Caicedo","Allister","Jakub Moder","Gilmour","Pascal","Richards","Sarmiento","Lallana","Mitoma","March","Enciso","Ferguson","Welbeck","Undav","Connolly","Kozlowski","Abdallah","Adingra","Alzate","Karbownik","Zeqirl","Scherpen","Shane Duffy"]
AstonVilla = ["Emiliano Martinez","Olsen","Danny Ings","Jed Steer","Sinisalo","Carlos","Mings","Konsa","Chambers","Hause","Digne","Cash","Young","Kamara","Dendoncker","Nskamba","Douglas Luiz","Jacob Ramsey","McGinn","Iroegbunam","Bailey","Coutinho","Philogene","Buendia","Bertrand","Watkins","Archer","Davis","Sanson","Wesley Moraes"]
Tottenham = ["Kane","Lloris","Fraser Forster","Whiteman","Brandon Austin","Romero","Dier","Matt Doherty","Davinson","Tanganga","Ben Davies","Royal","Skipp","Hojbjerg","Bentancur","Bissouma","Pape","Ryan Sessegnon","Perisic","Son","Moura","Richarlison","Ndombele","Udogie","Giovani","Reguilon","Spence","Winks","Bryan Gil","Joe Rodon"]
Brentford = ["Raya","Strakosha","Cox","Balcombe","Ajer","Pinnock","Jansson","Ban Mee","Zanka","Goode","Henry","Henry","Hickey","Roerslev","Fin Stevens","Janelt","Norgaard","Jensen","Dasilva","Onyeka","Baptiste","Ghoddos","Wissa","Keane Lewis","Kamsgaard","Tariqe","Mbeumo","Dervisoglu","Sergi Canos","Sorensen","Bidstrup","Joel Valencia"]
Fulham = ["Leno","Rodak","Diop","Adarabioyo","Tim Ream","Robinson","Kenny Tete","Steven Sessegnon","Palhinha","Harrison Reed","Tom Cairney","Francois","Andreas Pereira","Cordova","Kebano","Willian","Harry Wilson","Knockaert","Mitrovic","Muniz","Carlos Vinicius","Kevin Mbabu","Joe Bryan","Gazzaniga","Cavaleiro","Kongolo"]
CrystalPalace = ["Johnstone","Guaita","Matthews","Guehi","Joachim Andersen","Chris Richards","Ferguson","Tomkins","Tyrick Mitchell","Clyne","Joel Ward","Doucoure","Riedewald","Milivojevic","Will Hughes","McArthur","Schlupp","Eze","Zaha","Olise","Ebiowei","Edouard","Mateta","Jordan Ayew","Plange","Jack Butland","Brien"]
Chelsea = ["Edouard Mendy","Arrizabalaga","Slonina","Bettinelli","Wesley Fofana","Koulibaly","Chalobah","Thiago Silva","Cucurella","Chilewell","Lewis Hall","Rahman Baba","Reece James","Azpilicueta","Kante","Kovacic","Gallagher","Loftus","Chukwuemeka","Mason Mount","Havertz","Sterling","Pulisic","Ziyech","Broja","Aubameyang","Lukaku","Gusto","Odoi","Andrey Santos","Ampadu","Malang Sarr","Bakayoko","Jorginho"]
Wolves = ["Jose Sa","Sarkic","Moulden","Kilman","Collins","Toti","Nouri","Jonny Otto","Bueno","Semedo","Hoever","Neves","Hodge","Matheus Numes","Cundle","Moutinho","Podence","Chiquinho","Neto","Adama","Kalajdzic","Hee","Raul Jimenez","Diego Costa","Concalo Guedes","Conor Coady","Fabio Silva","Mosquera","Bendeguz Bolla","Kawabe","Jordao"]
WestHam = ["Alphonse","Fabianski","Randolph","Nayef","Craig Dawson","Zouma","Kehrer","Ogbonna","Emerson","Aaron Cresswell","Johnson","Coufal","Declan Rice","Tomas Soucek","Coventry","Downes","Paqueta","Fornals","Lanzini","Benrahma","Cornet","Bowen","Scamacca","Antonio","Nikola Vlasic","Nathan Trott","Ashby"]
Bournemouth = ["Neto","Travers","Will Dennis","Marcos Senesi","Lloyd Kelly","Mepham","James Hill","Jordan Zemura","Jack Stacey","Ryan Fredericks","Adam Smith","Jefferson Lerma","Philip Billing","Lewis Cook","Joe Rothwell","Ben Pearson","Gavin Kilkenny","Marcus Tavernier","Ryan Christie","Jaidon Anthony","Junior Stanislas","David Brooks","Jamal Lowe","Dominic Solanke","Moore","Saydee","Siriki Dembele","Emiliano Marcondes"]
NottmForest = ["Niakhate","Wayne Hennessey","Jordan Smith","Kanuric","McKenna","Joe Worrall","Willy Boly","Jonathan Panzo","Steve Cook","Harry Toffolo","Omar Richards","Neco Williams","Biancone","Aurier","Kouyate","Colback","Mangala","Freuler","Yates","Arter","Cafu","Morgan Gibbs","Brennan Johnson","Lingard","Andre Ayew","Mighten","Bowler","Awoniyi","Emmanuel Dennis","Sam Surridge","Lyle Taylor","Brien","Ui","Mbe Soh","Richie Laryea","Horvath","Braian Ojeda","Drager","Aguilera"]
Everton = ["Pickford","Asmir Begovic","Lonergan","Tarkowsli","Godfrey","Holgate","Yerry Mina","Michael Keane","Mykolenko","Patterson","Seamus Coleman","Amadou Onana","James Garner","Gordon","Doucoure","Tom Davies","Gueye","Alex Iwobi","Demarai Gray","Dwight McNeil","Townsend","Dominic Calvert","Neal Maupay","Andre Gomes","Dele Alli","Jarrad Branthwaite","Gbamin","Virginia"]
Leicester = ["Danny Ward","Daniel Iversen","Smithies","Wout Faes","Soyuncu","Amartey","Vestergaard","Jonny Evans","Luke Thomas","Ryan Bertrand","Timothy Castagne","James Justin","Ricardo Pereira","Soumare","Choudhury","Nampalys Mendy","Yorui Tielemans","Kiernan Dewsbury","James Maddison","Harvey Barnes","Patson Daka","Kelechi Iheanacho","Jamie Vardy","George Hirst","Ayoze Perez"]
Leeds = ["Meslier","Klaesson","Robles","Robin Koch","Charlie Cresswell","Liam Cooper","Hjelde","Pascal Strijk","Junior Firpo","Rasmus Kristensen","Dreameh","Luke Ayling","Stuart Dallas","Tyler Adams","Marc Roca","Jamie Shackleton","Forshaw","Brenden Aaronson","Sam Greenwood","Jack Harrison","Luis Sinisterra","Wilfried Gnonto","Daniel James","Summerville","Poveda","Bamford","Rodrigo","Joe Gelhardt","Tyler Roberts","Diego Llorente","Helder Costa"]
Southampton = ["Gavin Bazunu","McCarthy","Caballero","Kotchap","Salisu","Duje","Bednrek","Jack Stephens","Lyanco","Romain Perraud","Juan Larios","Peters","Livramento","Prowse","Lavia","Armstrong","Smallbone","Aribo","Elyounoussi","Moussa Djenepo","Edozie","Theo Walcott","Che Adams","Adam Armstrong","Sekou Mara","Dan Nlundulu","Mateusz Lis"]
Paris = ["Donnarumma","Rico","Sarabia","Letellier","Lavallee","Marquinhos","Kimpembe","Bitshiabu","Ramos","Mendes","Bernat","Nhaga","Hakimi","Mukiele","Pembele","Danilo Pareira","Verratti","Vitinha","Fabian Ruiz","Carlos Soler","Renato Sanches","Warren Zaire","Gharbi","Neymar","Messi","Mbappe","Housni","Icardi","Diallo","Paredes","Wijnaldum","Draxler","Navas","Dagba","Zurzawa","Michut","Ayman Kari","Djeidi","Kenny Nagera","Mathyas Randriamamy","Anfane"]
PSV = ["Madueke","Gakpo","Benitez","Drommel","Peersman","Waterman","Boscafli","Obispo","Junior","Ramalho","Jordan Teze","Mwene","Ibrahim Sangar","Veerman","Gutierrez","Xavi Simons","Guus Til","Saibari","Bakayoko","Ghazi","Luuk de Jong","Vertessen","Baumgartl","Maximiliano Romero","Ledezma","Oppegard"]
Benfica = ["Vlachodimos","Samuel Soares","Andre Gomes","Antonio Silva","Morato","Otamendi","Grimaldo","Ristic","Bah","Gilberto","Florentino","Enzo","Aursnes","Joao Mario","Ndour","Chiquinho","Schjelderup","David Neres","Rafa","Goncalo Ramos","Petar Musa","Joao Victor","Haris Seferovic","Gabriel Pires","Henrique Araujo","Soualiho","Tomas Araujo","Dantas","Paulo Bernardo","Gouveia","Sandro Cruz"]
Shakhtar = ["Mudirc","Anatoliy","Pyatov","Oleksiy","Matvienko","Bondar","Faryna","Kormienko","Konoplya","Taylor","Stempanenko","Djurasek","Kryskiv","Nazaryna","Sudakov","Bondarenko","Totovytskyi","Ocheretko","Petryak","Topalov","Toirov","Zubkov","Shved","Lassina","Sikan","Boryachuk","Tete","Manor Solomon","Pedrinho","Marlon","Vitao","Tobias","Kayode","Kashchuk","Drambajev","Bondarenko","Viunnyk","Kapinus","Chekh","Svityukha"]
Monaco = ["Badiashile","Lienard","Disasi","Maripan","Matsima","Okou","Henrique","Jakobs","Vanderson","Ruben Aguilar","Camara","Magassa","Youssouf","Jean Lucas","Matazo","Golovin","Akliouche","Minamino","Diatta","Embolo","Yedder","Volland","Boadu","Majecki","Marclin","Musaba","Zagre","Pele","Lemarechal"]
OtherLeague = ["Kiwor","Duran","Moreno","Zabarnyi","Ouattera","Antoine Semenyo","Randolph","Buonanotte","Ayari","Madueke","Malo Gusto","Andrey Santos","Datro Fofana","Naouirou Ahmada","Sasa Lukic","Georginio Rutter","Maximilian Wober","Souttar","Kristiansen","Maximo Perrone","Ronaldo","Garang Kuol","Danilo","Felipe Monteiro","Scarpa","Andre Ayew","Kamaldeen Sulemana","Onuachu","Carlos Alcaraz","Mislav Gomes","Mario Lemina","Craig Dawson","Daniel Bentley"]

# 2.분석 대상 팀 list
Teams = ["Manchester City","Arsenal","Manchester United","Newcastle","Liverpool","Brighton","AstonVilla","Tottenham","Brentford","Fulham","Crystal Palace","Chelsea","Wolverhampton","West Ham","Bournemouth","Nottingham","Everton","Leicester","Leeds","Southampton","Barcelona","Real Madrid","Atletico","Sociedad","Villarreal","Betis","Osasuna","Athletic","Mallorca","Girona","Sevilla","Vallecano","Celta","Valencia","Getafe","Cadiz","Almeria","Valladolid","Espanyol","Elche","Munich","Dortmund","Leipzig","Berlin","Freiburg","Leverkusen","Frankfurt","Wolfsburg","Mainz","gladbach","Koln","Hoffenheim","Bremen","Bochum","Augsburg","Stuttgart","Schalke","Hertha","Napoli","Lazio","Inter","Milan","Atalanta","Roma","Juventus","Fiorentina","Bologna","Torino","Monza","Udinese","Sassuolo","Empoli","Salernitana","Lecce","Spezia","Verona","Cremonese","Sampdoria","Paris","Lens","Marseille","Rennes","Lille","Monaco","Feyenoord","PSV","Ajax","Alkmaar","Rangers","Celtic","Benfica","Porto","Sporting","Genk","Brugge","Shakhtar"]

# 3.전체 선수 명단 list
Players = [ManchesterCity,Arsenal,ManUtd,Newcastle,Liverpool,Brighton,AstonVilla,Tottenham,Brentford,Fulham,CrystalPalace,Chelsea,Wolves,WestHam,Bournemouth,NottmForest,Everton,Leicester,Leeds,Southampton,Paris,PSV,Benfica,Shakhtar,OtherLeague]

# 4.실제 이적 명단 list
RealTransfer = [["Kiwior","Arsenal"],["Trossard","Arsenal"],["Jorginho","Arsenal"],["Duran","Villa"],["Alexandre Moreno","Villa"],["Zabarnyi","Bournemouth"],["Ouattara","Bournemouth"],["Antoine Semenyo","Bournemouth"],["Randolph","Bournemouth"],["Buonanotte","Brighton"],["Ayari","Brighton"],["Enzo","Chelsea"],["Mudryk","Chelsea"],["Badiashile","Chelsea"],["Madueke","Chelsea"],["Malo Gusto","Chelsea"],["Andrey Santos","Chelsea"],["Datro Fofana","Chelsea"],["Naouirou Ahmada","CristalPalace"],["Sasa Lukic","Fulham"],["Shane Duffy","Fulham"],["Georginio Rutter","Leeds"],["Maximilian Wober","Leeds"],["Souttar","Leicester"],["Kristiansen","Leicester"],["Gakpo","Liverpool"],["Maximo Perrone","ManchesterCity"],["Ronaldo","Nassr"],["Gordon","Newcastle"],["Ashby","Newcastle"],["Garang Kuol","Newcastle"],["Danilo","Nottingham"],["Felipe Monteiro","Nottingham"],["Scarpa","Nottingham"],["Jonjo Shelvey","Nottingham"],["Andre Ayew","Nottingham"],["Kamaldeen Sulemana","Southampton"],["Onuachu","Southampton"],["Carlos Alcaraz","Southampton"],["Mislav Orsic","Southampton"],["Bree","Southampton"],["Matt Doherty","AtleticoMadrid"],["Danny Ings","Westham"],["Luizao","Westham"],["Joao Gomes","Wolverhampton"],["Mario Lemina","Wolverhampton"],["Pablo Sarabia","Wolverhampton"],["Craig Dawson","Wolverhampton"],["Daniel Bentley","Wolverhampton"]]

# 5.분석 대상 미디어 list
MediaList = ["(Sun)","Sun","(Times - subscription required)","Times - subscription required","(Mail)","Mail","(Telegraph - subscription required)","Telegraph - subscription required","(Mirror)","Mirror"]

RumorList_before = []
RumorList = []



## code2 ##
# 문장으로 되어 있는 이적설에서 정보를 추출함
# BBC가 기사를 작성하는 방식을 분석하여 다음과 같은 법칙을 세움
# (해당팀선수) (상대팀선수) (상대팀)
#      O           O          O     --> 분석 불가
#      O           O          X     --> (상대팀선수)가 (해당팀) 으로 이적
#      O           X          O     --> (해당팀선수)가 (상대팀) 으로 이적
#      X           O          O     --> (상대팀선수)가 (해당팀) 으로 이적
#      X           X          O     --> 경우 없음
#      X           O          X     --> (상대팀선수)가 (해당팀) 으로 이적
#      O           X          X     --> 경우 없음
#      X           X          X     --> 경우 없음
# 위의 법칙에 따라 기사 분석 후 code1에서 [이적선수명,이적팀,매체명] 형태로 list에 저장

def InformationExtraction(str1,m,UniqueNumber):
    RumorListinList = []
    TeamsExceptMine = Teams[:UniqueNumber] + Teams[UniqueNumber+1:]
    
    PlayersExceptMine = Players[:UniqueNumber] + Players[UniqueNumber+1:]
    
    MyPlayer = ""
    OtherPlayer = ""
    OtherTeam = ""
    
    n = 0
    while n<len(Players[UniqueNumber]):
        if str1.find(Players[UniqueNumber][n]) != -1:
            MyPlayer = Players[UniqueNumber][n]
            break
        n += 1
        
    n = 0
    k = len(str1)
    while n<len(TeamsExceptMine): 
        if str1.find(TeamsExceptMine[n]) != -1:
            if str1.find(TeamsExceptMine[n])<k:
                k = str1.find(TeamsExceptMine[n])
                OtherTeam = TeamsExceptMine[n]
        n += 1

    n = 0
    k = len(str1)
    while n<len(PlayersExceptMine):
        j = 0
        while j<len(PlayersExceptMine[n]):
            if str1.find(PlayersExceptMine[n][j]) != -1:
                if str1.find(PlayersExceptMine[n][j])<k:
                    k = str1.find(PlayersExceptMine[n][j])
                    OtherPlayer = PlayersExceptMine[n][j]
            j += 1
        n += 1

    if len(MyPlayer) != 0 and len(OtherPlayer) != 0 and len(OtherTeam) == 0:
        RumorListinList.append(OtherPlayer)
        RumorListinList.append(Teams[UniqueNumber])
        RumorListinList.append(m)

    if len(MyPlayer) != 0 and len(OtherPlayer) == 0 and len(OtherTeam) != 0:
        RumorListinList.append(MyPlayer)
        RumorListinList.append(OtherTeam)
        RumorListinList.append(m)

    if len(MyPlayer) == 0 and len(OtherPlayer) != 0:
        RumorListinList.append(OtherPlayer)
        RumorListinList.append(Teams[UniqueNumber])
        RumorListinList.append(m)
    
    return RumorListinList



## code1 ##
# Web Crawling을 통해 기사의 내용을 하나씩 문자열로 불러옴 --> 형태 : 기사본문(매체명)
# data base의 MediaList에 있는 매체인 경우 code2로 기사 내용에서 이적한 선수와 이적한 팀을 RumorList_before에 추가함

import requests
from bs4 import BeautifulSoup

def STR(team,uniquenumber,start,end):
    page = start
    while page<end:
        url = 'https://www.bbc.com/sport/football/teams/%s?page=%s'%(team,page)
        html = requests.get(url)
        soup = BeautifulSoup(html.text)

        script_tag = soup.find_all(['span'])

        for script in script_tag:
            script.extract()

        content = soup.get_text('/', strip=True)

        numofS = content.count("/")
        i = 0
        j = -1
        while i<numofS:
            b = content[j+1:].find("/")
            c = content[b+1:].find("/")
            if (c == -1):
                break
            k = 0
            while k < len(MediaList):
                if (content[b+1:b+c+1] == MediaList[k]):
                    str1 = content[j+1:b]
                    print("*" + str1 + MediaList[k])
            
                    
                    RumorList_before.append(InformationExtraction(str1,k,uniquenumber))
                
                k += 1
            content = content[b+1:]
           
        page += 1

        


## code3 ##
# 실행문으로, 팀별로 기사 분석을 시행함

print("="*137)
print("[Article]")
print("="*137)

STR("manchester-city",Teams.index("Manchester City"),25,40)
STR("arsenal",Teams.index("Arsenal"),25,40)
STR("manchester-united",Teams.index("Manchester United"),25,40)
STR("newcastle-united",Teams.index("Newcastle"),25,40)
STR("liverpool",Teams.index("Liverpool"),25,40)
STR("brighton-and-hove-albion",Teams.index("Brighton"),25,40)
STR("aston-villa",Teams.index("AstonVilla"),25,40)
STR("tottenham-hotspur",Teams.index("Tottenham"),25,40)
STR("brentford",Teams.index("Brentford"),25,40)
STR("fulham",Teams.index("Fulham"),25,40)
STR("crystal-palace",Teams.index("Crystal Palace"),25,40)
STR("chelsea",Teams.index("Chelsea"),25,40)
STR("wolverhampton-wanderers",Teams.index("Wolverhampton"),25,40)
STR("west-ham-united",Teams.index("West Ham"),25,40)
STR("afc-bournemouth",Teams.index("Bournemouth"),25,40)
STR("nottingham-forest",Teams.index("Nottingham"),25,40)
STR("everton",Teams.index("Everton"),25,40)
STR("leicester-city",Teams.index("Leicester"),25,40)
STR("leeds-united",Teams.index("Leeds"),25,40)
STR("southampton",Teams.index("Southampton"),25,40)

print("="*137)
        

## code4 ##
# 분석되지 않거나 이적에 대한 기사가 아닌 경우 빈 list로 입력되었기 때문에 이들을 제외한 RumorList를 새로 작성

i = 0
while i < len(RumorList_before):
    if len(RumorList_before[i]) != 0:
        RumorList.append(RumorList_before[i])
    i += 1
print("[Rumor list]")
print("="*137)
print(RumorList)
print("="*137)



## code5 ##
# 분석된 이적설 정보를 토대로 매체별 정확도를 분석하는 class작성

class Media:
    def __init__(self):
        self.list = []
        self.numberofrumor = 0
        self.numberofscore = 0
        self.accuracy = 0

    # 매체별 이적설을 실제 이적과 비교하여 적중한 이적설의 개수 확인
    def Checking(self):
        count = 0
        i = 0
        while i<len(self.list):
            j = 0
            while j<len(RealTransfer):
                if self.list[i][0] == RealTransfer[j][0] and self.list[i][1] == RealTransfer[j][1]:
                    count += 1
                j += 1
            i += 1
        return count
    
    # 분석 결과를 출력
    def Analyze(self):
        self.numberofrumor = len(self.list)
        self.numberofscore = self.Checking()
        if self.numberofrumor == 0:
            self.accuracy = 0
        else:
            self.accuracy = self.Checking()/len(self.list)*100
        print(" number of score = ",self.numberofscore,"/"," number of rumor = ",self.numberofrumor," accuracy: (",self.accuracy,"% )")

        
The_Sun = Media()
Times_ = Media()
Mail_ = Media()
Telegraph_ = Media()
Mirror_ = Media()

## code6 ##
# MediaList와 RumorList의 2번째 index인 매체명을 비교하여 매체별로 자신이 작성한 이적설을 저장
i = 0
while i < len(RumorList):
    if RumorList[i][2] == 0 or RumorList[i][2] == 1:
        The_Sun.list.append(RumorList[i])

    elif RumorList[i][2] == 2 or RumorList[i][2] == 3:
        Times_.list.append(RumorList[i])

    elif RumorList[i][2] == 4 or RumorList[i][2] == 5:
        Mail_.list.append(RumorList[i])

    elif RumorList[i][2] == 6 or RumorList[i][2] == 7:
        Telegraph_.list.append(RumorList[i])

    elif RumorList[i][2] == 8 or RumorList[i][2] == 9:
        Mirror_.list.append(RumorList[i])

    i += 1
    
## code7 ##
# 실행문으로, 분석 결과 출력

print("="*137)
print("Data")
print("="*137)
print("[Data of TheSun]")
The_Sun.Analyze()
print("[Data of Times]")
Times_.Analyze()
print("[Data of Mail]")
Mail_.Analyze()
print("[Data of Telegraph]")
Telegraph_.Analyze()
print("[Data of Mirror]")
Mirror_.Analyze()

print("="*137)



## code8 ##
# 분석 결과를 그래프로 표현

import matplotlib.pyplot as plt
import numpy as np

print("="*137)
print("[Graph]")
print("="*137)
print("[Number Of Rumor]") #이적설 개수 그래프로 표현

media1 = np.array(["TheSun","Times","Mail","Telegraph","Mirror"])
numberofrumor = np.array([The_Sun.numberofrumor,Times_.numberofrumor,Mail_.numberofrumor,Telegraph_.numberofrumor,Mirror_.numberofrumor])
plt.bar(media1,numberofrumor,color = "lightskyblue")
plt.show()

print("="*137)
print("[Number Of Hit]") #적중한 이적설 개수 그래프로 표현

media2 = np.array(["TheSun","Times","Mail","Telegraph","Mirror"])
numberofscore = np.array([The_Sun.numberofscore,Times_.numberofscore,Mail_.numberofscore,Telegraph_.numberofscore,Mirror_.numberofscore])
plt.bar(media2,numberofscore,color = "palegreen")
plt.show()

print("="*137)
print("[Accuracy]") #정확도 그래프로 표현

media3 = np.array(["TheSun","Times","Mail","Telegraph","Mirror"])
accuracy = np.array([The_Sun.accuracy,Times_.accuracy,Mail_.accuracy,Telegraph_.accuracy,Mirror_.accuracy])
plt.bar(media3,accuracy,color = "crimson")
plt.show()


print("="*137)