class Experiments:
    def __init__(self):
        self.codes = [
            """# Code Snippet 1\nprint("Hello from Exp 1!")""",
            """# Code Snippet 2\nprint("Hello from Exp 2!")""",
            """# Code Snippet 3\nprint("Hello from Exp 3!")""",
            """# Code Snippet 4\nprint("Hello from Exp 4!")""",
            """# Code Snippet 5\nprint("Hello from Exp 5!")""",
            """# Code Snippet 6\nprint("Hello from Exp 6!")""",
            """# Code Snippet 7\nprint("Hello from Exp 7!")""",
            """# Code Snippet 8\nprint("Hello from Exp 8!")""",
            """# Code Snippet 9\nprint("Hello from Exp 9!")""",
            """# Code Snippet 10\nprint("Hello from Exp 10!")""",
        ]

    def showall():
        print('''
exp1--------
import numpy as np
from scipy.spatial.distance import euclidean, cityblock, cosine, minkowski
from sklearn.metrics import jaccard_score

# Define vectors
x1, y1 = np.array([5, 2, 3]), np.array([4, 9, 2])
x2, y2 = np.array([4, 6, 3]), np.array([8, 5, 9])
x3, y3 = np.array([2, 4, 6]), np.array([4, 7, 3])
x_bin, y_bin = np.array([1, 1, 0, 1]), np.array([1, 0, 1, 1])
p_value = 3

# Compute similarity and distance measures
print(f"Euclidean Distance: {euclidean(x1, y1)}")
print(f"Manhattan Distance: {cityblock(x2, y2)}")
print(f"Cosine Similarity: {1 - cosine(x3, y3)}")
print(f"Jaccard Similarity: {jaccard_score(x_bin, y_bin)}")
print(f"Minkowski Distance (p={p_value}): {minkowski(x3, y3, p_value)}")

exp2-----------
import numpy as np
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load dataset and split
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Apply PCA and SVD
pca, svd = PCA(n_components=2), TruncatedSVD(n_components=2)
X_train_pca, X_train_svd = pca.fit_transform(X_train_scaled), svd.fit_transform(X_train_scaled)

# Print explained variance
print(f"Explained Variance Ratio (PCA): {pca.explained_variance_ratio_}")
print(f"Explained Variance Ratio (SVD): {svd.explained_variance_ratio_}")
print(f"Total Variance Explained by PCA: {pca.explained_variance_ratio_.sum():.2f}")
print(f"Total Variance Explained by SVD: {svd.explained_variance_ratio_.sum():.2f}")

# Simple 2-line plotting
plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1], c=y_train, cmap='viridis', alpha=0.7)
plt.show()
plt.scatter(X_train_svd[:, 0], X_train_svd[:, 1], c=y_train, cmap='coolwarm', alpha=0.7)
plt.show()


exp3-----------
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample dataset
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 4, 5],
    'item_id': [101, 102, 103, 101, 104, 105, 104, 101],
    'rating': [5, 4, 3, 5, 4, 2, 3, 4],
    'item_features': [
        "Action Adventure", "Romantic Comedy", "Action Thriller",
        "Action Adventure", "Sci-Fi Mystery", "Drama History",
        "Sci-Fi Mystery", "Action Adventure"
    ],
}

df = pd.DataFrame(data)

# User-Item Matrix
user_item_matrix = df.pivot(index='user_id', columns='item_id', values='rating').fillna(0)

# TF-IDF and Item Similarity
tfidf = TfidfVectorizer().fit_transform(df.drop_duplicates('item_id')['item_features'])
item_similarity = cosine_similarity(tfidf)

# Build User Profiles
user_profiles = {uid: np.dot(ratings, item_similarity) for uid, ratings in user_item_matrix.iterrows()}
print(user_item_matrix)
print(user_profiles)

# Recommend Items
for uid, profile in user_profiles.items():
    print(f"User {uid} → Recommended: {df['item_id'].iloc[np.argmax(profile)]}")

exp4-------------
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.DataFrame({
    'title': ["Toy Story", "Jumanji", "Grumpier Old Men", "Waiting to Exhale", "Father of the Bride"],
    'genres': ["Adventure Animation Children Comedy Fantasy", "Adventure Children Fantasy",
               "Comedy Romance", "Comedy Drama Romance", "Comedy"]
})

tfidf = TfidfVectorizer().fit_transform(movies['genres'])
similarity = cosine_similarity(tfidf)

def recommend(movie_title):
    idx = movies.index[movies['title'] == movie_title][0]
    return movies['title'][similarity[idx].argsort()[-3:-1][::-1]].tolist()

print("Movies similar to 'Jumanji':", recommend("Jumanji"))

exp5-------------------
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error

# Sample Data: User-Item Ratings
data = {
    'User': [1, 1, 1, 2, 2, 3, 3, 4, 4, 5],
    'Item': ['A', 'B', 'C', 'A', 'D', 'B', 'D', 'C', 'D', 'A'],
    'Rating': [5, 3, 4, 2, 4, 5, 3, 2, 5, 4]
}
df = pd.DataFrame(data)

# Create User-Item Matrix
user_item_matrix = df.pivot(index='User', columns='Item', values='Rating')

# Fill missing values with 0 (for similarity calculation)
user_item_matrix_filled = user_item_matrix.fillna(0)

# Compute Similarity Matrices
user_similarity = cosine_similarity(user_item_matrix_filled)
item_similarity = cosine_similarity(user_item_matrix_filled.T)

# Function to predict missing ratings using User-User CF
def predict_ratings_user_based(user_item_matrix, user_similarity):
    mean_user_rating = user_item_matrix.mean(axis=1).values.reshape(-1, 1)
    ratings_diff = (user_item_matrix - mean_user_rating).fillna(0)
    pred = mean_user_rating + user_similarity @ ratings_diff / np.abs(user_similarity).sum(axis=1).reshape(-1, 1)
    return pred

# Function to predict missing ratings using Item-Item CF
def predict_ratings_item_based(user_item_matrix, item_similarity):
    pred = user_item_matrix.fillna(0) @ item_similarity / np.abs(item_similarity).sum(axis=1)
    return pred

# Predict Ratings
user_pred = predict_ratings_user_based(user_item_matrix, user_similarity)
item_pred = predict_ratings_item_based(user_item_matrix, item_similarity)

# Convert to DataFrame
user_pred_df = pd.DataFrame(user_pred, index=user_item_matrix.index, columns=user_item_matrix.columns)
item_pred_df = pd.DataFrame(item_pred, index=user_item_matrix.index, columns=user_item_matrix.columns)

# Calculate RMSE for User-User CF
user_rmse = np.sqrt(mean_squared_error(user_item_matrix.fillna(0), user_pred_df.fillna(0)))

# Calculate RMSE for Item-Item CF
item_rmse = np.sqrt(mean_squared_error(user_item_matrix.fillna(0), item_pred_df.fillna(0)))

# Print Results
print(f"RMSE for User-User Collaborative Filtering: {user_rmse:.4f}")
print(f"RMSE for Item-Item Collaborative Filtering: {item_rmse:.4f}")

exp6-------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create user-item rating matrix
data = {
    'Item1': [4, 3, 5, np.nan, 4],
    'Item2': [3, np.nan, 4, 5, 3],
    'Item3': [2, 1, 3, 2, np.nan],
    'Item4': [4, 5, np.nan, 4, 5],
    'TargetItem': [2, 3, 2, 3, 3]
}

ratings_df = pd.DataFrame(data, index=['User1', 'User2', 'User3', 'User4', 'User5'])

# Compute original average rating of the target item
original_avg = ratings_df['TargetItem'].mean()
print(f"Target Item Average Rating Before Attack: {original_avg:.2f}")

# Add 5 fake users with high ratings for the target item
for i in range(5):
    ratings_df.loc[f'FakeUser_{i+1}'] = [3, 3, 3, 3, 5]

# Compute new average rating after attack
after_attack_avg = ratings_df['TargetItem'].mean()
print(f"Target Item Average Rating After Attack: {after_attack_avg:.2f}")

# Simple Heatmap
sns.heatmap(ratings_df.fillna(0), cmap="gray", cbar=False)
plt.show()

exp7------------

import pandas as pd

# Sample restaurant dataset
data = {
    "id": [1, 2, 3, 4, 5],
    "location": ["London", "Paris", "London", "New York", "London"],
    "restaurant_name": ["The Ritz", "Le Gourmet", "Burger King", "NY Deli", "Kimchi House"],
    "price": [15, 20, 8, 12, 10],
    "restaurant_type": ["Fine Dining", "French", "Fast Food", "Deli", "Fast Food"]
}

# Convert to DataFrame
restaurants = pd.DataFrame(data)

# Function for filtering based on user preferences
def recommend_restaurants(location=None, max_price=None, restaurant_type=None):
    filtered = restaurants.copy()
    if location:
        filtered = filtered[filtered["location"] == location]
    if max_price:
        filtered = filtered[filtered["price"] <= max_price]
    if restaurant_type:
        filtered = filtered[filtered["restaurant_type"] == restaurant_type]
    return filtered

# User-defined constraints
user_constraints = {
    "location": "Paris",
    "max_price": 30,
    "restaurant_type": "French"
}

# Get recommendations
recommended = recommend_restaurants(**user_constraints)

# Display result
print("Recommended Restaurants:
", recommended)

exp8-------------------
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

# Generate a dataset (200 samples, 10 features) with some randomness
X, y = make_classification(n_samples=200, n_features=10, n_classes=2, random_state=42, flip_y=0.1)

# Split into training (70%) and testing (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict probabilities for class 1
y_prob = model.predict_proba(X_test)[:, 1]

# Compute ROC curve and AUC
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

# Display AUC value
print(f"AUC Score: {roc_auc:.2f}")

# Plot ROC Curve (TPR vs FPR)
plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {roc_auc:.2f})', color='blue')
plt.plot([0, 1], [0, 1], linestyle='--', color='gray')  # Random classifier reference line
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('ROC Curve (TPR vs FPR)')
plt.legend()
plt.show()

exp9---------------------
import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Users and items
users = ["U1", "U2", "U3", "U4"]
items = ["ItemA", "ItemB", "ItemC", "ItemD", "ItemE"]

# User interactions with items
edges = [("U1", "ItemA"), ("U1", "ItemB"), ("U2", "ItemB"), ("U2", "ItemC"),
         ("U3", "ItemC"), ("U3", "ItemD"), ("U4", "ItemD"), ("U4", "ItemE")]

G.add_edges_from(edges)

# Apply PageRank algorithm
pagerank_scores = nx.pagerank(G, alpha=0.85)

# Function to recommend items
def recommend_items(user, top_n=2):
    user_items = set(G.successors(user))  # Items user has interacted with
    recommended_items = {item: pagerank_scores[item] for item in items if item not in user_items}
    return sorted(recommended_items, key=recommended_items.get, reverse=True)[:top_n]

# Example: Recommend for User U1
print(f"Recommended items for U1: {recommend_items('U1')}")

# Visualize the graph with PageRank scores
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)

# Draw graph without default labels
nx.draw(G, pos, node_color="lightblue", edge_color="gray", node_size=2000, with_labels=False)

# Display only the PageRank scores as labels
labels = {node: f"{node}
{pagerank_scores[node]:.2f}" for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color="black")

plt.title("User-Item Graph with PageRank Scores")
plt.show()


''')

    def exp(self, index):
        if 1 <= index <= 10:
            print(self.codes[index - 1])
        else:
            print("Invalid experiment number. Choose between 1 and 10.")

# Create an instance for direct use
exp_runner = Experiments()
