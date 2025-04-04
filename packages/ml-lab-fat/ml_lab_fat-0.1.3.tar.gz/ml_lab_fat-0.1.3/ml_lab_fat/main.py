def show_options():
    options = {
        1: """import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

file_path = '/content/drive/My Drive/letterdata.csv'
df = pd.read_csv(file_path)
x = df.iloc[:,1:]
y = df.iloc[:,0]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
gnb = GaussianNB()
gnb.fit(x_train, y_train)
y_pred = gnb.predict(x_test)
y_pred_train = gnb.predict(x_train)
accuracy = accuracy_score(y_test, y_pred) * 100
print(f"Accuracy score for testing: {accuracy}")
accuracy_train = accuracy_score(y_train, y_pred_train)*100
print(f"Accuracy score for testing: {accuracy_train}")""",
        2: """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('/content/drive/My Drive/data.csv')
x = df.iloc[:,2:]
y = df.iloc[:,1]
y = LabelEncoder().fit_transform(df["diagnosis"])

plt.figure(figsize = (12, 8))
plot_tree(dtc, feature_names = df.columns[1:], class_names = ["B", "M"], filled = True)
plt.title("Decision Tree")
plt.show()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
dtc = DecisionTreeClassifier(criterion= "gini", random_state = 42)
dtc.fit(x_train, y_train)
y_pred = dtc.predict(x_test)
accuracy = accuracy_score(y_test, y_pred) * 100

print(f"Accuracy score for testing: {accuracy}")
print(f"Accuracy score for testing: {accuracy}")
""",
        3: """import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split;
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC

file_path = '/content/drive/My Drive/letterdata.csv'
df = pd.read_csv(file_path)
x = df.iloc[:, 1:].values
y = df.iloc[:, 0].values
y_encoded = LabelEncoder().fit_transform(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42, stratify = y_encoded)
linear_svm = SVC(kernel = "linear", random_state = 42)
linear_svm.fit(x_train, y_train)
y_pred = linear_svm.predict(x_test)
y_pred_train = linear_svm.predict(x_train)
accuracy = accuracy_score(y_test, y_pred) * 100
print(f"Accuracy score for testing: {accuracy}")
accuracy_train = accuracy_score(y_train, y_pred_train)*100
print(f"Accuracy score for testing: {accuracy_train}")
""",
        4: """import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split;
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC

file_path = '/content/drive/My Drive/letterdata.csv'
df = pd.read_csv(file_path)
x = df.iloc[:, 1:].values
y = df.iloc[:, 0].values
y_encoded = LabelEncoder().fit_transform(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42, stratify = y_encoded)
rbf_svm = SVC(kernel = "rbf", random_state = 42)
rbf_svm.fit(x_train, y_train)
y_pred = rbf_svm.predict(x_test)
y_pred_train = rbf_svm.predict(x_train)
accuracy = accuracy_score(y_test, y_pred) * 100
print(f"Accuracy score for testing: {accuracy}")
accuracy_train = accuracy_score(y_train, y_pred_train)*100
print(f"Accuracy score for testing: {accuracy_train}")""",
        5: """import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('/content/drive/My Drive/Iris.csv')

encoder = LabelEncoder()
df['Species'] = encoder.fit_transform(df['Species'])

features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
x = df[features]
y = df['Species']

dtree = DecisionTreeClassifier()
dtree.fit(x, y)

plot_tree(dtree, feature_names=features, class_names=encoder.classes_, filled=True)
""",
        6: """import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

# Load data
file_path = "/content/drive/My Drive/University_Clustering.csv"
df = pd.read_csv(file_path)

# Convert 'Expenses' column to integer after removing commas
df["Expenses"] = df["Expenses"].astype(str).str.replace(",", "").astype(int)

# Select features
features = ["SAT", "Top10", "Accept", "SFRatio", "Expenses", "GradRate"]

# Standardize data
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df[features]), columns=features)

# Finding the optimal k using silhouette score
silhouette_scores = []
k_values = range(2, 16)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10, max_iter=500)
    kmeans.fit(df_scaled)
    silhouette_scores.append(silhouette_score(df_scaled, kmeans.labels_))

# Best k based on silhouette score
best_k = k_values[silhouette_scores.index(max(silhouette_scores))]

# Final K-Means model
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10, max_iter=500)
df["Cluster"] = kmeans.fit_predict(df_scaled)

# Clustering evaluation metrics
silhouette = silhouette_score(df_scaled, df["Cluster"])
# Print evaluation metrics
print(f"Optimal k: {best_k}")
print(f"Silhouette Score: {silhouette:.4f}")""",
        7: """import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

filePath = '/content/drive/My Drive/letterdata.csv'
data = pd.read_csv(filePath, header=0)

scaler = StandardScaler()

X = data.drop(columns=["letter"])
y = LabelEncoder().fit_transform(data["letter"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Accuracy : {accuracy * 100:.2f} % ")
print("Classification Report: ")
print(report)""",
8: """ import numpy as np 
learningRate = 0.1 
epochs = 1000 
bias = 1 
w1 = 0 
w2 = 0 
x1 = [0 , 0 , 1 , 1] 
x2 = [0 , 1 , 0 , 1] 
y1 = [0 , 0 , 0 , 1]
 def activationFunction(y): 
if(y > 0): 
return 1;
 return 0;
 def calculateFunc(x1 , x2 , w1 , w2 , b): 
ans = x1*w1 + x2*w2 + b 
return activationFunction(ans); 
def updateWeights(w1 , w2 , b , x1 , x2 , y1 , y2): 
w1 += learningRate*(y1 - y2)*x1 
w2 += learningRate*(y1 - y2)*x2 
b += learningRate * (y1 - y2) 
return (w1 , w2 , b)
 while(epochs): 
tell = False 
for a , b , c in zip(x1 , x2 , y1): 
y2 = calculateFunc(a , b , w1 , w2 , bias) 
if y2 != c: 
tell = True 
(w1, w2 , bias) = updateWeights(w1 , w2 , bias , a , b , c , y2) 
break 
if tell == False: 
print("Objective Reached!"); 
print("W1 is : " , w1 , " W2 is : " , w2 , " bias is : " , bias) 
break 
else: 
print(epochs) 
epochs -= 1 
if(epochs == 0): 
print("No answer")
""",

9: """ import pandas as pd
 import numpy as np
 from sklearn.model_selection import train_test_split
 from sklearn.preprocessing import LabelEncoder, StandardScaler
 from sklearn.metrics import accuracy_score, classification_report
 file_path = "/home/anaconda/Desktop/data.csv"  # Use raw string or double backslashes
 data = pd.read_csv(file_path)
 data_cleaned = data.drop(['id', 'Unnamed: 32'], axis=1)
 label_encoder = LabelEncoder()
 data_cleaned['diagnosis'] = label_encoder.fit_transform(data_cleaned['diagnosis'])
 X = data_cleaned.drop('diagnosis', axis=1).values
 y = data_cleaned['diagnosis'].values.reshape(-1, 1)  # Reshape for matrix operations
 scaler = StandardScaler()
 X_scaled = scaler.fit_transform(X)
 X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
 input_size = X_train.shape[1]
 hidden_size = 10  # Number of neurons in the hidden layer
 output_size = 1  # Binary classification
 learning_rate = 0.01
 epochs = 50
 np.random.seed(42)  # For reproducibility
 weights_input_hidden = np.random.randn(input_size, hidden_size)
 bias_hidden = np.zeros((1, hidden_size))
 weights_hidden_output = np.random.randn(hidden_size, output_size)
 bias_output = np.zeros((1, output_size))
 def relu(x):
    return np.maximum(0, x)
 def relu_derivative(x):
    return np.where(x > 0, 1, 0)
 def sigmoid(x):
    return 1 / (1 + np.exp(-x))
 def sigmoid_derivative(x):
    return x * (1 - x)
 for epoch in range(epochs):
    # Forward Propagation
    hidden_layer_input = np.dot(X_train, weights_input_hidden) + bias_hidden
    hidden_layer_output = relu(hidden_layer_input)
    final_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    final_layer_output = sigmoid(final_layer_input)
    error = y_train - final_layer_output
    loss = np.mean(np.square(error))  # Mean Squared Error
    output_gradient = error * sigmoid_derivative(final_layer_output)
    hidden_gradient = np.dot(output_gradient, weights_hidden_output.T) * 
relu_derivative(hidden_layer_output)
    weights_hidden_output += learning_rate * np.dot(hidden_layer_output.T, output_gradient)
    bias_output += learning_rate * np.sum(output_gradient, axis=0, keepdims=True)
    weights_input_hidden += learning_rate * np.dot(X_train.T, hidden_gradient)
    bias_hidden += learning_rate * np.sum(hidden_gradient, axis=0, keepdims=True)
    if epoch % 50 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.6f}")
 # Prediction function
 def predict(X):
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = relu(hidden_layer_input)
    final_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    final_layer_output = sigmoid(final_layer_input)
    return (final_layer_output > 0.5).astype(int)  # Convert probabilities to class labels
 y_pred = predict(X_test)
 accuracy = accuracy_score(y_test, y_pred)
 report = classification_report(y_test, y_pred, target_names=['Benign', 'Malignant'])
 print(f'\nFinal Accuracy: {accuracy * 100:.2f}%')
 print('Classification Report:\n', report)""",

 10: """import pandas as pd 
import numpy as np from sklearn.model_selection 
import train_test_split from sklearn.preprocessing 
import LabelEncoder, StandardScaler from sklearn.linear_model 
import Perceptron from sklearn.metrics 
import accuracy_score, classification_report 
data = pd.read_csv("") 
data_cleaned = data.drop(['id', 'Unnamed: 32'], axis=1) 
label_encoder = LabelEncoder() 
data_cleaned['diagnosis'] = label_encoder.fit_transform(data_cleaned['diagnosis']) 
X = data_cleaned.drop('diagnosis', axis=1) 
y = data_cleaned['diagnosis'] 
scaler = StandardScaler() 
X_scaled = scaler.fit_transform(X) 
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42) 
weights = np.zeros(X_train.shape[1]) 
bias = 0 
learning_rate = 0.01 
n_iterations = 10000 
for _ in range(n_iterations): 
for xi, target in zip(X_train, y_train): 
linear_output = np.dot(xi, weights) + bias 
prediction = 1 if linear_output >= 0 else 0 
error = target - prediction 
weights += learning_rate * error * xi 
bias += learning_rate * error 
y_pred = [] 
for xi in X_test: 
linear_output = np.dot(xi, weights) + bias 
prediction = 1 if linear_output >= 0 else 0 
y_pred.append(prediction) 
accuracy = accuracy_score(y_test, y_pred) 
report = classification_report(y_test, y_pred, target_names=['Benign', 'Malignant']) 
print("Weights:", weights) 
print("Bias:", bias) print(f'Accuracy: {accuracy * 100:.2f}%') 
print('Classification Report:\n', report)
""",

11: """import pandas as pd
df = pd.read_csv(“/home/Download/EnjoySport.csv”, header = None)
features = df.iloc[: , : , -1]
target = df.iloc[:, -1]
hypo = None
for i in range(len(target)):
	if target[i] == ‘Yes’:
		if hypo is None:
			hypo = featurers.iloc[i].tolist()
		else:
			for j in range(len(hypo)):
				if hypo[j] != features.iloc[i, j]:
					hypo[j] = ‘?’
print(hypo)
""",

12: """ import pandas as pd
 from sklearn.model_selection import train_test_split
 from sklearn.ensemble import AdaBoostClassifier
 from sklearn.tree import DecisionTreeClassifier
 from sklearn.preprocessing import LabelEncoder
 from sklearn.metrics import accuracy_score 
file_path = "/home/anaconda/Downloads/Iris.csv"
 df = pd.read_csv(file_path)
 if 'Id' in df.columns:
 df = df.drop(columns=['Id'])
 X = df.iloc[:, :-1]
 y = df.iloc[:, -1]
 label_encoder = LabelEncoder()
 y = label_encoder.fit_transform(y)
 X_train, X_test, y_train, y_test = train_test_split(X, y,
 test_size=0.2, random_state=42)
 ada_clf = AdaBoostClassifier(
 estimator=DecisionTreeClassifier(max_depth=1), 
 n_estimators=50,
 learning_rate=1.0,
 random_state=42
 )
 ada_clf.fit(X_train, y_train)
 y_train_pred = ada_clf.predict(X_train)
 y_test_pred = ada_clf.predict(X_test)
 train_accuracy = accuracy_score(y_train, y_train_pred) *
 100
 test_accuracy = accuracy_score(y_test, y_test_pred) *
 100
 print(f"AdaBoost Train Accuracy: {train_accuracy:.2f} %")
 print(f"AdaBoost Test Accuracy: {test_accuracy:.2f} %")""",
 13: """import pandas as pd
import numpy as np

data = pd.read_csv('Desktop/EnjoySport.csv', header=None)

features = data.drop(data.columns[-1], axis=1).values
target = data[data.columns[-1]].values

num_features = features.shape[1]
S = ['null'] * num_features
G = [['?'] * num_features]

for i, instance in enumerate(features):
    if target[i] == 'Yes':
        for j in range(num_features):
            if S[j] == 'null':
                S[j] = instance[j]
            elif S[j] != instance[j]:
                S[j] = '?'
        G = [g for g in G if all(g[k] == '?' or g[k] == S[k] for k in range(num_features))]

    elif target[i] == 'No':
        new_G = []
        for g in G:
            for j in range(num_features):
                if g[j] == '?':
                    if S[j] != '?':
                        new_hypothesis = g.copy()
                        new_hypothesis[j] = S[j]
                        if new_hypothesis not in new_G:
                            new_G.append(new_hypothesis)
        G = new_G

print(f"Specific Hypothesis (S): {S}")
print(f"General Hypotheses (G): {G}")
""",
14: """import numpy as np
 x1 = np.array([60, 62, 67, 70, 71, 72, 75, 78])
 x2 = np.array([22, 25, 24, 20, 15, 14, 14, 11])
 y = np.array([140, 155, 159, 179, 192, 200, 212, 215])
 mean_x1 = np.sum(x1)/len(x1)
 sum_x1 = np.sum(x1)
 mean_x2 = np.sum(x2)/len(x2)
 sum_x2 = np.sum(x2)
 mean_y = np.sum(y)/len(y)
 sum_y = np.sum(y)
 sq_x1 = np.sum(x1 * x1)
 sq_x2 = np.sum(x2 * x2)
 x1y = np.sum(x1 * y)
 x2y = np.sum(x2 * y)
 x1x2 = np.sum(x1 * x2)
 rsum_x1 = sq_x1 - sum_x1 * sum_x1/len(x1)
 rsum_x2 = sq_x2 - sum_x2 * sum_x2/len(x2)
 rsum_x1y = x1y - sum_x1 * sum_y / len(y)
 rsum_x2y = x2y - sum_x2 * sum_y / len(y)
 rsum_x1x2 = x1x2 - sum_x1 * sum_x2 / len(x1)
 b1 = (rsum_x2 * rsum_x1y - rsum_x1x2 * rsum_x2y)/(rsum_x1 * rsum_x2 - rsum_x1x2 * 
rsum_x1x2)
 b2 = (rsum_x1 * rsum_x2y - rsum_x1x2 * rsum_x1y)/(rsum_x1 * rsum_x2 - rsum_x1x2 * 
rsum_x1x2)
 b0 = mean_y - b1 * mean_x1 - b2 * mean_x2
 print(b1, b2, b0)
""",
15: """import pandas as pd
 import numpy as np
 from sklearn.model_selection import train_test_split
 from sklearn.linear_model import LinearRegression
 from sklearn.metrics import mean_squared_error
 data = pd.read_csv('MLMultipleRegression.csv')
 X = data[['x1', 'x2']]
 y = data['y']
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 model = LinearRegression()
 model.fit(X_train, y_train)
 y_pred = model.predict(X_test)
 mse = mean_squared_error(y_test, y_pred)
 print(model.summary())
 print(f'Mean Squared Error: {mse}')"""
    }

    print("Choose an option (1-10):")
    print("1: Naive Bayes")
    print("2: CART decision tree")
    print("3: Linear SVM")
    print("4: Non-linear SVM")
    print("5: Decision Tree")
    print("6: K means")
    print("7: KNN")
    print("8: Single layer perceptron")
    print("9: Multi layer perceptron")
    print("10: Single layer perceptron without AND")
    print("11: Find-S")
    print("12: Adaboost")
    print("13: Candidate Elimination")
    print("14: Linear Regression without package")
    print("15: Linear Regression with package")

    try:
        choice = int(input("Enter your choice: "))
        print()
        print()
        print()
        print(options.get(choice, "Invalid choice!"))
    except ValueError:
        print("Please enter a valid number!")

show_options()
