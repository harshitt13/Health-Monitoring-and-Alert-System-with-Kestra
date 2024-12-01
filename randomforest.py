from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model(data):

    # Train a machine learning model on the input data.
    # Critical levels: heart rate > 120 or glucose_level > 180

    data['critical'] = ((data['heart_rate'] > 120) | (data['glucose_level'] > 180)).astype(int)
    X = data[['heart_rate', 'glucose_level']]
    y = data['critical']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model to a file
    with open('health_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model trained and saved successfully.")

def load_model():
    # Load the trained ML model from a file."
    with open('health_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def predict_critical_levels(model, heart_rate, glucose_level):
    # Predict whether the input levels are critical.
    return model.predict([[heart_rate, glucose_level]])[0]
