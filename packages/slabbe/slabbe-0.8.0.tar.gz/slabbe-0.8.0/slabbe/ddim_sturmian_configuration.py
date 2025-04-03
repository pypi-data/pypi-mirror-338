# -*- coding: utf-8 -*-
r"""
d-dimensional Sturmian Configurations

The `d`-dimensional Sturmian configuration is a function
`\mathbb{Z}^d\to\{0,1,\dots,d\}` as follows.
Given `\boldsymbol{\alpha}=(\alpha_1,\dots,\alpha_d)\in\mathbb{R}^d`, we define

.. MATH::

    \begin{array}{rccl}
    s_{\boldsymbol{\alpha}\rho}:&\mathbb{Z}^d & \to & \{0,1,\dots,d\}\\
    &\boldsymbol{n} & \mapsto &
    \sum_{i=1}^d \left(\lfloor\alpha_i+\boldsymbol{n}\cdot\boldsymbol{\alpha}+\rho\rfloor
    -\lfloor\boldsymbol{n}\cdot\boldsymbol{\alpha}+\rho\rfloor\right),\\
    \end{array}

and

.. MATH::

    \begin{array}{rccl}
    s'_{\boldsymbol{\alpha}\rho}:&\mathbb{Z}^d & \to & \{0,1,\dots,d\}\\
    &\boldsymbol{n} & \mapsto &
    \sum_{i=1}^d \left(\lceil\alpha_i+\boldsymbol{n}\cdot\boldsymbol{\alpha}+\rho\rceil
    -\lceil\boldsymbol{n}\cdot\boldsymbol{\alpha}+\rho\rceil\right),\\
    \end{array}

When `d=1`, this corresponds to Sturmian sequences, or more precisely, the
lower mechanical word and the upper mechanical word. When `d=2`, this
definition is equivalent to discrete planes as defined in
\cite{MR1782038,MR1906478}.

EXAMPLES::

    sage: z = polygen(QQ, 'z')
    sage: K = NumberField(z**2-z-1, 'phi', embedding=RR(1.6))
    sage: phi = K.gen()

    sage: from slabbe import dSturmianConfiguration
    sage: c_ceil = dSturmianConfiguration((phi^-1, sqrt(2)-1), 0, ceil_or_floor='ceil')
    sage: c_floor = dSturmianConfiguration((phi^-1, sqrt(2)-1), 0, ceil_or_floor='floor')
    sage: c_ceil.rectangular_subword_matrix(((-1,10), (-1,10)))
    [0 2 0 2 1 0 2 1 0 2 0]
    [2 0 2 1 0 2 1 0 2 0 2]
    [0 2 1 0 2 0 2 2 0 2 1]
    [2 1 0 2 0 2 1 0 2 1 0]
    [1 0 2 0 2 1 0 2 1 0 2]
    [0 2 0 2 1 0 2 0 2 2 0]
    [2 0 2 1 0 2 0 2 1 0 2]
    [0 2 1 0 2 0 2 1 0 2 1]
    [2 1 0 2 0 2 1 0 2 0 2]
    [0 2 2 0 2 1 0 2 0 2 1]
    [2 1 0 2 1 0 2 0 2 1 0]
    sage: c_floor.rectangular_subword_matrix(((-1,10), (-1,10)))
    [0 2 0 2 1 0 2 1 0 2 0]
    [2 0 2 1 0 2 1 0 2 0 2]
    [0 2 1 0 2 0 2 2 0 2 1]
    [2 1 0 2 0 2 1 0 2 1 0]
    [1 0 2 0 2 1 0 2 1 0 2]
    [0 2 0 2 1 0 2 0 2 2 0]
    [2 0 2 1 0 2 0 2 1 0 2]
    [0 2 1 0 2 0 2 1 0 2 1]
    [2 1 0 2 0 2 1 0 2 0 2]
    [1 0 2 0 2 1 0 2 0 2 1]
    [2 2 0 2 1 0 2 0 2 1 0]
    sage: window = ((0,30),(0,30))
    sage: sorted(c_floor.rectangular_subwords_matrix((2,2), window))
    [
    [0 2]  [0 2]  [1 0]  [1 0]  [2 0]  [2 1]  [2 1]  [2 2]
    [2 0], [2 1], [0 2], [2 2], [0 2], [0 2], [1 0], [1 0]
    ]
    sage: len(_)
    8

"""
#*****************************************************************************
#       Copyright (C) 2020 Sébastien Labbé <slabqc@gmail.com>
#
#  Distributed under the terms of the GNU General Public License version 2 (GPLv2)
#
#  The full text of the GPLv2 is available at:
#
#                  http://www.gnu.org/licenses/
#*****************************************************************************
from __future__ import absolute_import, print_function
from sage.modules.free_module_element import vector
from sage.functions.other import floor, ceil
from sage.matrix.constructor import matrix

class dSturmianConfiguration(object):
    r"""
    INPUT:

    - ``normal_vector`` -- tuple of coordinates
    - ``rho`` -- real number
    - ``ceil_or_floor`` -- string (default: ``'floor'``) ``'ceil'`` or
      ``'floor'``

    EXAMPLES::

        sage: from slabbe import dSturmianConfiguration
        sage: dSturmianConfiguration((.34, .72), 0)
        2-dim Sturmian Configuration: alpha=(0.340000000000000, 0.720000000000000), rho=0 using floor

    """
    def __init__(self, normal_vector, rho, ceil_or_floor='floor'):
        r"""
        Constructor.

        EXAMPLES::

            sage: from slabbe import dSturmianConfiguration
            sage: dSturmianConfiguration((.34, .72), 0)
            2-dim Sturmian Configuration: alpha=(0.340000000000000, 0.720000000000000), rho=0 using floor

        """
        self._normal_vector = vector(normal_vector)
        self._rho = rho
        self._d = len(self._normal_vector)
        self._ceil_of_floor = ceil_or_floor

    def __repr__(self):
        r"""
        Return the string representation.

        EXAMPLES::

            sage: from slabbe import dSturmianConfiguration
            sage: dSturmianConfiguration((.34, .72), 0)
            2-dim Sturmian Configuration: alpha=(0.340000000000000, 0.720000000000000), rho=0 using floor

        """
        return ("{}-dim Sturmian Configuration: "
                "alpha={}, rho={} using {}".format(self._d,
                    self._normal_vector, self._rho, self._ceil_of_floor))

    def __call__(self, n):
        r"""
        Return the letter at position ``n``.

        INPUT:

        - ``n`` -- tuple of coordinates

        EXAMPLES::

            sage: from slabbe import dSturmianConfiguration
            sage: c = dSturmianConfiguration((.34, .72), 0)
            sage: c((3,4))
            2

        """
        n = vector(n)
        scalar_product = n*self._normal_vector
        if self._ceil_of_floor == 'floor':
            return sum((floor(self._normal_vector[i] + scalar_product + self._rho) -
                        floor(scalar_product + self._rho)) for i in range(self._d))
        elif self._ceil_of_floor == 'ceil':
            return sum((ceil(self._normal_vector[i] + scalar_product + self._rho) -
                        ceil(scalar_product + self._rho)) for i in range(self._d))
        else:
            raise ValueError('ceil_or_floor (={})'.format(self._ceil_of_floor))

    def rectangular_subword(self, window):
        r"""
        Return the rectangular subword appearing in the
        given rectangular window.

        INPUT:

        - ``window`` -- tuple of 2-tuples

        OUTPUT:

        list of list with euclidean coordinates

        EXAMPLES::

            sage: from slabbe import dSturmianConfiguration
            sage: c = dSturmianConfiguration((.34, .72), 0)
            sage: window = ((0,3),(0,4))
            sage: sorted(c.rectangular_subword(window))
            [[0, 2, 1, 0], [1, 0, 2, 1], [2, 1, 0, 2]]

        """
        (xmin,xmax), (ymin,ymax) = window
        return [[self((a,b)) for b in range(ymin, ymax)]
                for a in range(xmin, xmax)]

    def rectangular_subword_matrix(self, window):
        r"""
        Return the rectangular subword appearing in the
        given rectangular window (as a matrix).

        INPUT:

        - ``window`` -- tuple of 2-tuples ``(start, stop)``

        OUTPUT:

        matrix

        EXAMPLES::

            sage: from slabbe import dSturmianConfiguration
            sage: c = dSturmianConfiguration((.34, .72), 0)
            sage: c.rectangular_subword_matrix(((0,3),(0,4)))
            [0 1 2]
            [1 2 0]
            [2 0 1]
            [0 1 2]

        """
        table = self.rectangular_subword(window)
        columns = [col[::-1] for col in table]
        return matrix.column(columns)

    def rectangular_subword_tikz(self, window, node_format=None, extra_code_after=''):
        r"""
        Return the rectangular subword appearing in the
        given rectangular window (as a TikzPicture).

        INPUT:

        - ``window`` -- tuple of 2-tuples ``(start, stop)``
        - ``node_format`` -- function or ``None``, a function giving the
          format for the matrix node at coordinate (i,j) like ``lambda
          i,j:r"{{\color{{black!60}}\symb{{{}}}}}"``.  If None, it gets
          replaced by a function which put red at positions `(0,...,0)` and
          `-e_i` and black elsewhere.
        - ``extra_code_after`` -- string (default: ``''``)

        OUTPUT:

        TikzPicture

        EXAMPLES::

            sage: from slabbe import dSturmianConfiguration
            sage: c = dSturmianConfiguration((.34, .72), 0)
            sage: tikz = c.rectangular_subword_tikz(((0,3),(0,4)))
            sage: tikz.pdf()    # not tested

        """
        M = self.rectangular_subword_matrix(window)
        if node_format is None:
            import itertools
            it = itertools.cycle([0]*self._d+[-1])
            F = set(tuple(next(it) for _ in range(self._d)) for _ in range(self._d+1))
            (xmin,xmax), (ymin,ymax) = window
            def node_format(i,j):
                if (j+xmin,ymax-1-i) in F:
                    return r"{{\color{{red!60}}\symb{{{}}}}}"
                else:
                    return r"{{\color{{black!60}}\symb{{{}}}}}"
        return matrix_to_tikz(M, node_format, boundary_dash_line=True,
                extra_code_after=extra_code_after)

    def rectangular_subword_discrete_plane_tikz(self, window,
            fill_color=None, extra_code_before='', extra_code_after=''):
        r"""
        Return the rectangular subword appearing in the
        given rectangular window (as a TikzPicture).

        INPUT:

        - ``window`` -- tuple of 2-tuples ``(start, stop)``
        - ``fill_color`` -- dict (default: ``None``), if ``None``, it is
          replaced by ``{0:'black!10',1:'black!30',2:'black!50'}``.
          Rhombus of type ``a`` have color ``fill_color[a]``.
          If tuple ``(i,j)`` is in ``fill_color``, then ``fill_color[(i,j)]``
          gives the color of the rhombus at position (i,j).
        - ``extra_code_before`` -- string (default: ``''``)
        - ``extra_code_after`` -- string (default: ``''``)

        OUTPUT:

        TikzPicture

        EXAMPLES::

            sage: from slabbe import dSturmianConfiguration
            sage: c = dSturmianConfiguration((.34, .72), 0)
            sage: tikz = c.rectangular_subword_discrete_plane_tikz(((0,3),(0,4)))
            sage: tikz.pdf()    # not tested

        A workaround using a convention based on the ordering of the normal
        vector was found to fix the overlaps of rhombus. I should
        understand and clean this hack some day::

            sage: c = dSturmianConfiguration((.72, .34), 0)
            sage: tikz = c.rectangular_subword_discrete_plane_tikz(((0,3),(0,4)))
            sage: tikz.pdf()    # not tested

        """
        # shift the coordinates of fill_color
        if fill_color:
            (xmin, xmax), (ymin, ymax) = window
            shifted_fill_color = {}
            for key, color in fill_color.items():
                try:
                    x, y = key
                except TypeError:
                    # we allow keys to be the type of rhombus (integer)
                    shifted_fill_color[key] = color
                else:
                    shifted_fill_color[(x - xmin, y - ymin)] = color
        else:
            shifted_fill_color = None
        # get the table
        table = self.rectangular_subword(window)

        # get the good convention for drawing the rhombus
        a1, a2 = self._normal_vector
        convention = 'increasing' if a1 < a2 else 'decreasing'

        return table_to_discrete_plane_tikz(table, 
                fill_color=shifted_fill_color,
                extra_code_before=extra_code_before,
                extra_code_after=extra_code_after,
                convention=convention)

    def pattern_number_occurrences(self, shape, window, avoid_border=0):
        r"""
        Return the number of occurrences of every pattern having a given
        shape inside of a rectangular window box.

        INPUT:

        - ``shape`` -- list, list of coordinates
        - ``window`` -- tuple of 2-tuples
        - ``avoid_border`` -- integer (default: 0), the size of the border
            to avoid during the computation

        OUTPUT

        a dict where each key is a tuple giving the tiles at each
        coordinate of the shape (in the same order) and values are integers

        EXAMPLES::

            sage: z = polygen(QQ, 'z')
            sage: K = NumberField(z**2-z-1, 'phi', embedding=RR(1.6))
            sage: phi = K.gen()

        ::

            sage: from slabbe import dSturmianConfiguration
            sage: c = dSturmianConfiguration((phi^-1, phi^-2), 0)
            sage: shape = [(0,0), (1,0), (0,1), (1,1)]
            sage: window = ((0,10),(0,10))
            sage: c.pattern_number_occurrences(shape, window)
            Counter({(0, 2, 1, 0): 20, (1, 0, 2, 1): 18, (2, 1, 0, 2): 18, 
                     (2, 0, 0, 2): 13, (0, 2, 2, 0): 12})

        Totally irrational normal vector::

            sage: c = dSturmianConfiguration((phi^-1, sqrt(2)), 0)
            sage: shape = [(0,0), (1,0), (0,1), (1,1)]
            sage: window = ((0,10),(0,10))
            sage: len(c.pattern_number_occurrences(shape, window))
            8

        """
        table = self.rectangular_subword(window)
        width = len(table)
        height = len(table[0])

        shape_xmin = min(x for (x,y) in shape)
        shape_xmax = max(x for (x,y) in shape)
        shape_ymin = min(y for (x,y) in shape)
        shape_ymax = max(y for (x,y) in shape)

        from collections import Counter
        C = Counter()
        for i in range(0-shape_xmin+avoid_border, width-shape_xmax-avoid_border):
            for j in range(0-shape_ymin+avoid_border, height-shape_ymax-avoid_border):
                pattern = tuple(table[i+x][j+y] for (x,y) in shape)
                C[pattern] += 1
        return C

    def pattern_complexity(self, shape, window, avoid_border=0, verbose=False):
        r"""
        Return the number of patterns having a given shape inside of a
        rectangular window box.

        INPUT:

        - ``shape`` -- list, list of coordinates
        - ``window`` -- tuple of 2-tuples
        - ``avoid_border`` -- integer (default: 0), the size of the border
            to avoid during the computation
        - ``verbose`` -- bool (default: ``False``), print the theoretical
          upper-bound

        OUTPUT

        integer

        EXAMPLES::

            sage: z = polygen(QQ, 'z')
            sage: K = NumberField(z**2-z-1, 'phi', embedding=RR(1.6))
            sage: phi = K.gen()

        ::

            sage: from slabbe import dSturmianConfiguration
            sage: c = dSturmianConfiguration((phi^-1, phi^-2), 0)
            sage: shape = [(0,0), (1,0), (0,1), (1,1)]
            sage: window = ((0,10),(0,10))
            sage: c.pattern_complexity(shape, window)
            5

        Totally irrational normal vector::

            sage: c = dSturmianConfiguration((phi^-1, sqrt(2)), 0)
            sage: shape = [(0,0), (1,0), (0,1), (1,1)]
            sage: window = ((0,10),(0,10))
            sage: c.pattern_complexity(shape, window)
            8

        """
        if verbose:
            print("upper bound is:", self.pattern_complexity_upper_bound(shape))
        C = self.pattern_number_occurrences(shape, window, avoid_border=avoid_border)
        return len(C)

    def pattern_complexity_upper_bound(self, shape):
        r"""
        Return the known upper bound for the number of patterns of given
        shape it may have.

        INPUT:

        - ``shape`` -- list, list of coordinates

        OUTPUT

        integer

        EXAMPLES::

            sage: z = polygen(QQ, 'z')
            sage: K = NumberField(z**2-z-1, 'phi', embedding=RR(1.6))
            sage: phi = K.gen()

        ::

            sage: from slabbe import dSturmianConfiguration
            sage: c = dSturmianConfiguration((phi^-1, phi^-2), 0)
            sage: shape = [(0,0), (1,0), (0,1), (1,1)]
            sage: c.pattern_complexity_upper_bound(shape)
            8

        Totally irrational normal vector::

            sage: c = dSturmianConfiguration((phi^-1, sqrt(2)), 0)
            sage: shape = [(0,0), (1,0), (0,1), (1,1)]
            sage: c.pattern_complexity_upper_bound(shape)
            8

        """
        F = [vector(t) for t in ((0,0), (0,-1), (-1,0))]
        S = [vector(t) for t in shape]
        F_minus_S = set(tuple(f - s) for f in F for s in S)
        return len(F_minus_S)

    def language(self, shape):
        r"""
        Return the language of a given shape.

        INPUT:

        - ``shape`` -- list, list of coordinates

        OUTPUT:

        list of tuples

        EXAMPLES::

            sage: sqrt2 = AA(sqrt(2))
            sage: sqrt3 = AA(sqrt(3))
            sage: from slabbe import dSturmianConfiguration
            sage: c = dSturmianConfiguration((sqrt2/2, sqrt3/4), 0)
            sage: shape = [(0,0), (1,0), (0,1), (1,1)]
            sage: sorted(c.language(shape))
            [(0, 2, 1, 0),
             (0, 2, 2, 0),
             (0, 2, 2, 1),
             (1, 0, 2, 1),
             (1, 0, 2, 2),
             (2, 0, 0, 2),
             (2, 1, 0, 2),
             (2, 2, 1, 0)]
            sage: len(set(c.language(shape)))
            8
            sage: c.pattern_complexity_upper_bound(shape)
            8

        """
        F = [vector(t) for t in ((0,0), (0,-1), (-1,0))]
        S = [vector(t) for t in shape]
        F_minus_S = set(tuple(f - s) for f in F for s in S)
        return [tuple(self(n+vector(f_s)) for n in S) for f_s in F_minus_S]


    def bispecial_patterns_of_shape(self, shape, a, b):
        r"""
        Return the patterns of a given shape bispecial at positions a and b

        INPUT:

        - ``shape`` -- list, list of coordinates
        - ``a`` -- position
        - ``b`` -- position

        EXAMPLES::

            sage: z = polygen(QQ, 'z')
            sage: K = NumberField(z**2-z-1, 'phi', embedding=RR(1.6))
            sage: phi = K.gen()

        ::

            sage: from slabbe import dSturmianConfiguration
            sage: c = dSturmianConfiguration((phi^-1, phi^-2), 0)
            sage: shape = [(0,0), (1,0), (0,1), (1,1)]
            sage: c.bispecial_patterns_of_shape(shape, (-1,0), (2,1))
            []

        With totally irrational normal vector::

            sage: c = dSturmianConfiguration((phi^-1, sqrt(2)), 0)
            sage: shape = [(0,0), (1,0), (0,1), (1,1)]
            sage: c.bispecial_patterns_of_shape(shape, (-1,0), (2,1))
            [(3, 1, 1, 3)]

        """
        a_shape_b = []
        a_shape_b.append(a)
        a_shape_b.extend(shape)
        a_shape_b.append(b)
        from collections import defaultdict
        E_left = defaultdict(set)
        E_right = defaultdict(set)
        language_Sab = self.language(a_shape_b)
        for pattern in language_Sab:
            E_left[tuple(pattern[1:-1])].add(pattern[0])
            E_right[tuple(pattern[1:-1])].add(pattern[-1])
        left_special = [pattern for (pattern,left_extensions) in
                                     E_left.items() if len(left_extensions) > 1]
        right_special = [pattern for (pattern,right_extensions) in
                                     E_right.items() if len(right_extensions) > 1]
        return sorted(set(left_special) & set(right_special))

    def bispecial_patterns_of_Lshape(self, v):
        r"""
        Return the patterns of a given L-shape bispecial of vector v

        INPUT:

        - ``v`` -- vector

        EXAMPLES::

            sage: z = polygen(QQ, 'z')
            sage: K = NumberField(z**2-z-1, 'phi', embedding=RR(1.6))
            sage: phi = K.gen()

        ::

            sage: from slabbe import dSturmianConfiguration
            sage: c = dSturmianConfiguration((phi^-1, sqrt(2)), 0)
            sage: c.bispecial_patterns_of_Lshape((3,1))
            [(3, 1, 3)]
            sage: c.bispecial_patterns_of_Lshape((0,7))
            [(3, 1, 3, 1, 2, 3)]
            sage: c.bispecial_patterns_of_Lshape((7,0))
            [(3, 1, 3, 2, 1, 3)]

        """
        i,j = v
        assert i >= 0
        if j > 0:
            shape = [(a,0) for a in range(1,i+1)]
            shape.extend((i,b) for b in range(1,j))
            bispecials = self.bispecial_patterns_of_shape(shape, (0,0), (i,j))
        elif j == 0:
            shape = [(a,0) for a in range(1,i)]
            bispecials = self.bispecial_patterns_of_shape(shape, (0,0), (i,j))
        else:
            j = -j
            assert i > 0
            shape = [(a,0) for a in range(1,i)]
            shape.extend((i,-b) for b in range(j))
            bispecials = self.bispecial_patterns_of_shape(shape, (0,0), (i,-j))
        return bispecials

    def bispecial_patterns(self, n):
        r"""
        Return the vectors of L-shaped bispecial patterns of size up to n.

        INPUT:

        - ``n`` -- integer, maximum size

        EXAMPLES::

            sage: z = polygen(QQ, 'z')
            sage: K = NumberField(z**2-z-1, 'phi', embedding=RR(1.6))
            sage: phi = K.gen()

        ::

            sage: from slabbe import dSturmianConfiguration
            sage: c = dSturmianConfiguration((phi^-1, phi^-2), 0)
            sage: c.bispecial_patterns(5)
            {(0, 0): [()],
             (0, 1): [()],
             (0, 3): [(2, 0)],
             (1, -2): [(0, 2)],
             (1, 0): [()],
             (1, 1): [(0,)],
             (2, -4): [(0, 2, 1, 0, 2)],
             (2, -1): [(0, 2)],
             (2, 2): [(0, 2, 0)],
             (3, -3): [(0, 2, 1, 0, 2)],
             (3, 0): [(0, 2)],
             (3, 3): [(0, 2, 1, 2, 0)],
             (4, -2): [(0, 2, 1, 0, 2)],
             (4, 4): [(0, 2, 1, 0, 1, 2, 0)]}

        With totally irrational normal vector::

            sage: c = dSturmianConfiguration((phi^-1, sqrt(2)), 0)
            sage: c.bispecial_patterns(5)
            {(0, 0): [()],
             (0, 1): [()],
             (0, 2): [(3,)],
             (0, 3): [(2, 3), (3, 1)],
             (1, -4): [(1, 3, 1, 3)],
             (1, -3): [(3, 1, 3)],
             (1, -2): [(1, 3)],
             (1, -1): [(3,)],
             (1, 0): [()],
             (1, 1): [(1,), (3,)],
             (1, 2): [(3, 1)],
             (1, 3): [(1, 3, 1)],
             (1, 4): [(3, 1, 2, 3)],
             (2, -3): [(3, 1, 3, 2)],
             (2, -2): [(1, 3, 2), (3, 1, 3)],
             (2, -1): [(1, 3)],
             (2, 0): [(3,)],
             (2, 1): [(1, 3)],
             (2, 2): [(1, 3, 1)],
             (2, 3): [(3, 1, 3, 1)],
             (2, 4): [(1, 3, 1, 3, 1)],
             (3, -2): [(3, 1, 3, 2)],
             (3, -1): [(1, 3, 2)],
             (3, 0): [(1, 3)],
             (3, 1): [(3, 1, 3)],
             (3, 2): [(1, 3, 2, 3)],
             (3, 4): [(3, 1, 3, 1, 3, 1)],
             (4, -4): [(1, 3, 2, 1, 3, 1, 3)],
             (4, 0): [(3, 1, 3)],
             (4, 1): [(1, 3, 2, 1)],
             (4, 2): [(3, 1, 3, 2, 3)],
             (4, 3): [(1, 3, 2, 1, 2, 3)]}

        """
        d = {}
        import itertools
        for i,j in itertools.product(range(n), range(-n+1,n)):
            if i == 0 and j < 0:
                continue
            bispecials = self.bispecial_patterns_of_Lshape((i,j))
            if bispecials:
                d[(i,j)] = bispecials
        return d

    def rectangular_subwords(self, sizes, window):
        r"""
        Return the list of rectangular subword appearing in the
        configuration.

        INPUT:

        - ``sizes`` -- tuple of integers
        - ``window`` -- tuple of 2-tuples

        OUTPUT:

        list of euclidean coordinate tables

        EXAMPLES::

            sage: z = polygen(QQ, 'z')
            sage: K = NumberField(z**2-z-1, 'phi', embedding=RR(1.6))
            sage: phi = K.gen()

        ::

            sage: from slabbe import dSturmianConfiguration
            sage: c = dSturmianConfiguration((phi^-1, sqrt(2)), 0)
            sage: c.rectangular_subwords((2,3), ((0,30),(0,30)))
            [[[1, 2, 3], [3, 1, 2]],
             [[2, 3, 1], [1, 2, 3]],
             [[3, 1, 3], [2, 3, 1]],
             [[1, 3, 1], [3, 1, 3]],
             [[3, 1, 2], [1, 3, 1]],
             [[1, 2, 3], [3, 1, 3]],
             [[2, 3, 2], [1, 3, 1]],
             [[3, 2, 3], [3, 1, 2]],
             [[3, 1, 3], [2, 3, 2]],
             [[1, 3, 1], [3, 2, 3]],
             [[3, 1, 3], [1, 3, 1]]]

        """
        import itertools
        shape = list(itertools.product(*[range(size) for size in sizes]))
        C = self.pattern_number_occurrences(shape, window)
        patterns = C.keys()
        L = []
        for pattern in patterns:
            table = [[None for _ in range(sizes[1])] for _ in range(sizes[0])]
            for i,(x,y) in enumerate(shape):
                table[x][y] = pattern[i] 
            L.append(table)
        return L

    def rectangular_subwords_matrix(self, sizes, window):
        r"""
        Return the list of rectangular subword appearing under the form of
        matrices.

        INPUT:

        - ``sizes`` -- tuple of integers
        - ``window`` -- tuple of 2-tuples

        OUTPUT:

        list of matrices

        EXAMPLES::

            sage: z = polygen(QQ, 'z')
            sage: K = NumberField(z**2-z-1, 'phi', embedding=RR(1.6))
            sage: phi = K.gen()

            sage: from slabbe import dSturmianConfiguration
            sage: c = dSturmianConfiguration((phi^-1, sqrt(2)), 0)
            sage: c.rectangular_subwords_matrix((2,3), ((0,30),(0,30)))
            [
            [3 2]  [1 3]  [3 1]  [1 3]  [2 1]  [3 3]  [2 1]  [3 2]  [3 2]  [1 3]
            [2 1]  [3 2]  [1 3]  [3 1]  [1 3]  [2 1]  [3 3]  [2 1]  [1 3]  [3 2]
            [1 3], [2 1], [3 2], [1 3], [3 1], [1 3], [2 1], [3 3], [3 2], [1 3],
            <BLANKLINE>
            [3 1]
            [1 3]
            [3 1]
            ]
            sage: len(_)
            11

        """
        L = self.rectangular_subwords(sizes, window)
        return [matrix.column([col[::-1] for col in table]) for table in L]

def matrix_to_tikz(M, node_format=None, boundary_dash_line=False, extra_code_after=''):
    r"""
    Return the matrix as a nice TikzPicture.

    INPUT:

    - ``M`` -- matrix
    - ``node_format`` -- format for the node or ``None``. If None,
      it gets replaced by ``lambda i,j:r"{{\color{{black!60}}\symb{{{}}}}}"``
    - ``boundary_dash_line`` -- boolean (default: ``False``)
    - ``extra_code_after`` -- string (default: ``''``)

    OUTPUT:

    TikzPicture

    .. NOTE::

        The tikz code below comes from Sebastián Barbieri.

    EXAMPLES::

        sage: from slabbe.ddim_sturmian_configuration import matrix_to_tikz
        sage: M = identity_matrix(4)
        sage: matrix_to_tikz(M)
        \documentclass[tikz]{standalone}
        \newcommand{\symb}[1]{\mathtt{#1}}  % Symbol
        \usetikzlibrary{matrix}
        \usetikzlibrary{fit}
        \begin{document}
        \begin{tikzpicture}
        [baseline=-\the\dimexpr\fontdimen22\textfont2\relax,ampersand replacement=\&]
          \matrix[matrix of math nodes,nodes={
               minimum size=1.2ex,text width=1.2ex,
               text height=1.2ex,inner sep=3pt,draw={gray!20},align=center,
        ...
        4 lines not printed (790 characters in total).
        ...
        };
        \end{tikzpicture}
        \end{document}

    """
    if node_format is None:
        node_format = lambda i,j:r"{{\color{{black!60}}\symb{{{}}}}}"

    lines = []
    lines.append(r"\begin{tikzpicture}")
    lines.append(r"[baseline=-\the\dimexpr\fontdimen22\textfont2\relax,ampersand replacement=\&]")
    lines.append(r"  \matrix[matrix of math nodes,nodes={")
    lines.append(r"       minimum size=1.2ex,text width=1.2ex,")
    lines.append(r"       text height=1.2ex,inner sep=3pt,draw={gray!20},align=center,")
    lines.append(r"       anchor=base")
    lines.append(r"     }, row sep=1pt,column sep=1pt")
    lines.append(r"  ] (config) {")
    for i,row in enumerate(M.rows()):
        lines.append(r'\&'.join([node_format(i,j).format(a) for j,a in enumerate(row)]) + r'\\')
    lines.append(r"};")
    if boundary_dash_line:
        lines.append(r"\node[draw,rectangle,dashed,help lines,fit=(config), inner sep=0.5ex] {};")
    if extra_code_after:
        lines.append(extra_code_after)
    lines.append(r"\end{tikzpicture}")

    from slabbe import TikzPicture
    usetikzlibrary = "matrix,fit".split(',')
    macros = [r'\newcommand{\symb}[1]{\mathtt{#1}}  % Symbol']
    return TikzPicture('\n'.join(lines), usetikzlibrary=usetikzlibrary, macros=macros)

def table_to_discrete_plane_tikz(table, fill_color=None,
        extra_code_before='', extra_code_after='', convention='increasing'):
    r"""
    Return a discrete plane representation of the table over alphabet `0`,
    `1` and `2`.

    INPUT:

    - ``table`` -- list of list (cartesian-like coordinates) over alphabet
      `0`, `1` and `2`
    - ``extra_code_before`` -- string (default: ``''``)
    - ``extra_code_after`` -- string (default: ``''``)
    - ``fill_color`` -- dict (default: ``None``), if ``None``, it is
      replaced by ``{0:'black!10',1:'black!30',2:'black!50'}``.
      Rhombus of type ``a`` have color ``fill_color[a]``.
      If tuple ``(i,j)`` is in ``fill_color``, then ``fill_color[(i,j)]``
      gives the color of the rhombus at position (i,j).
    - ``convention`` -- string, ``'decreasing'`` or ``'increasing'``, the
      convention for drawing the rhombus according to increasing or
      decreasing normal vectors

    OUTPUT:

    TikzPicture

    .. TODO::

        Understand, improve and replace the ``convention`` argument by
        something better.

    EXAMPLES::

        sage: from slabbe.ddim_sturmian_configuration import table_to_discrete_plane_tikz
        sage: from slabbe import dSturmianConfiguration
        sage: c = dSturmianConfiguration((.34, .72), 0)
        sage: table = c.rectangular_subword(((0,3),(0,4)))
        sage: table_to_discrete_plane_tikz(table)
        \documentclass[tikz]{standalone}
        \begin{document}
        \begin{tikzpicture}
        \draw[fill=black!10] (0.000000000000000, 0.000000000000000) -- (0.866025403784439, 0.500000000000000) -- (0.000000000000000, 1.00000000000000) -- (-0.866025403784439, 0.500000000000000) -- (0.000000000000000, 0.000000000000000);
        \draw[fill=black!70] (0.000000000000000, 0.000000000000000) -- ++ (30:1.7mm) arc (30:150:1.7mm);
        \node[label=90:0] at (0.000000000000000, 0.000000000000000) {};
        \draw[fill=black!50] (0.000000000000000, 1.00000000000000) -- (0.866025403784439, 0.500000000000000) -- (0.866025403784439, 1.50000000000000) -- (0.000000000000000, 2.00000000000000) -- (0.000000000000000, 1.00000000000000);
        ...
        28 lines not printed (4613 characters in total).
        ...
        \node[label=90:0] at (1.73205080756888, 3.00000000000000) {};
        \draw[fill=black!50] (1.73205080756888, 4.00000000000000) -- (2.59807621135332, 3.50000000000000) -- (2.59807621135332, 4.50000000000000) -- (1.73205080756888, 5.00000000000000) -- (1.73205080756888, 4.00000000000000);
        \draw[fill=black!70] (1.73205080756888, 4.00000000000000) -- ++ (-30:1.7mm) arc (-30:90:1.7mm);
        \node[label=30:2] at (1.73205080756888, 4.00000000000000) {};
        \end{tikzpicture}
        \end{document}

    """
    import itertools
    from slabbe import M3to2


    # faces of a unit cube
    zero = vector((0,0,0))
    e0 = vector((1,0,0))
    e1 = vector((0,1,0))
    e2 = vector((0,0,1))
    if convention == "increasing":
        cube_faces = {0:[zero, -e0, -e0-e1, -e1, zero],
                      1:[zero, e2, e2-e0, -e0, zero],
                      2:[zero, e1, e1+e2, e2, zero]}
        label_angle = {0:90, 1:80, 2:30}
        cone_angle = {0:(30,150), 1:(30,90), 2:(-30,90)}
    elif convention == "decreasing":
        cube_faces = {0:[zero, e1, e1+e2, e2, zero],
                      1:[zero, e2, e2-e0, -e0, zero],
                      2:[zero, -e0, -e0-e1, -e1, zero]}
        label_angle = {0:30, 1:80, 2:90}
        cone_angle = {0:(-30,90), 1:(30,90), 2:(30,150)}
    else:
        raise ValueError('convention(={}) is not a valid option'.format(convention))

    if fill_color is None:
        fill_color = {0:'black!10',
                      1:'black!30',
                      2:'black!50'}

    lines = []
    lines.append(r"\begin{tikzpicture}")
    if extra_code_before:
        lines.append(extra_code_before)
    width = len(table)
    height = len(table[0])
    for (i,j) in itertools.product(range(width), range(height)):
        a = table[i][j]
        start = vector((-i,0,j))
        startp = M3to2 * start
        # rhombus contour
        path_2d = [M3to2 * (start+v) for v in cube_faces[a]]
        path_str = ' -- '.join(r"{}".format(pt) for pt in path_2d)
        fill = fill_color.get((i,j), fill_color[a])
        lines.append(r'\draw[fill={}] {};'.format(fill, path_str))
        # arc
        c,d = cone_angle[a]
        lines.append(r'\draw[fill=black!70] {} -- ++ '
                     r'({}:1.7mm) arc ({}:{}:1.7mm);'.format(startp,c,c,d))
        # node
        lines.append(r'\node[label={}:{}] at {} {{}};'.format(label_angle[a],a,startp))
    if extra_code_after:
        lines.append(extra_code_after)
    lines.append(r"\end{tikzpicture}")

    from slabbe import TikzPicture
    return TikzPicture('\n'.join(lines))

