cdef class vectorDistance:
    cpdef object __init__(self)
    cpdef object check_data_dimension(self, data1, data2)
    cpdef object check_data_type(self, data_list)
    cpdef object example(self)

cdef class TypeValidate:
    cpdef object _value(self, target_type)
    cpdef object _list(self, element_type)
    cpdef object ensure_type(self, target_type)
    cpdef object ensure_list(self, element_type)
    cpdef object autodetect(self)

cdef class Vector:
    cpdef object display(self)
    cpdef object norm(self)
    cpdef object normalize(self)
    cpdef object dot_product(self, vec2)
    cpdef object generate(self, cols, form)

cdef class Euclidean:
    cdef object container
    cpdef object __init__(self)
    cpdef object vector_distance(self, v2)
    cpdef object matrix_distance(self, m2)
    cpdef object compute(self, a, b)

cdef class L2:
    cpdef object __init__(self)

cdef class Manhattan:
    cpdef object __init__(self)
    cpdef object compute(self, point1, point2)

cdef class L1:
    cpdef object __init__(self)

cdef class InverseTanimoto:
    cpdef object __init__(self)
    cpdef object compute(self, list_a, list_b)

cdef class Minkowski:
    cpdef object __init__(self, p)
    cpdef object compute(self, point1, point2)
    cpdef object exemple(self)

cdef class RussellRao:
    cpdef object __init__(self)
    cpdef object compute(self, vector1, vector2)

cdef class Chebyshev:
    cpdef object __init__(self)
    cpdef object compute(self, point1, point2)

cdef class Hausdorff:
    cpdef object __init__(self)
    cpdef object compute(self, set1, set2)
    cpdef object example(self)

cdef class KendallTau:
    cpdef object __init__(self)
    cpdef object compute(self, permutation1, permutation2)

cdef class Haversine:
    cpdef object __init__(self)
    cpdef object compute(self, p1, p2)
    cpdef object example(self)

cdef class Canberra:
    cpdef object __init__(self)
    cpdef object compute(self, point1, point2)

cdef class BrayCurtis:
    cpdef object __init__(self)
    cpdef object compute(self, point1, point2)

cdef class Hamming:
    cpdef object __init__(self)
    cpdef object compute(self, v2)
    cpdef object normalized_distance(self, v1, v2)
    cpdef object similarity(self, document1, document2)

cdef class Matching:
    cpdef object __init__(self)

cdef class Kulsinski:
    cpdef object __init__(self)
    cpdef object compute(self, set1, set2)

cdef class Yule:
    cpdef object __init__(self)
    cpdef object compute(self, binary_vector1, binary_vector2)

cdef class Bhattacharyya:
    cpdef object __init__(self)
    cpdef object compute(self, P, Q)

cdef class Gower:
    cpdef object __init__(self, ranges)
    cpdef object compute(self, vec1, vec2)
    cpdef object example(self)

cdef class Hellinger:
    cpdef object __init__(self)
    cpdef object compute(self, p, q)

cdef class CzekanowskiDice:
    cpdef object __init__(self)
    cpdef object compute(self, x, y)

cdef class Wasserstein:
    cpdef object __init__(self)
    cpdef object compute(self, distribution1, distribution2)
    cpdef object _cumulative_distribution(self, distribution)

cdef class Jaccard:
    cpdef object __init__(self)
    cpdef object compute(self, set2)
    cpdef object similarity(self, set1, set2)

cdef class CustomObject:
    cpdef object __init__(self, value)
    cpdef object __eq__(self, other)
    cpdef object __hash__(self)
    cpdef object __repr__(self)

cdef class Tanimoto:
    cpdef object __init__(self)

cdef class GeneralizedJaccard:
    cpdef object __init__(self)
    cpdef object compute(self, x, y)
    cpdef object example(self)

cdef class Pearson:
    cpdef object __init__(self)
    cpdef object compute(self, x, y)
    cpdef object exemple(self)

cdef class Spearman:
    cpdef object __init__(self)
    cpdef object compute(self, x, y)
    cpdef object exemple(self)

cdef class Ochiai:
    cpdef object __init__(self)
    cpdef object _convert_to_set(self)
    cpdef object validate_input(self)
    cpdef object compute(self, set_a, set_b)

cdef class MotzkinStraus:
    cpdef object __init__(self, p)
    cpdef object compute(self, x, y)

cdef class EnhancedRogersTanimoto:
    cpdef object __init__(self, alpha)
    cpdef object compute(self, vector_a, vector_b)

cdef class ContextualDynamicDistance:
    cpdef object __init__(self)
    cpdef object compute(self, x, y, context_x, context_y)
    cpdef object convolution_context_weight_func(self, context_x, context_y, index, kernel_size)
    cpdef object exemple(self)

cdef class Otsuka:
    cpdef object __init__(self)
    cpdef object compute(self, vector1, vector2)

cdef class RogersTanimoto:
    cpdef object __init__(self)
    cpdef object compute(self, vector1, vector2)

cdef class SokalMichener:
    cpdef object __init__(self)
    cpdef object compute(self, vector1, vector2)

cdef class SokalSneath:
    cpdef object __init__(self)
    cpdef object compute(self, vector1, vector2)

cdef class FagerMcGowan:
    cpdef object __init__(self, N)
    cpdef object compute(self, set1, set2)
    cpdef object example(self)

cdef class JensenShannonDivergence:
    cpdef object __init__(self)
    cpdef object compute(self, dist1, dist2)
    cpdef object _kl_divergence(self, dist_p, dist_q)
