# 5. Economic and Environmental Impact Analysis

## 5.1 Economic Effects
The economic impact analysis examines the potential consequences of future petroleum consumption and domestic production trends in India. The forecasts are used to estimate the domestic supply-demand gap, petroleum import dependency, import expenditure, and per-capita petroleum consumption.
These indicators help evaluate India's future reliance on external petroleum supplies and understand how increasing domestic demand may affect the country's economic requirements.

### 5.1.1 Domestic Supply-Demand Gap
The domestic supply-demand gap represents the difference between projected petroleum consumption and projected domestic petroleum production.
It is calculated as:
$$
Supply\ Gap_t = C_t-P_t
$$

Where:
$(C_t)$ represents forecasted petroleum consumption in year (t).
$(P_t)$ represents forecasted domestic petroleum production in year (t).


A positive supply gap indicates that domestic production is insufficient to satisfy projected consumption, suggesting a requirement for petroleum imports.
A negative supply gap indicates that projected domestic production exceeds consumption, implying a potential domestic surplus.
The calculated supply gap is visualized using a line plot to observe how the difference between domestic demand and production is expected to evolve over the forecast period. A horizontal reference line at zero is included to distinguish between surplus and deficit conditions.

![1793625904963](image/Documentation/1793625904963.png)

### 5.1.2 Projected Petroleum Import Dependency

Import dependency measures the proportion of domestic petroleum consumption that cannot be satisfied through domestic production.
It is calculated using:
$$
Projected\ Dependency_t =
\frac{\max(0,C_t-P_t)}{C_t}\times100
$$

Where:
$(C_t)$ represents forecasted petroleum consumption.
$(P_t)$ represents forecasted domestic petroleum production.

The maximum function ensures that import dependency does not become negative when domestic production exceeds consumption.
A higher dependency percentage indicates greater reliance on external petroleum supplies, potentially increasing the country's exposure to international oil price fluctuations, geopolitical uncertainties, and disruptions in global petroleum supply chains.
The projected dependency is visualized using a line plot to examine how India's potential dependence on petroleum imports changes throughout the forecast period.

![1793625921464](image/Documentation/1793625921464.png)

### 5.1.3 Projected Petroleum Import Expenditure

Petroleum import expenditure represents the estimated financial cost associated with importing petroleum to meet domestic requirements.
It is calculated as:
$$
Import\ Bill_t =
Net\ Import\ Quantity_t
\times Import\ Price_t
$$

Where:
Net Import Quantity represents the forecasted petroleum import quantity.
Import Price represents the forecasted average petroleum import price.
The estimated import expenditure is converted into billion US dollars by dividing the calculated value by (10^9).
A bar chart is used to visualize the projected annual petroleum import bill. This helps identify potential increases or decreases in India's petroleum import expenditure over the forecast period.
An increasing import bill may result from higher import quantities, rising international petroleum prices, or a combination of both factors.
This indicator is particularly important because petroleum imports represent an economic burden and can influence India's trade balance and foreign exchange requirements.

![1793625939106](image/Documentation/1793625939106.png)

### 5.1.4 Per-Capita Petroleum Consumption
Per-capita petroleum consumption measures the average petroleum consumption per person in a given year.
It is calculated as:
$$
Per\ Capita\ Consumption_t =
\frac{C_t}{Population_t}
$$

Where:
$(C_t)$ represents forecasted petroleum consumption.
$(Population_t)$ represents the projected population.

This indicator helps understand how petroleum consumption changes relative to population growth.
An increasing per-capita consumption trend may indicate rising energy requirements associated with economic development, industrialization, transportation activities, and changing consumption patterns.
The projected values are visualized using a line plot to examine the expected changes in average petroleum consumption per person.

![1793625951112](image/Documentation/1793625951112.png)

## 5.2 Environmental Impact Analysis

Petroleum consumption has significant environmental implications because the combustion of petroleum products releases carbon dioxide (CO₂) into the atmosphere.
The environmental impact analysis estimates future CO₂ emissions associated with projected petroleum consumption. It also examines emissions relative to population and petroleum consumption to understand the potential environmental implications of increasing petroleum demand.

### 5.2.1 Forecasted CO₂ Emissions
The projected CO₂ emissions are estimated using the petroleum consumption forecasts and an emission factor.
The calculation is based on:
$$
E_i = C_i \times 1000 \times EF_i
$$

Where:
$(E_i)$ represents the estimated CO₂ emissions of petroleum product (i), measured in tonnes of CO₂.
$(C_i)$ represents petroleum consumption in kilotonnes.
$(EF_i)$ represents the emission factor, expressed in tonnes of CO₂ per tonne of petroleum.

The factor 1000 converts kilotonnes into tonnes.
An emission factor of 3.10059 is used in the calculation.
The emissions are subsequently converted into million tonnes of CO₂ by dividing the estimated values by (10^6).
A line plot is generated to visualize the projected annual CO₂ emissions over the forecast period.
This analysis provides an indication of the potential environmental consequences of future petroleum consumption trends. Increasing petroleum consumption, assuming a constant emission factor, results in increasing estimated CO₂ emissions.

![1793625969378](image/Documentation/1793625969378.png)

### 5.2.2 Per-Capita CO₂ Emissions

Per-capita CO₂ emissions represent the average estimated CO₂ emissions attributable to each individual.
They are calculated as:
$$
CO_2\ Per\ Capita_t =
\frac{E_t}{Population_t}
$$

Where:

$(E_t)$ represents forecasted annual CO₂ emissions.
$(Population_t)$ represents projected population.

This indicator helps evaluate how average emissions per person may change over time.
Unlike total emissions, per-capita emissions account for population growth and provide a population-adjusted measure of environmental impact.
The projected values are visualized using a line plot to identify potential changes in average CO₂ emissions per person.
An increasing trend may indicate that petroleum-related emissions are growing faster than the population, while a decreasing trend may indicate a reduction in average emissions per person.

![1793625981255](image/Documentation/1793625981255.png)

### 5.2.3 Emission Intensity of Petroleum Consumption

Emission intensity measures the amount of CO₂ emitted per unit of petroleum consumed.
It is calculated as:
$$
Emission\ Intensity_t =
\frac{E_t}{C_t}
$$

Where:
$(E_t)$ represents forecasted CO₂ emissions.
$(C_t)$ represents forecasted petroleum consumption.

This indicator helps understand the relationship between petroleum consumption and its associated carbon emissions.
The emission intensity is visualized using a line plot to examine whether the estimated emissions per unit of petroleum consumption change throughout the forecast period.
A relatively stable emission intensity indicates that emissions are increasing proportionally with petroleum consumption. Changes in emission intensity may indicate variations in the petroleum product composition or emission factors, provided those factors are allowed to vary.
Since a constant emission factor is used in the current analysis, the emission intensity is expected to remain approximately constant.

![1793625991533](image/Documentation/1793625991533.png)

## 5.3 Summary of Economic and Environmental Indicators

The economic and environmental analyses provide complementary perspectives on the implications of India's projected petroleum consumption and production trends.
The economic indicators help assess:
Domestic Supply-Demand Gap: Identifies the potential difference between domestic petroleum requirements and production capacity.
Import Dependency: Estimates the proportion of petroleum consumption that cannot be met through domestic production.
Import Expenditure: Evaluates the potential financial burden associated with petroleum imports.
Per-Capita Consumption: Examines average petroleum consumption relative to population.
The environmental indicators help assess:
Total CO₂ Emissions: Estimates future petroleum-related carbon emissions.
Per-Capita CO₂ Emissions: Examines average emissions relative to population.
Emission Intensity: Measures the estimated carbon emissions associated with each unit of petroleum consumption.
Together, these indicators provide a broader understanding of the potential economic and environmental implications of India's future petroleum requirements. They also highlight the importance of strengthening domestic energy security, managing import dependency, and exploring cleaner and more sustainable energy alternatives.

