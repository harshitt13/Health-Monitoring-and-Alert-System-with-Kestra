import torch
import torch.nn as nn
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import json
import matplotlib.pyplot as plt

# Create a class for the LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_layers):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        _, (hidden, _) = self.lstm(x)
        return self.fc(hidden[-1])
        
#Initialize the model, loss function and optimizer
model = LSTMModel(input_dim=2, hidden_dim=64, output_dim=2, num_layers=2)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Load the data from the JSON file
with open('patient_data.json', 'r') as f:
    patient_data = json.load(f)

# Assuming the data is a list of sequences and labels
train_inout_seq = []
for item in patient_data:
    try:
        seq = torch.tensor([float(x) for x in item[0]], dtype=torch.float32).unsqueeze(0)
        label = torch.tensor(float(item[1]), dtype=torch.float32)
        train_inout_seq.append((seq, label))
    except ValueError as e:
        print(f"Skipping item due to error: {e}")

# Train the model
epoch = 100
for i in range(epoch):
    for seq, labels in train_inout_seq:
        optimizer.zero_grad()
        y_pred = model(seq)
        single_loss = criterion(y_pred, labels)
        single_loss.backward()
        optimizer.step()
    if i % 25 == 1 and 'single_loss' in locals():
        print(f'epoch: {i:3} loss: {single_loss.item():10.8f}')

#save the model
torch.save(model.state_dict(), 'lstm_model.pth')
print('Model saved')
