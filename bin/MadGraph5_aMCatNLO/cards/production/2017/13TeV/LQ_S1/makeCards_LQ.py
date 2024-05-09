import os
import sys

scheme = sys.argv[1] # Options: ["TLTL", "TLQ5L", "Q5LQ5L", "TLL", "Q5LL", "TLVL", "Q5LVL", "LL", "VLL" ]

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

mass_list = ['500','1000','1500','2000','2500','3000','3500','4000','4500','5000','5500','6000']
yuk_list = ['5','4pt5','4','3pt5','3','2pt5','2','1pt5','1','0pt5','0pt01']

print(f"Using procTemplate 'S1LQ_"+scheme+"_proc_card.dat'")
for mass in mass_list:
    for yuk in yuk_list:
        print (f"Generating cards for Mass = {mass} and Yuk = {yuk}")
        os.makedirs ("./LQ_Cards/S1LQ_"+scheme+"/S1LQ_"+scheme+"_M-"+mass+"_yuk-"+yuk)
        newprocCard = open("./LQ_Cards/S1LQ_"+scheme+"/S1LQ_"+scheme+"_M-"+mass+"_yuk-"+yuk+"/S1LQ_"+scheme+"_M-"+mass+"_yuk-"+yuk+"_proc_card.dat",'w+')
        newprocCard_1 = procCard.replace("LQMASS",mass)
        newprocCard_2 = newprocCard_1.replace("LQYUK",yuk)
        newprocCard.write(newprocCard_2)
        newprocCard.close()

        newcustoCard = open("./LQ_Cards/S1LQ_"+scheme+"/S1LQ_"+scheme+"_M-"+mass+"_yuk-"+yuk+"/S1LQ_"+scheme+"_M-"+mass+"_yuk-"+yuk+"_customizecards.dat",'w+')
        newcustoCard_1 = custoCard.replace("LQMASS",mass)
        newcustoCard.write(newcustoCard_1)
        newcustoCard.close()

        newmodelCard = open("./LQ_Cards/S1LQ_"+scheme+"/S1LQ_"+scheme+"_M-"+mass+"_yuk-"+yuk+"/S1LQ_"+scheme+"_M-"+mass+"_yuk-"+yuk+"_extramodels.dat",'w+')
        newmodelCard_1 = modelCard
        newmodelCard.write(newmodelCard_1)
        newmodelCard.close()        

        newrunCard = open("./LQ_Cards/S1LQ_"+scheme+"/S1LQ_"+scheme+"_M-"+mass+"_yuk-"+yuk+"/S1LQ_"+scheme+"_M-"+mass+"_yuk-"+yuk+"_run_card.dat",'w+')
        newrunCard_1 = runCard
        newrunCard.write(newrunCard_1)
        newrunCard.close()        
        
exit(0)
