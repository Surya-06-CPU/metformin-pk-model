# 1 Compartmental PK Model: Metformin IR

This project utilizies Python to simulate and track blood plasma concentration of Metformin Immediate-Release (IR/Oral Tablet) over a 48-hour period. Built upon a 1-compartmental pharmacokinetic (PK) model, this simulation applies an IV bolus assumption to mathematically model drug distribution and decay. This script specifically analyzes a regimen of the starting dose being 500 mg administered every 12 hours to evaluate drug accumulation against standard clinical therapeutic windows.

# Clinical Context

Metformin is a primary pharmacological treatment for Type 2 Diabetes, but maintaining the correct plasma concentration is critical for patient safety and efficacy:

* Sub-Therapeutic (Too Low): If plasma levels fall below the average therapeutic window (< 0,5 mg/L), the patient experiences inadequate glycemic control, which can lead to hyperglycemia and progressively worse diabetic complications.

* Toxicity (Too High): Excessive accumlation of the drug risks Metformin-Associated Lactic Acidosis (MALA). This is a severe, life threatening medical emergency triggered when blood pH drops below 7.35 and lactic acid levels cross 5 mmol/L.

This computational model visualizes the balance required to keep a patient safely within the established therapeutic window (0.5 - 2.0 mg/L (may depend on conditions))

# The Computational Tools

To accurately model the pharmacokinetics of Metformin progression, this project leveraged Python and standard computing libraries such as:

* Mathematical Modeling: Utilizes 'sciypy.integrate.odeint' to solve the ordinary differential equations (ODE) representing first-order drug elimination.

* Dose Accumulation Logic: Implements a loop structure to simulate repeated dosing intervals, accurately calculating the current drug concentration remaining from previous doses.

* Data Visualization: Uses 'matplotlib.pyplot' to generate a clinical graph, complete with a visual therapeutic window overlay for instant diagnostic feedback and visual cue.

* Automated Clinical Readout: Simple print statements extract and display critical clinical data, specifically the Peak and Trough plasma concentration, directly to the terminal.

# Clinical Findings

![Metformin Graph](metformin_decay.png) 

Running the simulation with the standard 500 mg dose every 12 hours yields the following insights:

* Sub-Therapeutic Maintenance: The peak blood plasma concentration reaches approximately 0.52 mg/L, barely scratching the minimum of the therapeutic window of 0.5 - 2.0 mg/L. The trough concentration drops to 0.10 mg/L, meaning the patient is unmedicated throughout most of the day.

* The Validation of "Starting Dose": This model perfectly shows why 500 mg twice a day is generally prescribed as a starting dose to study tolerance to and adapt to the gastrointestinal system.

* Titration Requirement: To achieve true homeostasis and keep the trough levels safely inside the therapeutic window as regimen advances, the doses must be titrated up to 850 mg ~ 1000 mg twice a day.

# How to Run the Simulation

1. Install Libraries:

Ensure you have Python installed, then install the required scientific libraries by running the following command in a selected terminal:

* MAC/LINUX - `pip3 install numpy scipy matplotlib`
* WINDOWS -`pip install numpy scipy matplotlib`

2. Execute the Script:

Run the Python file from your terminal to view the readout listed on the terminal and to generate the graph:

* MAC/LINUX - `python3 metformin_pk_model.py`
* WINDOWS - `python metformin_pk_model.py`

3. Adjusting Parameters: 

To simulate different patient regimens, open `metformin_pk_model.py` and proceed to modify the `dose_mg` and `dosing_interval` variables.