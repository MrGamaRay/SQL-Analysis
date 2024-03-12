**Solar Panel Production Data Cleaning and Analysis**

**Introduction**

This Python project focuses on cleaning and analyzing data related to the monthly production of solar panels. The dataset consists of two sheets: "Data" and "Monthly Expected Production". The goal of this project is to prepare the data for further analysis by cleaning, correcting, and filling missing values.

**Steps**

Read the Data: The project reads the "Data" and "Monthly Expected Production" sheets into their own separate DataFrames for processing.

Remove Duplicate Systems: Any systems with duplicate Meter Serial Numbers are removed from the dataset.

Correct System Size: System sizes less than 2.0 kW are corrected to 2.0 kW.

Set Negative Production Values to 0.0: Any negative daily production values are set to 0.0 kWh.

Fill Missing Daily Production Values: For each system, missing daily production values are filled in using the Monthly Expected Production divided by the number of days in that month as the fill-in value.

Calculate Monthly Production: Monthly production for each system is calculated, taking into account the changes made in the previous steps.

**Power BI Visualization Insights**

The Power BI visualizations provide valuable insights for a Solar Energy company looking to understand their monthly production for the year 2023:

Top Producers: Florida, New Jersey, California, and Nevada were the top producers of solar energy in 2023, indicating favorable conditions for solar energy production in these states.

Total and Average Production: The company had a total production of 18.30 million KW and an average production of 1.53 million KW in 2023.

Seasonal Pattern: Production starts peaking in April and declines in September, with the highest production months being May, June, July, and August. This suggests a seasonal pattern influenced by factors like weather conditions and daylight hours.

Potential Growth Areas: States like Texas, Louisiana, and Arizona, which are not among the top producers currently, could see an increase in systems, indicating a potential growth area for solar energy adoption.

Coastal Proximity: The highest-producing states are located near the coast, suggesting that proximity to the coast could play a role in solar energy production, possibly due to weather patterns or environmental factors.

**Usage**

To use this project, follow these steps:

Clone the repository to your local machine.

Install the required dependencies using pip install -r requirements.txt.

Ensure your input Excel file (Sunnova_Production_2023.xlsx) is in the project directory.

Run the main.py script to clean and analyze the data.

View the cleaned and analyzed data in the output Excel file (Sunnova_Programming_Test_Edson_Gamma.xlsx).

**Dependencies**

pandas

numpy

**Files**

main.py: Python script for cleaning and analyzing the data.

Sunnova_Production_2023.xlsx: Input Excel file containing the original data.

Sunnova_Programming_Test_Edson_Gamma.xlsx: Output Excel file containing the cleaned and analyzed data.

**Acknowledgements**

This project was created by Edson Gama for the purpose of cleaning and analyzing solar panel production data and providing business insights based on the data.
