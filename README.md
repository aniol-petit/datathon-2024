# Illinois Real Estate Price Prediction: A Machine Learning and Data Mining Approach

## 1. Introduction
We are Jan Aguiló, Pol Bonet, Pau Chaves and Aniol Petit, from the Mathematical Engineering in Data Science degree at Universitat Pompeu Fabra (UPF). We are really excited to have participated in our first datathon, the edition of the Datathon FME (2024), and we are proud of the project we have worked on. Huge thanks to Restb.ai for providing us with their real-world challenge in the real estate industry, which we found really interesting.

To put you into context, the main goal of the challenge was to build an Automated Valuation Model (AVM) so as to predict property prices in the state of Illinois using historical data and property features. As we have seen during the process, AVMs are crucial tools for real estate agents, allowing them to estimate the best possible selling price for a property based on available data.

## 2. Dataset
The dataset consists of real estate properties in Illinois for the last year, segmented into:

Train Dataset (train.csv): Data from the first 10 months (September 2023 to July 2024).
Test Dataset (test.csv): Data from the last 2 months (August 2024 and September 2024).

### Fields Description

The dataset for this challenge is sourced from three primary data origins—Image Data, Listing Data, and Census Data—and includes real estate properties located in select counties of Illinois, USA. The timeline spans from July 2023 to August 2024, with the last two months reserved for validation.

#### 1. Image Data:

Provided by Restb.ai, this data is derived from photos of properties.
It includes insights such as the condition (ImageData.c1c6) and quality (ImageData.q1q6) of the house, both summarized into scores.

**Note**: The photos used to generate these features are not provided as part of the dataset.

#### 2. Listing Data:

Sourced from Midwest Real Estate Data (MRED), this dataset includes detailed property listings of recently sold houses.
Key attributes include:
- Listing.ListingId: Unique identifier for each property.
- Listing.Price.ClosePrice: Final selling price (our target variable for prediction).
- Structural details such as Structure.LivingArea, TotalBathrooms, and Structure.BedroomsTotal.
- Location-related fields like Location.Address.City and Location.Address.CensusBlock.
#### 3. Census Data:

Derived from the US Census Bureau API, this data enriches listings with geographical and socioeconomic insights, including:
- Location.Address.CensusBlock and Location.Address.CensusTract: Key identifiers for census regions.
- Location.GIS.Latitude and Location.GIS.Longitude: Geographical coordinates of the properties.


## 3. Challenge
The goal is to create an AVM capable of predicting the most accurate property prices, providing:

A CSV submission based on the test dataset with:
- Listing.ListingId: Unique identifier for each property.
- Listing.Price.ClosePrice: Predicted sale price.
  
The evaluation metrics include:
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
The winning solution is not solely based on the best metrics but also on:
Depth of data analysis, justification of decisions, supported by data.

## 4. Files Description
<ul>
 <li>**data_cleaning.ipynb**: Jupyter notebook where we performed the Exploratory Data Analysis. We used different cells to handle every different feature</li> 
 <li>**training_model.ipynb**: Jupyter notebook where we trained our machine learning model and evaluated its performance</li> 
  <li>**REPORT**: pdf file where we explain every decision we made for handling the data processing, choosing the model, etc.</li>
</ul>









