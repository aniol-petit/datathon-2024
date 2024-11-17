# Real Estate Property Price Prediction in Illinois

## 1. Description
We are a team of four students from the Mathematical Engineering in Data Science program at Universitat Pompeu Fabra (UPF)—Pau, Aniol, Pol, and Jan. This project was developed as part of the Datathon FME 2024 where restb.ai presented real-world challenge in the real estate industry.

The goal of the challenge was to build an Automated Valuation Model (AVM) to predict property prices in Illinois, primarily in the Chicago metropolitan area, using historical data and property features. AVMs are crucial tools for real estate agents, allowing them to estimate the best possible selling price for a property based on available data.

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