#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tools.py
#  

def check_bin(str_):
    if str(str_) in "01":
        return True
    return False
    
def check_probability(number):
    if number>=0 and number <=1.0:
        return True
    else: return False
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def exp(x, terms=20):
    """
    Calculate the exponential of x using Taylor series expansion.
    
    Parameters:
    x (float): The exponent
    terms (int): Number of terms to use in the Taylor series (default: 20)
    
    Returns:
    float: An approximation of e^x
    """
    result = 0
    for n in range(terms):
        result += x**n / factorial(n)
    return result
    
def sin(x, terms=10):
    x = x % (2 * 3.141592653589793)  # réduction de l'angle à une période
    result = 0
    for n in range(terms):
        numerator = ((-1) ** n) * (x ** (2 * n + 1))
        denominator = factorial(2 * n + 1)
        result += numerator / denominator
    return result
    
def cos(x, terms=10):
    x = x % (2 * 3.141592653589793)  # réduction de l'angle à une période
    result = 0
    for n in range(terms):
        numerator = ((-1) ** n) * (x ** (2 * n))
        denominator = factorial(2 * n)
        result += numerator / denominator
    return result
    
def degrees_to_radians(degrees):
    pi = 3.141592653589793
    radians = degrees * (pi / 180)
    return radians
    
def atan(x, terms=10):
    result = 0
    for n in range(terms):
        result += ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
    return result

def atan2(y, x, terms=10):
    if x > 0:
        return atan(y / x, terms)
    elif x < 0 and y >= 0:
        return atan(y / x, terms) + 3.141592653589793
    elif x < 0 and y < 0:
        return atan(y / x, terms) - 3.141592653589793
    elif x == 0 and y > 0:
        return 3.141592653589793 / 2
    elif x == 0 and y < 0:
        return -3.141592653589793 / 2
    else:
        return 0  # (0, 0) case
	
def log(x, iterations=1000):
    """
    Approximates the natural logarithm (log base e) of x using Newton's method.
    
    :param x: The value to compute the natural logarithm for.
    :param iterations: The number of iterations to improve the approximation.
    :return: Approximated natural logarithm of x.
    """
    if x <= 0:
        raise ValueError("Math domain error. Input must be greater than 0.")
    
    # Initial guess
    guess = x if x < 2 else x / 2
    
    # Newton's method to approximate log(x)
    for _ in range(iterations):
        guess -= (guess - x / (2.718281828459045 ** guess)) / (1 + x / (2.718281828459045 ** guess))
    
    return guess
    


    
def rank(data):
    """
    Spearman
    Calcule les rangs des valeurs dans la liste donnée.
    
    :param data: Liste des valeurs à classer.
    :return: Liste des rangs correspondant aux valeurs.
    """
    sorted_indices = sorted(range(len(data)), key=lambda i: data[i])
    ranks = [0] * len(data)
    rank_sum = 0
    last_value = None
    
    for index in sorted_indices:
        if last_value is None or data[index] != last_value:
            rank_sum = index + 1
        else:
            rank_sum += index + 1
        
        ranks[index] = rank_sum / (sorted_indices.index(index) + 1)
        last_value = data[index]
    
    return ranks

def spearman_correlation(x, y):
    """
    Spearman
    Calcule le coefficient de corrélation de Spearman entre deux listes de données.
    
    :param x: Liste des valeurs de la première variable.
    :param y: Liste des valeurs de la seconde variable.
    :return: Coefficient de corrélation de Spearman entre x et y.
    """
    if len(x) != len(y):
        raise ValueError("Les listes x et y doivent avoir la même longueur.")
    
    n = len(x)
    
    # Calcul des rangs
    rank_x = rank(x)
    rank_y = rank(y)
    
    # Calcul de la différence des rangs
    d_squared_sum = sum((rank_x[i] - rank_y[i]) ** 2 for i in range(n))
    
    # Calcul du coefficient de corrélation de Spearman
    spearman_corr = 1 - (6 * d_squared_sum) / (n * (n * n - 1))
    
    return spearman_corr
    
##############################
from typing import Generator, List, Tuple
from random import randint,uniform,choice
from decimal import Decimal, ROUND_DOWN
from string import ascii_letters
class Generation():
	
	def __init__(self, min_value: float = 0.0, max_value: float = 10, seed: int = None) -> None:
		"""
		Initialize the random matrix generator.
        
		Args:
			min_value: Minimum value for random numbers (default: 0.0)
			max_value: Maximum value for random numbers (default: 10)
			seed: Random seed for reproducibility (default: None)
		"""
		self.min_value = min_value
		self.max_value = max_value
		if seed is not None:
			random.seed(seed)
			
	#def generate(self,dimx,form='float'):
	#	if isinstance(self,Vector):
	#		self.generate_vector(dimx,form)
			
	def _generate_random_float(self) -> float:
		"""
		Generate a random float number with one decimal place.
        
		Returns:
			float: Random number rounded to one decimal place
		"""
		# Generate random float and convert to Decimal for precise rounding
		value = uniform(self.min_value, self.max_value)
		decimal_value = Decimal(str(value)).quantize(Decimal('0.1'), rounding=ROUND_DOWN)
		return float(decimal_value)
	def _generate_random_proba(self) -> float:
		"""
		Generate a random float number with one decimal place.
        
		Returns:
			float: Random number rounded to one decimal place
		"""
		# Generate random float and convert to Decimal for precise rounding
		value = uniform(0.0, 1.0)
		decimal_value = Decimal(str(value)).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
		return float(decimal_value)
		
	def _generate_random_int(self) -> int:
		"""
		Generate a random int number.
		Returns:
			int: Random number int
		"""
		return  randint(self.min_value, self.max_value)
		
	def _generate_random_bin(self) -> int:
		"""
		Generate a random binary number.
		Returns:
			int: Random number binary
		"""
		return randint(0,1)
		
	def _generate_random_bool(self) -> int:
		"""
		Generate a random boolean number.
		Returns:
			bool: Random number boolean
		"""
		return choice([True, False])
		
	def _generate_random_letter(self) -> int:
		"""
		Generate a random letter.
		Returns:
			bool: Random letter
		"""
		return choice(ascii_letters)

	def generate_row(self, rows: int, cols: int) -> Generator[List[float], None, None]:
		"""
		Generate a matrix of random float numbers row by row.
        
		Args:
			rows: Number of rows in the matrix
			cols: Number of columns in the matrix
            
		Yields:
			List[float]: A row of random numbers
            
		Raises:
			ValueError: If rows or cols are less than 1
		"""
		
		if rows < 1 or cols < 1:
			raise ValueError("Matrix dimensions must be positive integers")
            
		for _ in range(rows):
			row = [self._generate_random_float() for _ in range(cols)]
			yield row
			
	def generate_vector(self, cols: int, form:str='float') -> List[float]:
		"""
		Generate a matrix of random float numbers row by row.
        
		Args:
			rows: Number of rows in the matrix
			cols: Number of columns in the matrix
            
		Yields:
			List[float]: A row of random numbers
            
		Raises:
			ValueError: If rows or cols are less than 1
		"""
		
		if cols < 1:
			raise ValueError("Vector dimension must be positive integers")
		if form=='float':
			return [self._generate_random_float() for _ in range(cols)]
		if form=='proba':
			return [self._generate_random_proba() for _ in range(cols)]
		if form=='int':
			return [self._generate_random_int() for _ in range(cols)]
		if form=='bin':
			return [self._generate_random_bin() for _ in range(cols)]
		if form=='bool':
			return [self._generate_random_bool() for _ in range(cols)]
		if form=='letter':
			return [self._generate_random_letter() for _ in range(cols)]

#############################################
from typing import List, Type, Any, TypeVar, Generic,Optional

T = TypeVar('T')

class Container(Generic[T]):
    """Generic container that can store an object of type T."""
    
    def __init__(self, container: T,types: List[Type]) -> None:
        self.container: T = container
        self.types: T = types
        
    def get_types(self, types: List[Type])-> None:
        self.types: List[Type] = types
        
    @staticmethod    
    def get_data_container(data: Any):
        if type(data) == list or type(data[0])==list:
          if type(data[0])==list:
            container=list[list]
            types=[type(data[0][0])]
            container_data=Container(container,types)
          else:
            container=list
            types=[type(data[0])]
            container_data=Container(container,types)
          return container_data
        else: 
          return None
          
    @staticmethod       
    def is_compatible_container(container1,container2):
      if container1.container==container2.container and container2.types[0] in container1.types:
        return True
      else:
        return False

import inspect
import importlib
from distancia import Distance,vectorDistance

class Find():
    """
    Utility class to find an appropriate container for any data structure type.
    Searches through available containers based on container compatibility
    and type compatibility.
    """
    
    def __init__(self,lst_structure:list=None):
        """
        Initialize with a list of distance class for searching.
        
        Args:
            available_containers: List of pre-defined containers to search through
        """
        
        if lst_structure==None:
          self.lst_structure=['vectorDistance','matrixDistance','textDistance']
        else:
          self.lst_structure=lst_structure
        
    def search(self) -> list:
      
      package = importlib.import_module('distancia')
      lst_cls=[]
      for structure in self.lst_structure:
        module = importlib.import_module('distancia.'+structure)
        cls = getattr(module, structure)
        # Find all class in package
        for nom, objet in inspect.getmembers(package):
            if inspect.isclass(objet):
              if issubclass(objet,cls) and objet!=cls:
                lst_cls.append(objet)
      return lst_cls
      
    def structure(self, data: Any) -> Optional[Any]:
        """
        Find a suitable container for the given data based on two criteria:
        1. If the data type is compatible with the class container's type list
        
        Args:
            data: Any data object to find a container for
            
        Returns:
            Class Container that matches the data, or None if no match found
        """
        # Get the data container
        data_container = Container.get_data_container(data)
        lst_cls_compatible=[]
        # First check: find containers where data's container type matches
        for cls in self.search():
            for cont in cls.containers:
              # Check if data can be stored in the container's container
              if Container.is_compatible_container(cont,data_container):
                lst_cls_compatible.append(cls)
        return lst_cls_compatible
        

#############################################
#TO DO with claude
#@dataclass
class Proba:
    """Represents a number between 0,1"""
    data: float

#######################################
from dataclasses import dataclass

@dataclass
class Point:
    """Represents a data point with features and label"""
    features: List[float]
    label: int

from typing import List, Tuple, Set, Optional
from dataclasses import dataclass
'''
@dataclass
class Matrix:
    """
    A simple matrix class implementation with basic matrix operations.
    
    Attributes:
        rows (int): Number of rows in the matrix
        cols (int): Number of columns in the matrix
        data (List[List[float]]): Matrix data stored as a list of lists
    """
    rows: int
    cols: int
    data: List[List[float]]



    @classmethod
    def identity(cls, size: int) -> 'Matrix':
        """Create an identity matrix of given size"""
        matrix = cls.zeros(size, size)
        for i in range(size):
            matrix.data[i][i] = 1.0
        return matrix
'''


#claude ai
from typing import Dict, Set, List, Tuple, Optional, Iterator
from collections import defaultdict
import heapq
import random
from math import inf

class Graph:
    """
    A class representing a graph with various graph operations.
    The graph can be either directed or undirected, weighted or unweighted.
    """
    
    def __init__(self, directed: bool = False, weighted: bool = False) -> None:
        """
        Initialize a new graph.
        
        Args:
            directed (bool): If True, the graph is directed. Default is False.
            weighted (bool): If True, the graph is weighted. Default is False.
        """
        self.directed = directed
        self.weighted = weighted
        self.nodes: Set[str] = set()
        if weighted:
        # For weighted graphs:Dict[str, Dict[str, float]]
        # For unweighted graphs: Dict[str, Set[str]]
          self.adj_list: Dict[str, Dict[str, float]] = defaultdict(dict)
        else:
          self.adj_list: Dict[str, Set[str]] = defaultdict(dict)
          
    @staticmethod
    def display(matrix: List[List[float]]) -> None:
      """
      Display a matrix in a readable format.
    
      Args:
      matrix (List[List[Number]]): Matrix to display
      """
      print(self.adjacency_to_string())
        
    def add_node(self, node: str) -> None:
        """
        Add a node to the graph.
        
        Args:
            node (str): The node to add
        """
        self.nodes.add(node)
        if node not in self.adj_list:
            self.adj_list[node] = {}

    def add_edge(self, source: str, target: str, weight: float = 1.0) -> None:
        """
        Add an edge to the graph.
        
        Args:
            source (str): Source node
            target (str): Target node
            weight (float): Edge weight (default is 1.0)
            
        Raises:
            ValueError: If trying to add weighted edge in unweighted graph
        """
        if not self.weighted and weight != 1.0:
            raise ValueError("Cannot add weighted edge to unweighted graph")
            
        self.nodes.add(source)
        self.nodes.add(target)
        if self.weighted:
                self.adj_list[source][target] = weight
                if not self.directed:
                    self.adj_list[target][source] = weight
        else:
                self.adj_list[source].add(target)
                if not self.directed:
                    self.adj_list[target].add(source)

    def remove_edge(self, source: str, target: str) -> None:
        """
        Remove an edge from the graph.
        
        Args:
            source (str): Source node
            target (str): Target node
            
        Raises:
            KeyError: If edge doesn't exist
        """
        if target in self.adj_list[source]:
            del self.adj_list[source][target]
            if not self.directed and source in self.adj_list[target]:
                del self.adj_list[target][source]
        else:
            raise KeyError(f"Edge ({source}, {target}) not found in graph")
            
    def get_edges(self) -> List[Tuple[str, str]]:
        """
        Get all edges in the graph as a list of tuples.
        For undirected graphs, each edge is returned only once.
        
        Returns:
            List[Tuple[str, str]]: List of edges where each edge is a tuple (source, target)
        
        Example:
            >>> g = Graph()
            >>> g.add_edge('A', 'B')
            >>> g.add_edge('C', 'D')
            >>> g.get_edges()
            [('A', 'B'), ('C', 'D')]
        """
        edges: List[Tuple[str, str]] = []
        visited_edges: Set[Tuple[str, str]] = set()
        
        for source in self.adj_list:
            for target in self.adj_list[source]:
                # Pour les graphes non dirigés, on ne veut pas ('B', 'A') si on a déjà ('A', 'B')
                if not self.directed:
                    edge = tuple(sorted([source, target]))  # type: ignore
                    if edge not in visited_edges:
                        edges.append((edge[0], edge[1]))
                        visited_edges.add(edge)
                else:
                    edges.append((source, target))
                    
        return edges
        
    def remove_node(self, node: str) -> None:
        """
        Remove a node and all its edges from the graph.
        
        Args:
            node (str): The node to remove
            
        Raises:
            KeyError: If node doesn't exist
        """
        if node not in self.nodes:
            raise KeyError(f"Node {node} not found in graph")
            
        # Remove all edges pointing to this node
        for other_node in self.adj_list:
            if node in self.adj_list[other_node]:
                del self.adj_list[other_node][node]
        
        # Remove the node and its edges
        del self.adj_list[node]
        self.nodes.remove(node)

    def get_adjacency_matrix(self) -> List[List[float]]:
        """
        Convert the graph to its adjacency matrix representation.
        
        Returns:
            List[List[float]]: The adjacency matrix of the graph
        """
        # Create a mapping of node labels to indices
        sorted_nodes = sorted(self.nodes)
        node_to_index = {node: i for i, node in enumerate(sorted_nodes)}
        n = len(self.nodes)
        
        # Initialize the adjacency matrix with zeros
        adj_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
        
        # Fill the adjacency matrix
        for source in self.adj_list:
            for target, weight in self.adj_list[source].items():
                adj_matrix[node_to_index[source]][node_to_index[target]] = weight
                
        return adj_matrix
        
    def adjacency_to_string(self):
      """
      Convert the adjacency matrix to a string representation.

      :param matrix: Adjacency matrix of a graph
      :return: String representation of the adjacency matrix
      """
      return ''.join([''.join(map(str, row)) for row in self.get_adjacency_matrix()])

    def get_neighbors(self, node: str) -> Set[str]:
        """
        Get all neighbors of a node.
        
        Args:
            node (str): The node to get neighbors for
            
        Returns:
            Set[str]: Set of neighboring nodes
            
        Raises:
            KeyError: If node doesn't exist
        """
        if node not in self.nodes:
            raise KeyError(f"Node {node} not found in graph")
        return set(self.adj_list[node].keys())

    def get_degree(self, node: str) -> int:
        """
        Get the degree of a node.
        
        Args:
            node (str): The node to get degree for
            
        Returns:
            int: Degree of the node
            
        Raises:
            KeyError: If node doesn't exist
        """
        if node not in self.nodes:
            raise KeyError(f"Node {node} not found in graph")
        return len(self.adj_list[node])
        
    def compute_degree_matrix(self) -> Dict[str, float]:
        degree_matrix = {}
        for node in self.nodes:
            if self.weighted:
                degree_matrix[node] = sum(self.adj_list[node].values())
            else:
                degree_matrix[node] = len(self.adj_list[node])
        return degree_matrix
        
    def compute_degrees(self) -> Dict[int, float]:
        degrees = {}
        
        if self.weighted:
            # For weighted graphs, count non-zero weight connections
            for node in self.nodes:
                if self.directed:
                    # For directed graphs, calculate both in and out degrees
                    out_degree = len([dest for dest, weight in self.adj_list[node].items() if weight != 0])
                    in_degree = len([src for src in self.nodes if node in self.adj_list[src] and self.adj_list[src][node] != 0])
                    degree = out_degree + in_degree
                else:
                    # For undirected graphs, count non-zero weight edges
                    degree = len([dest for dest, weight in self.adj_list[node].items() if weight != 0])
                
                if degree in degrees:
                    degrees[degree] += 1
                else:
                    degrees[degree] = 1
        else:
            # For unweighted graphs
            for node in self.nodes:
                if self.directed:
                    # For directed graphs, calculate both in and out degrees
                    out_degree = len(self.adj_list[node])
                    in_degree = len([src for src in self.nodes if node in self.adj_list[src]])
                    degree = out_degree + in_degree
                else:
                    # For undirected graphs, just count the number of neighbors
                    degree = len(self.adj_list[node])
                
                if degree in degrees:
                    degrees[degree] += 1
                else:
                    degrees[degree] = 1

        # Convert to probability distribution
        total_nodes = len(self.nodes)
        if total_nodes > 0:  # Avoid division by zero
            for degree in degrees:
                degrees[degree] = degrees[degree] / total_nodes

        return degrees
      
    def multiply_matrix_vector(matrix: Dict[str, Dict[str, float]], vector: Dict[str, float]) -> Dict[str, float]:
      """
      Multiplie une matrice par un vecteur.
      matrix: matrice sous forme de dictionnaire de dictionnaires
      vector: vecteur sous forme de dictionnaire
      """
      result = {node: 0.0 for node in vector}
      for i in matrix:
        for j in matrix[i]:
            result[i] += matrix[i][j] * vector[j]
      return result

    def normalize_vector(vector: Dict[str, float]) -> Dict[str, float]:
      """
      Normalise un vecteur pour que la somme soit 1.
      """
      total = sum(vector.values())
      if total == 0:
        return vector
      return {k: v/total for k, v in vector.items()}
      
    def compute_laplacian(self) -> Dict[str, Dict[str, float]]:
        laplacian = defaultdict(dict)
        degree = self.compute_degree_matrix()
        
        for node in self.nodes:
            laplacian[node][node] = degree[node]
            neighbors = (self.adj_list[node].keys() if self.weighted 
                       else self.adj_list[node])
            
            for neighbor in neighbors:
                weight = (1.0 if not self.weighted 
                         else self.adj_list[node][neighbor])
                laplacian[node][neighbor] = -weight
        
        return laplacian
        
    def get_transition_matrix(self) -> Dict[str, Dict[str, float]]:
      """
      Calcule la matrice de transition pour une marche aléatoire sur le graphe.
      """
      transition_matrix = defaultdict(dict)
    
      for node in self.nodes:
        # Pour les graphes non pondérés
        if not self.weighted:
            neighbors = self.adj_list[node]
            degree = len(neighbors) if isinstance(neighbors, set) else len(neighbors.keys())
            if degree > 0:
                if isinstance(neighbors, set):
                    for neighbor in neighbors:
                        transition_matrix[node][neighbor] = 1.0 / degree
                else:
                    for neighbor in neighbors.keys():
                        transition_matrix[node][neighbor] = 1.0 / degree
        # Pour les graphes pondérés
        else:
            total_weight = sum(self.adj_list[node].values())
            if total_weight > 0:
                for neighbor, weight in self.adj_list[node].items():
                    transition_matrix[node][neighbor] = weight / total_weight
                    
      return transition_matrix
      
    def compute_stationary_distribution(self,graph,max_iterations = 100,epsilon = 1e-10) -> Dict[str, float]:
        matrix = Graph.get_transition_matrix(graph)
        vector = {node: 1.0/len(graph.nodes) for node in graph.nodes}
        
        for _ in range(max_iterations):
            new_vector = Graph.multiply_matrix_vector(matrix, vector)
            new_vector = Graph.normalize_vector(new_vector)
            
            diff = sum(abs(new_vector[node] - vector[node]) for node in graph.nodes)
            if diff < epsilon:
                return new_vector
                
            vector = new_vector
        
        return vector
        
    def count_motifs(self, motif_size):
      motifs = {}
      for node in self.nodes:
       neighbors = self.adj_list[node]
       if len(neighbors) >= motif_size - 1:
          for sub_motif in self._find_sub_motifs(node, neighbors, motif_size - 1):
            sub_motif = tuple(sorted(sub_motif))
            if sub_motif in motifs:
              motifs[sub_motif] += 1
            else:
              motifs[sub_motif] = 1
      return motifs 
           
    def _find_sub_motifs(self, node, neighbors, remaining):
      if remaining == 1:
        return [(node, neighbor) for neighbor in neighbors]
      sub_motifs = []
      for i, neighbor in enumerate(neighbors):
        new_neighbors = neighbors[i + 1:]
      for sub_motif in self._find_sub_motifs(neighbor, new_neighbors, remaining - 1):
        sub_motifs.append((node,) + sub_motif)
      return sub_motifs
      
    def dijkstra(self, start_node: str, end_node: str) -> Tuple[float, List[str]]:
        """
        Find the shortest path between two nodes using Dijkstra's algorithm.
        
        Args:
            start_node (str): Starting node
            end_node (str): Target node
            
        Returns:
            Tuple[float, List[str]]: (shortest distance, path as list of nodes)
            
        Raises:
            KeyError: If either node doesn't exist
        """
        if start_node not in self.nodes or end_node not in self.nodes:
            raise KeyError("Start or end node not found in graph")
            
        distances: Dict[str, float] = {node: inf for node in self.nodes}
        distances[start_node] = 0
        previous: Dict[str, Optional[str]] = {node: None for node in self.nodes}
        pq: List[Tuple[float, str]] = [(0, start_node)]
        visited: Set[str] = set()
        
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            
            if current_node == end_node:
                path: List[str] = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = previous[current_node]
                return current_distance, path[::-1]
                
            if current_node in visited:
                continue
                
            visited.add(current_node)
            
            for neighbor, weight in self.adj_list[current_node].items():
                if neighbor not in visited:
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        previous[neighbor] = current_node
                        heapq.heappush(pq, (distance, neighbor))
        
        return inf, []

    def random_walk(self, start_node: str, steps: int) -> List[str]:
        """
        Perform a random walk starting from a given node.
        
        Args:
            start_node (str): Starting node for the walk
            steps (int): Number of steps to take
            
        Returns:
            List[str]: List of nodes visited during the walk
            
        Raises:
            KeyError: If start node doesn't exist
            ValueError: If steps is negative
        """
        if start_node not in self.nodes:
            raise KeyError(f"Start node {start_node} not found in graph")
        if steps < 0:
            raise ValueError("Number of steps cannot be negative")
            
        walk: List[str] = [start_node]
        current_node = start_node
        
        for _ in range(steps):
            neighbors = list(self.adj_list[current_node].keys())
            if not neighbors:
                break
            current_node = random.choice(neighbors)
            walk.append(current_node)
            
        return walk

    def bfs(self, start_node: str) -> Iterator[str]:
        """
        Perform Breadth-First Search starting from a given node.
        
        Args:
            start_node (str): Starting node for BFS
            
        Yields:
            str: Nodes in BFS order
            
        Raises:
            KeyError: If start node doesn't exist
        """
        if start_node not in self.nodes:
            raise KeyError(f"Start node {start_node} not found in graph")
            
        visited: Set[str] = set()
        queue: List[str] = [start_node]
        visited.add(start_node)
        
        while queue:
            current = queue.pop(0)
            yield current
            
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start_node: str) -> Iterator[str]:
        """
        Perform Depth-First Search starting from a given node.
        
        Args:
            start_node (str): Starting node for DFS
            
        Yields:
            str: Nodes in DFS order
            
        Raises:
            KeyError: If start node doesn't exist
        """
        if start_node not in self.nodes:
            raise KeyError(f"Start node {start_node} not found in graph")
            
        visited: Set[str] = set()
        stack: List[str] = [start_node]
        
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                yield current
                stack.extend(neighbor for neighbor in reversed(list(self.adj_list[current]))
                           if neighbor not in visited)

    def is_cyclic(self) -> bool:
        """
        Check if the graph contains any cycles.
        
        Returns:
            bool: True if the graph contains a cycle, False otherwise
        """
        visited: Set[str] = set()
        rec_stack: Set[str] = set()
        
        def _is_cyclic_util(node: str) -> bool:
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    if _is_cyclic_util(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
                    
            rec_stack.remove(node)
            return False
        
        for node in self.nodes:
            if node not in visited:
                if _is_cyclic_util(node):
                    return True
        return False


    
from typing import Any

class TreeNode:

	def __init__(self, value: Any, children: List['TreeNode'] = None) -> None:
		"""
		Initializes a node in the tree.

		:param value: The value of the node.
		:param children: A list of child nodes.
		"""
		super().__init__()

		self.value: Any = value
		self.children: List[TreeNode] = children if children is not None else []

      
import random
from typing import List, Dict, Tuple

class MarkovChain:

	mc_1 = [[0.9, 0.1], [0.2, 0.8]]  # Transition matrix for Markov chain 1
	mc_2 = [[0.85, 0.15], [0.25, 0.75]]  # Transition matrix for Markov chain 2
    
	def __init__(self, n: int = 2):
		self.n = n  # Ordre de la chaîne de Markov
		self.chain: Dict[Tuple[str, ...], Dict[str, int]] = {}
		self.start_tokens: List[Tuple[str, ...]] = []

	@staticmethod
	def display(matrix: List[List[float]]) -> None:
		"""
		Display a matrix in a readable format.
    
		Args:
			matrix (List[List[Number]]): Matrix to display
		"""
		for row in matrix:
			print([f"{x:>5.2f}" for x in row])
			
	def add_text(self, text: str) -> None:
		"""
		Ajoute un texte à la chaîne de Markov.
		"""
		words = text.split()
		for i in range(len(words) - self.n):
			state = tuple(words[i:i+self.n])
			next_word = words[i+self.n]
            
			if i == 0:
				self.start_tokens.append(state)

			if state not in self.chain:
				self.chain[state] = {}
			if next_word not in self.chain[state]:
				self.chain[state][next_word] = 0
			self.chain[state][next_word] += 1

	def generate_text(self, length: int = 100) -> str:
		"""
		Génère un nouveau texte basé sur la chaîne de Markov.
		"""
		if not self.chain:
			return ""

		current = random.choice(self.start_tokens)
		result = list(current)

		for _ in range(length - self.n):
			if current not in self.chain:
				break
            
		possible_next = self.chain[current]
		next_word = self._weighted_choice(possible_next)
		result.append(next_word)
		current = tuple(result[-self.n:])

		return ' '.join(result)

	def _weighted_choice(self, choices: Dict[str, int]) -> str:
		"""
		Choisit un élément en fonction de son poids.
		"""
		total = sum(choices.values())
		r = random.uniform(0, total)
		upto = 0
		for choice, weight in choices.items():
			if upto + weight >= r:
				return choice
			upto += weight
		assert False, "Shouldn't get here"

	def get_probability(self, state: Tuple[str, ...], next_word: str) -> float:
		"""
		Retourne la probabilité d'un mot suivant un état donné.
		"""
		if state not in self.chain or next_word not in self.chain[state]:
			return 0.0
		total = sum(self.chain[state].values())
		return self.chain[state][next_word] / total

	def get_most_likely_next(self, state: Tuple[str, ...]) -> str:
		"""
		Retourne le mot le plus probable suivant un état donné.
		"""
		if state not in self.chain:
			return ""
		return max(self.chain[state], key=self.chain[state].get)

	def example(self) -> None:
		"""
		Exemple d'utilisation de la classe MarkovChain.
		"""
		# Ajout de texte à la chaîne
		self.add_text("le chat mange la souris le chien mange le chat")
		self.add_text("le chat dort sur le tapis le chien dort dans sa niche")

		# Génération de texte
		print("Texte généré:")
		print(self.generate_text(20))

		# Probabilité d'un mot suivant un état
		print("\nProbabilité de 'mange' après 'le chat':")
		print(self.get_probability(("le", "chat"), "mange"))

		# Mot le plus probable suivant un état
		print("\nMot le plus probable après 'le chien':")
		print(self.get_most_likely_next(("le", "chien")))
	@staticmethod
	def stationary_distribution(matrix, tolerance=1e-10, max_iterations=1000):
		"""
		Compute the stationary distribution of a Markov chain from its transition matrix.
        
		Parameters:
		matrix (list of list of float): Transition matrix of the Markov chain.
		tolerance (float): Tolerance level for convergence.
		max_iterations (int): Maximum number of iterations for convergence.
        
		Returns:
		list of float: The stationary distribution of the Markov chain.
		"""
		num_states=len(matrix)
		
		dist = [1.0 / num_states] * num_states  # Initial uniform distribution
		for _ in range(max_iterations):
			next_dist = [0] * num_states
			for i in range(num_states):
				for j in range(num_states):
					next_dist[i] += dist[j] * matrix[j][i]
				if all(abs(next_dist[i] - dist[i]) < tolerance for i in range(num_states)):
					break
				dist = next_dist
		return dist

import cmath

import os
import struct
import zlib
from tkinter import Tk, Canvas

class Image:
    def __init__(self, filepath=None):
        """
        Initialize a CustomImage instance.

        :param filepath: Path to the image file (optional).
        """
        self.image = None
        self.width = None
        self.height = None
        self.filepath = filepath
        if filepath:
            self.open(filepath)

    def open(self, filepath):
        """
        Open a BMP or PNG image file.

        :param filepath: Path to the image file.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        ext = os.path.splitext(filepath)[1].lower()
        if ext == '.bmp':
            self._open_bmp(filepath)
        elif ext == '.png':
            self._open_png(filepath)
        else:
            raise ValueError("Unsupported file format. Only BMP and PNG are supported.")

    def _open_bmp(self, filepath):
        """
        Open a BMP image file.

        :param filepath: Path to the BMP file.
        """
        with open(filepath, 'rb') as f:
            header = f.read(54)  # BMP header is 54 bytes
            if header[:2] != b'BM':
                raise ValueError("Unsupported BMP format.")

            self.width = struct.unpack('<I', header[18:22])[0]
            self.height = struct.unpack('<I', header[22:26])[0]

            # Read pixel data
            pixel_data_offset = struct.unpack('<I', header[10:14])[0]
            f.seek(pixel_data_offset)

            row_padded = (self.width * 3 + 3) & ~3
            self.image = []

            for y in range(self.height):
                row = []
                for x in range(self.width):
                    blue = ord(f.read(1))
                    green = ord(f.read(1))
                    red = ord(f.read(1))
                    row.append((red, green, blue))
                self.image.append(row)
                f.read(row_padded - self.width * 3)

            self.image.reverse()  # BMP files are stored bottom-to-top

    def _open_png(self, filepath):
        """
        Open a PNG image file.

        :param filepath: Path to the PNG file.
        """
        with open(filepath, 'rb') as f:
            signature = f.read(8)
            if signature != b'\x89PNG\r\n\x1a\n':
                raise ValueError("Unsupported PNG format.")

            chunks = []
            while True:
                length = struct.unpack('>I', f.read(4))[0]
                chunk_type = f.read(4)
                chunk_data = f.read(length)
                crc = f.read(4)  # CRC, ignored for now
                chunks.append((chunk_type, chunk_data))
                if chunk_type == b'IEND':
                    break

            # Parse IHDR
            ihdr = next(chunk for chunk in chunks if chunk[0] == b'IHDR')[1]
            self.width = struct.unpack('>I', ihdr[:4])[0]
            self.height = struct.unpack('>I', ihdr[4:8])[0]
            bit_depth = ihdr[8]
            color_type = ihdr[9]

            if bit_depth != 8 or color_type != 2:  # Only support 8-bit RGB PNGs
                raise ValueError("Unsupported PNG bit depth or color type.")

            # Parse IDAT chunks and decompress
            idat_data = b''.join(chunk[1] for chunk in chunks if chunk[0] == b'IDAT')
            decompressed_data = zlib.decompress(idat_data)

            # Read pixel data
            row_bytes = self.width * 3
            self.image = []
            for y in range(self.height):
                filter_type = decompressed_data[y * (row_bytes + 1)]
                if filter_type != 0:
                    raise ValueError("Unsupported PNG filter type.")
                row_start = y * (row_bytes + 1) + 1
                row = []
                for x in range(self.width):
                    r = decompressed_data[row_start + x * 3]
                    g = decompressed_data[row_start + x * 3 + 1]
                    b = decompressed_data[row_start + x * 3 + 2]
                    row.append((r, g, b))
                self.image.append(row)

    def save(self, filepath):
        """
        Save the image to a BMP file.

        :param filepath: Path to save the image.
        """
        if self.image is None:
            raise ValueError("No image to save. Load or create an image first.")

        ext = os.path.splitext(filepath)[1].lower()
        if ext == '.bmp':
            self._save_bmp(filepath)
        else:
            raise ValueError("Unsupported file format for saving. Only BMP is supported.")

    def _save_bmp(self, filepath):
        """
        Save the image as a BMP file.

        :param filepath: Path to save the BMP file.
        """
        with open(filepath, 'wb') as f:
            row_padded = (self.width * 3 + 3) & ~3
            file_size = 54 + row_padded * self.height

            # Write BMP header
            f.write(b'BM')
            f.write(struct.pack('<I', file_size))
            f.write(b'\x00\x00')
            f.write(b'\x00\x00')
            f.write(struct.pack('<I', 54))

            # DIB header
            f.write(struct.pack('<I', 40))  # DIB header size
            f.write(struct.pack('<I', self.width))
            f.write(struct.pack('<I', self.height))
            f.write(struct.pack('<H', 1))  # Planes
            f.write(struct.pack('<H', 24))  # Bits per pixel
            f.write(b'\x00\x00\x00\x00')  # Compression
            f.write(struct.pack('<I', row_padded * self.height))  # Image size
            f.write(b'\x13\x0B\x00\x00')  # X pixels per meter
            f.write(b'\x13\x0B\x00\x00')  # Y pixels per meter
            f.write(b'\x00\x00\x00\x00')  # Total colors
            f.write(b'\x00\x00\x00\x00')  # Important colors

            # Write pixel data
            for row in reversed(self.image):
                for pixel in row:
                    f.write(bytes(pixel[::-1]))  # Write as BGR
                f.write(b'\x00' * (row_padded - self.width * 3))

    def show(self):
        """
        Display the image in a graphical window using tkinter and a Canvas.
        """
        if self.image is None:
            raise ValueError("No image to display. Load or create an image first.")

        # Create a tkinter window
        root = Tk()
        root.title("Image Viewer")

        # Create a canvas widget
        canvas = Canvas(root, width=self.width, height=self.height)
        canvas.pack()

        # Draw each pixel onto the canvas
        for y, row in enumerate(self.image):
            for x, (r, g, b) in enumerate(row):
                # Convert RGB to hexadecimal color code
                color = f"#{r:02x}{g:02x}{b:02x}"
                # Draw a 1x1 rectangle for each pixel
                canvas.create_rectangle(x, y, x+1, y+1, outline=color, fill=color)

        # Run the tkinter main loop
        root.mainloop()

    def resize(self, new_width, new_height):
        """
        Resize the image to new dimensions using nearest neighbor.

        :param new_width: The desired width of the image.
        :param new_height: The desired height of the image.
        """
        if self.image is None:
            raise ValueError("No image to resize. Load or create an image first.")

        resized_image = []
        x_ratio = self.width / new_width
        y_ratio = self.height / new_height

        for i in range(new_height):
            row = []
            for j in range(new_width):
                src_x = int(j * x_ratio)
                src_y = int(i * y_ratio)
                row.append(self.image[src_y][src_x])
            resized_image.append(row)

        self.image = resized_image
        self.width = new_width
        self.height = new_height
'''
# Example usage
if __name__ == "__main__":
    img = Image("../sample/file1.bmp")  # Replace with the path to a BMP or PNG image
    img.show()
    img.resize(50, 50)
    img.show()
    img.save("resized_example.bmp")
'''


		
import wave#utile pour save au format wav a tester!
import struct
import math

class Sound:
	@staticmethod
	def example():
		signal1 = [0.5, 0.1, 0.2, 0.4, 0.3, 0.2, 0.1, 0.0]
		signal2 = [0.4, 0.2, 0.2, 0.5, 0.3, 0.1, 0.2, 0.0]
		return signal1,signal2
		
	def generate_test_signals(duration: float = 1.0, sample_rate: int = 16000) -> tuple[list[float], list[float]]:
		"""
		Génère deux signaux audio de test.

		Args:
		duration (float): Durée du signal en secondes. Par défaut 1.0 seconde.
		sample_rate (int): Taux d'échantillonnage en Hz. Par défaut 16000 Hz.

		Returns:
		tuple[list[float], list[float]]: Deux signaux audio de test.
		"""
		num_samples = int(duration * sample_rate)

		# Signal 1: Combinaison de deux sinusoïdes (440 Hz et 880 Hz)
		signal1 = [
			0.5 * math.sin(2 * math.pi * 440 * t / sample_rate) +
			0.3 * math.sin(2 * math.pi * 880 * t / sample_rate)
			for t in range(num_samples)
		]

		# Signal 2: Combinaison de trois sinusoïdes (330 Hz, 660 Hz et 990 Hz)
		signal2 = [
			0.4 * math.sin(2 * math.pi * 330 * t / sample_rate) +
			0.3 * math.sin(2 * math.pi * 660 * t / sample_rate) +
			0.2 * math.sin(2 * math.pi * 990 * t / sample_rate)
			for t in range(num_samples)
		]

		return signal1, signal2

	def generate_sine_wave(frequency: float, duration: float, sample_rate: int = 44100, amplitude: float = 0.5) -> list:
		"""
		Génère une onde sinusoïdale d'une fréquence et d'une durée données.

		:param frequency: Fréquence de l'onde sinusoïdale en Hz.
		:param duration: Durée de l'onde sinusoïdale en secondes.
		:param sample_rate: Taux d'échantillonnage en Hz.
		:param amplitude: Amplitude de l'onde (entre 0 et 1).
		:return: Liste contenant les échantillons de l'onde sinusoïdale.
		"""
		num_samples = int(sample_rate * duration)  # Nombre total d'échantillons
		wave_data = []
    
		for n in range(num_samples):
			# Calcul du temps pour chaque échantillon
			t = n / sample_rate
			# Calcul de l'échantillon sinusoïdal
			sample = amplitude * math.sin(2 * math.pi * frequency * t)
			wave_data.append(sample)
    
		return wave_data

	def save_wave(filename: str, data: list[float], sample_rate: int = 44100) -> None:
		"""
		Saves the NumPy array as a .wav file.
    
		:param filename: The name of the output .wav file.
		:param data: The audio data to save.
		:param sample_rate: The sampling rate in Hz.
		"""
		n_samples = data.shape[0]
		wav_file = wave.open(filename, 'w')
		wav_file.setparams((1, 2, sample_rate, n_samples, 'NONE', 'not compressed'))

		for sample in data:
			wav_file.writeframes(struct.pack('<h', int(sample * 32767)))

		wav_file.close()
    
	def FFT(self,signal: List[float]) -> List[complex]:
		"""
		Compute the Fast Fourier Transform (FFT) of the input signal.

		:param signal: The input signal as a list of floats.
		:return: The FFT of the signal as a list of complex numbers.
		"""
		n: int = len(signal)
		if n == 1:
			return signal
		else:
			even: List[complex] = self.FFT(signal[0::2])
			odd: List[complex] = self.FFT(signal[1::2])
			combined: List[complex] = [0] * n
			for k in range(n // 2):
				t: complex = cmath.exp(-2j * cmath.pi * k / n) * odd[k]
				combined[k] = even[k] + t
				combined[k + n // 2] = even[k] - t
			return combined
			
	@staticmethod
	def pad_to_power_of_two(signal: List[float]) -> List[float]:
		"""
		Complète le signal avec des zéros pour atteindre une longueur qui est une puissance de 2.

		Args:
		signal (List[float]): Le signal d'entrée.

		Returns:
		List[float]: Le signal complété.
		"""
		n = 1
		while n < len(signal):
			n *= 2
		return signal + [0.0] * (n - len(signal))
		
	def inverse_fft(self, spectrum: List[float]) -> List[float]:
		"""
		Computes the inverse FFT (simplified for illustration purposes).
        
		:param spectrum: The power spectrum of the audio signal.
		:return: The time-domain cepstral coefficients as a list of floats.
		"""
		return [math.exp(s) for s in spectrum]  # Simplified inverse

	@staticmethod
	def magnitude(spectrum: List[complex]) -> List[float]:
		"""
		Compute the magnitude of a complex spectrum.

		:param spectrum: A list of complex numbers representing the frequency spectrum.
		:return: A list of floats representing the magnitude of the spectrum.
		"""
		return [abs(value) for value in spectrum]
	@staticmethod
	def _apply_window(segment: List[float]) -> List[float]:
		"""
		Applique une fenêtre de Hann au segment.

		Args:
		segment (List[float]): Segment du signal.

		Returns:
		List[float]: Segment après application de la fenêtre.
		"""
		return [s * 0.5 * (1 - math.cos(2 * math.pi * i / (len(segment) - 1)))
                for i, s in enumerate(segment)]
                
	@staticmethod
	def _mean_squared_error( cqt1: List[List[float]], cqt2: List[List[float]]) -> float:
		if len(cqt1) != len(cqt2) or len(cqt1[0]) != len(cqt2[0]):
			raise ValueError("Both CQT matrices must have the same dimensions.")

		mse: float = sum(
			(frame1[i] - frame2[i]) ** 2
			for frame1, frame2 in zip(cqt1, cqt2)
			for i in range(len(frame1))
			) / (len(cqt1) * len(cqt1[0]))
		return mse
		
	def read_audio(self, filepath: str) -> Tuple[List[float], int]:
		"""
		Reads the audio file and returns the waveform data along with the sample rate.
        
		:param filepath: Path to the audio file.
		:return: Tuple containing the audio data (as a list of floats) and the sample rate.
		"""
		with wave.open(filepath, 'rb') as wav_file:
			n_frames: int = wav_file.getnframes()
			audio_data: List[float] = list(wav_file.readframes(n_frames))
			return audio_data, wav_file.getframerate()
