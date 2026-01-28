import pandas as pd
# Import the dataset
data = pd.read_csv('./Whole_Sale.csv')
print("DATA HEADER")
print(data.head())

#null values
print("\nNULL VALUES")
print(data.isnull().sum())

#kmean k value using elbow method
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['Region'] = le.fit_transform(data['Region'])
X = data.drop(['Region'], axis=1)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters (k)')
plt.ylabel('WCSS')
plt.show()

#training kmeans with optimal k
optimal_k = 3  # Set optimal k based on elbow method
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=42)
y_kmeans=kmeans.fit_predict(X)
print("\nKMEANS CLUSTERING RESULTS")
print(y_kmeans)

#adding cluster info to original data
data['Cluster'] = y_kmeans
print("\nDATA WITH CLUSTER INFO")
print(data.head())

#visualizing clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of customers')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()