#total resource utlization is less but central and edge nodes are both being used more in modified
#our profit isn't increasing as much because we are using more central nodes too, which drives up the cost
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import csv
import math
import linecache
import ast
from config import episodes, repetitions
episodes = str(episodes)
repetitions = str(repetitions)

print("[DEBUG]", episodes, repetitions)

profit_line_number = 3
acpt_rate_line_number = 27
res_utl_line_number = 42
central_utl_line_number = 51
edge_utl_line_number = 48
bw_utl_line_number = 45
deepsara_modified_output = "deepsara_20_output_modified.txt"
deepsara_output = "deepsara_20_output.txt"
deepsara_modified_profit = ast.literal_eval(linecache.getline(deepsara_modified_output, profit_line_number))
deepsara_profit = ast.literal_eval(linecache.getline(deepsara_output, profit_line_number))

def average(lista): # funcion para retornar el promedio de una lista de datos
    sum=0.0
    for l in range(0,len(lista)):
        sum=sum+lista[l] 
    return sum/len(lista)

def standardDev(lista): # funcion para calcular desviacion standard
    sum = 0.0
    size = len(lista)
    avrg = average(lista)
    #print "average: ",avrg
    for l in range(0,len(lista)):
        sum = sum + math.pow((lista[l] - avrg), 2.0)    
    return math.sqrt(sum/(size));


x = []
topologies = ["16BA","abilene"]

########### arrivalRate20 ############
arrival_rate = "20"

#deeprl state3de10 actions30 160episodes replay_start_size=500 anneal_rate=(1/5000):
#these will be deepsara, not nr. TODO:
profit_nr = deepsara_profit
profit_nr_modified = deepsara_modified_profit

print(len(profit_nr))
# profit_rl = profit_rl + profit_rl + profit_rl + profit_rl
# profit_nr = profit_nr + profit_nr + profit_nr + profit_nr
# profit_aar = profit_aar + profit_aar + profit_aar + profit_aar

# for i in range(11,len(profit_rl)):
#     for j in range(8):
#         profit_rl[i].append(0.56)
#         res_utl_rl[i].append(0.52)

margin_error1 = []
margin_error2 = []
margin_error3 = []
margin_error4 = []
margin_error5 = []
margin_error6 = []

me_embb_profit_rl = []
me_urllc_profit_rl = []
me_miot_profit_rl = []
me_embb_acpt_rl = []
me_urllc_acpt_rl = []
me_miot_acpt_rl = []

me_utl_deepsara = []
me_utl_deepsara_modified = []
me_centralutl_deepsara_modified = []
me_centralutl_deepsara = []
me_edgeutl_deepsara_modified = []
me_edgeutl_deepsara = []

me_utl_rl=[]
me_utl_nr=[]
me_utl_aar=[]
me_centralutl_rl = []
me_centralutl_nr = []
me_edgeutl_rl = []
me_edgeutl_nr = []

profit_rl_aux = []
profit_nr_aux = []
profit_nr_modified_aux = []
profit_aar_aux = []
embb_profit_rl_aux = []
urllc_profit_rl_aux = []
miot_profit_rl_aux = []

acpt_rate_deepsara_modified = ast.literal_eval(linecache.getline(deepsara_modified_output, acpt_rate_line_number))
acpt_rate_deepsara = ast.literal_eval(linecache.getline(deepsara_output, acpt_rate_line_number))
acpt_rate_deepsara_modified_aux = []
acpt_rate_deepsara_aux = []

acpt_rate_rl_aux = []
acpt_rate_nr_aux = []
acpt_rate_aar_aux = []
embb_acpt_rl_aux = []
urllc_acpt_rl_aux = []
miot_acpt_rl_aux = []

res_utl_deepsara_modified = ast.literal_eval(linecache.getline(deepsara_modified_output, res_utl_line_number))
res_utl_deepsara = ast.literal_eval(linecache.getline(deepsara_output, res_utl_line_number))
res_utl_deepsara_modified_aux = []
res_utl_deepsara_aux = []

res_centralutl_deepsara_modified = ast.literal_eval(linecache.getline(deepsara_modified_output, central_utl_line_number))
res_centralutl_deepsara = ast.literal_eval(linecache.getline(deepsara_output, central_utl_line_number))
res_centralutl_deepsara_modified_aux = []
res_centralutl_deepsara_aux = []

res_edgeutl_deepsara_modified = ast.literal_eval(linecache.getline(deepsara_modified_output, edge_utl_line_number))
res_edgeutl_deepsara = ast.literal_eval(linecache.getline(deepsara_output, edge_utl_line_number))
res_edgeutl_deepsara_modified_aux = []
res_edgeutl_deepsara_aux = []

res_utl_rl_aux = []
res_utl_nr_aux = []
res_utl_aar_aux = []
central_utl_rl_aux = []
central_utl_nr_aux = []
edge_utl_rl_aux = []
edge_utl_nr_aux = []

me_bwutl_deepsara_modified = []
me_bwutl_deepsara = []
bw_utl_deepsara_modified = ast.literal_eval(linecache.getline(deepsara_modified_output, bw_utl_line_number))
bw_utl_deepsara = ast.literal_eval(linecache.getline(deepsara_output, bw_utl_line_number))
bw_utl_deepsara_modified_aux = []
bw_utl_deepsara_aux = []

bw_utl_rl_aux = []
bw_utl_nr_aux = []
bw_utl_aar_aux = []
me_bwutl_rl=[]
me_bwutl_nr=[]
me_bwutl_aar=[]
embb_bw_utl_rl_aux = []
urllc_bw_utl_rl_aux = []
miot_bw_utl_rl_aux = []
me_embb_bwutl_rl = []
me_urllc_bwutl_rl = []
me_miot_bwutl_rl = []

print("[DEBUG] LEN PROFIT", len(profit_nr))
print("[DEBUG] LEN CENTRAL RES UTL", len(res_centralutl_deepsara_modified))

for i in range(len(profit_nr)):
    x.append(i+1)
    
    #Profit (SARA, NR, AAR) x episodes, 
    # margin_error1.append(1.96*standardDev(profit_rl[i])/math.sqrt(100))
    # profit_rl[i] = average(profit_rl[i])
    # profit_rl_aux.append(profit_rl[i]+0.1)

    #TODO: Plot profit_modified
    margin_error1.append(1.96*standardDev(profit_nr_modified[i])/math.sqrt(100))    
    profit_nr_modified[i] = average(profit_nr_modified[i])
    profit_nr_modified_aux.append(profit_nr_modified[i]+0.1)
    
    #plot profit
    margin_error2.append(1.96*standardDev(profit_nr[i])/math.sqrt(100))    
    profit_nr[i] = average(profit_nr[i])
    profit_nr_aux.append(profit_nr[i]+0.1)
    # profit_nr_aux.append(profit_nr[i]-0.041)
    
    # margin_error3.append(1.96*standardDev(profit_aar[i])/math.sqrt(100))
    # profit_aar[i] = average(profit_aar[i])
    # profit_aar_aux.append(profit_aar[i]+0.1)
    # profit_aar_aux.append(profit_aar[i]- 0.041)

    
    #Acceptance Rate (SARA, NR, AAR) x episodes 
    #modified deepsara
    margin_error4.append(1.96*standardDev(acpt_rate_deepsara_modified[i])/math.sqrt(100))
    acpt_rate_deepsara_modified[i] = average(acpt_rate_deepsara_modified[i])
    acpt_rate_deepsara_modified_aux.append(acpt_rate_deepsara_modified[i]+0.1)

    #deepsara
    margin_error5.append(1.96*standardDev(acpt_rate_deepsara[i])/math.sqrt(100))    
    acpt_rate_deepsara[i] = average(acpt_rate_deepsara[i])
    acpt_rate_deepsara_aux.append(acpt_rate_deepsara[i]+0.1)
    
    # margin_error6.append(1.96*standardDev(acpt_rate_aar[i])/math.sqrt(100))
    # acpt_rate_aar[i] = average(acpt_rate_aar[i])
    # acpt_rate_aar_aux.append(acpt_rate_aar[i]+0.05)


    #Total Node resource utilization (SARA, NR, AAR) x episodes
    #modified deepsara
    me_utl_deepsara_modified.append(1.96*standardDev(res_utl_deepsara_modified[i])/math.sqrt(100))
    res_utl_deepsara_modified[i] = average(res_utl_deepsara_modified[i])
    res_utl_deepsara_modified_aux.append(res_utl_deepsara_modified[i]+0.1)

    #deepsara
    me_utl_deepsara.append(1.96*standardDev(res_utl_deepsara[i])/math.sqrt(100))    
    res_utl_deepsara[i] = average(res_utl_deepsara[i])
    res_utl_deepsara_aux.append(res_utl_deepsara[i]+0.1)

    # me_utl_aar.append(1.96*standardDev(res_utl_aar[i])/math.sqrt(100))    
    # res_utl_aar[i] = average(res_utl_aar[i])
    # res_utl_aar_aux.append(res_utl_aar[i]+0.1)

    #Centralized resource utilization
    #deepsara modified
    me_centralutl_deepsara_modified.append(1.96*standardDev(res_centralutl_deepsara_modified[i])/math.sqrt(100))
    res_centralutl_deepsara_modified[i] = average(res_centralutl_deepsara_modified[i])
    res_centralutl_deepsara_modified_aux.append(res_centralutl_deepsara_modified[i]+0.03333)

    #deepsara
    me_centralutl_deepsara.append(1.96*standardDev(res_centralutl_deepsara[i])/math.sqrt(100))    
    res_centralutl_deepsara[i] = average(res_centralutl_deepsara[i])
    res_centralutl_deepsara_aux.append(res_centralutl_deepsara[i])

    #Edge resource utilization
    #deepsara modified
    me_edgeutl_deepsara_modified.append(1.96*standardDev(res_edgeutl_deepsara_modified[i])/math.sqrt(100))
    res_edgeutl_deepsara_modified[i] = average(res_edgeutl_deepsara_modified[i])
    res_edgeutl_deepsara_modified_aux.append(res_edgeutl_deepsara_modified[i]+0.03333)

    #deepsara
    me_edgeutl_deepsara.append(1.96*standardDev(res_edgeutl_deepsara[i])/math.sqrt(100))    
    res_edgeutl_deepsara[i] = average(res_edgeutl_deepsara[i])
    res_edgeutl_deepsara_aux.append(res_edgeutl_deepsara[i])

    #Bw utilization
    #modified deepsara
    me_bwutl_deepsara_modified.append(1.96*standardDev(bw_utl_deepsara_modified[i])/math.sqrt(100))
    bw_utl_deepsara_modified[i] = average(bw_utl_deepsara_modified[i])
    bw_utl_deepsara_modified_aux.append(bw_utl_deepsara_modified[i]+0.03333)

    #deepsara
    me_bwutl_deepsara.append(1.96*standardDev(bw_utl_deepsara[i])/math.sqrt(100))    
    bw_utl_deepsara[i] = average(bw_utl_deepsara[i])
    bw_utl_deepsara_aux.append(bw_utl_deepsara[i]*8)

    # me_bwutl_aar.append(1.96*standardDev(bw_utl_aar[i])/math.sqrt(100))    
    # bw_utl_aar[i] = average(bw_utl_aar[i])
    # bw_utl_aar_aux.append(bw_utl_aar[i]*8)

    # #Bw by use case
    # # me_embb_bwutl_rl.append(1.96*standardDev(embb_bw_utl_rl[i])/math.sqrt(33))
    # # embb_bw_utl_rl[i] = average(embb_bw_utl_rl[i])
    # # embb_bw_utl_rl_aux.append(embb_bw_utl_rl[i])

    # # me_urllc_bwutl_rl.append(1.96*standardDev(urllc_bw_utl_rl[i])/math.sqrt(33))
    # # urllc_bw_utl_rl[i] = average(urllc_bw_utl_rl[i])
    # # urllc_bw_utl_rl_aux.append(urllc_bw_utl_rl[i])

    # # me_miot_bwutl_rl.append(1.96*standardDev(miot_bw_utl_rl[i])/math.sqrt(33))
    # # miot_bw_utl_rl[i] = average(miot_bw_utl_rl[i])
    # # miot_bw_utl_rl_aux.append(miot_bw_utl_rl[i])

    # # Profit x NSLR type
    # me_embb_profit_rl.append(1.96*standardDev(embb_profit_rl[i])/math.sqrt(100))
    # embb_profit_rl[i] = average(embb_profit_rl[i])
    # # embb_profit_rl_aux.append(embb_profit_rl[i])
    # embb_profit_rl_aux.append(embb_profit_rl[i]+0.1)

    # me_urllc_profit_rl.append(1.96*standardDev(urllc_profit_rl[i])/math.sqrt(100))
    # urllc_profit_rl[i] = average(urllc_profit_rl[i])
    # # urllc_profit_rl_aux.append(urllc_profit_rl[i])
    # urllc_profit_rl_aux.append(urllc_profit_rl[i])

    # me_miot_profit_rl.append(1.96*standardDev(miot_profit_rl[i])/math.sqrt(100))
    # miot_profit_rl[i] = average(miot_profit_rl[i])
    # miot_profit_rl_aux.append(miot_profit_rl[i])

    # # Acceptance rate x NSLR type
    # me_embb_acpt_rl.append(1.96*standardDev(embb_acpt_rl[i])/math.sqrt(100))
    # embb_acpt_rl[i] = average(embb_acpt_rl[i])
    # embb_acpt_rl_aux.append(embb_acpt_rl[i]+0.03333)

    # me_urllc_acpt_rl.append(1.96*standardDev(urllc_acpt_rl[i])/math.sqrt(100))
    # urllc_acpt_rl[i] = average(urllc_acpt_rl[i])
    # urllc_acpt_rl_aux.append(urllc_acpt_rl[i]+0.03333)

    # me_miot_acpt_rl.append(1.96*standardDev(miot_acpt_rl[i])/math.sqrt(100))
    # miot_acpt_rl[i] = average(miot_acpt_rl[i])
    # miot_acpt_rl_aux.append(miot_acpt_rl[i]+0.03333)

font = {'family' : 'normal',
        'size'   : 16}
matplotlib.rc('font', **font)

# Profit
plt.axvline(x=12, color = "silver", linestyle='--')
# plt.errorbar(x,profit_rl_aux,yerr = margin_error1,fmt="-",label="SARA",ecolor="lightgray",capsize=2)
plt.errorbar(x,profit_nr_modified_aux,yerr = margin_error1,fmt="-",label="DEEPSARA_Modified", color="blue", ecolor="lightgray",capsize=2)
plt.errorbar(x,profit_nr_aux,yerr = margin_error2,fmt="-",label="DEEPSARA", color="red", ecolor="lightgray",capsize=2)
# plt.errorbar(x,profit_aar_aux,yerr = margin_error3,fmt="-",label="AAR", color="gray",ecolor="lightgray",capsize=2)
plt.xlabel('Episodes')
plt.ylabel('Profit')
# plt.title('Time Step Profit')
# plt.legend()
plt.legend(fontsize = 14,loc='lower right', fancybox=True, shadow=True)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), fancybox=True, shadow=True, ncol=3)
#plt.show() 
plt.savefig("Output_Plots\profit_EPISODES_"+ episodes + "_REP"+ repetitions + "_" +arrival_rate+"_"+topologies[0]+".png",bbox_inches = 'tight') 
plt.close()

# Aceptance rate
# plt.errorbar(x,acpt_rate_rl_aux,yerr = margin_error4,fmt="-",label="SARA",ecolor="lightgray",capsize=2)
plt.errorbar(x,acpt_rate_deepsara_modified_aux,yerr = margin_error4,fmt="-",label="DEEPSARA_MODIFIED", color="blue", ecolor="lightgray",capsize=2)
plt.errorbar(x,acpt_rate_deepsara_aux,yerr = margin_error5,fmt="-",label="DEEPSARA", color="red",ecolor="lightgray",capsize=2)
plt.xlabel('Episodes')
plt.ylabel('Acceptance Rate')
# plt.title('Time Step Acceptance Rate')
plt.legend(fontsize = 14,fancybox=True,shadow=True,bbox_to_anchor=(1, 0.61))
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), fancybox=True, shadow=True, ncol=3)
# #plt.show()
plt.savefig("Output_Plots\\acptrate_EPISODES_"+ episodes + "_REP"+ repetitions + "_"+arrival_rate+"_"+topologies[0]+".png",bbox_inches = 'tight')  
plt.close()


# Resource Utilization
plt.axvline(x=12, color = "silver", linestyle='--')
# plt.errorbar(x,res_utl_rl_aux,yerr = me_utl_rl,fmt="-",label="SARA",ecolor="lightgray",capsize=2)
plt.errorbar(x,res_utl_deepsara_modified_aux,yerr = me_utl_deepsara_modified,fmt="-",label="DEEPSARA_MODIFIED", color="blue", ecolor="lightgray",capsize=2)
plt.errorbar(x,res_utl_deepsara_aux,yerr = me_utl_deepsara,fmt="-",label="DEEPSARA", color="red",ecolor="lightgray",capsize=2)
plt.xlabel('Episodes')
plt.ylabel('Resource Utilization')
# plt.title('Time Step Resource Utilization')
plt.legend(fontsize = 14,loc='lower right', fancybox=True, shadow=True)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), fancybox=True, shadow=True, ncol=3)
#plt.show()
# plt.ylim(0.48,0.61)
plt.savefig("Output_Plots\\resutl_EPISODES_"+ episodes + "_REP"+ repetitions + "_"+arrival_rate+"_"+topologies[0]+".png",bbox_inches = 'tight')  
plt.close()

# Centralized nodes Utilization
plt.errorbar(x,res_centralutl_deepsara_modified_aux,yerr = me_centralutl_deepsara_modified,fmt="-",label="DEEPSARA_MODIFIED", color = "blue", ecolor="lightgray",capsize=2)
plt.errorbar(x,res_centralutl_deepsara_aux,yerr = me_centralutl_deepsara,fmt="-",label="DEEPSARA", color="red", ecolor="lightgray",capsize=2)
# plt.errorbar(x,acpt_rate_aar_aux,yerr = margin_error6,fmt="-",label="no NR ", color="gray",ecolor="lightgray",capsize=2)
plt.xlabel('Episodes')
plt.ylabel('Centralized CPU Utilization')
plt.title('Time Step Centralized Resource Utilization')
plt.legend()
#plt.show()
plt.savefig("Output_Plots\\time_step_centralutl_EPISODES_"+ episodes + "_REP"+ repetitions + ".png")    
plt.close()

# Edge nodes Utilization
plt.errorbar(x,res_edgeutl_deepsara_modified_aux,yerr = me_edgeutl_deepsara_modified,fmt="-",label="DEEPSARA_MODIFIED", color= "blue", ecolor="lightgray",capsize=2)
plt.errorbar(x,res_edgeutl_deepsara_aux,yerr = me_edgeutl_deepsara,fmt="-",label="DEEPSARA", color="red", ecolor="lightgray",capsize=2)
# plt.errorbar(x,acpt_rate_aar_aux,yerr = margin_error6,fmt="-",label="no NR ", color="gray",ecolor="lightgray",capsize=2)
plt.xlabel('Episodes')
plt.ylabel('Edge CPU Utilization')
plt.title('Time Step Edge Resource Utilization')
plt.legend()
#plt.show()
plt.savefig("Output_Plots\\time_step_edgeutl_EPISODES_"+ episodes + "_REP"+ repetitions + ".png") #    
plt.close()

# BW Utilization
plt.errorbar(x,bw_utl_deepsara_modified_aux,yerr = me_bwutl_deepsara_modified,fmt="-",label="DEEPSARA_MODIFIED",color="blue", ecolor="lightgray",capsize=2)
plt.errorbar(x,bw_utl_deepsara_aux,yerr = me_bwutl_deepsara,fmt="-",label="DEEPSARA", color="red", ecolor="lightgray",capsize=2)
# plt.errorbar(x,bw_utl_aar_aux,yerr = me_bwutl_aar,fmt="-",label="AAR", color="gray",ecolor="lightgray",capsize=2)
plt.xlabel('Episodes')
plt.ylabel('Bandwidth Utilization')
# plt.title('Time Step Bandwidth Utilization')
plt.legend()
#plt.show()
plt.savefig("Output_Plots\\time_step_bwutl_EPISODES_"+ episodes + "_REP"+ repetitions + ".png",bbox_inches = 'tight') #    
plt.close()


# # # Resource Utilization discriminado x tipo de node
# plt.axvline(x=12, color = "silver", linestyle='--')
# plt.errorbar(x,res_utl_rl_aux,yerr = me_utl_rl,fmt="-",label="Total",ecolor="lightgray",capsize=2)
# plt.errorbar(x,edge_utl_rl_aux,yerr = me_edgeutl_rl,fmt="-",label="edge",color="orange",ecolor="lightgray",capsize=2)
# plt.errorbar(x,central_utl_rl_aux,yerr = me_centralutl_rl,fmt="-",label="central",color='#00d63d',ecolor="lightgray",capsize=2)
# plt.errorbar(x,bw_utl_rl_aux,yerr = me_bwutl_rl,fmt="-",label="links",color='brown',ecolor="lightgray",capsize=2)
# plt.xlabel('Episodes')
# plt.ylabel('Resource Utilization')
# # plt.title('Time Step Resource Utilization')
# plt.legend(fontsize = 14,loc="lower right", shadow=True)
# #plt.show()
# plt.savefig("resutlxnodetype_"+arrival_rate+"_"+topologies[0]+".eps",bbox_inches = 'tight')   
# plt.close()

# # Profit discriminado x tipo de request
# plt.axvline(x=12, color = "silver", linestyle='--')
# plt.errorbar(x,embb_profit_rl_aux,yerr = me_embb_profit_rl,fmt="-",label="eMBB",color='orange',ecolor="lightgray",capsize=2)
# plt.errorbar(x,urllc_profit_rl_aux,yerr = me_urllc_profit_rl,fmt="-",label="URLLC",ecolor="lightgray",capsize=2)
# plt.errorbar(x,miot_profit_rl_aux,yerr = me_miot_profit_rl,fmt="-",label="MIoT",color='#00d63d',ecolor="lightgray",capsize=2)
# plt.xlabel('Episodes')
# plt.ylabel('Profit')
# plt.legend(fontsize = 14,shadow=True,bbox_to_anchor=(1, 0.73),fancybox=True)
# # plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), fancybox=True, shadow=True, ncol=3)
# plt.savefig("profitxreqtype_"+arrival_rate+"_"+topologies[0]+".eps",bbox_inches = 'tight')    
# plt.close()

# # Acceptance rate discriminado x tipo de request
# plt.axvline(x=12, color = "silver", linestyle='--')
# plt.errorbar(x,embb_acpt_rl_aux,yerr = me_embb_acpt_rl,fmt="-",label="eMBB",color='orange',ecolor="lightgray",capsize=2)
# plt.errorbar(x,urllc_acpt_rl_aux,yerr = me_urllc_acpt_rl,fmt="-",label="URLLC",ecolor="lightgray",capsize=2)
# plt.errorbar(x,miot_acpt_rl_aux,yerr = me_miot_acpt_rl,fmt="-",label="MIoT",color='#00d63d',ecolor="lightgray",capsize=2)
# plt.xlabel('Episodes')
# plt.ylabel('Acceptance rate')
# plt.legend(fontsize = 14,loc="lower right", shadow=True)
# # plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), fancybox=True, shadow=True, ncol=3)
# plt.savefig("acptxreqtype_"+arrival_rate+"_"+topologies[0]+".eps",bbox_inches = 'tight')     
# plt.close()

# # BW Utilization discrinado x tipo de request
# plt.errorbar(x,embb_bw_utl_rl_aux,yerr = me_bwutl_rl,fmt="-",label="SARA",ecolor="lightgray",capsize=2)
# plt.errorbar(x,urllc_bw_utl_nr_aux,yerr = me_bwutl_nr,fmt="-",label="NR", color="red", ecolor="lightgray",capsize=2)
# plt.errorbar(x,miot_bw_utl_aar_aux,yerr = me_bwutl_aar,fmt="-",label="AAR", color="gray",ecolor="lightgray",capsize=2)
# plt.xlabel('Episodes')
# plt.ylabel('Bandwidth Utilization')
# # plt.title('Time Step Bandwidth Utilization')
# plt.legend()
# #plt.show()
# plt.savefig("time_step_bwutl.eps",bbox_inches = 'tight') #    
# plt.close()
