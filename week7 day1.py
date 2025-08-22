#Case Study
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

#Dataseti oxu
df = pd.read_csv(r"C:\Users\UniSoft PC\Downloads\Country-data (1).csv")
df.columns = [c.strip().lower() for c in df.columns]

#Rəqəmsal sütunları seç
num_cols = ['child_mort','exports','health','imports','income',
            'inflation','life_expec','total_fer','gdpp']
X = df[num_cols]

#Standartlaşdırma
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("Standardized mean (income):", X_scaled[:,4].mean())

#PCA tətbiqi
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

expl_var = pca.explained_variance_ratio_
cumulative_var = np.cumsum(expl_var)
print("Explained variance per component:", expl_var)
print("Cumulative explained variance:", cumulative_var)

#Scree plot
plt.figure(figsize=(8,5))
plt.plot(range(1, len(cumulative_var)+1), cumulative_var, marker='o')
plt.xlabel("Principal Component")
plt.ylabel("Cumulative Explained Variance")
plt.title("PCA Scree Plot")
plt.grid(True)
plt.show()

#K-Means clustering (3 cluster)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=20)
kmeans.fit(X_scaled)
df['cluster'] = kmeans.labels_

cluster_summary = df.groupby('cluster')[num_cols].mean()
print("\nK-Means Cluster Summary:\n", cluster_summary)

#Vizualizasiya PCA 2 komponent üzərində
pca_2 = PCA(n_components=2, random_state=42)
X_pca_2 = pca_2.fit_transform(X_scaled)

plt.figure(figsize=(8,6))
for cluster in range(3):
    plt.scatter(
        X_pca_2[df['cluster']==cluster, 0], 
        X_pca_2[df['cluster']==cluster, 1], 
        label=f"Cluster {cluster}"
    )
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("K-Means Clustering on PCA Components")
plt.legend()
plt.show()

#Hierarchical clustering
Z = linkage(X_scaled, method='ward')

plt.figure(figsize=(12, 6))
dendrogram(Z, labels=df['country'].values, leaf_rotation=90)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Countries")
plt.ylabel("Distance")
plt.show()

#Hierarchical cluster təyini (3 cluster)
df['h_cluster'] = fcluster(Z, 3, criterion='maxclust')
h_cluster_summary = df.groupby('h_cluster')[num_cols].mean()
print("\nHierarchical Cluster Summary:\n", h_cluster_summary)




#Homework

#Lazımi kitabxanaları import edirik
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

#Dataset-i oxuyuruq
df = pd.read_csv(r"C:\Users\UniSoft PC\Downloads\Iris.csv")

print("Datasetin ilk 5 sətri:")
print(df.head())

#İstifadə olunacaq xüsusiyyətlər
X = df.drop(["Id", "Species"], axis=1)

#Məlumatı standartlaşdırırıq
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#PCA ilə 2 ölçüyə endiririk (vizual üçün)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# --- K-MEANS CLUSTERING ---

#Elbow Method (istəyə bağlı)
inertia = []
for k in range(1, 10):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertia.append(km.inertia_)

plt.figure(figsize=(6,4))
plt.plot(range(1,10), inertia, marker="o")
plt.title("Elbow Method")
plt.xlabel("Cluster sayı")
plt.ylabel("Inertia")
plt.show()

#KMeans 3 cluster ilə
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["KMeans_Cluster"] = kmeans.fit_predict(X_scaled)

plt.figure(figsize=(6,4))
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=df["KMeans_Cluster"], palette="Set1")
plt.title("KMeans Clustering (PCA ilə)")
plt.show()

# --- HIERARCHICAL CLUSTERING ---

#Dendrogram
linked = linkage(X_scaled, method='ward')
plt.figure(figsize=(10,6))
dendrogram(linked, truncate_mode='lastp', p=20)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()

#3 cluster ilə Hierarchical
hc = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
df["Hier_Cluster"] = hc.fit_predict(X_scaled)

plt.figure(figsize=(6,4))
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=df["Hier_Cluster"], palette="Set2")
plt.title("Hierarchical Clustering (PCA ilə)")
plt.show()

#Real növlərlə müqayisə
print("\nKMeans nəticələri ilə Species müqayisəsi:")
print(pd.crosstab(df["Species"], df["KMeans_Cluster"]))

print("\nHierarchical nəticələri ilə Species müqayisəsi:")
print(pd.crosstab(df["Species"], df["Hier_Cluster"]))
