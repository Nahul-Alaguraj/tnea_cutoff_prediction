📊 TNEA College Cutoff Predictor and Recommender System
This project provides an exploratory analysis, visualization, and machine learning-based recommendation system using TNEA cutoff data from 2022 to 2024. It includes:

🧹 Cleaned and structured historical cutoff data.

📈 Exploratory Data Analysis (EDA) and Tier classification.

🤖 An LSTM model to predict future cutoffs.


📁 Dataset
The dataset was scraped from tneaonline.org for the years 2022, 2023, and 2024. Each record includes:

College Name, College Code

Branch Name, Branch Code

Cutoffs for categories: OC, BC, BCM, MBC, SC, SCA, ST

Year of the data

🧼 Data Cleaning
All rows with missing (NaN) or invalid (***, *) cutoffs are removed.

Only colleges with valid OC cutoff values are retained for ML model training.

Pivoted into time-series format (e.g., [2022, 2023, 2024] per college-branch).

📊 Exploratory Data Analysis (EDA)
Distribution of cutoffs by category and year.

Tier classification:

Tier 1: All branches have median OC cutoff ≥ 180

Tier 2: Most cutoffs between 170–180

Tier 3: Best branches in 160s, lowest ~150

Tier 4: Below 150 or low reputation/fill rate

Pie charts, box plots, and heatmaps were used to visualize trends.

🧠 Machine Learning Model: LSTM
A Long Short-Term Memory (LSTM) network was trained to predict OC cutoff for 2024 based on historical trends (2022 and 2023).

Input: OC cutoffs for each College–Branch for past years

Output: Predicted 2024 OC cutoff

Features scaled with MinMaxScaler

Performance evaluated via MSE, R², and actual vs predicted plots

📌 Future Enhancements

Build college ranking system using overall cutoff difficulty and popularity.

Extend to include seat matrix, placement stats, or counseling simulations.

🤝 Contributing
Feel free to raise issues or submit pull requests if you'd like to enhance the models or app!

📜 License
This project is open-source under the MIT License.
