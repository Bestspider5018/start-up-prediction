Start-Up Profitability Predictor 

This project predicts whether a start-up is profitable or not based on various features like funding round, funding amount, valuation, revenue, market share, industry, and exit status.

Requirements

1.Python 3.x
2.Streamlit
3.Scikit-learn
4.Numpy
5.Pickle

pip install -r requirements.txt

Features

Predicts the profitability of a start-up based on:

 1.Funding Round
 2.Funding Amount
 3.Valuation
 4.Revenue
 5.Market Share
 6.Industry
 7.Exit Status

User-friendly interface built with Streamlit

Input Details

1.Funding Round: Integer value between 1 and 5.
2.Funding Amount: Float value (0.50 to 300.0).
3.Valuation: Float value (2.5 to 4500.0).
4.Revenue: Float value (0.10 to 100.0).
5.Market Share: Float value (0.10 to 10.0).
6.Industry: Select from a list of common start-up industries.
7.Exit Status: Select the current exit status of the start-up.


├── model
│   ├── ordinal.pkl
│   ├── scaler.pkl
│   └── grid.pkl
├── notebook
│   └── eda.ipynb
├── app.py
├── requirements.txt
└── README.md
