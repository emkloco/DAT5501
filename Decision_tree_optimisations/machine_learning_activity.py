import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

# 1. FETCH THE DATA
print("Fetching data...")
car_evaluation = fetch_ucirepo(id=19)
X = car_evaluation.data.features
y = car_evaluation.data.targets

# 2. ENCODE THE DATA (Thursday's Task)
# The features are categorical, so we use OneHotEncoder [cite: 400]
print("Encoding features...")
encoder = OneHotEncoder(sparse_output=False)
X_encoded = encoder.fit_transform(X)

# The target ('unacc', 'acc', etc.) also needs to be numbers for metrics to work
le = LabelEncoder()
y_encoded = le.fit_transform(y.values.ravel())

# 3. SPLIT THE DATA
# Standard 70/30 split [cite: 98]
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded
)

print("Data ready. Features shape:", X_train.shape)

# --- PASTE THIS AT THE BOTTOM OF YOUR FILE ---

# 4. OPTIMISATION: FIND THE BEST TREE DEPTH
# Lists to store scores for plotting
depths = range(1, 20)
precisions = []
recalls = []
f1_scores = []
train_accuracies = [] # To check for overfitting

print("Training trees at different depths...")

for depth in depths:
    # Initialize and train the tree
    clf = DecisionTreeClassifier(max_depth=depth, random_state=42)
    clf.fit(X_train, y_train)
    
    # Predict on test data
    preds = clf.predict(X_test)
    
    # Calculate scores (using 'weighted' because we have 4 classes: unacc, acc, good, vgood)
    precisions.append(precision_score(y_test, preds, average='weighted', zero_division=0))
    recalls.append(recall_score(y_test, preds, average='weighted'))
    f1_scores.append(f1_score(y_test, preds, average='weighted'))
    
    # Check training accuracy (if this is 1.0 but test score is low, it's overfitting)
    train_preds = clf.predict(X_train)
    train_accuracies.append(accuracy_score(y_train, train_preds))

# 5. PLOT THE RESULTS
plt.figure(figsize=(12, 6))
plt.plot(depths, precisions, label='Precision', marker='o', linestyle='--')
plt.plot(depths, recalls, label='Recall', marker='s', linestyle='--')
plt.plot(depths, f1_scores, label='F1 Score', linewidth=3, marker='^') # Make F1 thicker
plt.plot(depths, train_accuracies, label='Training Accuracy', color='grey', alpha=0.5)

plt.xlabel('Tree Depth')
plt.ylabel('Score (0.0 - 1.0)')
plt.title('Optimisation: F1 Score vs Tree Depth')
plt.legend()
plt.grid(True)
plt.xticks(depths) # Show all depth numbers on x-axis
plt.tight_layout()

print("Close the graph window to see the Feature Importance...")
plt.show()

# 6. FEATURE IMPORTANCE
# Train a final model at a "good" depth (e.g., 12 is usually good for this dataset)
final_clf = DecisionTreeClassifier(max_depth=12, random_state=42)
final_clf.fit(X_train, y_train)

# Extract importance scores
importances = final_clf.feature_importances_
# Get the names of the encoded columns (e.g., 'safety_low', 'buying_high')
feature_names = encoder.get_feature_names_out(X.columns)

# Sort them from most to least important
indices = np.argsort(importances)[::-1]

print("\n" + "="*40)
print("TOP 5 MOST IMPORTANT FEATURES")
print("="*40)
for i in range(5):
    # Print: 1. Feature Name: 0.4532
    print(f"{i+1}. {feature_names[indices[i]]}: {importances[indices[i]]:.4f}")
print("="*40)