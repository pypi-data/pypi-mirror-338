import numpy as np
from sklearn.cluster import KMeans
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

class SMK:
    def __init__(self, n_clusters=3, kernel="linear", C=1.0):
        """
        Initializes the SMK model.

        Parameters:
        - n_clusters (int): Number of clusters for KMeans.
        - kernel (str): Kernel type for SVM (default: "linear").
        - C (float): Regularization parameter for SVM.
        """
        self.n_clusters = n_clusters
        self.kernel = kernel
        self.C = C
        self.scaler = StandardScaler()
        self.kmeans = KMeans(n_clusters=self.n_clusters, n_init=10, random_state=42)
        self.svm = SVC(kernel=self.kernel, C=self.C)
        self.mode = None  # Will be determined in fit()

    def fit(self, X, y=None):
        """
        Trains the model in either clustering (unsupervised) or classification (supervised) mode.

        Parameters:
        - X (array-like): Feature matrix.
        - y (array-like, optional): Labels for supervised classification.

        Returns:
        - self
        """
        X_scaled = self.scaler.fit_transform(X)  # Always scale the features

        if y is None:
            self.mode = "clustering"
            self.kmeans.fit(X_scaled)
        else:
            self.mode = "classification"
            self.svm.fit(X_scaled, y)

        return self

    def predict(self, X):
        """
        Predicts labels based on the trained model.

        Parameters:
        - X (array-like): Feature matrix.

        Returns:
        - Predicted labels (for classification) or cluster assignments (for clustering).
        """
        if self.mode is None:
            raise ValueError("Model must be trained using `fit` before making predictions.")

        X_scaled = self.scaler.transform(X)

        if self.mode == "classification":
            return self.svm.predict(X_scaled)
        else:
            return self.kmeans.predict(X_scaled)

    def fit_predict(self, X):
        """
        Fits the clustering model and returns cluster assignments.

        Parameters:
        - X (array-like): Feature matrix.

        Returns:
        - Cluster assignments.
        """
        self.fit(X)
        return self.kmeans.labels_

    def score(self, X, y=None):
        """
        Computes the model's performance.

        Parameters:
        - X (array-like): Feature matrix.
        - y (array-like, optional): True labels for classification.

        Returns:
        - Accuracy score (for classification).
        - KMeans inertia (for clustering).
        """
        if self.mode is None:
            raise ValueError("Model must be trained before evaluating performance.")

        X_scaled = self.scaler.transform(X)

        if self.mode == "classification":
            if y is None:
                raise ValueError("True labels (y) are required for scoring classification performance.")
            y_pred = self.svm.predict(X_scaled)
            return accuracy_score(y, y_pred)
        else:
            return self.kmeans.inertia_  # Lower is better

    def get_params(self):
        """
        Returns model parameters.

        Returns:
        - Dictionary containing model parameters.
        """
        return {
            "mode": self.mode,
            "n_clusters": self.n_clusters,
            "kernel": self.kernel,
            "C": self.C
        }
