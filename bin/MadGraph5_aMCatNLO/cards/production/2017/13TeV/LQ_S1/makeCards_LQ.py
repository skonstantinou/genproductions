# EXAMPLES: python3 makeCards_LQ.py TLTL  tau
# FIXME: left-right, mixed flav - should be added in the output file and restrict file in proc card
import os
import sys

scheme = sys.argv[1] # Options: ["TLTL", "TLQ5L", "Q5LQ5L", "TLL", "Q5LL", "TLVL", "Q5LVL", "LL", "VLL" ]
lflav  = sys.argv[2] # Options: ["ele", "mu", "tau", "eletau", "mutau"]

procTemplate = open("./S1LQ_"+scheme+"_proc_card.dat")
procCard = procTemplate.read()
procTemplate.close()
custoTemplate = open("./S1LQ_customizecards.dat")
custoCard = custoTemplate.read()
custoTemplate.close()
modelTemplate = open("./S1LQ_extramodels.dat")
modelCard = modelTemplate.read()
modelTemplate.close()
runTemplate = open("./S1LQ_run_card.dat")
runCard = runTemplate.read()
runTemplate.close()

mass_list = ['400','600','800',"1000", '1200','1400','1600','1800','2000','2200','2400','2600', '2800', '3000']
yuk_list = ['0pt01'] # ['5','4pt5','4','3pt5','3','2pt5','2','1pt5','1','0pt5','0pt01']
chrl_list = ['L'] # ['L', 'R']

print("Generating "+str(len(mass_list)*len(yuk_list)*len(chrl_list))+" folders")
print(f"Using procTemplate 'S1LQ_"+scheme+"_proc_card.dat'")
for mass in mass_list:
    for yuk in yuk_list:
        for chrl in chrl_list:
            print (f"Generating cards for Mass = {mass}, Yuk = {yuk}, chirality = {chrl}")
            prefix = "S1LQ_"+scheme+"_"+lflav+"_M-"+mass+"_yuk"+chrl+"-"+yuk
            os.makedirs ("./LQ_Cards/S1LQ_"+scheme+"/"+prefix)
            newprocCard = open("./LQ_Cards/S1LQ_"+scheme+"/"+prefix+"/"+prefix+"_proc_card.dat",'w+')
            newprocCard_1 = procCard.replace("LQMASS",mass).replace("LQYUK",yuk).replace("LEPF",lflav).replace("CHRL", chrl).replace("LQOUTPUT", prefix)
            newprocCard.write(newprocCard_1)
            newprocCard.close()
            
            newcustoCard = open("./LQ_Cards/S1LQ_"+scheme+"/"+prefix+"/"+prefix+"_customizecards.dat",'w+')
            newcustoCard_1 = custoCard.replace("LQMASS",mass)
            newcustoCard.write(newcustoCard_1)
            newcustoCard.close()
            
            newmodelCard = open("./LQ_Cards/S1LQ_"+scheme+"/"+prefix+"/"+prefix+"_extramodels.dat",'w+')
            newmodelCard_1 = modelCard
            newmodelCard.write(newmodelCard_1)
            newmodelCard.close()        
            
            newrunCard = open("./LQ_Cards/S1LQ_"+scheme+"/"+prefix+"/"+prefix+"_run_card.dat",'w+')
            newrunCard_1 = runCard
            newrunCard.write(newrunCard_1)
            newrunCard.close()        
        
exit(0)
