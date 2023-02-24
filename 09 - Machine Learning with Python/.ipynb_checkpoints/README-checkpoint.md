# Course #9: Machine Learning with Python
<p align="center">
    <img src = "machine-learning-with-python.png">
</p>

## Project: [Rainfall in Australia Classification Project](https://github.com/collinbashore/IBM-Data-Science-Professional-Certification/blob/main/09%20-%20Machine%20Learning%20with%20Python/Rainfall%20Machine%20Learning%20Project.ipynb)
### Project Overview
This project utilizes four classification algorithms used to predict wether it'll rain tomorrow (the next day) or not using the dataset from the Daily Weather Observation page on the Australian Government's Bureau of Meteorology website. Based on the four different classification algorithms used, the **Logistic Regression** performs the best and presents the highest accuracy that it'll rain the next day.

### About the Dataset
The original source of the data is Australian Government's Bureau of Meteorology and the latest data can be gathered from [http://www.bom.gov.au/climate/dwo/](http://www.bom.gov.au/climate/dwo/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01).

Link to dataset: [Weather_Data.csv](https://github.com/collinbashore/IBM-Data-Science-Professional-Certification/blob/main/09%20-%20Machine%20Learning%20with%20Python/Weather_Data.csv)

The dataset contains observations of weather metrics for each day from 2008 to 2017. This dataset includes the following field:

| Field         | Description                                           | Unit            | Type   |
| ------------- | ----------------------------------------------------- | --------------- | ------ |
| Date          | Date of the Observation in YYYY-MM-DD                 | Date            | object |
| Location      | Location of the Observation                           | Location        | object |
| MinTemp       | Minimum temperature                                   | Celsius         | float  |
| MaxTemp       | Maximum temperature                                   | Celsius         | float  |
| Rainfall      | Amount of rainfall                                    | Millimeters     | float  |
| Evaporation   | Amount of evaporation                                 | Millimeters     | float  |
| Sunshine      | Amount of bright sunshine                             | hours           | float  |
| WindGustDir   | Direction of the strongest gust                       | Compass Points  | object |
| WindGustSpeed | Speed of the strongest gust                           | Kilometers/Hour | object |
| WindDir9am    | Wind direction averaged of 10 minutes prior to 9am    | Compass Points  | object |
| WindDir3pm    | Wind direction averaged of 10 minutes prior to 3pm    | Compass Points  | object |
| WindSpeed9am  | Wind speed averaged of 10 minutes prior to 9am        | Kilometers/Hour | float  |
| WindSpeed3pm  | Wind speed averaged of 10 minutes prior to 3pm        | Kilometers/Hour | float  |
| Humidity9am   | Humidity at 9am                                       | Percent         | float  |
| Humidity3pm   | Humidity at 3pm                                       | Percent         | float  |
| Pressure9am   | Atmospheric pressure reduced to mean sea level at 9am | Hectopascal     | float  |
| Pressure3pm   | Atmospheric pressure reduced to mean sea level at 3pm | Hectopascal     | float  |
| Cloud9am      | Fraction of the sky obscured by cloud at 9am          | Eights          | float  |
| Cloud3pm      | Fraction of the sky obscured by cloud at 3pm          | Eights          | float  |
| Temp9am       | Temperature at 9am                                    | Celsius         | float  |
| Temp3pm       | Temperature at 3pm                                    | Celsius         | float  |
| RainToday     | If there was rain today                               | Yes/No          | object |
| RISK_MM       | Amount of rain tomorrow                               | Millimeters     | float  |
| RainTomorrow  | If there is rain tomorrow                             | Yes/No          | float  |


The link to the column definitions can be found here: [http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml](http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01)

### Machine Learning Algorithms Used
Below are the list of classification algorithms used in this project:
1. Logistic Regression
2. K Nearest Neighbors
3. Decision Tree
4. Support Vector Machines

### Overview of the Classification Metrics used
1. **Jaccard Index** <br>
The Jaccard Index, commonly referred to as the Jaccard similarity coefficient, is a statistic used to determine how similar two sample sets are to one another. The measurement, which stresses similarity between finite sample sets, is officially defined as the intersection's size divided by the sample sets' union's size. Below is the formula used to calculate the Jaccard Index:

![Jaccard Index](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.Fur1nVsTmxDRn3LBLiQyNgHaB_%26pid%3DApi&f=1&ipt=75c39c709b29b8d7e4f8a1274a84a06958bbb787e00d640ced47d660303eb7bd&ipo=images)
Image source: [jaccard index](https://deepai.org/machine-learning-glossary-and-terms/jaccard-index)

Where set A is the "true" values of the target variable ($y$) and set B are the predicted target values ($\hat{y}$).

The values of the Jaccard Index are between 0 and 1. A higher value of the Jaccard Index will provide the highest accuracy.  

2. **F1-score** <br>
The F1 score is a statistical measure of a test's accuracy calculated from the model's precison and recall. It can be thought of as a harmonic mean of precision and recall, with the best value being 1 and the poorest being 0. Precision and recall both contribute equally in terms of percentage to the F1 score.

$F1-Score = 2 * \frac{precision  *  recall}{precision  +  recall}$

Values of the F1 score range from 0 to 1, with 1 providing the highest accuracy with precision and recall being perfect.

3. **Accuracy Score** <br>
The accuracy score can be thought of as the number of True Positives(TP) + the number of True Negatives(TN) divided by the sample size.

Accuracy score = (TP + TN) / sample size

4. **Log loss (only used for Logistic Regression)** <br>
The performance of a classifier where the projected output is a probability value between 0 and 1 is measured by logarithmic loss (log loss). The model with the lowest value of log loss has the highest accuracy.

### Results
| Algorithm               | Log Loss | Accuracy Score | Jaccard Index | F1 Score |
|-------------------------|----------|----------------|---------------|----------|
| Logistic Regression     | 5.484063 | 0.841221       | 0.527273      | 0.690476 |
| K-Nearest Neighbours    | NaN      | 0.818321       | 0.425121      | 0.596610 |
| Decision Tree           | NaN      | 0.749618       | 0.392593      | 0.563830 |
| Support Vector Machines | NaN      | 0.719084       | 0.000000      | 0.000000 |

**Notes on Results Above**<br>
From the results above, the **Logistic Regression** classification model performed better since the model has the highest Accuracy (84.12%), Jaccard Index (0.527), and F1 Score (0.690) than the other three models used.

## Appendix: Linear Regression (Why does it not work for Classification)

The submission of this project required that I'd perform a Linear Regression. The problem with using Linear Regression as a Classification Algorithm is that Linear Regression requires that the values of the target variable are continuous. SInce the target variable (RainTomorrow) only consists of 0s and 1s and are discrete, this will improperly fit the model.

Below is an example of the scatter plot that attempts to perform Linear Regression on the data points.

<p align="center">
    <img src="https://github.com/collinbashore/IBM-Data-Science-Professional-Certification/blob/main/09%20-%20Machine%20Learning%20with%20Python/Regression%20Plot%20Rainfall%20vs%20Rain%20Tomorrow.JPG">
</p>

From the plot above, it's obvious that the fitted line DOES NOT fit the model since the data points are not scattered evenly around the fitted line. Thus, it's improper to use the Linear Regression Algorithm for solving a Classification Problem!

Since the assignment required that I perform a linear Regression model, let's see what the results are like using the same features and target variable defined in this project. 

### Results of Linear Regression

| Algorithm         | Mean Absolute Error | Mean Squared Error | R-Squared |
|-------------------|---------------------|--------------------|-----------|
| Linear Regression | 0.256319            | 0.115723           | 0.427121  |

According to the above metrics, there seems to be roughly a 43% variation of the RainTomorrow classifier that can be explained by the amount of Rainfall on a particular day. 

Again, since the data points are not evenly scattered aroud the fitted regression line, the metrics above are not useful to use.