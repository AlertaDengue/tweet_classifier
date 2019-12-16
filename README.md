# tweet classifier
Classification model for tweets aiming at predicting dengue, zika and chikungunya.

# Main files
## Scripts
* classifier: 
* keyword_retrieval.ipynb: gets all possible variations (mispellings) for word chikungunya.
* exploratory_analysis.ipynb: build visualizations for the data (years 2016-2018).
* anvil_data_builder.ipynb: builds data (in JSON format) which feeds the anvil app for people to classify each tweet.
* dengue-2012: Old notebook which tries to predict dengue by using UFMG database (from 2010-2018, doesn't contain extended_text) and old classification model. It should be kept as reference. What it does: simulates predictions over the year 2012, uses TF (TF-IDF doesn't work because each text sample is too long as it comprises tweets over a whole week), gets most important features (using Lasso and Random Forest), applies Machine Learning (just linear model as a baseline).

Database notebooks:
* file_manager.ipynb: fixes dengue.json.bz2 (which had a parsing error), building the dengue_fixed.json.bz2. Then it inserts all relevant data into a MongoDB collection. Warning: special characters had to be removed in order for the fix to work properly.

## Databases
* dengue.json.bz2: main database from UFMG, with all variables. This database has a parsing error and had to be fixed.
* dengue_fixed.json.bz2: fixed from previous database. Warning: special characters had to be removed in order for the fix to work properly.
* mongo_ufmg_filtered (folder): MongoDB collection containing only relevant variables from previous file.
* amostra.tgz: UFMG database (from 2010-2018, doesn't contain extended_text)
* tweets_anvil_input.json': input for anvil app.