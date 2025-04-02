class Experiments:
    def __init__(self):
        self.experiments = {
                    "1": """import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
items_data = {'Item1': [3, 4, 5], 'Item2': [1, 2, 3], 'Item3': [4, 5, 6], 'Item4': [2, 3, 4]}
items_matrix = np.array(list(items_data.values()))
print(items_matrix)
similarity_matrix = cosine_similarity(items_matrix)
print("Similarity Matrix:")
print(similarity_matrix)
#Euclidean
import numpy as np
P1 = np.array((19, 16, 35))
P2 = np.array((11, 24, 29))
temp = P1 - P2
euclid_dist = np.sqrt(np.dot(temp.T, temp))
print(euclid_dist)
from scipy.spatial import distance
P1 = (19, 16, 35)
P2 = (11,24, 29)
print(distance.euclidean(P1,P2))
#Manhattan
import numpy as np
P1 = np.array((19, 16, 35))
P2 = np.array((11, 24, 29))
manhattan_dist = np.sum(np.abs(P1 - P2))
print(manhattan_dist)
#JaccardSimi
def jaccard_similarity(set1,set2):
  intersection=len(set1.intersection(set2))
  union=len(set1.union(set2))
  return intersection/union
set1={"Sri","Krishna","College","of","technology"}
set2={"Sri","Krishna","College","of","Technology"}
similarity=jaccard_similarity(set1,set2)
print(similarity)
#Minkowski
import numpy as np
P1 = np.array((19, 16, 35))
P2 = np.array((11, 24, 29))
p = 3
minkowski_dist = np.sum(np.abs(P1 - P2) ** p) ** (1 / p)

print(f"Minkowski Distance (p={p}) between P1 and P2 is:", minkowski_dist)
""",

        "2": """import numpy as np
import pandas as pd
from scipy.linalg import svd

# Sample User-Item Interaction Matrix (Ratings)
ratings_matrix = np.array([
    [5, 4, 0, 3, 2],
    [4, 0, 5, 3, 1],
    [0, 5, 4, 0, 3],
    [3, 3, 0, 5, 4],
    [2, 1, 3, 4, 0]
])

# Convert to DataFrame for better visualization
ratings_df = pd.DataFrame(ratings_matrix, columns=["Item1", "Item2", "Item3", "Item4", "Item5"])

# Handle Missing Values (Replacing 0s with Column Mean)
ratings_filled = ratings_df.replace(0, ratings_df.mean())

# Perform SVD
U, sigma, Vt = svd(ratings_filled)

# Keep top 2 singular values (dimensionality reduction)
k = 2
sigma_k = np.diag(sigma[:k])
U_k = U[:, :k]
Vt_k = Vt[:k, :]

# Reconstruct the Ratings Matrix
ratings_reconstructed = np.dot(U_k, np.dot(sigma_k, Vt_k))

# Convert Back to DataFrame
recommendation_df = pd.DataFrame(ratings_reconstructed, columns=ratings_df.columns)

# Get the top recommended item for each user
top_recommendations = recommendation_df.idxmax(axis=1)

# Print recommendations
print(top_recommendations)

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Sample User-Item Interaction Matrix (Ratings)
ratings_matrix = np.array([
    [5, 4, 0, 3, 2],
    [4, 0, 5, 3, 1],
    [0, 5, 4, 0, 3],
    [3, 3, 0, 5, 4],
    [2, 1, 3, 4, 0]
])

# Convert to DataFrame for better visualization
ratings_df = pd.DataFrame(ratings_matrix, columns=["Item1", "Item2", "Item3", "Item4", "Item5"])

# Handle Missing Values (Replacing 0s with Column Mean)
ratings_filled = ratings_df.replace(0, ratings_df.mean())

# Standardize the Data
scaler = StandardScaler()
ratings_scaled = scaler.fit_transform(ratings_filled)

# Apply PCA
n_components = 2  # Choosing 2 principal components
pca = PCA(n_components=n_components)
ratings_pca = pca.fit_transform(ratings_scaled)

# Reconstruct the Matrix
ratings_reconstructed = pca.inverse_transform(ratings_pca)

# Convert Back to DataFrame
recommendation_df = pd.DataFrame(ratings_reconstructed, columns=ratings_df.columns)

# Print Recommended Ratings (Approximated Ratings)
print(recommendation_df)
""",

        "3": """import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
data = pd.DataFrame({
    'user_id': [1, 1, 1, 2, 2, 3, 4, 5],
    'item_id': [101, 102, 103, 101, 104, 105, 104, 101],
    'rating': [5, 4, 3, 5, 4, 2, 3, 4],
    'item_features': [
        "Action Adventure", "Romantic Comedy", "Action Thriller",
        "Action Adventure", "Sci-Fi Mystery", "Drama History",
        "Sci-Fi Mystery", "Action Adventure"
    ]
})
vectorizer = TfidfVectorizer()
item_profiles = vectorizer.fit_transform(data['item_features'])
user_profiles = {}
for user in data['user_id'].unique():
    liked_items = data[(data['user_id'] == user) & (data['rating'] >= 4)].index
    if len(liked_items) > 0:
        user_profiles[user] = np.mean(item_profiles[liked_items].toarray(), axis=0)  # Convert to dense array before averaging
for user, profile in user_profiles.items():
    print(f"User {user} Profile:\n", profile)""",

        "4": """import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.DataFrame({
    'movieId': [1, 2, 3, 4, 5],
    'title': ["Toy Story", "Jumanji", "Grumpier Old Men", "Waiting to Exhale", "Father of the Bride"],
    'genres': ["Adventure|Animation|Children|Comedy|Fantasy",
               "Adventure|Children|Fantasy",
               "Comedy|Romance",
               "Comedy|Drama|Romance",
               "Comedy"]
})
vectorizer = TfidfVectorizer()
genre_matrix = vectorizer.fit_transform(movies['genres'])
similarity_matrix = cosine_similarity(genre_matrix)
def recommend_movies(movie_title, num_recommendations=3):
    if movie_title not in movies['title'].values:
        return "Movie not found in the dataset!"
    idx = movies[movies['title'] == movie_title].index[0]
    similarity_scores = list(enumerate(similarity_matrix[idx]))
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommended_titles = [movies.iloc[i[0]]['title'] for i in sorted_movies[1:num_recommendations+1]]
    return recommended_titles
recommended_movies = recommend_movies("Jumanji")
print("Movies similar to 'Jumanji':", recommended_movies)""",

        "5": """import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.DataFrame({
    "user_id": [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5],
    "movie_id": [101, 102, 103, 101, 104, 105, 102, 103, 101, 103, 105, 102, 104],
    "rating": [5, 4, 3, 4, 2, 5, 4, 3, 5, 2, 4, 3, 4]
})

matrix = df.pivot(index="user_id", columns="movie_id", values="rating").fillna(0)
similarity = pd.DataFrame(cosine_similarity(matrix), index=matrix.index, columns=matrix.index)

def get_similar_users(user, n=3):
    return similarity[user].nlargest(n+1)[1:]

def recommend_movies(user, n=3):
    similar_users = get_similar_users(user).index
    seen = set(df[df["user_id"] == user]["movie_id"])
    recommendations = df[df["user_id"].isin(similar_users) & ~df["movie_id"].isin(seen)]
    return recommendations.groupby("movie_id")["rating"].mean().nlargest(n)

print(f"\nTop Similar Users to User 1:\n{get_similar_users(1)}")
print(f"\nTop Movie Recommendations for User 1:\n{recommend_movies(1)}")""",

        "6": """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.sparse.linalg import svds
np.random.seed(42)
num_users = 10
num_items = 10
ratings = np.random.randint(1, 11, (num_users, num_items))  # Ratings between 1 and 10
ratings_df = pd.DataFrame(ratings, columns=[f'Item_{i+1}' for i in range(num_items)])
ratings_df.index = [f'User_{i+1}' for i in range(num_users)]
def recommend_items(rating_matrix, k=3):
    rating_matrix = rating_matrix.astype(float)
    U, sigma, Vt = svds(rating_matrix, k=k)
    sigma = np.diag(sigma)
    reconstructed_matrix = np.dot(np.dot(U, sigma), Vt)
    return reconstructed_matrix
original_recommendations = recommend_items(ratings)
fake_user = np.random.randint(1, 3, (1, num_items))
fake_user[0, 3] = 5
ratings_with_attack = np.vstack([ratings, fake_user])
attacked_recommendations = recommend_items(ratings_with_attack)
original_ranking = np.argsort(-original_recommendations.mean(axis=0))
attacked_ranking = np.argsort(-attacked_recommendations.mean(axis=0))
ranking_df = pd.DataFrame({
    'Item': [f'Item_{i+1}' for i in range(num_items)],
    'Rank Before Attack': np.argsort(original_ranking) + 1,
    'Rank After Attack': np.argsort(attacked_ranking) + 1
})
plt.figure(figsize=(14, 5))
plt.subplot(1, 2, 1)
sns.heatmap(ratings, annot=True, cmap="Blues", fmt="d", xticklabels=[f'Item_{i+1}' for i in range(num_items)],
            yticklabels=[f'User_{i+1}' for i in range(num_users)])
plt.title("User-Item Ratings Before Attack")
plt.subplot(1, 2, 2)
sns.heatmap(ratings_with_attack, annot=True, cmap="Reds", fmt="d", xticklabels=[f'Item_{i+1}' for i in range(num_items)],
            yticklabels=[f'User_{i+1}' for i in range(num_users)] + ["Attacker"])
plt.title("User-Item Ratings After Attack")
plt.show()
plt.figure(figsize=(10, 5))
sns.barplot(x='Item', y='Rank Before Attack', data=ranking_df, label="Before Attack", color="blue")
sns.barplot(x='Item', y='Rank After Attack', data=ranking_df, label="After Attack", color="red", alpha=0.6)
plt.legend()
plt.title("Item Rankings Before and After Attack")
plt.ylabel("Rank (Lower is Better)")
plt.show()""",

        "7": """import pandas as pd

data = {
    'ProductName': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories'],
    'Brand': ['BrandA', 'BrandB', 'BrandA', 'BrandC', 'BrandB'],
    'Price': [800, 500, 300, 100, 250],
    'Rating': [4.5, 4.0, 4.7, 3.8, 4.2]
}

df = pd.DataFrame(data)

user_prefs = {'min_price': 200, 'max_price': 800, 'category': 'Electronics', 'brand': None, 'min_rating': 4.0}

df = df[(df['Price'].between(user_prefs['min_price'], user_prefs['max_price'])) & (df['Rating'] >= user_prefs['min_rating'])]
if user_prefs['category']: df = df[df['Category'] == user_prefs['category']]
if user_prefs['brand']: df = df[df['Brand'] == user_prefs['brand']]

df = df.sort_values(by=['Rating', 'Price'], ascending=[False, True])
print(df[['ProductName', 'Category', 'Brand', 'Price', 'Rating']])""",

        "8": """import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
y_scores = clf.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='grey', linestyle='--') # Diagonal line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.grid()
plt.show()""",

        "9": """import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
edges = [
    ('User1', 'ItemA'), ('User1', 'ItemB'), ('User2', 'ItemA'),
    ('User2', 'ItemC'), ('User3', 'ItemB'), ('User3', 'ItemD'),
    ('User4', 'ItemC'), ('User4', 'ItemD'), ('User5', 'ItemE')
]
G.add_edges_from(edges)
pagerank_values = nx.pagerank(G, alpha=0.85)
print("PageRank Scores (Recommendation Scores):")
for node, score in pagerank_values.items():
    print(f"{node}: {score:.4f}")
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
plt.title("Graph Representation of User-Item Interactions")
plt.show()""",
            # Add other experiments here
        }

    def show(self, experiment_number):
        return self.experiments.get(str(experiment_number), "Experiment not found. Enter a number between 1 and 9.")