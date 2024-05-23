# ConductivityPrediction
Predicting conductivity of various salt solutions

First set the parameters in "main.py", then run the program.
Solute parameters are formatted like this:
{"cat":"Na","z_cat":1,"v_cat":1,"an":"Cl","z_an":-1,"v_an":1,"lambda_cat":50.08,"lambda_an":72.31}
- z is the charge number for the ion
- v is the number of moles of ion per mole of electrolyte
- lambda is the conductivity at infinite dilution

-----
assym_conduct and Simple_conduct are backend code, don't edit them.
assym_conduct  is for asymmetrical electrolytes, and was developed following the paper "EVALUATION OF THE SOLUBILITY OF ELECTROLYTES FROM CONDUCTIVITY MEASUREMENTS" by R. FERNANDEZ-PRINI and J-C. JUSTICE

Simple_conduct is for symmetrial electrolyes, it's not really used cause assym_conduct covers everything. It is based on the paper "Predicting Electrolyte Conductivity Directly from Molecular-Level Interactions" by Yumin Zhang, Imanuel Bier, and Venkatasubramanian Viswanathan