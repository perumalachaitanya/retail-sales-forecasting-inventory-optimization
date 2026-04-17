import numpy as np

def inventory_calc(forecast):
    lead_time = 7
    
    mean_demand = np.mean(forecast[:lead_time])
    std_demand = np.std(forecast[:lead_time])
    
    safety_stock = 1.65 * std_demand
    reorder_point = mean_demand + safety_stock
    
    return safety_stock, reorder_point