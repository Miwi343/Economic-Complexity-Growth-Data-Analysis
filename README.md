# Exploring the Impact of Public Data Transparency on Economic Complexity Index Growth (1995-2021)

## Project Overview

This project investigates whether there is a significant difference in economic complexity growth from 1995 to 2021 among countries with varying levels of public data transparency. The goal is to explore if government transparency with public data can lead to more complex and robust economic conditions. 

The analysis leverages data from the Harvard Atlas of Economic Complexity and the Open Data Barometer to examine the relationship between governmental data transparency and economic complexity. By clustering countries into different groups based on their transparency levels, this study compares the economic complexity growth trends and assesses the statistical significance of the observed differences.

## Key Features

- **Data Sources:** Utilizes the Harvard Atlas of Economic Complexity and the Open Data Barometer.
- **Clustering:** Countries are segmented into four groups based on data transparency ratings: High Capacity, Emerging & Advancing, Capacity Constrained, and One-Sided Initiatives.
- **Analysis:** Regression analysis and two-sample t-tests are conducted to compare economic complexity growth across clusters.
- **Tools:** Analysis performed using Python, Jupyter Notebook, and Sci-Kit Learn.

## Methodology

1. **Data Collection:** Economic Complexity Index (ECI) data from 1995 to 2021 and public data transparency ratings.
2. **Clustering:** Countries are clustered into four groups based on transparency ratings.
3. **Regression Analysis:** Individual regression lines are produced for each country's ECI growth.
4. **Statistical Testing:** A two-sample t-test is conducted to compare the slopes of ECI growth between the most contrasting clusters.

## Findings

- **High Capacity Countries:** Showed a general trend of slight negative slopes, indicating minor declines or stability in economic complexity.
- **One-Sided Initiative Countries:** Displayed slightly positive slopes, suggesting minimal growth in economic complexity.
- **Statistical Significance:** The two-sample t-test indicated a significant difference in economic complexity growth between the high transparency and low transparency clusters, although normality conditions were not fully met.

## Conclusion

The study highlights a nuanced relationship between public data transparency and economic complexity growth. While findings suggest that countries with higher data transparency might have different economic growth patterns compared to those with lower transparency, the results must be interpreted cautiously due to some statistical limitations. 

## Future Work

Future research could focus on alternative statistical methods to account for deviations from normality, and a more granular analysis of the types of data transparency and their direct effects on specific economic sectors.

## Author

Mihir Kulshreshtha
Thomas Jefferson High School for Science and Technology

## Acknowledgments

Special thanks to Dr. Catherine Scott for her guidance and support.
