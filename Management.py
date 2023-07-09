import pandas as pd

# [Function #1]
# team 이름을 입력하면 해당 team instance를 return하는 함수
def CallTeamInstance(team):
    if team == "ManchesterCity":
        return ManCity
    elif team == "Arsenal":
        return Arsenal
    elif team == "Tottenham":
        return Tottenham
    elif team == "Chelsea":
        return Chelsea
    elif team == "Barcelona":
        return Barcelona

# [class #1-1]
# team별 instance의 member인 player_df를 입력된 정보를 토대로 수정함
# [method 종류]
# transfer(완전이적): 기존 팀의 dataframe에서 삭제 / 새로운 팀의 dataframe에 추가
# loanout(임대이적): 기존 팀의 dataframe에서 loan정보 "OUT"으로 수정 / 새로운 임대팀의 dataframe에서 loan정보 "IN"으로 추가
# loancomeback(임대복귀): 기존 팀의 dataframe에서 loan정보 "F"로 수정 / 전 임대팀의 dataframe에서 선수 정보 삭제
# release(방출): 해당 팀의 dataframe에서 삭제
# callup(유스콜업): 해당 팀의 dataframe에 추가
# recontract(재계약): 해당 팀의 dataframe에서 contract정보 수정
# changenumber(등번호변경): 해당 팀의 dataframe에서 number정보 수정
class Transfer:

    def transfer(self,name,after_team,number,contract):

        # 입력된 선수 이름을 찾고, 기존 팀의 dataframe에서 삭제
        index = -1
        for i in range(len(self.player_list)):
            if (self.player_list[i].count(name) == 1):
                index = i
        if (index != -1):
            self.player_df.drop(self.player_df.index[index],inplace=True)

        # 새로운 팀의 dataframe에 추가
        data = pd.DataFrame({'name':["%s"%(name)],'number':[number],'contract':[contract],"loan":["F"]})
        CallTeamInstance(after_team).player_df = pd.concat([CallTeamInstance(after_team).player_df,data],ignore_index=True)

        # list와 dataframe의 index를 일치시키기 위해 player_list를 변경된 player_df를 바탕으로 수정
        self.makelist()
        CallTeamInstance(after_team).makelist()

    def loanout(self,name,loan_team,number,contract):

        # 입력된 선수 이름을 찾고, 기존 팀의 dataframe에서 loan정보를 "F"에서 "OUT"으로 수정
        index = -1
        for i in range(len(self.player_list)):
            if (self.player_list[i].count(name) == 1):
                index = i
        if (index != -1):
            self.player_df.iloc[index,3] = 'OUT'
        
        # 새로운 팀의 dataframe에 추가 (loan정보는 IN으로)
        data = pd.DataFrame({'name':["%s"%(name)],'number':[number],'contract':[contract],"loan":["IN"]})
        CallTeamInstance(loan_team).player_df = pd.concat([CallTeamInstance(loan_team).player_df,data],ignore_index=True)

        self.makelist()
        CallTeamInstance(loan_team).makelist()

    def loancomeback(self,name,loan_team):

        # 입력된 선수 이름을 찾고, 기존 팀의 dataframe에서 loan정보를 "OUT"에서 "F"로 수정
        index = -1
        for i in range(len(self.player_list)):
            if (self.player_list[i].count(name) == 1):
                index = i
        if (index != -1):
            self.player_df.iloc[index,3] = 'F'
        
        # 전 임대팀의 dataframe에서 삭제
        for i in range(len(CallTeamInstance(loan_team).player_list)):
            if (CallTeamInstance(loan_team).player_list[i].count(name) == 1):
                index = i
        if (index != -1):
            CallTeamInstance(loan_team).player_df.drop(CallTeamInstance(loan_team).player_df.index[index],inplace=True)        

        self.makelist()
        CallTeamInstance(loan_team).makelist()        

    def release(self,name):

        # 입력된 선수 이름을 찾고, 해당 팀의 dataframe에서 삭제
        index = -1
        for i in range(len(self.player_list)):
            if (self.player_list[i].count(name) == 1):
                index = i
        if (index != -1):
            self.player_df.drop(self.player_df.index[index],inplace=True)

        self.makelist()

    def callup(self,name,number,contract):

        # 해당 팀의 dataframe에 추가
        data = pd.DataFrame({'name':["%s"%(name)],'number':[number],'contract':[contract],"loan":["F"]})
        self.player_df = pd.concat([self.player_df,data],ignore_index=True)

        self.makelist()

    def recontract(self,name,contract):

        # 해당 팀의 dataframe에서 contract정보 수정
        index = -1
        for i in range(len(self.player_list)):
            if (self.player_list[i].count(name) == 1):
                index = i
        if (index != -1):
            self.player_df.iloc[index,2] = contract

        self.makelist()

    def changenumber(self,name,newnum):

        # 해당 팀의 dataframe에서 number정보 수정
        index = -1
        for i in range(len(self.player_list)):
            if (self.player_list[i].count(name) == 1):
                index = i
        if (index != -1):
            self.player_df.iloc[index,1] = newnum

        self.makelist()

# [class #1-2]      
# team별로 instance를 만들 때 이전 선수명단 excel에 있는 sheet 이름을 입력하면 해당 sheet의 내용을 dataframe, list로 각각 member로 저장
# [method 종류]
# 생성자 : excel의 정보를 dataframe, list형태로 member player_df, player_list에 저장
# makelist : base class인 Transfer class에서 player_df를 수정한 후 player_list도 함께 수정하기 위한 method
class Team(Transfer):
    def __init__(self,team):

        #player_df 생성
        self.player_df = player_df['%s'%(team)]

        #player_list 생성
        self.makelist()

    def makelist(self):
        i = 0
        for j in self.player_df.iloc[:,0]:
            i += 1
        list2 = []
        for j in range(i):
           list1 = []
           for k in range(4):
              list1.append(self.player_df.iloc[j,k])
           list2.append(list1)       
        self.player_list = list2   


# [class #2]
# 선수 변동 형태별로 instance를 만들 때 변동 정보 excel에 있는 sheet 이름을 입력하면 해당 sheet의 내용을 dataframe, list로 각각 member typevariation_df, typevariation_list에 저장
# 변동 형태별로 Transfer class의 method를 변동 정보 excel에 있는 정보대로 실행시켜주는 class
class DoVariation:
    def __init__(self,typevariation):

        #typevariation_df 생성
        self.typevariation_df = variationdf['%s'%(typevariation)]

        #typevariation_list 생성
        i = 0
        for j in self.typevariation_df.iloc[:,0]:
            i += 1
        num = len(self.typevariation_df.columns)
        list2 = []
        for j in range(i):
           list1 = []
           for k in range(num):
              list1.append(self.typevariation_df.iloc[j,k])
           list2.append(list1)       
        self.typevariation_list = list2

    # transfer(완전이적) 정보대로 Transfer class의 transfer method가 실행되도록 함
    def dotransfer(self):

        for i in range(len(self.typevariation_list)):
            CallTeamInstance(self.typevariation_list[i][1]).transfer(self.typevariation_list[i][0],self.typevariation_list[i][2],self.typevariation_list[i][3],self.typevariation_list[i][4])
            
    # loanout(임대이적) 정보대로 Transfer class의 loanout method가 실행되도록 함
    def doloanout(self):

        for i in range(len(self.typevariation_list)):
            CallTeamInstance(self.typevariation_list[i][1]).loanout(self.typevariation_list[i][0],self.typevariation_list[i][2],self.typevariation_list[i][3],self.typevariation_list[i][4])

    # loancomeback(임대복귀) 정보대로 Transfer class의 loancomeback method가 실행되도록 함
    def doloancomeback(self):

        for i in range(len(self.typevariation_list)):
            CallTeamInstance(self.typevariation_list[i][1]).loancomeback(self.typevariation_list[i][0],self.typevariation_list[i][2])

    # release(방출) 정보대로 Transfer class의 release method가 실행되도록 함
    def dorelease(self):

        for i in range(len(self.typevariation_list)):
            CallTeamInstance(self.typevariation_list[i][1]).release(self.typevariation_list[i][0])

    # callup(유스콜업) 정보대로 Transfer class의 callup method가 실행되도록 함
    def docallup(self):

        for i in range(len(self.typevariation_list)):
            CallTeamInstance(self.typevariation_list[i][1]).callup(self.typevariation_list[i][0],self.typevariation_list[i][2],self.typevariation_list[i][3])

    # recontract(재계약) 정보대로 Transfer class의 recontract method가 실행되도록 함
    def dorecontract(self):

        for i in range(len(self.typevariation_list)):
            CallTeamInstance(self.typevariation_list[i][1]).recontract(self.typevariation_list[i][0],self.typevariation_list[i][2])        

    # changenumber(등번호변경) 정보대로 Transfer class의 changenumber method가 실행되도록 함
    def dochangenumber(self):

        for i in range(len(self.typevariation_list)):
            CallTeamInstance(self.typevariation_list[i][1]).changenumber(self.typevariation_list[i][0],self.typevariation_list[i][2])
            
# [실행문]

# 기존선수명단(2223SpringRosterExample.xlsx) 정보 저장 
file_name = '2223SpringRosterExample.xlsx'
player_df = pd.read_excel(file_name,sheet_name=['ManCity','Arsenal','Tottenham','Chelsea','Barcelona'])

# team별 instance생성
Arsenal = Team("Arsenal")
ManCity = Team("ManCity")
Tottenham = Team("Tottenham")
Chelsea = Team("Chelsea")
Barcelona = Team("Barcelona")

# 명단변동(2223SummerVariationExample.xlsx) 정보 저장
file_name = '2223SummerVariationExample.xlsx'
variationdf = pd.read_excel(file_name,sheet_name=['Transfer','Loanout','Loancomeback','Release','Callup','Recontract','Changenumber'])

# 변동별 instance생성
doTransfer = DoVariation("Transfer")
doLoanout = DoVariation("Loanout")
doLoancomeback = DoVariation("Loancomeback")
doRelease = DoVariation("Release")
doCallup = DoVariation("Callup")
doRecontract = DoVariation("Recontract")
doChangenumber = DoVariation("Changenumber")

# 변동 적용
doTransfer.dotransfer()
doLoanout.doloanout()
doLoancomeback.doloancomeback()
doRelease.dorelease()
doCallup.docallup()
doRecontract.dorecontract()
doChangenumber.dochangenumber()

# 적용된 변동사항 새로운선수명단(2324FallRosterExample.xlsx)에 저장
file_name = '2324FallRosterExample.xlsx'
with pd.ExcelWriter(file_name) as w:
    ManCity.player_df.to_excel(w,sheet_name='ManCity',index =False)
    Arsenal.player_df.to_excel(w,sheet_name='Arsenal',index=False)
    Tottenham.player_df.to_excel(w,sheet_name='Tottenham',index =False)
    Chelsea.player_df.to_excel(w,sheet_name='Chelsea',index=False)
    Barcelona.player_df.to_excel(w,sheet_name='Barcelona',index=False)

print("[Roster change complete]")