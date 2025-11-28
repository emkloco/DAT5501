import numpy as np
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def main():
    # grabbing the data from the uci repository
    print("fetching data...")
    car_evaluation = fetch_ucirepo(id=19)
    X = car_evaluation.data.features
    y = car_evaluation.data.targets

    # the features are categories (like 'vhigh', 'low'), so we need to encode them
    # otherwise the math won't work
    print("encoding features...")
    encoder = OneHotEncoder(sparse_output=False)
    X_encoded = encoder.fit_transform(X)

    # same for the target column ('unacc', 'acc'), turning them into numbers
    le = LabelEncoder()
    y_encoded = le.fit_transform(y.values.ravel())

    # standard 70/30 split. using stratify to make sure we keep the same balance of classes
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded
    )

    print(f"data ready. features shape: {X_train.shape}")

    # --- optimization loop ---
    
    # we want to find the best depth for the tree.
    # if it's too shallow, it learns nothing. if it's too deep, it memorizes everything (overfitting).
    depths = range(1, 20)
    precisions = []
    recalls = []
    f1_scores = []
    train_accuracies = [] 

    print("training trees at different depths...")

    for depth in depths:
        # train a fresh tree at this specific depth
        clf = DecisionTreeClassifier(max_depth=depth, random_state=42)
        clf.fit(X_train, y_train)
        
        # test it on data it hasn't seen before
        preds = clf.predict(X_test)
        
        # calculate metrics. using 'weighted' average because the classes aren't balanced
        precisions.append(precision_score(y_test, preds, average='weighted', zero_division=0))
        recalls.append(recall_score(y_test, preds, average='weighted'))
        f1_scores.append(f1_score(y_test, preds, average='weighted'))
        
        # check how well it memorized the training data
        # if this is 100% but the test score is low, we are definitely overfitting
        train_preds = clf.predict(X_train)
        train_accuracies.append(accuracy_score(y_train, train_preds))

    # --- plotting the results ---
    
    plt.figure(figsize=(12, 6))
    plt.plot(depths, precisions, label='Precision', marker='o', linestyle='--')
    plt.plot(depths, recalls, label='Recall', marker='s', linestyle='--')
    plt.plot(depths, f1_scores, label='F1 Score', linewidth=3, marker='^') # making f1 thicker since it's our main metric
    plt.plot(depths, train_accuracies, label='Training Accuracy', color='grey', alpha=0.5)

    plt.xlabel('Tree Depth')
    plt.ylabel('Score (0.0 - 1.0)')
    plt.title('Optimisation: F1 Score vs Tree Depth')
    plt.legend()
    plt.grid(True)
    plt.xticks(depths) 
    plt.tight_layout()

    print("graph generated. close the window to see feature importance...")
    plt.show()

    # --- feature importance ---
    
    # training one final model at depth 12 (based on the graph, this is usually the sweet spot)
    final_clf = DecisionTreeClassifier(max_depth=12, random_state=42)
    final_clf.fit(X_train, y_train)

    # figuring out which factors actually matter for car safety
    importances = final_clf.feature_importances_
    feature_names = encoder.get_feature_names_out(X.columns)

    # sorting from most impactful to least
    indices = np.argsort(importances)[::-1]

    print("\n" + "="*40)
    print("TOP 5 MOST IMPORTANT FEATURES")
    print("="*40)
    for i in range(5):
        print(f"{i+1}. {feature_names[indices[i]]}: {importances[indices[i]]:.4f}")
    print("="*40)

if __name__ == "__main__":
    main()