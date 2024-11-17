# Illinois Real Estate Price Prediction: A Machine Learning and Data Mining Approach

## 1. Introduction
We are Jan Aguiló, Pol Bonet, Pau Chaves and Aniol Petit, from the Mathematical Engineering in Data Science degree at Universitat Pompeu Fabra (UPF). We are really excited to have participated in this edition of the Datathon FME (2024) and proud of the project we have worked on. Huge thanks to Restb.ai for providing us with their real-world challenge in the real estate industry, which we found really interesting.

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

## 4. Process
The workflow involved the following steps:
# Real Estate Property Price Prediction in Illinois

## 1. Description
We are Jan Aguiló, Pol Bonet, Pau Chaves and Aniol Petit, from the Mathematical Engineering in Data Science degree at Universitat Pompeu Fabra (UPF). We are really excited to have participated in this edition of the Datathon FME (2024) and proud of the project we have worked on. Huge thanks to Restb.ai for providing us with their real-world challenge in the real estate industry, which we found really interesting.

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

## 4. EDA (Exploratory Data Analysis)
The workflow involved the following steps:
### 1. Data Preprocessing:
In this step, which is the most crucial one when dealing with this type of projects, we will integrate processes such as data cleaning, data integration, data selection and data transformation. 
#### 1.1 Dropping Unnecessary Features
- Characteristics.LotFeatures: taking into account this variable could lead to data inconsistency due to the difficulty to transform to numerical form given the high amount of NaN values, which is 60%.
- Characteristics.LotSizeSquareFeet: we agreed to drop this feature since 98% of the values are missing. Even though we think it’s one of the most interesting aspects to consider for predicting the price of the house, it’s mandatory for us to delete.
- Location.Address.PostalCodePlus4: 97% of NaN values, impossible to impute since would lose lots of information.
- Location.Address.UnparsedAddress: very difficult to deal with in terms of transforming to numerical. Better have each of the features in separate columns.
- Location.Address.StreetDirectionPrefix: doesn’t make any sense to rely on the prefix or suffix of the street direction of the house. +50% of NaN values.
- Location.Address.StreetDirectionSuffix: same. 99% NaN values.
- Location.Address.StreetSuffix: we dropped it after seeing that it had a very weak correlation with our target feature and concluded it was not relevant.
- Location.Address.StreetNumber: by having the postal code we already have a potential acknowledgement of how the prices are going to go in that area.
- Listing.Dates.CloseDate: completely irrelevant since all the bought dates are just between 10 months, so there won't be a significant increase/decrease in the properties price in such a thin range of time.
- Location.Address.StateOrProvince: we are in the state of Illinois so it is irrelevant since all of the properties have the same value here.
- Location.GIS.Latitude: this is categorical data that is so hard to convert to some valuable numerical information. Furthermore, this is information whose value can be extracted from other existing features as postal code, so we can prescind of this. 
- Location.GIS.Longitude: same as above.
- Location.Address.UnitNumber: 77% of Nan values, very difficult to impute.
- Location.Area.SubdivisionName: categorical values difficult to convert and 66% of NaN values.
- Location.School.HighSchoolDistrict: we calculated scores, saw that the model gave less accuracy and that correlation wasn’t very relevant.
- Structure.BelowGradeFinishedArea: not enough info and +85% of NaN values.
- Structure.BelowGradeUnfinishedArea: same
- Structure.ParkingFeatures: 87% of NaN values so it gets very difficult to impute values for it.
- Tax.Zoning: 93% NaN values
- UnitTypes.UnitTypeType: 95% of NaN values.
- Location.Address.City: we can get it by the postal code, redundant
- Location.Address.CountyOrParish: same
- ImageData.style.exterior.summary.label: we had 42 different unique values and 25% NaN. Transforming it into numerical values given these data could lead to inconsistency in our data.
- Location.Address.StreetName: we can get it by the suffix.
- Structure.Heating: irrelevant, most of the houses have heating supply and it doesn’t make a difference.
#### *1.2 Removing Biased Rows
In this step, we deleted the 3.97% (4%) of our rows, which is equivalent to
deleting 6688 rows. We decided to use a threshold of ⅓ (approx and after already removing the unnecessary features), that is, removing the rows that have 10 or more NaN values across their features since then it will be very hard to impute the values and gain solid information from there.

*After doing that and delivering the first submission through Discord, we noticed that this was wrong and that we weren’t able to delete rows since when running the Restb.ai model it would lead to an error due to row size difference. So we had to go back and leave these changes as they were initially, with the whole 107438 rows. 

#### 1.3 Categorical → Numerical and Imputing NaN values
- ImageData.c1c6.summary.” ” & ImageData.q1q6.summary.” ”: since all the features of this type have a range of NaN values between [10-15%] except for the property summary that only has 1%, we reached the conclusion that we must impute all the blanks with the median (more representative than the mean since the median is not affected by extreme values) of the other rows.
- ImageData.features_reso.results & ImageData.room_type_reso.results: here we compute the length of the list in order to convert it to numerical.
- ImageData.style.stories.summary.label: we extracted numeric values from labels (1, 2, 3, 1.5 and 2.5), imputed missing values with the median, and capped higher values at 3.
- Location.Address.PostalCode: we calculated the mean Listing.Price.ClosePrice by postal code, then normalised these values to a range of 0 to 1 using MinMaxScaler. Then we merged PostalCode_Score back into the dataset, by replacing the original postal code column (dropped). We tried to improve this approach by computing the scores based on a real dataset of incomes based on the postal code, however after some submissions we realised that it didn’t really improve accuracy and the model performed better with the other approach, so we kept the initial proposal.
- Location.Address.CensusBlock: We used the same normalised method as before to  convert the feature from categorical to numerical and being able to use it in our model.
  * Location.Address.CensusTract: we also calculated scores, but we saw that the model gave less accuracy and that correlation wasn’t very relevant.
- Property.PropertyType: here we applied one–hot encoding and we added the encoded columns to the dataset, of course removing the original column then.
- Structure.Basement: we transformed into binary (1 if basement exists, 0 otherwise), using both Structure.Basement and ImageData.room_type_reso.results.
- Structure.BathroomsFull & Structure.BathroomsHalf: here we created a new feature TotalBathrooms as a weighted sum of both features and then dropped the original columns.
- Structure.BedroomsTotal: imputed null values by computing the median of the others.
- Structure.Cooling: transformed into binary (1 if cooling exists, 0 otherwise). Use ImageData.features_reso.results to look for cooling instances to determine if some null value had an instance of cooling to set to 1. Otherwise we set the nulls to 0.
- Structure.FireplacesTotal: we applied the same methods as in the Structure.Cooling column.
- Structure.GarageSpaces: we imputed missing values within groups (Property.PropertyType) using the median; for groups with no data, imputed using the global median.
- Structure.LivingArea: imputed missing values by computing the mean of the others. 
- Structure.NewConstructionYN: imputed by using the construction year (True if built after 2020).
- Structure.Rooms.RoomsTotal: filled the missing values based on the sum of bedrooms, bathrooms and an additional 2 rooms (kitchen, living room).
- Structure.YearBuilt: filled missing values with the median, calculated PropertyAge (CurrentYear – YearBuilt), and then dropped the original column.
- Listing.Price.ClosePrice: of course, leave as it is since it is our target label. 
	
	*We tend to use the median since it is not affected by extreme values (outliers), unlike the mean, which can be skewed by very high or very low values. 










