import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# PHASE 1: CLINICAL PHARMACOKINETIC PARAMETERS
# Drug: Metformin IR (Oral Tablet)

# Patient & Dosing Parameters

dose_mg = 500.0  # mg, standard starting dose
bioavailability = 0.5  # 50%, oral bioavailability (F)
dosing_interval = 12.0  # hrs, twice a day dosage (every 12 hours)

# Pharmacokinetic Parameters
# average apparent volume of distribution in litres (Vd)

volume_distribution = 654.0
half_life = 6.2  # hours, plasma elimination half life

# Calculating elimination rate constant // k_e = ln(2) / half_life
# continious rate of decay (how much kindeys clear per hour)

k_e = np.log(2) / half_life

# PHASE 2: DIFFERENTIAL EQUATION ENGINE

# NOTE ON MODEL 1:
# This 1-Compartmental model treats the oral dose as an IV Bolus, assuming
# instantaneous absoprtion of the bioavaliable mass  at t=0. It simplifies
# the absoprtion phase (k_a) to strictly highlight the elimination kinetics
# (k_e) and steady-state accumulation. This can also fall under the
# superposition principle.

# First Order Kinetics
# dC/dt = -k_e * C (change in concentration over time equal to negative elimination rate multiplied by concentration (negative = leaving the body))


def calculate_decay(C, t, k_e):  # t second parameter according to scipy notation
    dC_dt = -k_e * C
    return dC_dt

# Calculating Initial Concentration when Metformin is ingested
# concentration = mass/volume and factor in bioavailability after oral ingestion


C0 = (dose_mg * bioavailability) / volume_distribution

# Evenly spaced time slots to run a timeline for our equation
# start at 0 hrs, end at 24 hrs, generate 100 evenly spaced data points in between

time_hours = np.linspace(0, 24, 100)

# Implementing Ordinary Differential Equation tool
# giving odeint function starting point and timeline #args is used to pass the elimination rate into this function

concentration_profile = odeint(calculate_decay, C0, time_hours, args=(k_e,))

# This assumes that once a dosage is taken, there not a second dosage for this time frame
# Implementing second dosage in 12 hour time frame

# PHASE 3: MULTI-DOSE STEADY STATE SIMULATION

# The time conditions for the multi-dose timeline

total_time = []
total_concentration = []

# The tracking variable (from the first pill)

current_C = C0

# The Multi-Dose loop (4 doses signifying 48 hours passed)
# Running the simulation for this chunk of data
# Storing the data in the timeline

for dose in range(4):
    # changed bounds of the 12 hour shift for each time interval from 0 to 48 hrs
    timeframe_time = np.linspace(
        (dose * dosing_interval), ((dose + 1) * (dosing_interval)), 100)
    # changed starting concentration and time interval
    timeframe_results = odeint(
        calculate_decay, current_C, timeframe_time, args=(k_e,))
    total_time.extend(timeframe_time)
    timeframe_results = timeframe_results.flatten().tolist()  # cleaning up the structure
    total_concentration.extend(timeframe_results)
    # concentration in the blood left over added to additional concentration from ingested pill
    current_C = C0 + total_concentration[-1]

# PHASE 4: CLINICAL SUMMARY REPORT

print("Metformin IR Simulation Results")  # header
# regimen for patient
print(
    f"The patient is taking a dosage of {dose_mg} every {dosing_interval} hours.")
print(f"The peak plasma concentration is {max(total_concentration):.2f}.")
print(f"The trough plasma concentration is {min(total_concentration):.2f}.")


# PHASE 5: DATA VISUALIZATION

plt.plot(total_time, total_concentration)  # line
# average therapeutic range for metformin IR is between 0.5 to 2.0 mg/L. rest are visualizing properties
plt.axhspan(0.5, 2.0, color="green", alpha=0.15, label="Therapeutic Window")
plt.title("Metformin Pharmacokinetic Decay (1-Compartment Model)")  # graph title
plt.xlabel("Time (hours)")  # x-axis title
plt.ylabel("Metformin Concentration (mg/L)")  # y-axis title
plt.grid(True)  # easier to read
# changing pop-up title and specifying resolution
plt.legend(loc="upper left")  # placing legend in the upper left of the graph
plt.show()  # displaying

# The reason for which the data barely scratches the therapeutic window is because what is being prescribed at the moment is the "starting dose".
# This also proves why a 500 mg dose twice a day is not a sufficient dosage for long term homeostasis.
# Most clinicians increase the dosage steadily to up to 850 mg to 1000 mg twice a day. This is roughly the maintenance dose that keeps them square in the therapeutic range.
# An extreme outcome of overdosing with around 2850 mg or greater of a dose a day is being diagnosed with Metformin-Associated Lactic Acidosis (MALA).
# MALA mostly stems from an acute trigger from the drug in the body, more can be about this condition in the README file.
