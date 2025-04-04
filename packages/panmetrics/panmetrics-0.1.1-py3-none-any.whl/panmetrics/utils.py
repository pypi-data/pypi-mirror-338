import numpy as np
import pandas as pd
from scipy.stats import kstest
from scipy.spatial.distance import cdist
from typing import Union, Optional
from scipy.ndimage import label
import torch
import warnings

class RegressionDataValidator:
    def __init__(self, raise_warning=True):
        """Initialize the DataValidator class"""
        self.raise_warning = raise_warning

    def check_data_type(self, y_true, y_pred):
        """Check if input data types are valid"""
        valid_types = (np.ndarray, pd.Series, pd.DataFrame, list)
        if not isinstance(y_true, valid_types) or not isinstance(y_pred, valid_types):
            raise TypeError("y_true and y_pred must be numpy array, pandas series, or list")

    def check_shapes(self, y_true, y_pred):
        """Check if y_true and y_pred have the same shape"""
        if np.shape(y_true) != np.shape(y_pred):
            raise ValueError("y_true and y_pred must have the same shape")

    def check_missing_values(self, y_true, y_pred):
        """Check for missing values"""
        if np.any(pd.isnull(y_true)) or np.any(pd.isnull(y_pred)):
            raise ValueError("Missing values (NaN) detected in data")

    def check_inf_values(self, y_true, y_pred):
        """Check for infinite values"""
        if np.any(np.isinf(y_true)) or np.any(np.isinf(y_pred)):
            raise ValueError("Infinite values (inf) detected in data")

    def check_lengths(self, y_true, y_pred):
        """Check if y_true and y_pred have the same length"""
        if len(y_true) != len(y_pred):
            raise ValueError("y_true and y_pred must have the same length")

    def check_numeric_values(self, y_true, y_pred):
        """Check if values are numeric"""
        if not np.issubdtype(np.array(y_true).dtype, np.number) or not np.issubdtype(np.array(y_pred).dtype, np.number):
            raise TypeError("y_true and y_pred must contain numeric values")

    def check_variance(self, y_true, y_pred):
        """Check if variance of y_true is zero (can cause issues in R-squared calculation)"""
        if np.var(y_true) == 0:
            raise ValueError("Variance of y_true is zero. R-squared may not be meaningful")

    def check_non_negative(self, y_true, y_pred):
        """Check that values are non-negative for Logarithmic Mean Squared Error"""
        if np.any(y_true < -1) or np.any(y_pred < -1):
            raise ValueError("y_true and y_pred must be greater than or equal to -1 for log-based metrics")

    def check_multicollinearity(self, X, threshold=0.9):
        """Check for multicollinearity in input features"""
        if isinstance(X, pd.DataFrame):
            corr_matrix = X.corr().abs()
            high_corr = (corr_matrix > threshold).sum().sum() - len(X.columns)
            if high_corr > 0:
                raise ValueError("High multicollinearity detected in input features")
        else:
            if self.raise_warning:
                print("Warning: Multicollinearity check requires a pandas DataFrame")

    def check_outliers(self, y_true, y_pred, threshold=3):
        """Check for outliers using Z-score"""
        z_scores = (y_true - np.mean(y_true)) / np.std(y_true)
        if np.any(np.abs(z_scores) > threshold):
            raise ValueError("Outliers detected in y_true")

    def check_distribution(self, y_true, y_pred, distribution='normal'):
        """Check if data follows a specific distribution"""
        if distribution == 'normal':
            stat, p_value = kstest(y_true, 'norm')
            if p_value < 0.05:
                raise ValueError("y_true does not follow a normal distribution")

    def check_correlation(self, y_true, y_pred, threshold=0.8):
        """Check for high correlation between y_true and y_pred"""
        corr = np.corrcoef(y_true, y_pred)[0, 1]
        if corr > threshold:
            raise ValueError("High correlation detected between y_true and y_pred")

    def check_missing_values_large_data(self, y_true, y_pred, sample_size=1000):
        """Check for missing values in large data using sampling"""
        indices = np.random.choice(len(y_true), sample_size, replace=False)
        if np.any(pd.isnull(y_true[indices])) or np.any(pd.isnull(y_pred[indices])):
            raise ValueError("Missing values (NaN) detected in data")

    def validate_all(self, y_true, y_pred, log_based=False, check_missing_large= False, check_outliers=False, check_distribution=False, check_correlation=False, sample_size=1000):
        """Run all validation checks"""
        self.check_data_type(y_true, y_pred)
        self.check_shapes(y_true, y_pred)
        self.check_missing_values(y_true, y_pred)
        self.check_inf_values(y_true, y_pred)
        self.check_lengths(y_true, y_pred)
        self.check_numeric_values(y_true, y_pred)
        self.check_variance(y_true, y_pred)
        if check_missing_large:
            self.check_missing_values_large_data(y_true, y_pred, sample_size)
        else:
            self.check_missing_values(y_true, y_pred)
        if log_based:
            self.check_non_negative(y_true, y_pred)
        if check_outliers:
            self.check_outliers(y_true, y_pred)
        if check_distribution:
            self.check_distribution(y_true, y_pred)
        if check_correlation:
            self.check_correlation(y_true, y_pred)
        return True  # Return True if all checks pass

class ClassificationDataValidator:
    def __init__(self, raise_warning=True):
        """Initialize the ClassificationDataValidator class"""
        self.raise_warning = raise_warning

    def check_data_type(self, y_true, y_pred, y_probs=None):
        """
        Check if input data types are valid.

        Parameters:
        -----------
        y_true : array-like
            Ground truth (correct) labels.
        y_pred : array-like
            Predicted labels.
        y_probs : array-like, optional
            Predicted probabilities for each class (2D array).
        """
        valid_types = (np.ndarray, list)
        if not isinstance(y_true, valid_types) or not isinstance(y_pred, valid_types):
            raise TypeError("y_true and y_pred must be numpy array or list")

        if y_probs is not None:
            if not isinstance(y_probs, valid_types):
                raise TypeError("y_probs must be numpy array or list")
            if len(np.array(y_probs).shape) != 2:
                raise ValueError("y_probs must be a 2D array (samples x classes)")

    def check_missing_values(self, y_true, y_pred, y_probs=None):
        """
        Check for missing values in y_true, y_pred, and y_probs.
        """
        if np.any(np.isnan(y_true)) or np.any(np.isnan(y_pred)):
            raise ValueError("Missing values (NaN) detected in y_true or y_pred")

        if y_probs is not None:
            if np.any(np.isnan(y_probs)):
                raise ValueError("Missing values (NaN) detected in y_probs")

    def check_lengths(self, y_true, y_pred, y_probs=None):
        """
        Check if y_true, y_pred, and y_probs have the same length.
        """
        if len(y_true) != len(y_pred):
            raise ValueError("y_true and y_pred must have the same length")

        if y_probs is not None:
            if len(y_true) != len(y_probs):
                raise ValueError("y_true and y_probs must have the same length")

    def check_classes(self, y_true, y_pred):
        """
        Check if y_true and y_pred have the same set of classes.
        """
        unique_true = np.unique(y_true)
        unique_pred = np.unique(y_pred)
        if not np.array_equal(unique_true, unique_pred):
            raise ValueError("y_true and y_pred must have the same set of classes")

    def check_class_labels(self, y_true, y_pred):
        """
        Check if y_true and y_pred contain valid class labels (integers).
        """
        y_true_arr = np.array(y_true)
        y_pred_arr = np.array(y_pred)

        # Skip check if arrays are empty
        if len(y_true_arr) == 0 or len(y_pred_arr) == 0:
            return

        if not np.issubdtype(y_true_arr.dtype, np.integer) or not np.issubdtype(y_pred_arr.dtype, np.integer):
            raise TypeError("y_true and y_pred must contain integer class labels")

    def check_outliers(self, y_true, threshold=3):
        """
        Check for outliers in y_true using Z-score.
        """
        z_scores = (y_true - np.mean(y_true)) / np.std(y_true)
        if np.any(np.abs(z_scores) > threshold):
            if self.raise_warning:
                print("Warning: Outliers detected in y_true")
            else:
                raise ValueError("Outliers detected in y_true")

    def check_distribution(self, y_true, distribution='normal'):
        """
        Check if y_true follows a specific distribution.
        """
        if distribution == 'normal':
            stat, p_value = kstest(y_true, 'norm')
            if p_value < 0.05:
                if self.raise_warning:
                    print("Warning: y_true does not follow a normal distribution")
                else:
                    raise ValueError("y_true does not follow a normal distribution")

    def check_correlation(self, y_true, y_pred, threshold=0.8):
        """
        Check for high correlation between y_true and y_pred.
        """
        corr = np.corrcoef(y_true, y_pred)[0, 1]
        if corr > threshold:
            if self.raise_warning:
                print(f"Warning: High correlation detected between y_true and y_pred (corr={corr})")
            else:
                raise ValueError(f"High correlation detected between y_true and y_pred (corr={corr})")

    def check_missing_large_data(self, y_true, y_pred, sample_size=1000):
        """
        Check for missing values in large data using sampling.
        """
        indices = np.random.choice(len(y_true), sample_size, replace=False)
        if np.any(np.isnan(y_true[indices])) or np.any(np.isnan(y_pred[indices])):
            if self.raise_warning:
                print("Warning: Missing values (NaN) detected in sampled data")
            else:
                raise ValueError("Missing values (NaN) detected in sampled data")
    def check_empty_arrays(self, y_true, y_pred):
        """
        Check if input arrays are empty.
        """
        if len(y_true) == 0 or len(y_pred) == 0:
            raise ValueError("Input arrays cannot be empty")

    def validate_probabilities(self, y_probs):
        """
        Check if probabilities are valid (between 0 and 1 and sum to 1).
        """
        if np.any(y_probs < 0) or np.any(y_probs > 1):
            raise ValueError("y_probs must have values between 0 and 1")

        # Check if probabilities sum to 1 for each sample
        if not np.allclose(np.sum(y_probs, axis=1), 1):
            raise ValueError("Probabilities in y_probs must sum to 1 for each sample")

    def validate_top_k(self, y_probs, k):
        """
        Check if k is valid for top-k accuracy.
        """
        if k > y_probs.shape[1]:
            raise ValueError(f"k={k} is greater than the number of classes {y_probs.shape[1]}")
        if k <= 0:
            raise ValueError(f"k={k} must be a positive integer")

    def check_class_balance(self, y_true, threshold=0.1):
        """
        Check if classes are imbalanced.
        """
        class_counts = np.bincount(y_true)
        min_count = np.min(class_counts)
        max_count = np.max(class_counts)

        if min_count / max_count < threshold:
            if self.raise_warning:
                print(f"Warning: Class imbalance detected (min_count={min_count}, max_count={max_count})")
            else:
                raise ValueError(f"Class imbalance detected (min_count={min_count}, max_count={max_count})")
    def check_probabilities_classes(self, y_true, y_probs):
        """
        Check if the number of classes in y_probs matches the number of classes in y_true,
        and that the probabilities make sense for the given true labels.
        """
        n_classes_true = len(np.unique(y_true))
        n_classes_probs = y_probs.shape[1]

        if n_classes_probs != n_classes_true:
            raise ValueError(
                f"Number of classes in y_probs ({n_classes_probs}) "
                f"does not match number of classes in y_true ({n_classes_true})"
            )

        # Additional check that the predicted class probabilities make sense
        predicted_classes = np.argmax(y_probs, axis=1)
        if not np.array_equal(np.sort(np.unique(predicted_classes)), np.sort(np.unique(y_true))):
            if self.raise_warning:
                print("Warning: Predicted classes from probabilities don't match true class labels")
            else:
                raise ValueError("Predicted classes from probabilities don't match true class labels")

    def validate_all(self, y_true, y_pred, y_probs=None, check_outliers=False, check_distribution=False, check_correlation=False, check_missing_large=False, check_class_balance=False, sample_size=1000):
        """
        Run all validation checks.
        """
        self.check_empty_arrays(y_true, y_pred)  # Check for empty arrays first
        self.check_data_type(y_true, y_pred, y_probs)
        self.check_missing_values(y_true, y_pred, y_probs)
        self.check_lengths(y_true, y_pred, y_probs)
        self.check_classes(y_true, y_pred)
        self.check_class_labels(y_true, y_pred)

        if y_probs is not None:
            self.validate_probabilities(y_probs)
            self.check_probabilities_classes(y_true, y_probs)

        if check_outliers:
            self.check_outliers(y_true)
        if check_distribution:
            self.check_distribution(y_true)
        if check_correlation:
            self.check_correlation(y_true, y_pred)
        if check_missing_large:
            self.check_missing_large_data(y_true, y_pred, sample_size)
        if check_class_balance:
            self.check_class_balance(y_true)

        return True  # Return True if all checks pass


class ClusteringDataValidator:
    def __init__(self, raise_warning=True):
        """Initialize the ClusteringDataValidator class"""
        self.raise_warning = raise_warning

    def check_data_type(self, X, labels=None):
        """
        Check if input data types are valid.
        """
        valid_types = (np.ndarray, list)
        if not isinstance(X, valid_types):
            raise TypeError("X must be a numpy array or list")

        # Convert X to numpy array if it's a list
        if isinstance(X, list):
            X = np.array(X)

        if labels is not None:
            if not isinstance(labels, valid_types):
                raise TypeError("labels must be a numpy array or list")

    def check_missing_values(self, X, labels=None):
        """
        Check for missing values in X and labels.
        """
        if np.any(np.isnan(X)):
            raise ValueError("Missing values (NaN) detected in X")

        if labels is not None:
            if np.any(np.isnan(labels)):
                raise ValueError("Missing values (NaN) detected in labels")

    def check_lengths(self, X, labels=None):
        """
        Check if X and labels have the same length.
        """
        if labels is not None:
            if len(X) != len(labels):
                raise ValueError("X and labels must have the same length")

    def check_feature_dimensions(self, X, min_features=1):
        """
        Check if X has at least the minimum number of features.
        """
        if X.shape[1] < min_features:
            raise ValueError(f"X must have at least {min_features} features")

    def check_outliers(self, X, threshold=3):
        """
        Check for outliers in X using Z-score.
        """
        z_scores = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
        if np.any(np.abs(z_scores) > threshold):
            if self.raise_warning:
                print("Warning: Outliers detected in X")
            else:
                raise ValueError("Outliers detected in X")

    def check_distribution(self, X, distribution='normal'):
        """
        Check if X follows a specific distribution.
        """
        if distribution == 'normal':
            for feature in range(X.shape[1]):
                stat, p_value = kstest(X[:, feature], 'norm')
                if p_value < 0.05:
                    if self.raise_warning:
                        print(f"Warning: Feature {feature} does not follow a normal distribution")
                    else:
                        raise ValueError(f"Feature {feature} does not follow a normal distribution")

    def check_correlation(self, X, threshold=0.8):
        """
        Check for high correlation between features in X.
        """
        corr_matrix = np.corrcoef(X, rowvar=False)
        for i in range(corr_matrix.shape[0]):
            for j in range(i + 1, corr_matrix.shape[1]):
                if abs(corr_matrix[i, j]) > threshold:
                    if self.raise_warning:
                        print(f"Warning: High correlation detected between features {i} and {j} (corr={corr_matrix[i, j]})")
                    else:
                        raise ValueError(f"High correlation detected between features {i} and {j} (corr={corr_matrix[i, j]})")

    def check_missing_large_data(self, X, sample_size=1000):
        """
        Check for missing values in large data using sampling.
        """
        indices = np.random.choice(len(X), sample_size, replace=False)
        if np.any(np.isnan(X[indices])):
            if self.raise_warning:
                print("Warning: Missing values (NaN) detected in sampled data")
            else:
                raise ValueError("Missing values (NaN) detected in sampled data")

    def check_cluster_labels(self, cluster_labels):
        """
        Check if cluster_labels contain valid integer values.
        """
        if not np.issubdtype(np.array(cluster_labels).dtype, np.integer):
            raise TypeError("cluster_labels must contain integer values")

    def check_number_of_clusters(self, labels, min_clusters=2, max_clusters=None):
        """
        Check if the number of clusters is within a valid range.
        """
        unique_clusters = np.unique(labels)
        num_clusters = len(unique_clusters)

        if num_clusters < min_clusters:
            raise ValueError(f"Number of clusters ({num_clusters}) is less than the minimum allowed ({min_clusters})")

        if max_clusters is not None and num_clusters > max_clusters:
            raise ValueError(f"Number of clusters ({num_clusters}) exceeds the maximum allowed ({max_clusters})")

    def check_cluster_balance(self, labels, threshold=0.1):
        """
        Check if clusters are balanced.
        """
        cluster_counts = np.bincount(labels)
        min_count = np.min(cluster_counts)
        max_count = np.max(cluster_counts)

        if min_count / max_count < threshold:
            if self.raise_warning:
                print(f"Warning: Cluster imbalance detected (min_count={min_count}, max_count={max_count})")
            else:
                raise ValueError(f"Cluster imbalance detected (min_count={min_count}, max_count={max_count})")

    def check_cluster_separation(self, X, labels, min_distance=0.1):
        """
        Check if clusters are well-separated based on pairwise distances.
        """
        unique_clusters = np.unique(labels)
        centroids = np.array([np.mean(X[labels == c], axis=0) for c in unique_clusters])
        distances = cdist(centroids, centroids)
        np.fill_diagonal(distances, np.inf)  # Ignore self-distances

        if np.min(distances) < min_distance:
            if self.raise_warning:
                print(f"Warning: Some clusters are too close to each other (min_distance={np.min(distances)})")
            else:
                raise ValueError(f"Some clusters are too close to each other (min_distance={np.min(distances)})")

    def validate_all(self, X, labels=None, check_outliers=False, check_distribution=False,
                     check_correlation=False, check_missing_large=False, min_features=1,
                     min_clusters=2, max_clusters=None, check_balance=False, check_separation=False,
                     min_distance=0.1, sample_size=1000):
        """
        Run all validation checks.
        """
        self.check_data_type(X, labels)
        self.check_missing_values(X, labels)
        self.check_lengths(X, labels)
        self.check_feature_dimensions(X, min_features)

        if labels is not None:
            self.check_cluster_labels(labels)
            self.check_number_of_clusters(labels, min_clusters, max_clusters)
            if check_balance:
                self.check_cluster_balance(labels)
            if check_separation:
                self.check_cluster_separation(X, labels, min_distance)

        if check_outliers:
            self.check_outliers(X)
        if check_distribution:
            self.check_distribution(X)
        if check_correlation:
            self.check_correlation(X)
        if check_missing_large:
            self.check_missing_large_data(X, sample_size)

        return True  # Return True if all checks pass


class DataValidator:
    def __init__(self, raise_warning=True):
        """Initialize the DataValidator class"""
        self.raise_warning = raise_warning

    def check_data_type(self, y_true, y_pred):
        """Check if input data types are valid"""
        valid_types = (np.ndarray, pd.Series, pd.DataFrame, list)
        if not isinstance(y_true, valid_types) or not isinstance(y_pred, valid_types):
            raise TypeError("y_true and y_pred must be numpy array, pandas series, or list")

    def check_shapes(self, y_true, y_pred):
        """Check if y_true and y_pred have the same shape"""
        if np.shape(y_true) != np.shape(y_pred):
            raise ValueError("y_true and y_pred must have the same shape")

    def check_missing_values(self, y_true, y_pred):
        """Check for missing values"""
        if np.any(pd.isnull(y_true)) or np.any(pd.isnull(y_pred)):
            raise ValueError("Missing values (NaN) detected in data")

    def check_inf_values(self, y_true, y_pred):
        """Check for infinite values"""
        if np.any(np.isinf(y_true)) or np.any(np.isinf(y_pred)):
            raise ValueError("Infinite values (inf) detected in data")

    def check_lengths(self, y_true, y_pred):
        """Check if y_true and y_pred have the same length"""
        if len(y_true) != len(y_pred):
            raise ValueError("y_true and y_pred must have the same length")

    def check_numeric_values(self, y_true, y_pred):
        """Check if values are numeric"""
        if not np.issubdtype(np.array(y_true).dtype, np.number) or not np.issubdtype(np.array(y_pred).dtype, np.number):
            raise TypeError("y_true and y_pred must contain numeric values")

    def check_variance(self, y_true, y_pred):
        """Check if variance of y_true is zero (can cause issues in R-squared calculation)"""
        if np.var(y_true) == 0:
            raise ValueError("Variance of y_true is zero. R-squared may not be meaningful")

    def check_non_negative(self, y_true, y_pred):
        """Check that values are non-negative for Logarithmic Mean Squared Error"""
        if np.any(y_true < -1) or np.any(y_pred < -1):
            raise ValueError("y_true and y_pred must be greater than or equal to -1 for log-based metrics")

    def check_multicollinearity(self, X, threshold=0.9):
        """Check for multicollinearity in input features"""
        if isinstance(X, pd.DataFrame):
            corr_matrix = X.corr().abs()
            high_corr = (corr_matrix > threshold).sum().sum() - len(X.columns)
            if high_corr > 0:
                raise ValueError("High multicollinearity detected in input features")
        else:
            if self.raise_warning:
                print("Warning: Multicollinearity check requires a pandas DataFrame")

    def check_outliers(self, y_true, y_pred, threshold=3):
        """Check for outliers using Z-score"""
        z_scores = (y_true - np.mean(y_true)) / np.std(y_true)
        if np.any(np.abs(z_scores) > threshold):
            raise ValueError("Outliers detected in y_true")

    def check_distribution(self, y_true, y_pred, distribution='normal'):
        """Check if data follows a specific distribution"""
        if distribution == 'normal':
            stat, p_value = kstest(y_true, 'norm')
            if p_value < 0.05:
                raise ValueError("y_true does not follow a normal distribution")

    def check_correlation(self, y_true, y_pred, threshold=0.8):
        """Check for high correlation between y_true and y_pred"""
        corr = np.corrcoef(y_true, y_pred)[0, 1]
        if corr > threshold:
            raise ValueError("High correlation detected between y_true and y_pred")

    def check_missing_values_large_data(self, y_true, y_pred, sample_size=1000):
        """Check for missing values in large data using sampling"""
        indices = np.random.choice(len(y_true), sample_size, replace=False)
        if np.any(pd.isnull(y_true[indices])) or np.any(pd.isnull(y_pred[indices])):
            raise ValueError("Missing values (NaN) detected in data")

    def validate_all(self, y_true, y_pred, log_based=False, check_outliers=False, check_distribution=False, check_correlation=False):
        """Run all validation checks"""
        self.check_data_type(y_true, y_pred)
        self.check_shapes(y_true, y_pred)
        self.check_missing_values(y_true, y_pred)
        self.check_inf_values(y_true, y_pred)
        self.check_lengths(y_true, y_pred)
        self.check_numeric_values(y_true, y_pred)
        self.check_variance(y_true, y_pred)
        if log_based:
            self.check_non_negative(y_true, y_pred)
        if check_outliers:
            self.check_outliers(y_true, y_pred)
        if check_distribution:
            self.check_distribution(y_true, y_pred)
        if check_correlation:
            self.check_correlation(y_true, y_pred)
        return True  # Return True if all checks pass


class SegmentationDataValidator(DataValidator):
    def __init__(self, raise_warning: bool = True):
        super().__init__(raise_warning=raise_warning)

    def _ensure_numpy(self, data: Union[np.ndarray, list, torch.Tensor]) -> np.ndarray:
        """Convert input to numpy array if needed."""
        if str(type(data)) == "<class 'torch.Tensor'>":
            data = data.detach().cpu().numpy()
        elif isinstance(data, list):
            data = np.array(data)
        return data

    def check_empty_masks(self, y_true: np.ndarray, y_pred: np.ndarray) -> None:
        """Check if masks are empty and raise appropriate warnings."""
        if np.all(y_true == 0):
            warnings.warn("y_true is completely empty (all background pixels).",
                         UserWarning, stacklevel=2)
        if np.all(y_pred == 0):
            warnings.warn("y_pred is completely empty (all background pixels).",
                         UserWarning, stacklevel=2)

    def check_binary(self, y_true: np.ndarray, y_pred: np.ndarray) -> None:
        """Check if inputs are strictly binary (0 or 1)."""
        y_true = self._ensure_numpy(y_true)
        y_pred = self._ensure_numpy(y_pred)

        for name, data in [("y_true", y_true), ("y_pred", y_pred)]:
            unique = np.unique(data)
            if not np.all(np.isin(unique, [0, 1])):
                raise ValueError(f"{name} must be binary (0 or 1). Found values: {unique}")

    def check_spatial_consistency(self, y_true: np.ndarray, y_pred: np.ndarray) -> None:
        """Ensure spatial dimensions match (HxW, HxWxD, etc.)."""
        if y_true.shape != y_pred.shape:
            raise ValueError(
                f"Shape mismatch: y_true {y_true.shape} != y_pred {y_pred.shape}"
            )

    def check_connected_components(self, mask: np.ndarray, max_components: int = 10) -> None:
        """Warn if mask has too many disconnected regions (possible noise)."""
        labeled, n_components = label(mask)
        if n_components > max_components:
            warnings.warn(f"Mask has {n_components} connected components (possible noise).")

    def check_class_imbalance(self, y_true: np.ndarray, threshold: float = 0.01, is_binary: bool = False) -> None:
        """Warn if a class is extremely rare."""
        counts = np.bincount(y_true.flatten())
        total = np.sum(counts)

        for class_id, count in enumerate(counts):
            ratio = count / total
            if ratio < threshold:
                class_type = "foreground" if (is_binary and class_id == 1) else f"class {class_id}"
                warnings.warn(f"{class_type} is rare ({ratio:.2%} pixels).", UserWarning, stacklevel=2)

    def validate_all(
        self,
        y_true: Union[np.ndarray, torch.Tensor],
        y_pred: Union[np.ndarray, torch.Tensor],
        is_binary: bool = False,
        is_multiclass: bool = False,
        is_probabilistic: bool = False,
        n_classes: Optional[int] = None,
        check_connected_components: bool = False,
        check_class_imbalance: bool = False,
        check_empty_masks: bool = True,
    ) -> bool:
        """
        Run all validations with complete checks.
        """
        # Convert to numpy first
        y_true = self._ensure_numpy(y_true)
        y_pred = self._ensure_numpy(y_pred)

        # General data checks
        super().check_data_type(y_true, y_pred)
        super().check_shapes(y_true, y_pred)
        super().check_missing_values(y_true, y_pred)
        super().check_inf_values(y_true, y_pred)

        if not is_probabilistic:  
            super().check_numeric_values(y_true, y_pred)

        # Segmentation-specific checks
        self.check_spatial_consistency(y_true, y_pred)

        if check_empty_masks:
            self.check_empty_masks(y_true, y_pred)

        if is_binary and not is_probabilistic:
            self.check_binary(y_true, y_pred)
        elif is_multiclass:
            if n_classes is None:
                raise ValueError("n_classes must be specified for multi-class validation.")
            if len(np.unique(y_true)) < 2:
                warnings.warn("Less than 2 classes in y_true.")

        if check_connected_components and not is_probabilistic:
            self.check_connected_components(y_true)
            self.check_connected_components(y_pred)

        if check_class_imbalance and is_multiclass:
            self.check_class_imbalance(y_true, is_binary=False)

        return True


class ImageTranslationDataValidator:
    def __init__(self, raise_warning: bool = True):
        self.raise_warning = raise_warning
        self._supported_dtypes = (np.float32, np.float64, np.uint8, np.uint16)

    def _ensure_numpy(self, data: Union[np.ndarray, 'torch.Tensor']) -> np.ndarray:
        """Smart conversion to float32 while preserving value range"""
        if str(type(data)) == "<class 'torch.Tensor'>":
            data = data.detach().cpu().numpy()

        if data.dtype not in self._supported_dtypes:
            raise TypeError(f"Unsupported dtype: {data.dtype}. Supported: {self._supported_dtypes}")

        # Automatic conversion to float32 while preserving values
        if data.dtype == np.uint8:
            return data.astype(np.float32) / 255.0
        elif data.dtype == np.uint16:
            return data.astype(np.float32) / 65535.0
        return data.astype(np.float32, copy=False)

    def _auto_detect_range(self, img: np.ndarray) -> tuple[float, float]:
        """Automatic detection of image value range"""
        if img.dtype == np.uint8:
            return (0, 255)
        elif img.dtype == np.uint16:
            return (0, 65535)
        return (float(np.min(img)), float(np.max(img)))

    def validate_all(
        self,
        img1: Union[np.ndarray, 'torch.Tensor'],
        img2: Union[np.ndarray, 'torch.Tensor'],
        expected_range: Optional[tuple[float, float]] = None,
        check_channels: bool = True,
        auto_scale: bool = True
    ) -> tuple[np.ndarray, np.ndarray]:
        """Advanced validation with features:
        - Automatic range detection
        - Smart data type conversion
        - Automatic normalization
        """
        img1 = self._ensure_numpy(img1)
        img2 = self._ensure_numpy(img2)

        # Automatic range detection if not specified
        if expected_range is None:
            range1 = self._auto_detect_range(img1)
            range2 = self._auto_detect_range(img2)
            expected_range = (min(range1[0], range2[0]), max(range1[1], range2[1]))

        # Dimension check
        if img1.shape != img2.shape:
            raise ValueError(f"Shape mismatch: {img1.shape} vs {img2.shape}")

        # Channel check
        if check_channels and img1.shape[-1] != img2.shape[-1]:
            if self.raise_warning:
                warnings.warn(f"Channel mismatch: {img1.shape[-1]} vs {img2.shape[-1]}", UserWarning)

        # Automatic normalization
        if auto_scale:
            img1 = (img1 - expected_range[0]) / (expected_range[1] - expected_range[0])
            img2 = (img2 - expected_range[0]) / (expected_range[1] - expected_range[0])
            expected_range = (0.0, 1.0)

        # Final range check
        for img, name in [(img1, "Image1"), (img2, "Image2")]:
            current_min, current_max = np.min(img), np.max(img)
            if current_min < expected_range[0] - 1e-6 or current_max > expected_range[1] + 1e-6:
                raise ValueError(
                    f"{name} pixel range violation: "
                    f"Expected [{expected_range[0]:.2f}, {expected_range[1]:.2f}], "
                    f"got [{current_min:.2f}, {current_max:.2f}]"
                )

        return img1, img2

# # Example usage
# if __name__ == "__main__":
#   pass