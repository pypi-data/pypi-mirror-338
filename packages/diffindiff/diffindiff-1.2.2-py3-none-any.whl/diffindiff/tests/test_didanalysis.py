#-------------------------------------------------------------------------------
# Name:        test_didanalysis (diffindiff)
# Purpose:     Tests for function in the didanalysis module
# Author:      Thomas Wieland (geowieland@googlemail.com)
# Version:     1.2.0
# Last update: 2025-03-25 19:23
# Copyright (c) 2025 Thomas Wieland
#-------------------------------------------------------------------------------

import pandas as pd
from diffindiff.didanalysis import did_model, did_analysis

Corona_Hesse=pd.read_excel("data/Corona_Hesse.xlsx")
# Test data effective reproduction number and Corona NPI Hesse
# Data source: Wieland (2024) https://doi.org/10.1007/s10389-024-02218-x

Hesse_model1=did_analysis(
    data=Corona_Hesse,
    unit_col="REG_NAME",
    time_col="infection_date",
    treatment_col=["Nighttime_curfew"],    
    outcome_col="R7_rm"
    )
# Model with staggered adoption (FE automatically)

Hesse_model1.summary()
# Model summary

fixed_effects_regions=Hesse_model1.fixef()[0]
print (fixed_effects_regions.head())
fixed_effects_time=Hesse_model1.fixef()[1]
print (fixed_effects_time.head())
# Printing fixed effects

Hesse_model1.plot(
    y_label="R_t (mean by group)",
    plot_title="Nighttime curfews in Hesse - Treatment group vs. control group",
    plot_observed=True
    )
# Plot of treatment vs. control group (observed and expected) over time

Hesse_model1.plot_counterfactual()
# Plot of treatment group fit and counterfactual

Hesse_model1.plot_timeline(
    y_label="Hessian counties",
    plot_title="Nighttime curfews in Hesse - Treatment time",
    treatment_group_only=False
    )
# Plot timeline of intervention by region

Hesse_model2 = did_analysis(
    data = Corona_Hesse,
    unit_col = "REG_NAME",
    time_col = "infection_date",
    treatment_col = "Nighttime_curfew",
    outcome_col = "R7_rm",
    ITT = True
    )
# same model but including region-specific time trends (ITT=True)

Hesse_model2.summary()
# Model summary

Hesse_model2.plot(
    y_label = "R_t (mean by group)",
    plot_title = "Nighttime curfews in Hesse - Treatment group vs. control group",
    plot_observed=True
    )
# Plot of effects of Hesse_model2

Hesse_model3 = did_analysis(
    data = Corona_Hesse,
    unit_col = "REG_NAME",
    time_col = "infection_date",
    treatment_col = "Nighttime_curfew",
    outcome_col = "R7_rm",
    ITE = True
    )
# Model with individual treatment effects (ITE=True)

Hesse_model3.summary()

Hesse_model3.plot(plot_observed=True)

Hesse_model3.plot_individual_treatment_effects()

Hesse_model3.plot_individual_treatment_effects(
    sort_by="coef",
    x_label="Treatment effect (Reduction in R_t)",
    y_label="Hessian counties with nighttime curfew",
    plot_title="Individual treatment effects of nighttime curfews in Hesse",
    treatment_group_only=True,
    show_central_tendency=True
    )
# Plot individual treatment effects of Hesse_model3

Hesse_model4=did_analysis(
    data=Corona_Hesse,
    unit_col="REG_NAME",
    time_col="infection_date",
    treatment_col=["Nighttime_curfew", "Mobility_restrictions"],    
    outcome_col="R7_rm"
    )
# Model with two interventions (both staggered adoption)

Hesse_model4.summary()
# Model summary