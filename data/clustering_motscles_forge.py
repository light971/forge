"""
Clustering sémantique de mots-clés — Projet Forge
---------------------------------------------------
Regroupe une liste de mots-clés SEO par similarité de sens,
pour construire des "cocons sémantiques" (thématiques de contenu).

Prérequis :
    pip install sentence-transformers scikit-learn pandas

Utilisable aussi sur Google Colab (gratuit, pas d'install locale nécessaire) :
    https://colab.research.google.com

Input attendu : un fichier CSV avec au moins une colonne "keyword"
    (et idéalement une colonne "volume" pour prioriser ensuite)

Output : un CSV avec une colonne "cluster" ajoutée, groupant
    les mots-clés par thématique.
"""

import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import AgglomerativeClustering
import numpy as np

# --- 1. Charger les mots-clés ---
# Remplace "mots_cles_forge.csv" par le nom de ton export
df = pd.read_csv("mots_cles_forge.csv")  # colonnes attendues : keyword, volume (optionnel)

keywords = df["keyword"].astype(str).tolist()

# --- 2. Générer les embeddings (vecteurs sémantiques) ---
# Modèle multilingue léger, adapté au français
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
embeddings = model.encode(keywords, show_progress_bar=True)

# --- 3. Clustering hiérarchique ---
# distance_threshold : plus bas = clusters plus fins/nombreux, plus haut = clusters plus larges
# À ajuster selon la taille de ta liste (commence à 1.3, ajuste en regardant les résultats)
clustering = AgglomerativeClustering(
    n_clusters=None,
    distance_threshold=1.3,
    metric="cosine",
    linkage="average"
)
labels = clustering.fit_predict(embeddings)

df["cluster"] = labels

# --- 4. Nommer les clusters (mot-clé le plus représentatif = le plus court par cluster, approximation) ---
cluster_names = (
    df.groupby("cluster")["keyword"]
    .apply(lambda x: min(x, key=len))
    .to_dict()
)
df["cluster_nom"] = df["cluster"].map(cluster_names)

# --- 5. Export ---
df = df.sort_values(["cluster", "volume"], ascending=[True, False]) if "volume" in df.columns else df.sort_values("cluster")
df.to_csv("mots_cles_forge_clusterises.csv", index=False)

print(f"{len(keywords)} mots-clés regroupés en {df['cluster'].nunique()} clusters.")
print("Export : mots_cles_forge_clusterises.csv")
print("\nAperçu des clusters :")
for cluster_id, group in df.groupby("cluster"):
    print(f"\n--- Cluster {cluster_id} ({cluster_names[cluster_id]}) ---")
    print(group["keyword"].tolist()[:8])
