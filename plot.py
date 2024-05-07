# total resource utlization is less but central and edge nodes are both being used more in modified
# our profit isn't increasing as much because we are using more central nodes too, which drives up the cost
from typing import *
import matplotlib

matplotlib.use("agg")
import matplotlib.pyplot as plt
import csv
import math
import linecache
import ast
import config
from config import episodes, repetitions

episodes = str(episodes)
repetitions = str(repetitions)

print("[DEBUG]", episodes, repetitions)

# [PROFIT]
profit_line_number = 3
profit_embb_line_number = 18
profit_urllc_line_number = 21
profit_miot_line_number = 24

# [ACPT RATE]
acpt_rate_line_number = 27
acpt_rate_embb_line_number = 30
acpt_rate_urllc_line_number = 33
acpt_rate_miot_line_number = 36

# [RESOURCE UTL]
res_utl_line_number = 42
central_utl_line_number = 51
edge_utl_line_number = 48
bw_utl_line_number = 45

res_utl_embb_line_number = 54
res_utl_urllc_line_number = 57
res_utl_miot_line_number = 60

# [DELAY]
total_delay_line_number = 63
embb_delay_line_number = 66
urllc_delay_line_number = 69
miot_delay_line_number = 72

deepsara_modified_output = "deepsara_20_output_modified.txt"
deepsara_output = "deepsara_20_output.txt"

# [DELAY]
deepsara_modified_total_delay = ast.literal_eval(
    linecache.getline(deepsara_modified_output, total_delay_line_number)
)
deepsara_total_delay = ast.literal_eval(
    linecache.getline(deepsara_output, total_delay_line_number)
)

deepsara_modified_embb_delay = ast.literal_eval(
    linecache.getline(deepsara_modified_output, embb_delay_line_number)
)
deepsara_modified_urllc_delay = ast.literal_eval(
    linecache.getline(deepsara_modified_output, urllc_delay_line_number)
)
deepsara_modified_miot_delay = ast.literal_eval(
    linecache.getline(deepsara_modified_output, miot_delay_line_number)
)

deepsara_embb_delay = ast.literal_eval(
    linecache.getline(deepsara_output, embb_delay_line_number)
)
deepsara_urllc_delay = ast.literal_eval(
    linecache.getline(deepsara_output, urllc_delay_line_number)
)
deepsara_miot_delay = ast.literal_eval(
    linecache.getline(deepsara_output, miot_delay_line_number)
)

# [PROFIT]
deepsara_modified_profit = ast.literal_eval(
    linecache.getline(deepsara_modified_output, profit_line_number)
)
deepsara_profit = ast.literal_eval(
    linecache.getline(deepsara_output, profit_line_number)
)

deepsara_modified_embb_profit = ast.literal_eval(
    linecache.getline(deepsara_modified_output, profit_embb_line_number)
)
deepsara_embb_profit = ast.literal_eval(
    linecache.getline(deepsara_output, profit_embb_line_number)
)

deepsara_modified_urllc_profit = ast.literal_eval(
    linecache.getline(deepsara_modified_output, profit_urllc_line_number)
)
deepsara_urllc_profit = ast.literal_eval(
    linecache.getline(deepsara_output, profit_urllc_line_number)
)

deepsara_modified_miot_profit = ast.literal_eval(
    linecache.getline(deepsara_modified_output, profit_miot_line_number)
)
deepsara_miot_profit = ast.literal_eval(
    linecache.getline(deepsara_output, profit_miot_line_number)
)

# [ACPT RATE]
acpt_rate_deepsara_modified = ast.literal_eval(
    linecache.getline(deepsara_modified_output, acpt_rate_line_number)
)
acpt_rate_deepsara = ast.literal_eval(
    linecache.getline(deepsara_output, acpt_rate_line_number)
)
acpt_rate_embb_deepsara_modified = ast.literal_eval(
    linecache.getline(deepsara_modified_output, acpt_rate_embb_line_number)
)
acpt_rate_embb_deepsara = ast.literal_eval(
    linecache.getline(deepsara_output, acpt_rate_embb_line_number)
)

acpt_rate_urllc_deepsara_modified = ast.literal_eval(
    linecache.getline(deepsara_modified_output, acpt_rate_urllc_line_number)
)
acpt_rate_urllc_deepsara = ast.literal_eval(
    linecache.getline(deepsara_output, acpt_rate_urllc_line_number)
)
acpt_rate_miot_deepsara_modified = ast.literal_eval(
    linecache.getline(deepsara_modified_output, acpt_rate_miot_line_number)
)
acpt_rate_miot_deepsara = ast.literal_eval(
    linecache.getline(deepsara_output, acpt_rate_miot_line_number)
)

# [RESOURCE UTL]
res_utl_deepsara_modified = ast.literal_eval(
    linecache.getline(deepsara_modified_output, res_utl_line_number)
)
res_utl_deepsara = ast.literal_eval(
    linecache.getline(deepsara_output, res_utl_line_number)
)

#[embb]
res_utl_embb_deepsara = ast.literal_eval(
    linecache.getline(deepsara_output, res_utl_embb_line_number)
)
res_utl_embb_deepsara_modified = ast.literal_eval(
    linecache.getline(deepsara_modified_output, res_utl_embb_line_number)
)
#[urllc]
res_utl_urllc_deepsara = ast.literal_eval(
    linecache.getline(deepsara_output, res_utl_urllc_line_number)
)
res_utl_urllc_deepsara_modified = ast.literal_eval(
    linecache.getline(deepsara_modified_output, res_utl_urllc_line_number)
)
#[miot]
res_utl_miot_deepsara = ast.literal_eval(
    linecache.getline(deepsara_output, res_utl_miot_line_number)
)
res_utl_miot_deepsara_modified = ast.literal_eval(
    linecache.getline(deepsara_modified_output, res_utl_miot_line_number)
)


res_centralutl_deepsara_modified = ast.literal_eval(
    linecache.getline(deepsara_modified_output, central_utl_line_number)
)
res_centralutl_deepsara = ast.literal_eval(
    linecache.getline(deepsara_output, central_utl_line_number)
)

res_edgeutl_deepsara_modified = ast.literal_eval(
    linecache.getline(deepsara_modified_output, edge_utl_line_number)
)
res_edgeutl_deepsara = ast.literal_eval(
    linecache.getline(deepsara_output, edge_utl_line_number)
)

bw_utl_deepsara_modified = ast.literal_eval(
    linecache.getline(deepsara_modified_output, bw_utl_line_number)
)
bw_utl_deepsara = ast.literal_eval(
    linecache.getline(deepsara_output, bw_utl_line_number)
)


def average(lista):  # funcion para retornar el promedio de una lista de datos
    sum = 0.0
    for l in range(0, len(lista)):
        sum = sum + lista[l]
    return sum / len(lista)


def standardDev(lista):  # funcion para calcular desviacion standard
    sum = 0.0
    size = len(lista)
    avrg = average(lista)
    # print "average: ",avrg
    for l in range(0, len(lista)):
        sum = sum + math.pow((lista[l] - avrg), 2.0)
    return math.sqrt(sum / (size))


x = []
topologies = ["16BA", "abilene"]

########### arrivalRate20 ############
arrival_rate = "20"

# [PROFIT]
me_profit_deepsara = []
me_profit_deepsara_modified = []
me_profit_embb_deepsara = []
me_profit_embb_deepsara_modified = []
me_profit_urllc_deepsara = []
me_profit_urllc_deepsara_modified = []
me_profit_miot_deepsara = []
me_profit_miot_deepsara_modified = []

# [ACPT RATE]
me_acpt_rate_deepsara = []
me_acpt_rate_deepsara_modified = []
me_acpt_rate_embb = []
me_acpt_rate_embb_modified = []
me_acpt_rate_urllc = []
me_acpt_rate_urllc_modified = []
me_acpt_rate_miot = []
me_acpt_rate_miot_modified = []

# [DELAY]
me_delay_deepsara_modified = []
me_delay_deepsara = []
me_delay_embb_modified = []
me_delay_urllc_modified = []
me_delay_miot_modified = []
me_delay_embb = []
me_delay_urllc = []
me_delay_miot = []

# [RESOURCE UTL]
me_utl_deepsara = []
me_utl_deepsara_modified = []
me_centralutl_deepsara_modified = []
me_centralutl_deepsara = []
me_edgeutl_deepsara_modified = []
me_edgeutl_deepsara = []
me_bwutl_deepsara_modified = []
me_bwutl_deepsara = []

me_utl_embb = []
me_utl_embb_modified = []
me_utl_urllc = []
me_utl_urllc_modified = []
me_utl_miot = []
me_utl_miot_modified = []

# [DELAY]
deepsara_modified_total_delay_aux = []
deepsara_total_delay_aux = []

deepsara_modified_embb_delay_aux = []
deepsara_modified_urllc_delay_aux = []
deepsara_modified_miot_delay_aux = []
deepsara_embb_delay_aux = []
deepsara_urllc_delay_aux = []
deepsara_miot_delay_aux = []

# [PROFIT]
profit_deepsara_modified_aux = []
profit_deepsara_aux = []

deepsara_modified_embb_profit_aux = []
deepsara_embb_profit_aux = []
deepsara_modified_urllc_profit_aux = []
deepsara_urllc_profit_aux = []
deepsara_modified_miot_profit_aux = []
deepsara_miot_profit_aux = []

# [ACPT RATE]
acpt_rate_deepsara_modified_aux = []
acpt_rate_deepsara_aux = []

acpt_rate_embb_deepsara_aux = []
acpt_rate_embb_deepsara_modified_aux = []
acpt_rate_urllc_deepsara_aux = []
acpt_rate_urllc_deepsara_modified_aux = []
acpt_rate_miot_deepsara_aux = []
acpt_rate_miot_deepsara_modified_aux = []

# [RESOURCE UTL]
res_utl_deepsara_modified_aux = []
res_utl_deepsara_aux = []

res_utl_embb_deepsara_modified_aux = []
res_utl_embb_deepsara_aux  = []
res_utl_urllc_deepsara_modified_aux = []
res_utl_urllc_deepsara_aux = []
res_utl_miot_deepsara_modified_aux = []
res_utl_miot_deepsara_aux = []

res_centralutl_deepsara_modified_aux = []
res_centralutl_deepsara_aux = []
res_edgeutl_deepsara_modified_aux = []
res_edgeutl_deepsara_aux = []

bw_utl_deepsara_modified_aux = []
bw_utl_deepsara_aux = []


def modify_data(ds, ds_mod, me_ds, me_ds_mod, ds_aux, ds_mod_aux):
    for i in range(int(episodes)):
        div = 1

        me_ds.append(1.96 * standardDev(ds[i]) / math.sqrt(100))
        me_ds_mod.append(1.96 * standardDev(ds_mod[i]) / math.sqrt(100))

        ds[i] = average(ds[i]) / div
        ds_mod[i] = average(ds_mod[i]) / div

        ds_aux.append(ds[i] + 0.1)
        ds_mod_aux.append(ds_mod[i] + 0.1)
    return [ds_aux, ds_mod_aux]


#[PROFIT]
modify_data(
    deepsara_profit,
    deepsara_modified_profit,
    me_profit_deepsara,
    me_profit_deepsara_modified,
    profit_deepsara_aux,
    profit_deepsara_modified_aux,
)
modify_data(
    deepsara_embb_profit,
    deepsara_modified_embb_profit,
    me_profit_embb_deepsara,
    me_profit_embb_deepsara_modified,
    deepsara_embb_profit_aux,
    deepsara_modified_embb_profit_aux,
)
modify_data(
    deepsara_urllc_profit,
    deepsara_modified_urllc_profit,
    me_profit_urllc_deepsara,
    me_profit_urllc_deepsara_modified,
    deepsara_urllc_profit_aux,
    deepsara_modified_urllc_profit_aux,
)
modify_data(
    deepsara_miot_profit,
    deepsara_modified_miot_profit,
    me_profit_miot_deepsara,
    me_profit_miot_deepsara_modified,
    deepsara_miot_profit_aux,
    deepsara_modified_miot_profit_aux,
)

#[ACPT RATE]
modify_data(
    acpt_rate_deepsara,
    acpt_rate_deepsara_modified,
    me_acpt_rate_deepsara,
    me_acpt_rate_deepsara_modified,
    acpt_rate_deepsara_aux,
    acpt_rate_deepsara_modified_aux,
)
modify_data(
    acpt_rate_embb_deepsara,
    acpt_rate_embb_deepsara_modified,
    me_acpt_rate_embb,
    me_acpt_rate_embb_modified,
    acpt_rate_embb_deepsara_aux,
    acpt_rate_embb_deepsara_modified_aux
)
modify_data(
    acpt_rate_urllc_deepsara,
    acpt_rate_urllc_deepsara_modified,
    me_acpt_rate_urllc,
    me_acpt_rate_urllc_modified,
    acpt_rate_urllc_deepsara_aux,
    acpt_rate_urllc_deepsara_modified_aux
)
modify_data(
    acpt_rate_miot_deepsara,
    acpt_rate_miot_deepsara_modified,
    me_acpt_rate_miot,
    me_acpt_rate_miot_modified,
    acpt_rate_miot_deepsara_aux,
    acpt_rate_miot_deepsara_modified_aux
)

#[RES UTL]
modify_data(
    res_utl_deepsara,
    res_utl_deepsara_modified,
    me_utl_deepsara,
    me_utl_deepsara_modified,
    res_utl_deepsara_aux,
    res_utl_deepsara_modified_aux,
)

modify_data(
    res_utl_embb_deepsara,
    res_utl_embb_deepsara_modified,
    me_utl_embb,
    me_utl_embb_modified,
    res_utl_embb_deepsara_aux,
    res_utl_embb_deepsara_modified_aux,
)
modify_data(
    res_utl_urllc_deepsara,
    res_utl_urllc_deepsara_modified,
    me_utl_urllc,
    me_utl_urllc_modified,
    res_utl_urllc_deepsara_aux,
    res_utl_urllc_deepsara_modified_aux,
)
modify_data(
    res_utl_miot_deepsara,
    res_utl_miot_deepsara_modified,
    me_utl_miot,
    me_utl_miot_modified,
    res_utl_miot_deepsara_aux,
    res_utl_miot_deepsara_modified_aux,
)

# central utl
modify_data(
    res_centralutl_deepsara,
    res_centralutl_deepsara_modified,
    me_centralutl_deepsara,
    me_centralutl_deepsara_modified,
    res_centralutl_deepsara_aux,
    res_centralutl_deepsara_modified_aux,
)
# edge utl
modify_data(
    res_edgeutl_deepsara,
    res_edgeutl_deepsara_modified,
    me_edgeutl_deepsara,
    me_edgeutl_deepsara_modified,
    res_edgeutl_deepsara_aux,
    res_edgeutl_deepsara_modified_aux,
)
# bw utl
modify_data(
    bw_utl_deepsara,
    bw_utl_deepsara_modified,
    me_bwutl_deepsara,
    me_bwutl_deepsara_modified,
    bw_utl_deepsara_aux,
    bw_utl_deepsara_modified_aux,
)

# Delay
modify_data(
    deepsara_total_delay,
    deepsara_modified_total_delay,
    me_delay_deepsara,
    me_delay_deepsara_modified,
    deepsara_total_delay_aux,
    deepsara_modified_total_delay_aux,
)
# embb delay
modify_data(
    deepsara_embb_delay,
    deepsara_modified_embb_delay,
    me_delay_embb,
    me_delay_embb_modified,
    deepsara_embb_delay_aux,
    deepsara_modified_embb_delay_aux,
)
# urllc delay
modify_data(
    deepsara_urllc_delay,
    deepsara_modified_urllc_delay,
    me_delay_urllc,
    me_delay_urllc_modified,
    deepsara_urllc_delay_aux,
    deepsara_modified_urllc_delay_aux,
)
# miot delay
modify_data(
    deepsara_miot_delay,
    deepsara_modified_miot_delay,
    me_delay_miot,
    me_delay_miot_modified,
    deepsara_miot_delay_aux,
    deepsara_modified_miot_delay_aux,
)

for i in range(len(deepsara_profit)):
    x.append(i + 1)

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


def plot_comparison(x, y_ds, y_ds_mod, me_ds, me_ds_mod, title: str):
    plt.axvline(x=12, color="silver", linestyle="--")
    plt.errorbar(
        x,
        y_ds_mod,
        # yerr=me_ds_mod,
        fmt="-",
        label="DEEPSARA_Modified",
        color="blue",
        ecolor="lightgray",
        capsize=2,
    )
    plt.errorbar(
        x,
        y_ds,
        # yerr=me_ds,
        fmt="-",
        label="DEEPSARA",
        color="red",
        ecolor="lightgray",
        capsize=2,
    )
    print("reached here")
    plt.xlabel("Episodes")
    plt.ylabel(title)
    plt.legend(fontsize=14, loc="lower right", fancybox=True, shadow=True)
    plt.savefig(
        f"Output_Plots\\"
        + "_"
        + title
        + "_EPISODES_"
        + episodes
        + "_REP"
        + repetitions
        + "_"
        + arrival_rate
        + "_"
        + topologies[0]
        + ".png",
        bbox_inches="tight",
    )
    plt.close()

def plot_nslr_comparison(x, y_sets, me_sets, labels, colors, title: str):
    n = len(y_sets)
    plt.figure(figsize=(10, 6))  # Set the figure size
    plt.axvline(x=12, color="silver", linestyle="--")
    for i in range(n):
        plt.errorbar(
            x,
            y_sets[i],
            # yerr=me_sets[i],
            fmt="-",
            label=labels[i],
            color=colors[i],
            capsize=2,
        )

    plt.xlabel("Episodes")
    plt.ylabel(title)
    plt.legend(fontsize=14, loc="lower right", fancybox=True, shadow=True)
    plt.savefig(
        f"Output_Plots\\_{title}_EPISODES_{episodes}_REP{repetitions}_{arrival_rate}_{topologies[0]}.png",
        bbox_inches="tight",
    )
    plt.close()

def plot_all():
    #[DELAY]
    delay_data = [
        deepsara_embb_delay_aux,
        deepsara_modified_embb_delay_aux,
        deepsara_urllc_delay_aux,
        deepsara_modified_urllc_delay_aux,
        deepsara_miot_delay_aux,
        deepsara_modified_miot_delay_aux,
    ]

    delay_errors = [
        me_delay_embb,
        me_delay_embb_modified,
        me_delay_urllc,
        me_delay_urllc_modified,
        me_delay_miot,
        me_delay_miot_modified,
    ]

    all_labels = [
        "DEEPSARA EMBB",
        "DEEPSARA_Modified EMBB",
        "DEEPSARA URLLC",
        "DEEPSARA_Modified URLLC",
        "DEEPSARA MIOT",
        "DEEPSARA_Modified MIOT",
    ]

    all_colors = ["yellow", "blue", "orange", "green", "red", "purple"]
    # all_colors = ["red", "blue", "green", "orange", "purple", "brown"]

    # Plot all types of delay on the same plot
    plot_nslr_comparison(x, delay_data, delay_errors, all_labels, all_colors, "NSLR_DELAY")

    #[PROFIT]
    profit_data = [
        deepsara_embb_profit_aux,
        deepsara_modified_embb_profit_aux,
        deepsara_urllc_profit,
        deepsara_modified_urllc_profit_aux,
        deepsara_miot_profit,
        deepsara_modified_miot_profit_aux,
    ]

    profit_errors = [
        me_profit_embb_deepsara,
        me_profit_embb_deepsara_modified,
        me_profit_urllc_deepsara,
        me_profit_urllc_deepsara_modified,
        me_profit_miot_deepsara,
        me_profit_miot_deepsara_modified      
    ]

    # Plot all types of profits on the same plot
    plot_nslr_comparison(x, profit_data, profit_errors, all_labels, all_colors, "NSLR_PROFIT")

    #[ACPT RATE]
    acpt_rate_data = [
        acpt_rate_embb_deepsara_aux,
        acpt_rate_embb_deepsara_modified_aux,
        acpt_rate_urllc_deepsara_aux,
        acpt_rate_urllc_deepsara_modified_aux,
        acpt_rate_miot_deepsara_aux,
        acpt_rate_miot_deepsara_modified_aux,   
    ]
    acpt_rate_errors = [
        me_acpt_rate_embb,
        me_acpt_rate_embb_modified,
        me_acpt_rate_urllc, 
        me_acpt_rate_urllc_modified,
        me_acpt_rate_miot,
        me_acpt_rate_miot_modified
    ]
    # Plot all types of acpt rate on the same plot
    plot_nslr_comparison(x, acpt_rate_data, acpt_rate_errors, all_labels, all_colors, "NSLR_ACPT_RATE")

    #[RESOURCE UTL]
    res_utl_data = [
        res_centralutl_deepsara_aux,
        res_centralutl_deepsara_modified_aux,
        res_edgeutl_deepsara_aux,
        res_edgeutl_deepsara_modified_aux,
        bw_utl_deepsara_aux,
        bw_utl_deepsara_modified_aux   
    ]
    res_utl_errors = [
        me_centralutl_deepsara,
        me_centralutl_deepsara_modified,
        me_edgeutl_deepsara,
        me_edgeutl_deepsara_modified,
        me_bwutl_deepsara,
        me_bwutl_deepsara_modified
    ]
    # Plot all types of delay on the same plot
    plot_nslr_comparison(x, res_utl_data, res_utl_errors, all_labels, all_colors, "NSLR_RES_UTL")


def plot_graphs_episodes():
    font = {"family": "normal", "size": 16}
    matplotlib.rc("font", **font)
    plot_all()
    
    #Delay v/s episode
    plot_comparison(
        x,
        deepsara_total_delay_aux,
        deepsara_modified_total_delay_aux,
        me_delay_deepsara,
        me_delay_deepsara_modified,
        "DELAY",
    )
    
    # Profit v/s episode
    plot_comparison(
        x,
        profit_deepsara_aux,
        profit_deepsara_modified_aux,
        me_profit_deepsara,
        me_profit_deepsara_modified,
        "PROFIT",
    )
    
    # Aceptance rate v/s episode
    plot_comparison(
        x,
        acpt_rate_deepsara_aux,
        acpt_rate_deepsara_modified_aux,
        me_acpt_rate_deepsara,
        me_acpt_rate_deepsara_modified,
        "ACCEPTANCE_RATE",
    )

    # Resource Utilization v/s episode
    plot_comparison(
        x,
        res_utl_deepsara_aux,
        res_utl_deepsara_modified_aux,
        me_utl_deepsara,
        me_utl_deepsara_modified,
        "RESOURCE_UTILIZATION",
    )

    return
    # DELAY
    plot_comparison(
        x,
        deepsara_total_delay_aux,
        deepsara_modified_total_delay_aux,
        me_delay_deepsara,
        me_delay_deepsara_modified,
        "DELAY",
    )

    # embb Delay
    plot_comparison(
        x,
        deepsara_embb_delay_aux,
        deepsara_modified_embb_delay_aux,
        me_delay_embb,
        me_delay_embb_modified,
        "EMBB_DELAY",
    )

    # urllc Delay
    plot_comparison(
        x,
        deepsara_urllc_delay_aux,
        deepsara_modified_urllc_delay_aux,
        me_delay_urllc,
        me_delay_urllc_modified,
        "URLLC_DELAY",
    )

    # miot delay
    plot_comparison(
        x,
        deepsara_miot_delay_aux,
        deepsara_modified_miot_delay_aux,
        me_delay_miot,
        me_delay_miot_modified,
        "MIOT_DELAY",
    )

# Centralized nodes Utilization
plot_comparison(
    x,
    res_centralutl_deepsara_aux,
    res_centralutl_deepsara_modified_aux,
    me_centralutl_deepsara,
    me_centralutl_deepsara_modified,
    "CENTRALIZED_NODES_RES_UTL",
)

# Edge nodes Utilization
plot_comparison(
    x,
    res_edgeutl_deepsara_aux,
    res_edgeutl_deepsara_modified_aux,
    me_edgeutl_deepsara,
    me_edgeutl_deepsara_modified,
    "EDGE_NODES_RES_UTL",
)

# BW Utilization
plot_comparison(
    x,
    bw_utl_deepsara_aux,
    bw_utl_deepsara_modified_aux,
    me_bwutl_deepsara,
    me_bwutl_deepsara_modified,
    "BW_UTL",
)

def plot_graphs_arrival_rate():
    plt.axvline(x=12, color = "silver", linestyle='--')
    plt.errorbar(x,acpt_rate_embb_deepsara_aux,yerr = me_acpt_rate_embb_modified,fmt="-",label="eMBB",color='orange',ecolor="lightgray",capsize=2)
    plt.errorbar(x,acpt_rate_urllc_deepsara_aux,yerr = me_acpt_rate_urllc_modified,fmt="-",label="URLLC",ecolor="lightgray",capsize=2)
    plt.errorbar(x,acpt_rate_miot_deepsara_aux,yerr = me_acpt_rate_miot_modified,fmt="-",label="MIoT",color='#00d63d',ecolor="lightgray",capsize=2)
    plt.xlabel('Episodes')
    plt.ylabel('Acceptance rate')
    plt.legend(fontsize = 14,loc="lower right", shadow=True)
    # plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.1), fancybox=True, shadow=True, ncol=3)
    plt.savefig("acptxreqtype_"+arrival_rate+"_"+topologies[0]+".jpg",bbox_inches = 'tight')
    plt.close()

plot_graphs_arrival_rate()
plot_graphs_episodes()
plot_all()
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
