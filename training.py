import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle

# Load your .csv here
df = pd.read_csv("dataset.csv")
X = df[["a","b","c"]] # put your X factor here !!
y = df["g"] # Put your Y factor here !!


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


model = LinearRegression()
model.fit(X_scaled, y)

# Saves your model to .pkl files
with open("prediction_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model and Scaler Saved.")
