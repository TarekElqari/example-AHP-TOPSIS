import numpy as np
import ahp
import topsis
import visualise

# Example dataset representing performance of cars on each criterion
# Rows: Criteria (Price, Fuel Efficiency, Safety Rating)
# Columns: Cars (Car 1, Car 2, Car 3)
dataset = np.array([
    [30000, 25000, 35000],  # Price ($) - Lower is better
    [30, 35, 25],            # Fuel Efficiency (miles per gallon) - Higher is better
    [4.5, 5.0, 4.8]          # Safety Rating (out of 5) - Higher is better
])

# Criterion type: 'min' for price, 'max' for fuel efficiency and safety rating
criterion_type = ['min', 'max', 'max']

# Apply AHP method to determine weights of criteria
weights, consistency_ratio = ahp.ahp_method(dataset)
print("AHP Weights:", weights)
print("Consistency Ratio:", consistency_ratio)

# Apply TOPSIS method to rank alternatives
c_i = topsis.topsis_method(dataset, weights, criterion_type)
print("TOPSIS Scores:", c_i)

# Visualize the ranking
flow = np.copy(c_i)
flow = np.reshape(flow, (c_i.shape[0], 1))
flow = np.insert(flow, 0, list(range(1, c_i.shape[0]+1)), axis=1)
flow = flow[np.argsort(flow[:, 1])]
flow = flow[::-1]
visualise.ranking(flow)
