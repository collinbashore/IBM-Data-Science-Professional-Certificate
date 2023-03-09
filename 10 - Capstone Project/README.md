# Course #10: [Applied Data Science Capstone](https://github.com/collinbashore/IBM-Data-Science-Professional-Certification/blob/main/10%20-%20Capstone%20Project/Data-Science-Capstone-Collin.pdf)

<p align="center">
    <img src = "https://github.com/collinbashore/IBM-Data-Science-Professional-Certification/blob/main/10%20-%20Capstone%20Project/Data%20Sciecne%20Capstone%20Project%20Cover%20Slide.JPG">
</p>

## Project Overview
During the existing commercial space age, companies such as Blue Orgin and Starlink are wanting to make space travel more afforadable for everyone. Space X, compared to other companies, conducts the most expensive launches (62 million USD vs. 165 million USD). This is because Space X is able to recover rocket parts during Stage One landings.

A space company, called Space Y, wants to compete with Space X to dtrain a machine learning model to predict successful Stage One recovery. If there appears to be a high amount of successful landings, Space Y could use the model to predict whether a launch will have successful Stage One landing before determining whether a launch should be made or not.

### Project Tasks
- **Week 1:** [Data Collection, Web Scraping, and Data Wrangling](https://github.com/collinbashore/IBM-Data-Science-Professional-Certification/tree/main/10%20-%20Capstone%20Project/Week%201%20Data%20Cleaning%20-%20Webscraping%20-%20Data%20Wrangling)
    - Data Collection via Space X API
    - Data Collection vis Web Scraping
    - Data Wrangling
        - Converting categorical columns by one hot encoding
        - Converting numeric columns to float64 data type
- **Week 2:** [Exploratory Data Analysis](https://github.com/collinbashore/IBM-Data-Science-Professional-Certification/tree/main/10%20-%20Capstone%20Project/Week%202%20Exploratory%20Data%20Analysis)
    - EDA via SQL (via Python-SQL integration)
    - EDA via Data Visualization
- **Week 3:** [Interactive Visual Analytics and Dashboard](https://github.com/collinbashore/IBM-Data-Science-Professional-Certification/tree/main/10%20-%20Capstone%20Project/Week%203%20Visual%20Analytics%20and%20Interactive%20Dashboards)
    - Interactive Maps via Folium
    - Interactive Dashboard via Plotly Dash
- **Week 4:** [Predictive Analytics (Classification)](https://github.com/collinbashore/IBM-Data-Science-Professional-Certification/tree/main/10%20-%20Capstone%20Project/Week%204%20Predictive%20Analytics%20(Classification))
    - Machine Learning using Classification Algorithms
    - Used GridSearchCV to determine the ideal parameters using standardized dataset.
- **Week 5:** [Presentation on Data-Driven Insights](https://github.com/collinbashore/IBM-Data-Science-Professional-Certification/blob/main/10%20-%20Capstone%20Project/Data-Science-Capstone-Collin.pdf)
    - Created a PowerPoint presentation highlighting the entire process of this project by providing snapshots of SQL queries, flowcharts of the data collection and wrangling process, and data visualizations.
    - Type of Audience for the presentation: Technical audience 
## Results

- There are a total of **three** unique launch sites that are relatively located close to coastlines and relatively far from cities. 

- FT Booster Version had the most successful landings (13 of 15) with payload mass range of 2,000 to 5,500 kg.

- KSC LC-39A launch site has highest success rate of 41.7%

- Rockets surrounding the orbits ES-L1, GEO, HEO, and SSO had the highest average success rates

- There are no rockets lauch for heavy payload mass (greater than 10,000 kg) in the VAFB-SLC launch site.

- Four machine learning models were used for predictive analysis: Logistic Regression, Support Vector Machines, Decision Tree Classifier, and K Nearest Neighbors (KNN). All models (except for KNN – 77.78%) produced similar results around 83.33% accuracy rate. All models over predicted true successful landings.

- More data will be required for better model determination (dataset used had only 90 records) since the test dataset only has 18 samples.
