def calculate_profit_nodes(nslr,end_simulation_time, service_type_priority):
    #Calculates profit per time unit and then multiplies it by the nslr op. time
    #profit = revenue-cost 
    cost = 0
    revenue = 0    
    vnfs = nslr.nsl_graph_reduced["vnodes"]
    time = 0.0

    cf_cpu = 0 #cost factor of physical nodes(depends on node type)
    for vnf in vnfs:
        if vnf["type"] == 0:#central
            cf_cpu = 1
        elif vnf["type"] == 1:#edge
            cf_cpu = 3
        # else:
        #     cf_cpu = 4 
        cost += vnf["cpu"]*cf_cpu
        revenue += vnf["cpu"]*cf_cpu*2#revenue es el doble del costo (hasta ahora) 

    if nslr.end_time > end_simulation_time:
        #si es mayor, se considera la porcion de tiempo hasta acabar la simulacion  
        time = nslr.operation_time - (nslr.end_time-end_simulation_time)
    else:
        time = nslr.operation_time

    #TODO: Check what is the unit of the times. 
    # if nslr.end_time - nslr.incoming_time > 1:
    #     print("[DEBUG] REQUEST.START TIME", nslr.incoming_time)
    #     print("[DEBUG] REQUEST.END TIME", nslr.end_time)
        
    #TODO: add req delay to cost
    cost_check = (nslr.end_time - nslr.incoming_time) * service_type_priority[nslr.service_type]
    # add a threshold maybe else if priority if too high then even a small delay [normalise this]
    #update cost function here cost += (delay * priority) ?
    profit = (revenue-cost)*time
    # profit = (revenue-(cost + cost_check))*time 
    #TODO: profit and reward are separate
    reward = - cost_check
    return reward, profit

def calculate_profit_links(nslr,end_simulation_time, service_type_priority):
    #Calculates profit per time unit and then multiplies it by the nslr op. time
    #profit = revenue-cost 
    cost = 0
    revenue = 0        
    vlinks = nslr.nsl_graph_reduced["vlinks"]    
    cf_bw =  0.5#cost factor of physical links    
    time = 0.0

#TODO: Check number of hops in modified and original. Plot graphs.
    for vlink in vlinks:
        try:
            hops = len(vlink["mapped_to"])-1
        except KeyError:
            hops=0
        cost += vlink["bw"]*cf_bw*hops #cost is proportional to the number of hops
        revenue += vlink["bw"]*cf_bw*5*1.5 #(5:se cobra considerando el max num de hops permitido y 1.5: un 50% adicional al cost con 5hops)

    if nslr.end_time > end_simulation_time:
        #si es mayor, se considera la porcion de tiempo hasta acabar la simulacao  
        time = nslr.operation_time - (nslr.end_time-end_simulation_time)
    else:
        time = nslr.operation_time

    # print servie type and priority 
    # print("[SERVICE TYPE]", nslr.service_type, "[PRIORITY]", service_type_priority[nslr.service_type])
    cost_check = (nslr.end_time - nslr.incoming_time) * service_type_priority[nslr.service_type]

    #10 unit penalty -> -10
    #-10 -> -1 -> 1 unit penalty 
    #TODO: [Ipsita] Check output with our old reward function modification [100, 240 iterations]
    # reward = (revenue - (cost + cost_check)) * time
    profit = (revenue-cost)*time
    reward = - cost_check
    return reward, profit


#number of hops less: So profit for those links are less 
def calculate_request_utilization(nslr,end_simulation_time,substrate):
    vnfs = nslr.nsl_graph_reduced["vnodes"]
    vlinks = nslr.nsl_graph_reduced["vlinks"]
    time = 0.0
    central_sum = 0
    edge_sum = 0
    bw_sum = 0 
    
    for vnf in vnfs:
        if vnf["type"] == 0:#central
            central_sum += vnf["cpu"]
        elif vnf["type"] == 1:#edge
            edge_sum += vnf["cpu"]

    for vlink in vlinks:
        bw_sum += vlink["bw"]      

    if nslr.end_time > end_simulation_time:
        #si es mayor, se considera la porcion de tiempo hasta acabar la simulacion  
        time = nslr.operation_time - (nslr.end_time-end_simulation_time)
    else:
        time = nslr.operation_time

    edge_utl = edge_sum*time
    central_utl = central_sum*time
    links_utl = bw_sum*time  

    return edge_utl, central_utl, links_utl
