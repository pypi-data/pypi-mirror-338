#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  distancia.py
#  
"""
MIT License

Copyright (c) 2025 Yves Mercadier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from .mainClass import Distance
#from .tools import Matrix
from .vectorDistance import *
from .matrixDistance import *
from .lossFunction import *
from .timeSeriesDistance import *
from .textDistance import *
from .fileDistance import *
from .imageDistance import *
from .soundDistance import *

class CustomDistanceFunction:
    """
    A class to compute custom distance between two data points using a user-defined function.
    """

    def __init__(self, func=Euclidean()):
        """
        Initialize the CustomDistanceFunction class with a user-defined function.

        Parameters:
        func (function): A function that takes two inputs (data points) and returns a distance metric.
        """
        if not callable(func):
            raise ValueError("The provided custom function must be callable.")
        self.func = func

    def compute(self, data1, data2):
        """
        Compute the distance between two data points using the custom function.

        Parameters:
        data1: The first data point.
        data2: The second data point.

        Returns:
        The result of the custom function applied to data1 and data2.
        """
        return self.func(data1, data2)

try:
    import pandas as pd
    pandas_installed = True

except ImportError:
    pd = None
try:
    import numpy as np
    numpy_installed = True

except ImportError:
    np = None

class IntegratedDistance:
    def __init__(self, func=Euclidean()):
        """
        Initialize the IntegratedDistance class with a distance function.
        
        Parameters:
        func (callable): A function that takes two points and returns a distance. 
                         Default is Euclidean distance.
        """
        self.func = func
        if not pandas_installed:
          raise ImportError("IntegratedDistance need pandas. Install pandas 'pip install pandas'.")
        if not numpy_installed:
          raise ImportError("IntegratedDistance need numpy. Install numpy 'pip install numpy'.")

    def compute(self, point1, point2):
        """
        Compute the distance between two points using the specified distance function.
        
        Parameters:
        point1, point2: The points between which to compute the distance. Can be tuples, lists, or numpy arrays.
        
        Returns:
        float: The computed distance.
        """
        return self.func(point1, point2)

    def apply_to_dataframe(self, df, col1, col2, result_col='distance'):
        """
        Apply the distance function to columns of a pandas DataFrame.
        
        Parameters:
        df (pandas.DataFrame): The DataFrame containing the points.
        col1 (str): The name of the first column containing the points.
        col2 (str): The name of the second column containing the points.
        result_col (str): The name of the column to store the computed distances.
        
        Returns:
        pandas.DataFrame: The DataFrame with an additional column containing the distances.
        """
        df[result_col] = df.apply(lambda row: self.compute(row[col1], row[col2]), axis=1)
        return df

    def apply_to_sklearn(self, X, Y=None):
        """
        Apply the distance function within a scikit-learn pipeline.
        
        Parameters:
        X (numpy array or pandas DataFrame): The data for which to compute distances.
        Y (numpy array or pandas DataFrame, optional): Another data set to compare with.
        
        Returns:
        numpy.array: An array of computed distances.
        """
        if Y is None:
            Y = X
        
        distances = np.zeros((X.shape[0], Y.shape[0]))
        for i in range(X.shape[0]):
            for j in range(Y.shape[0]):
                distances[i, j] = self.compute(X[i].tolist(), Y[j].tolist())
                
        return distances

class DistanceMatrix:
    def __init__(self, data_points, metric=Euclidean()):
        """
        Initializes the DistanceMatrix class.

        Parameters:
        - data_points: List or array-like, a collection of data points where each point is an iterable of coordinates.
        - metric: str, the distance metric to be used (e.g., 'euclidean', 'cosine', 'manhattan'). The metric must be one of the predefined metrics in the `distancia` package.
        """
        self.data_points = data_points
        self.metric = metric
        self.distance_matrix = self.compute_distance_matrix()

    def compute_distance_matrix(self):
        """
        Computes the distance matrix for the provided data points using the specified metric.

        Returns:
        - A 2D list representing the distance matrix where element (i, j) is the distance between data_points[i] and data_points[j].
        """
        num_points = len(self.data_points)
        matrix = [[0.0] * num_points for _ in range(num_points)]

        for i in range(num_points):
            for j in range(i + 1, num_points):
                distance = self.metric.compute(self.data_points[i], self.data_points[j])
                matrix[i][j] = distance
                matrix[j][i] = distance

        return matrix

    def get_matrix(self):
        """
        Returns the computed distance matrix.
        """
        return self.distance_matrix

import concurrent.futures
from functools import partial
import multiprocessing

class ParallelandDistributedComputation:
    def __init__(self, data_points, metric):
        """
        Initializes the ParallelDistanceCalculator with a set of data points and a distance metric.

        :param data_points: A list or array of data points.
        :param metric: A callable that computes the distance between two data points.
        """
        self.data_points = data_points
        self.metric = metric

    def compute_distances_parallel(self, reference_point=None, max_workers=None, use_multiprocessing=False):
        """
        Computes distances in parallel between the reference point and all data points or pairwise among all data points.

        :param reference_point: A single data point to compare with all other data points. 
                                If None, computes pairwise distances among all data points.
        :param max_workers: The maximum number of workers to use for parallel computation.
                            If None, it will use the number of processors on the machine.
        :param use_multiprocessing: If True, uses multiprocessing for parallel computation.
                                    If False, uses multithreading.
        :return: A list of computed distances.
        """
        if reference_point is not None:
            compute_func = partial(self.metric.calculate, reference_point)
            data_iterable = self.data_points
        else:
            data_iterable = ((self.data_points[i], self.data_points[j]) for i in range(len(self.data_points)) for j in range(i + 1, len(self.data_points)))
            compute_func = lambda pair: self.metric.calculate(*pair)

        if use_multiprocessing:
            with multiprocessing.Pool(processes=max_workers) as pool:
                distances = pool.map(compute_func, data_iterable)
        else:
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                distances = list(executor.map(compute_func, data_iterable))

        return distances

from collections import defaultdict

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

try:
    import seaborn as sns
except ImportError:
    sns = None

try:
    from scipy.cluster.hierarchy import dendrogram, linkage
except ImportError:
    dendrogram = None
    linkage = None

try:
    from sklearn.decomposition import PCA
except ImportError:
    PCA = None
    
class OutlierDetection:
    def __init__(self, data_points, metric=Euclidean(), threshold=2.0):
        """
        Initialize the OutlierDetection class.

        :param data_points: A list of data points, where each data point is a list or tuple of numeric values.
        :param metric: The distance metric to use for outlier detection. Supported metrics: 'euclidean', 'manhattan', 'mahalanobis'.
        :param threshold: The threshold value for determining outliers. Points with distances greater than this threshold times the standard deviation from the centroid are considered outliers.
        """
        if plt==None:
          raise ImportError("OutlierDetection need matplotlib. Install matplotlib 'pip install matplotlib'.")
        if dendrogram==None:
          raise ImportError("OutlierDetection need scipy. Install scipy 'pip install scipy'.")
        if sns==None:
          raise ImportError("OutlierDetection need seaborn. Install seaborn 'pip install seaborn'.")
        if PCA==None:
          raise ImportError("OutlierDetection need sklearn. Install sklearn 'pip install scikit-learn'.")
          
        self.data_points = data_points
        self.metric = metric
        self.threshold = threshold
        self.centroid = self._calculate_centroid()
        self.distances = self._calculate_distances()

    def _calculate_centroid(self):
        """
        Calculate the centroid of the data points.

        :return: The centroid as a list of numeric values.
        """
        n = len(self.data_points)
        centroid = [sum(dim)/n for dim in zip(*self.data_points)]
        return centroid

    def _calculate_distances(self):
        """
        Calculate the distances of all points from the centroid using the specified metric.

        :return: A list of distances as floats.
        """
        distances = []
        for point in self.data_points:
            distance = self.metric.calculate(point, self.centroid)
            distances.append(distance)
        return distances

    def detect_outliers(self):
        """
        Detect outliers based on the distance from the centroid.

        :return: A list of outliers, where each outlier is a tuple containing the point and its distance from the centroid.
        """
        mean_distance = sum(self.distances) / len(self.distances)
        std_distance = (sum((d - mean_distance) ** 2 for d in self.distances) / len(self.distances))**0.5

        outliers = []
        for i, distance in enumerate(self.distances):
            if distance > mean_distance + self.threshold * std_distance:
                outliers.append((self.data_points[i], distance))

        return outliers


    
class BatchDistance:
    def __init__(self, points_a, points_b, metric):
        """
        Initialize the BatchDistance class with two sets of points and a distance metric.

        :param points_a: A list of tuples representing the first set of points.
        :param points_b: A list of tuples representing the second set of points.
        :param metric: A string representing the distance metric to be used ('euclidean', 'manhattan', etc.).
        """
        self.points_a = points_a
        self.points_b = points_b
        self.metric = metric

    def compute_batch(self):
        """
        Compute the distances for all pairs in the two sets of points.

        :return: A list of distances for each pair of points.
        """
        if len(self.points_a) != len(self.points_b):
            raise ValueError("The two point sets must have the same length.")

        distances = []
        for point1, point2 in zip(self.points_a, self.points_b):
            distance = self.metric.calculate(point1, point2)
            distances.append(distance)

        return distances

import time

class ComprehensiveBenchmarking:
    def __init__(self, metrics, data, repeat=1):
        """
        Initialize the ComprehensiveBenchmarking class.

        :param metrics: List of metric functions to benchmark.
        :param data: The data points to use in the benchmarking.
        :param repeat: Number of times to repeat each metric calculation for averaging.
        """
        self.metrics = metrics
        self.data    = data
        self.repeat  = repeat
        self.results = {}

    def run_benchmark(self):
        """
        Run the benchmark for each metric on the provided data.

        :return: Dictionary with metrics as keys and their average computation time as values.
        """
        for metric in self.metrics:
            start_time = time.time()
            for _ in range(self.repeat):
                _ = [metric.calculate(x, y) for x, y in self.data]
            end_time = time.time()
            average_time = (end_time - start_time) / self.repeat
            self.results[metric.__class__.__name__] = average_time

        return self.results

    def print_results(self):
        """
        Print the benchmarking results in a readable format.
        """
        for metric, time_taken in self.results.items():
            print(f"Metric: {metric}, Average Time: {time_taken:.6f} seconds")
#claude ai
from typing import List, Tuple, Set, Optional
from dataclasses import dataclass
import random
import math
import matplotlib.pyplot as plt

@dataclass
class Point:
    """Represents a data point with features and label"""
    features: List[float]
    label: int

class LMNN:
    """
    Pure Python implementation of Large Margin Nearest Neighbor classifier.
    This implementation avoids using NumPy and other external libraries.
    """
    
    def __init__(
        self, 
        k: int = 3, 
        max_iter: int = 100, 
        learning_rate: float = 0.01, 
        tol: float = 1e-6
    ) -> None:
        """
        Initialize LMNN classifier
        
        Args:
            k: Number of target neighbors
            max_iter: Maximum iterations for optimization
            learning_rate: Learning rate for gradient descent
            tol: Convergence tolerance
        """
        self.k = k
        self.max_iter = max_iter
        self.learning_rate = learning_rate
        self.tol = tol
        self.transformation_matrix: Optional[Matrix] = None

    def _euclidean_distance(self, p1: List[float], p2: List[float]) -> float:
        """Calculate Euclidean distance between two points"""
        if len(p1) != len(p2):
            raise ValueError("Points must have same dimension")
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

    def _find_target_neighbors(
        self, 
        points: List[Point]
    ) -> List[Set[int]]:
        """Find k nearest neighbors of same class for each point"""
        n_points = len(points)
        neighbors: List[Set[int]] = [set() for _ in range(n_points)]
        
        for i in range(n_points):
            # Find points of same class
            same_class = [
                (j, self._euclidean_distance(
                    points[i].features, 
                    points[j].features
                ))
                for j in range(n_points)
                if points[j].label == points[i].label and i != j
            ]
            
            # Sort by distance and take k nearest
            same_class.sort(key=lambda x: x[1])
            neighbors[i].update(j for j, _ in same_class[:self.k])
            
        return neighbors

    def _transform_point(self, point: List[float]) -> List[float]:
        """Apply transformation matrix to point"""
        if self.transformation_matrix is None:
            raise ValueError("Transformation matrix not initialized")
        
        point_matrix = Matrix(1, len(point), [point])
        result = point_matrix * self.transformation_matrix
        return result.data[0]

    def fit(self, points: List[Point]) -> 'LMNN':
        """
        Fit LMNN model to training data using gradient descent
        
        Args:
            points: List of training points with features and labels
        """
        if not points:
            raise ValueError("Empty training set")
            
        n_features = len(points[0].features)
        self.transformation_matrix = Matrix.identity(n_features)
        
        target_neighbors = self._find_target_neighbors(points)
        
        # Simple gradient descent optimization
        for _ in range(self.max_iter):
            # Transform all points
            transformed_points = [
                self._transform_point(p.features) for p in points
            ]
            
            # Calculate gradient
            gradient = Matrix(n_features, n_features)
            loss = 0.0
            
            # Compute pull term (attract target neighbors)
            for i, neighbors in enumerate(target_neighbors):
                for j in neighbors:
                    dist = self._euclidean_distance(
                        transformed_points[i],
                        transformed_points[j]
                    )
                    loss += dist ** 2
            
            # Update transformation matrix using gradient
            for i in range(n_features):
                for j in range(n_features):
                    self.transformation_matrix.data[i][j] -= (
                        self.learning_rate * gradient.data[i][j]
                    )
            
            if loss < self.tol:
                break
                
        return self

    def transform(self, features: List[List[float]]) -> List[List[float]]:
        """
        Transform data using learned transformation matrix
        
        Args:
            features: List of feature vectors to transform
            
        Returns:
            Transformed feature vectors
        """
        if self.transformation_matrix is None:
            raise ValueError("Model not fitted yet")
            
        return [self._transform_point(f) for f in features]

    def fit_transform(self, points: List[Point]) -> List[List[float]]:
        """Fit model and transform training data"""
        self.fit(points)
        return self.transform([p.features for p in points])

class DistanceMetricLearning:
    def __init__(self, data, labels, method='lmnn', **kwargs):
        """
        Initialize the DistanceMetricLearning class.

        Parameters:
        - data: array-like, shape (n_samples, n_features)
            The input data points.
        - labels: array-like, shape (n_samples,)
            The class labels or targets associated with the data points.
        - method: str, optional (default='lmnn')
            The distance metric learning method to use. Options are 'lmnn', 'itml', 'nca', etc.
        - kwargs: additional keyword arguments specific to the chosen method.
        """
        self.data = data
        self.labels = labels
        self.method = method.lower()
        self.kwargs = kwargs
        self.metric = None

    def fit(self):
        """
        Fit the distance metric to the data using the specified method.
        """
        if self.method == 'lmnn':
            self.metric = self._learn_lmnn()
        elif self.method == 'itml':
            self.metric = self._learn_itml()
        elif self.method == 'nca':
            self.metric = self._learn_nca()
        else:
            raise ValueError(f"Method {self.method} is not supported.")
    
    def transform(self, X):
        """
        Transform the data using the learned metric.

        Parameters:
        - X: array-like, shape (n_samples, n_features)
            The data to transform.

        Returns:
        - X_transformed: array-like, shape (n_samples, n_features)
            The data transformed using the learned metric.
        """
        if self.metric is None:
            raise ValueError("The model needs to be fitted before transformation.")
        return self.metric.transform(X)
    
    def _learn_lmnn(self):
        # Placeholder function for learning LMNN
        # In practice, you would use a library like metric-learn, or implement LMNN from scratch.
        lmnn = LMNN(**self.kwargs)
        lmnn.fit(self.data, self.labels)
        return lmnn

    def _learn_itml(self):
        # Placeholder function for learning ITML
        from metric_learn import ITML
        itml = ITML(**self.kwargs)
        itml.fit(self.data, self.labels)
        return itml

    def _learn_nca(self):
        # Placeholder function for learning NCA
        from sklearn.neighbors import NeighborhoodComponentsAnalysis
        nca = NeighborhoodComponentsAnalysis(**self.kwargs)
        nca.fit(self.data, self.labels)
        return nca

    def get_metric(self):
        """
        Get the learned metric.
        
        Returns:
        - metric: the learned metric object
        """
        if self.metric is None:
            raise ValueError("The model needs to be fitted before accessing the metric.")
        return self.metric

class MetricFinder:
    def __init__(self):
        """
        Initialize the MetricFinder class.
        """
        self.list_metric=[]

    def find_metric(self, point1, point2):
        """
        Determines the most appropriate metric for the given points based on their structure.

        Parameters:
        point1: The first point (can be a list, string, or other iterable).
        point2: The second point (can be a list, string, or other iterable).

        Returns:
        str: The name of the most appropriate metric.
        """
        if isinstance(point1, str) and isinstance(point2, str):self.find_string_metric(point1, point2)
        elif isinstance(point1, (list)) and isinstance(point2, (list)):
            self.list_metric.append(LongestCommonSubsequence().__class__.__name__)

            if all(isinstance(x, (tuple)) for x in point1) and all(isinstance(x, (tuple)) for x in point2):
                self.list_metric.append(Frechet().__class__.__name__)

            if all(isinstance(x, (float,int)) for x in point1) and all(isinstance(x, (float,int)) for x in point2):
                if len(point1)==len(point2):
                    self.list_metric.append(Euclidean().__class__.__name__)
                    self.list_metric.append(Manhattan().__class__.__name__)
                    self.list_metric.append(Minkowski().__class__.__name__)
                    self.list_metric.append(L1().__class__.__name__)
                    self.list_metric.append(L2().__class__.__name__)
                    self.list_metric.append(Canberra().__class__.__name__)
                    self.list_metric.append(BrayCurtis().__class__.__name__)
                    self.list_metric.append(Gower().__class__.__name__)
                    self.list_metric.append(Pearson().__class__.__name__)
                    self.list_metric.append(Spearman().__class__.__name__)
                    self.list_metric.append(CzekanowskiDice().__class__.__name__)
                    self.list_metric.append(MotzkinStraus().__class__.__name__)
                    self.list_metric.append(EnhancedRogersTanimoto().__class__.__name__)
                    self.list_metric.append(DynamicTimeWarping().__class__.__name__)
                    self.list_metric.append(CosineInverse().__class__.__name__)
                    self.list_metric.append(Cosine().__class__.__name__)
                    self.list_metric.append(GeneralizedJaccard().__class__.__name__)
                    self.list_metric.append(Chebyshev().__class__.__name__)
                    

            if all(isinstance(x, (int)) for x in point1) and all(isinstance(x, (int)) for x in point2):
                    self.list_metric.append(KendallTau().__class__.__name__)
                    
            if all(check_bin(x) for x in point1) and all(check_bin(x) for x in point2) and len(point1)==len(point2):
                    self.list_metric.append(Kulsinski().__class__.__name__)
                    self.list_metric.append(Yule().__class__.__name__)
                    self.list_metric.append(RogersTanimoto().__class__.__name__)
                    self.list_metric.append(SokalMichener().__class__.__name__)
                    self.list_metric.append(SokalSneath().__class__.__name__)
            if all(check_probability(x) for x in point1) and all(check_probability(x) for x in point2) and len(point1)==len(point2):
                    self.list_metric.append(CrossEntropy().__class__.__name__)
                    self.list_metric.append(MeanAbsoluteError().__class__.__name__)
                    self.list_metric.append(MAE().__class__.__name__)
                    self.list_metric.append(MeanAbsolutePercentageError().__class__.__name__)
                    self.list_metric.append(MAPE().__class__.__name__)
                    self.list_metric.append(MeanSquaredError().__class__.__name__)
                    self.list_metric.append(MSE().__class__.__name__)
                    self.list_metric.append(SquaredLogarithmicError().__class__.__name__)
                    self.list_metric.append(SLE().__class__.__name__)
                    self.list_metric.append(KullbackLeibler().__class__.__name__)
                    self.list_metric.append(Bhattacharyya().__class__.__name__)
                    self.list_metric.append(Hellinger().__class__.__name__)
                    self.list_metric.append(Wasserstein().__class__.__name__)
        elif isinstance(point1, (set)) and isinstance(point2, (set)):
                if all(isinstance(x, (float,int)) for x in point1) and all(isinstance(x, (float,int)) for x in point2):
                    self.list_metric.append(InverseTanimoto().__class__.__name__)
                    self.list_metric.append(Tanimoto().__class__.__name__)
                    self.list_metric.append(Dice().__class__.__name__)
                    self.list_metric.append(Kulsinski().__class__.__name__)
                    self.list_metric.append(Tversky().__class__.__name__)
                    self.list_metric.append(FagerMcGowan().__class__.__name__)
                    self.list_metric.append(FagerMcGowan().__class__.__name__)
                    self.list_metric.append(Hausdorff().__class__.__name__)
                if all(isinstance(x, (bool)) for x in point1) and all(isinstance(x, (bool)) for x in point2):
                    self.list_metric.append(Ochiai().__class__.__name__)

        return self.list_metric

    def find_string_metric(self, str1, str2):
        """
        Determines the appropriate string-based metric.

        Parameters:
        str1: The first string.
        str2: The second string.

        Returns:
        str: The name of the most appropriate string metric.
        """
        if len(str1) == len(str2):
            if str1.isdigit() and str2.isdigit():
                self.list_metric.append(Hamming().__class__.__name__)
                self.list_metric.append(Matching().__class__.__name__)
        
        self.list_metric.append(Jaro().__class__.__name__)
        self.list_metric.append(JaroWinkler().__class__.__name__)
        self.list_metric.append(Levenshtein().__class__.__name__)
        self.list_metric.append(DamerauLevenshtein().__class__.__name__)
        self.list_metric.append(RatcliffObershelp().__class__.__name__)
        self.list_metric.append(SorensenDice().__class__.__name__)
        self.list_metric.append(Otsuka().__class__.__name__)
        



    def find_similarity_metric(self, point1, point2):
        """
        Determines the most appropriate similarity metric for the given points.

        Parameters:
        point1: The first point (can be a list, string, or other iterable).
        point2: The second point (can be a list, string, or other iterable).

        Returns:
        str: The name of the most appropriate similarity metric.
        """
        if isinstance(point1, str) and isinstance(point2, str):
            return "Jaccard Similarity"
        elif isinstance(point1, (list, tuple)) and isinstance(point2, (list, tuple)):
            if all(isinstance(x, (int, float)) for x in point1) and all(isinstance(x, (int, float)) for x in point2):
                return "Cosine Similarity"
        return "Unknown Similarity Metric"



import json
try:
    from flask import Flask, jsonify
except ImportError:
    Flask = None
    request = None
    jsonify = None

#app = Flask(__name__)
def create_flask_app():
    if Flask is None:
        raise ImportError(
            "APICompatibility need Flask. Install Flask : pip install flask"
        )
    return Flask(__name__)
    
class APICompatibility:
    def __init__(self, distance_metric):
        """
        Initialize with a specific distance metric.
        
        :param distance_metric: A function or class from the distancia package, e.g., EuclideanDistance
        """
        self.distance_metric = distance_metric
    
    def rest_endpoint(self, host="0.0.0.0", port=5000):
        """
        Set up a REST API endpoint using Flask.
        
        :param host: Host IP address for the REST service.
        :param port: Port number for the REST service.
        """
        app=create_flask_app()   

        @app.route('/calculate_distance', methods=['POST'])
        def calculate_distance():
            data = request.json
            point1 = data['point1']
            point2 = data['point2']
            distance = self.distance_metric(point1, point2)
            return jsonify({"distance": distance})

        app.run(host=host, port=port)

class AutomatedDistanceMetricSelection:
    def __init__(self, metrics=None):
        """
        Initialize the selector with a list of potential distance metrics.
        
        :param metrics: List of distance metric classes or functions to choose from.
        """
        if metrics is None:
            self.metrics = [
                Euclidean(),
                Cosine(),
                Manhattan(),
                Jaccard(),
                Mahalanobis(),
                DynamicTimeWarping(),
                Frechet(),
                # Add other metrics as needed
            ]
        else:
            self.metrics = metrics
    
    def select_metric(self, data):
        """
        Automatically select the best distance metric based on data characteristics.
        
        :param data: The data to analyze (e.g., a numpy array or pandas DataFrame).
        :return: The selected distance metric class/function.
        """
        # Example heuristic based on data characteristics
        if self.is_high_dimensional(data):
            return CosineSimilarity()
        elif self.is_binary_data(data):
            return Jaccard()
        elif self.has_outliers(data):
            return Manhattan()
        elif self.is_time_series(data):
            return DynamicTimeWarping()
        else:
            # Default choice if no specific conditions are met
            return Euclidean()

    def is_high_dimensional(self, data):
        """Heuristic: Check if the data is high-dimensional."""
        return data.shape[1] > 50

    def is_binary_data(self, data):
        """Heuristic: Check if the data consists of binary values."""
        return np.array_equal(data, data.astype(bool))

    def has_outliers(self, data):
        """Heuristic: Check if the data has significant outliers."""
        q1, q3 = np.percentile(data, [25, 75], axis=0)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        return np.any((data < lower_bound) | (data > upper_bound))

    def is_time_series(self, data):
        """Heuristic: Check if the data is time-series data."""
        # Simple heuristic: time series often have more rows than columns
        return data.shape[0] > data.shape[1]

class StatisticalAnalysis:
    def __init__(self, distance_function):
        """
        Initializes the StatisticalAnalysis class with a distance function.
        
        :param distance_function: A function that computes the distance between two points.
        """
        self.distance_function = distance_function

    def mean_distance(self, dataset):
        """
        Computes the mean distance between all pairs of points in a given dataset.
        
        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :return: The mean distance between all pairs of points.
        """
        n = len(dataset)
        if n < 2:
            return 0

        total_distance = 0
        num_pairs = 0

        for i in range(n):
            for j in range(i + 1, n):

                total_distance += self.distance_function(dataset[i], dataset[j])
                num_pairs += 1

        return total_distance / num_pairs

    def variance_distance(self, dataset):
        """
        Calculates the variance of the distances in the dataset.
        
        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :return: The variance of the distances between all pairs of points.
        """
        n = len(dataset)
        if n < 2:
            return 0
        mean_dist = self.mean_distance(dataset)

        total_squared_diff = 0
        num_pairs = 0

        for i in range(n):
            for j in range(i + 1, n):

                distance = self.distance_function(dataset[i], dataset[j])
                total_squared_diff += (distance - mean_dist) ** 2
                num_pairs += 1

        return total_squared_diff / num_pairs

    def distance_distribution(self, dataset, bins=10):
        """
        Returns a distribution (e.g., histogram) of the distances within the dataset.
        
        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param bins: The number of bins to use for the histogram.
        :return: A histogram of the distances within the dataset.
        """
        from collections import Counter
        
        n = len(dataset)
        if n < 2:
            return {}

        distances = []
        for i in range(n):
            for j in range(i + 1, n):
                distance = self.distance_function(dataset[i], dataset[j])
                distances.append(distance)

        min_dist = min(distances)
        max_dist = max(distances)
        bin_width = (max_dist - min_dist) / bins
        
        histogram = Counter((int((dist - min_dist) / bin_width) for dist in distances))
        return {min_dist + bin * bin_width: count for bin, count in histogram.items()}

    def correlation_with_other_metric(self, dataset, other_metric):
        """
        Calculates the correlation between the current distance metric and another distance metric.
        
        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param other_metric: A function that computes the distance between two points, used for comparison.
        :return: The Pearson correlation coefficient between the two metrics.
        """

        n = len(dataset)
        if n < 2:
            return 0

        distances_self = []
        distances_other = []

        for i in range(n):
            for j in range(i + 1, n):

                distances_self.append(self.distance_function(dataset[i], dataset[j]))
                distances_other.append(other_metric(dataset[i], dataset[j]))
        total = 0
        for num in distances_self:
          total += num
        mean_self = total / len(distances_self)
        total = 0
        for num in distances_other:
          total += num
        mean_other = total / len(distances_other)

        sum_covariance = 0
        sum_self_variance = 0
        sum_other_variance = 0

        for d_self, d_other in zip(distances_self, distances_other):
            sum_covariance += (d_self - mean_self) * (d_other - mean_other)
            sum_self_variance += (d_self - mean_self) ** 2
            sum_other_variance += (d_other - mean_other) ** 2

        return sum_covariance / (sum_self_variance * sum_other_variance)**0.5


#import matplotlib.pyplot as plt
#import seaborn as sns
import itertools

class Visualization:
    def __init__(self, distance_function):
        """
        Initializes the Visualization class with a distance function.

        :param distance_function: A function that computes the distance between two points.
        """
        self.distance_function = distance_function

    def plot_distance_matrix(self, dataset):
        """
        Generates a heatmap or other visual representation of the distance matrix for a given dataset.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        """
        n = len(dataset)
        distance_matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                distance_matrix[i][j] = self.distance_function(dataset[i], dataset[j])

        plt.figure(figsize=(8, 6))
        sns.heatmap(distance_matrix, annot=True, cmap="YlGnBu", square=True, cbar=True)
        plt.title("Distance Matrix Heatmap")
        plt.show()

    def plot_distance_histogram(self, dataset, bins=10):
        """
        Plots a histogram of distances between all pairs in the dataset.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param bins: The number of bins to use for the histogram.
        """
        distances = []

        for i, j in itertools.combinations(range(len(dataset)), 2):
            distance = self.distance_function(dataset[i], dataset[j])
            distances.append(distance)

        plt.figure(figsize=(8, 6))
        plt.hist(distances, edgecolor='black',bins=bins, alpha=0.7, color='blue')
        plt.title("Distance Histogram")
        plt.xlabel("Distance")
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.show()

    def plot_similarity_matrix(self, dataset, metric=Jaccard()):
        """
        Generates a heatmap for the similarity matrix, if the metric is a similarity measure.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        """
        n = len(dataset)
        similarity_matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                similarity_matrix[i][j] = 1 / (1 + metric.similarity(dataset[i], dataset[j]))

        plt.figure(figsize=(8, 6))
        sns.heatmap(similarity_matrix, annot=True, cmap="YlGnBu", square=True, cbar=True)
        plt.title("Similarity Matrix Heatmap")
        plt.show()
    '''    
    def compute_distance_matrix(self, dataset):
        """
        Computes the distance matrix for the given dataset using the provided distance function.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :return: A distance matrix.
        """
        n = len(dataset)
        distance_matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j:
                    distance_matrix[i][j] = self.distance_function(dataset[i], dataset[j])

        return distance_matrix
    '''
    def find_clusters(self, distance_matrix):
        """
        Performs hierarchical clustering using a single-linkage approach.

        :param distance_matrix: The precomputed distance matrix.
        :return: A list of clusters and distances at which they were merged.
        """
        clusters = [[i] for i in range(len(distance_matrix))]
        distances = []

        while len(clusters) > 1:
            min_dist = float('inf')
            to_merge = None

            for i in range(len(clusters)):
                for j in range(i + 1, len(clusters)):
                    # Find the minimum distance between two clusters
                    for a in clusters[i]:
                        for b in clusters[j]:
                            if distance_matrix[a][b] < min_dist:
                                min_dist = distance_matrix[a][b]
                                to_merge = (i, j)

            # Merge the closest clusters
            distances.append(min_dist)
            i, j = to_merge
            clusters[i] += clusters[j]
            clusters.pop(j)

        return clusters, distances

    def plot_dendrogram(self, dataset):
        """
        Generates a dendrogram plot for hierarchical clustering.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        """
        #distance_matrix = self.compute_distance_matrix(dataset)
        #clusters, distances = self.find_clusters(distance_matrix)
        # Standardiser les données (important pour le clustering hiérarchique)
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(dataset)

        # Créer une instance de la classe et générer le dendrogramme
        dendrogram_plotter = PlotDendrogram(method='ward')
        dendrogram_plotter.fit(X_scaled)
        dendrogram_plotter.plot()

    def plot_pca(self, dataset, n_components=2):
        """
        Generates a PCA scatter plot to visualize data in reduced dimensions.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param n_components: The number of principal components to consider.
        """
        # Center the data
        mean = [sum(col) / len(col) for col in zip(*dataset)]
        centered_data = [[x - m for x, m in zip(point, mean)] for point in dataset]

        # Calculate covariance matrix
        n = len(centered_data)
        cov_matrix = [[sum(centered_data[i][k] * centered_data[j][k] for k in range(len(centered_data[0]))) / (n - 1)
                       for j in range(len(centered_data[0]))] for i in range(len(centered_data[0]))]

        # Eigenvalue decomposition
        eigenvalues, eigenvectors = self.eigen_decomposition(cov_matrix)
        
        # Select top n_components eigenvectors
        principal_components = [eigenvectors[i] for i in range(n_components)]
        
        # Project the data onto the principal components
        reduced_data = [[sum(point[k] * pc[k] for k in range(len(pc))) for pc in principal_components] for point in centered_data]

        # Plot the PCA result
        plt.figure(figsize=(8, 6))
        plt.scatter([row[0] for row in reduced_data], [row[1] for row in reduced_data], c='blue', marker='o')
        plt.title('PCA Scatter Plot')
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
        plt.grid(True)
        plt.show()

    def eigen_decomposition(self, matrix):
        """
        Computes the eigenvalues and eigenvectors of a square matrix.

        :param matrix: The square matrix to decompose.
        :return: A tuple of (eigenvalues, eigenvectors).
        """
        # Using the power iteration method to find the dominant eigenvalue and corresponding eigenvector
        def power_iteration(matrix, num_simulations: int):
            b_k = [1.0] * len(matrix)
            for _ in range(num_simulations):
                # calculate the matrix-by-vector product Ab
                b_k1 = [sum(matrix[i][j] * b_k[j] for j in range(len(matrix))) for i in range(len(matrix))]

                # calculate the norm
                b_k1_norm = math.sqrt(sum(x ** 2 for x in b_k1))

                # re normalize the vector
                b_k = [x / b_k1_norm for x in b_k1]

            # Rayleigh quotient gives the eigenvalue
            eigenvalue = sum(b_k[i] * sum(matrix[i][j] * b_k[j] for j in range(len(matrix))) for i in range(len(matrix)))
            eigenvector = b_k

            return eigenvalue, eigenvector

        # Compute the eigenvalues and eigenvectors for a symmetric matrix
        eigenvalues = []
        eigenvectors = []

        for _ in range(len(matrix)):
            eigenvalue, eigenvector = power_iteration(matrix, 100)
            eigenvalues.append(eigenvalue)
            eigenvectors.append(eigenvector)

            # Deflate the matrix
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    matrix[i][j] -= eigenvalue * eigenvector[i] * eigenvector[j]

        return eigenvalues, eigenvectors
	
#import matplotlib.pyplot as plt
try:
    from scipy.cluster.hierarchy import dendrogram, linkage
except ImportError:
    dendrogram = None
    linkage = None
    
try:
    from sklearn.datasets import load_iris
    from sklearn.preprocessing import StandardScaler

except ImportError:
    load_iris = None
    StandardScaler = None

class PlotDendrogram:
    def __init__(self, method='ward'):
        """
        Initialise la classe avec la méthode de linkage pour le clustering hiérarchique.
        
        :param method: Méthode de linkage à utiliser ('ward', 'single', 'complete', 'average').
        """
        if dendrogram == None or linkage == None:
          raise ImportError("PlotDendrogram need scipy. Install scipy 'pip install scipy'.")
        if load_iris == None or StandardScaler == None:
          raise ImportError("PlotDendrogram need load_iris and StandardScaler. Install sklearn 'pip install sikit-learn'.")
        self.method = method

    def fit(self, X):
        """
        Prépare les données pour le dendrogramme en effectuant un linkage hiérarchique.
        
        :param X: Les données à clusteriser (généralement standardisées).
        """
        # Calculer la matrice de linkage
        self.linkage_matrix = linkage(X, method=self.method)

    def plot(self):
        """
        Affiche le dendrogramme à partir de la matrice de linkage calculée.
        """
        # Vérifier si la matrice de linkage a été calculée
        if not hasattr(self, 'linkage_matrix'):
            raise ValueError("Veuillez d'abord exécuter la méthode 'fit' avec vos données.")

        # Créer le dendrogramme
        plt.figure(figsize=(10, 7))
        dendrogram(self.linkage_matrix)
        plt.title(f'Dendrogram using {self.method} linkage')
        plt.xlabel('Sample index')
        plt.ylabel('Distance')
        plt.show()

import random
import itertools

class ComparisonAndValidation:
    def __init__(self, distance_function):
        """
        Initializes the ComparisonAndValidation class with a distance function.

        :param distance_function: A function that computes the distance between two points.
        """
        self.distance_function = distance_function

    def compare_with_other_metric(self, dataset, other_metric):
        """
        Compares the results of the current metric with another metric, showing similarities and differences.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param other_metric: A function that computes the distance using another metric.
        :return: A comparison dictionary with the differences.
        """
        comparison_results = []
        for i, j in itertools.combinations(range(len(dataset)), 2):
            dist1 = self.distance_function(dataset[i], dataset[j])
            dist2 = other_metric(dataset[i], dataset[j])
            comparison_results.append({
                'pair': (i, j),
                'distance_1': dist1,
                'distance_2': dist2,
                'difference': abs(dist1 - dist2)
            })
        return comparison_results

    def cross_validation_score(self, dataset, labels,metric, k_folds=5):
        """
        Performs cross-validation using the current metric to assess its performance in clustering or classification tasks.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param labels: The true labels for the dataset points.
        :param k_folds: Number of folds to use in cross-validation.
        :return: The average cross-validation score.
        """
        fold_size = len(dataset) // k_folds
        scores = []

        for i in range(k_folds):
            test_indices = list(range(i * fold_size, (i + 1) * fold_size))
            train_indices = list(set(range(len(dataset))) - set(test_indices))

            train_data = [dataset[i] for i in train_indices]
            test_data = [dataset[i] for i in test_indices]
            train_labels = [labels[i] for i in train_indices]
            test_labels = [labels[i] for i in test_indices]

            # Simple Nearest Neighbor classifier for demonstration
            correct = 0
            for test_point, true_label in zip(test_data, test_labels):
                distances = [self.distance_function(test_point, train_point) for train_point in train_data]
                nearest_neighbor_index = distances.index(min(distances))
                predicted_label = train_labels[nearest_neighbor_index]

                if predicted_label == true_label:
                    correct += 1

            accuracy = correct / len(test_labels)
            scores.append(accuracy)

        return sum(scores) / len(scores)

    def evaluate_metric_on_benchmark(self, dataset, labels, benchmark_metric):
        """
        Tests the metric on a standardized benchmark dataset to evaluate its effectiveness in specific tasks.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param labels: The true labels for the dataset points.
        :param benchmark_metric: A function that represents the benchmark metric.
        :return: A dictionary with the benchmark evaluation results.
        """
        results = {
            'metric_performance': self.cross_validation_score(dataset, labels,self.distance_function),
            'benchmark_performance': self.cross_validation_score(dataset, labels, benchmark_metric)
        }

        return results

class DimensionalityReductionAndScaling:
    def __init__(self, distance_function):
        """
        Initializes the DimensionalityReductionAndScaling class with a distance function.

        :param distance_function: A function that computes the distance between two points.
        """
        self.distance_function = distance_function

    def metric_scaling(self, distance, multiplier):
        """
        Scales the distance by a given multiplier.

        :param distance: The original distance value.
        :param multiplier: The multiplier to scale the distance.
        :return: The scaled distance.
        """
        return distance * multiplier
    
    def compute_distance_matrix(self, dataset):
        """
        Computes the distance matrix for a given dataset.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :return: A 2D list representing the distance matrix.
        """
        n = len(dataset)
        distance_matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                distance = self.distance_function(dataset[i], dataset[j])
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance  # Symmetric matrix

        return distance_matrix
    
    def dimensionality_reduction_embedding(self, dataset, method='MDS', dimensions=2, max_iter=300, epsilon=1e-9):
        """
        Provides an embedding of the dataset in a lower-dimensional space using techniques like
        Multi-Dimensional Scaling (MDS) based on the computed distances.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param method: The dimensionality reduction method to use (default is 'MDS').
        :param dimensions: The number of dimensions for the reduced space (default is 2).
        :param max_iter: Maximum number of iterations for the MDS algorithm (default is 300).
        :param epsilon: Small value to check for convergence (default is 1e-9).
        :return: A list of points representing the dataset in the reduced dimensional space.
        """
        if method == 'MDS':
            return self._mds_embedding(dataset, dimensions, max_iter, epsilon)
        else:
            raise ValueError(f"Method '{method}' is not supported. Use 'MDS'.")

    def _mds_embedding(self, dataset, dimensions, max_iter, epsilon):
        """
        Performs Multi-Dimensional Scaling (MDS) to reduce the dimensionality of the dataset.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param dimensions: The number of dimensions for the reduced space.
        :param max_iter: Maximum number of iterations for the MDS algorithm.
        :param epsilon: Small value to check for convergence.
        :return: A list of points representing the dataset in the reduced dimensional space.
        """
        # Step 1: Compute the distance matrix
        distance_matrix = self.compute_distance_matrix(dataset)

        # Step 2: Initialize positions randomly
        import random
        positions = [[random.uniform(-1, 1) for _ in range(dimensions)] for _ in range(len(dataset))]

        # Step 3: Iterate to minimize the stress function
        for _ in range(max_iter):
            # Compute current distances in the embedding space
            embedded_distances = self.compute_distance_matrix(positions)

            # Compute the gradient and update positions
            stress = 0
            for i in range(len(dataset)):
                for j in range(len(dataset)):
                    if i != j:
                        delta = distance_matrix[i][j] - embedded_distances[i][j]
                        stress += delta ** 2

                        # Update positions based on gradient
                        for d in range(dimensions):
                            if embedded_distances[i][j] != 0:
                                positions[i][d] += delta * (positions[i][d] - positions[j][d]) / embedded_distances[i][j]

            # Check for convergence
            if stress < epsilon:
                break

        return positions


import math
import random

class AdvancedAnalysis:
    def __init__(self, distance_function):
        """
        Initializes the AdvancedAnalysis class with a distance function.

        :param distance_function: A function that computes the distance between two points.
        """
        self.distance_function = distance_function

    def sensitivity_analysis(self, dataset, perturbation):
        """
        Analyzes the sensitivity of the metric to small perturbations in the dataset.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param perturbation: The amount of perturbation to apply to each point in the dataset.
        :return: The average sensitivity of the metric to the perturbation.
        """
        original_distances = self._compute_average_distance(dataset)
        perturbed_dataset = self._perturb_dataset(dataset, perturbation)
        perturbed_distances = self._compute_average_distance(perturbed_dataset)
        
        sensitivity = abs(original_distances - perturbed_distances)
        return sensitivity

    def robustness_analysis(self, dataset, noise_level):
        """
        Evaluates the robustness of the metric under different levels of noise or missing data.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param noise_level: The amount of noise to introduce into the dataset.
        :return: The robustness score of the metric under noise.
        """
        noisy_dataset = self._add_noise_to_dataset(dataset, noise_level)
        original_distances = self._compute_average_distance(dataset)
        noisy_distances = self._compute_average_distance(noisy_dataset)
        
        robustness = abs(original_distances - noisy_distances)
        return robustness

    def entropy_of_distances(self, dataset):
        """
        Calculates the entropy or information content of the distance distribution in a dataset.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :return: The entropy of the distance distribution.
        """
        distances = self._compute_all_distances(dataset)
        frequency_distribution = self._compute_frequency_distribution(distances)
        
        entropy = -sum(p * math.log2(p) for p in frequency_distribution.values() if p > 0)
        return entropy

    def consistency_check_over_subsets(self, dataset, num_subsets=5):
        """
        Tests if the metric gives consistent results when applied to different subsets of the dataset.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param num_subsets: The number of random subsets to test (default is 5).
        :return: The consistency score (lower is better).
        """
        subset_distances = []
        for _ in range(num_subsets):
            subset = random.sample(dataset, k=len(dataset)//2)
            subset_distances.append(self._compute_average_distance(subset))
        
        consistency = max(subset_distances) - min(subset_distances)
        return consistency

    def _compute_average_distance(self, dataset):
        """
        Computes the average distance between all pairs of points in a dataset.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :return: The average distance.
        """
        n = len(dataset)
        total_distance = 0
        num_pairs = 0

        for i in range(n):
            for j in range(i + 1, n):
                total_distance += self.distance_function(dataset[i], dataset[j])
                num_pairs += 1
        
        return total_distance / num_pairs if num_pairs > 0 else 0

    def _compute_all_distances(self, dataset):
        """
        Computes the list of all pairwise distances in a dataset.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :return: A list of all pairwise distances.
        """
        distances = []
        n = len(dataset)

        for i in range(n):
            for j in range(i + 1, n):
                distances.append(self.distance_function(dataset[i], dataset[j]))

        return distances

    def _compute_frequency_distribution(self, distances):
        """
        Computes the frequency distribution of a list of distances.

        :param distances: A list of distances.
        :return: A dictionary representing the frequency distribution.
        """
        frequency_distribution = {}
        total = len(distances)

        for distance in distances:
            if distance not in frequency_distribution:
                frequency_distribution[distance] = 0
            frequency_distribution[distance] += 1

        # Convert frequencies to probabilities
        for key in frequency_distribution:
            frequency_distribution[key] /= total

        return frequency_distribution

    def _perturb_dataset(self, dataset, perturbation):
        """
        Applies a small perturbation to each point in the dataset.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param perturbation: The amount of perturbation to apply to each point.
        :return: The perturbed dataset.
        """
        perturbed_dataset = []
        for point in dataset:
            perturbed_point = [x + random.uniform(-perturbation, perturbation) for x in point]
            perturbed_dataset.append(perturbed_point)
        
        return perturbed_dataset

    def _add_noise_to_dataset(self, dataset, noise_level):
        """
        Adds noise to the dataset by randomly altering each point.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param noise_level: The amount of noise to introduce.
        :return: The noisy dataset.
        """
        noisy_dataset = []
        for point in dataset:
            noisy_point = [x + random.uniform(-noise_level, noise_level) for x in point]
            noisy_dataset.append(noisy_point)
        
        return noisy_dataset


import csv

class ReportingAndDocumentation:
    def __init__(self, distance_function, metric_name="Custom Metric"):
        """
        Initializes the ReportingAndDocumentation class with a distance function and a metric name.

        :param distance_function: A function that computes the distance between two points.
        :param metric_name: The name of the metric being analyzed.
        """
        self.distance_function = distance_function
        self.metric_name = metric_name

    def generate_metric_report(self, dataset):
        """
        Creates a comprehensive report on the behavior and performance of the metric on a given dataset,
        including basic statistics and a sample distance matrix.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :return: A string containing the comprehensive report.
        """
        report = f"Metric Report: {self.metric_name}\n"
        report += "=" * 40 + "\n\n"

        # Basic Information
        report += f"Dataset Size: {len(dataset)} points\n"
        report += f"Metric: {self.metric_name}\n\n"

        # Example Distance Computation
        report += "Example Distance Computation:\n"
        if len(dataset) > 1:
            report += f"Distance between first two points: {self.distance_function(dataset[0], dataset[1])}\n"
        else:
            report += "Dataset too small for distance computation.\n"

        # Distance Matrix Sample
        report += "\nSample Distance Matrix (first 5x5):\n"
        report += self._format_distance_matrix(dataset[:5])

        # Additional Analysis
        report += "\nBasic Statistical Analysis:\n"
        report += f"Mean Distance: {self._compute_mean_distance(dataset)}\n"
        report += f"Variance of Distances: {self._compute_variance_distance(dataset)}\n"

        return report

    def export_distance_matrix(self, dataset, file_format='csv', filename='distance_matrix.csv'):
        """
        Exports the computed distance matrix to a file in the specified format.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :param file_format: The file format for export ('csv' supported).
        :param filename: The name of the file to save the matrix.
        """
        if file_format == 'csv':
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                n = len(dataset)
                for i in range(n):
                    row = [self.distance_function(dataset[i], dataset[j]) for j in range(n)]
                    writer.writerow(row)
        else:
            raise ValueError("Unsupported file format. Only 'csv' is supported.")

    def document_metric_properties(self):
        """
        Generates a summary document that outlines the theoretical properties and practical applications
        of the selected metric.

        :return: A string containing the summary document.
        """
        document = f"Metric Documentation: {self.metric_name}\n"
        document += "=" * 40 + "\n\n"
        
        document += "1. Theoretical Background:\n"
        document += "   - The metric is based on the principle of ... (include metric-specific theory here).\n\n"
        
        document += "2. Metric Properties:\n"
        document += "   - Symmetry: ... (discuss whether the metric is symmetric).\n"
        document += "   - Positivity: ... (discuss whether the metric is positive definite).\n"
        document += "   - Triangle Inequality: ... (discuss whether the metric satisfies the triangle inequality).\n\n"
        
        document += "3. Practical Applications:\n"
        document += "   - Commonly used in ... (e.g., clustering, classification, etc.).\n"
        document += "   - Effective for ... (describe specific tasks where the metric is effective).\n\n"
        
        document += "4. Example Usage:\n"
        document += "   - The metric can be applied to ... (describe how the metric can be used in practical scenarios).\n\n"
        
        document += "5. References:\n"
        document += "   - (Include academic references and sources that discuss the metric.)\n"

        return document

    def _format_distance_matrix(self, dataset):
        """
        Formats a sample distance matrix for inclusion in the report.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :return: A string representation of a sample distance matrix.
        """
        matrix_str = ""
        n = len(dataset)
        for i in range(n):
            row = [self.distance_function(dataset[i], dataset[j]) for j in range(n)]
            matrix_str += "\t".join(f"{dist:.2f}" for dist in row) + "\n"
        return matrix_str

    def _compute_mean_distance(self, dataset):
        """
        Computes the mean distance between all pairs of points in a dataset.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :return: The mean distance as a float.
        """
        n = len(dataset)
        total_distance = 0
        num_pairs = 0

        for i in range(n):
            for j in range(i + 1, n):
                total_distance += self.distance_function(dataset[i], dataset[j])
                num_pairs += 1
        
        return total_distance / num_pairs if num_pairs > 0 else 0

    def _compute_variance_distance(self, dataset):
        """
        Computes the variance of distances between all pairs of points in a dataset.

        :param dataset: A list of points (each point is a list or tuple of coordinates).
        :return: The variance of distances as a float.
        """
        mean_distance = self._compute_mean_distance(dataset)
        n = len(dataset)
        variance_sum = 0
        num_pairs = 0

        for i in range(n):
            for j in range(i + 1, n):
                distance = self.distance_function(dataset[i], dataset[j])
                variance_sum += (distance - mean_distance) ** 2
                num_pairs += 1
        
        return variance_sum / num_pairs if num_pairs > 0 else 0
