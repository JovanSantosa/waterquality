
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load the dataset
file_path = 'data_set_kualitas_air.csv'
data = pd.read_csv(file_path, delimiter=';')

# Replacing commas with dots in numeric columns if they are strings and converting them to floats
numeric_columns = ['pH', 'Temperature (°C)', 'Turbidity (NTU)', 'Conductivity (µS/cm)']
for col in numeric_columns:
    # Apply replacement only if the column has string values
    if data[col].dtype == 'object':
        data[col] = data[col].str.replace(',', '.').astype(float)
    else:
        data[col] = data[col].astype(float)

# Defining features and target variable
X = data[numeric_columns]  # Features: pH, Temperature, Turbidity, Conductivity
y = data['Kualitas Air']    # Target: Kualitas Air (Baik or Buruk)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing and training the Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Making predictions on the test set
y_pred = clf.predict(X_test)

# Evaluating the model's performance
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Checking the ranges for pH, Temperature, Turbidity, and Conductivity for "Baik" and "Buruk" classifications
# This will help identify ranges typically associated with each quality level.

# Splitting the dataset by quality type
baik_data = data[data['Kualitas Air'] == 'Baik']
buruk_data = data[data['Kualitas Air'] == 'Buruk']

# Calculating the min, max, and average values for each feature based on quality
baik_ranges = baik_data[numeric_columns].describe().loc[['min', 'max']]
buruk_ranges = buruk_data[numeric_columns].describe().loc[['min', 'max']]

baik_ranges, buruk_ranges

# Output the results
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:")
print(report)
print(baik_ranges)
joblib.dump(clf, 'model_kualitas_air.pkl')
