# -*- coding: utf-8 -*-
r"""
TikzPicture

A Python Module for tikz pictures. A TikzPicture object is created from a string
starting with ``r'\begin{tikzpicture}'`` and ending with
``r'\end{tikzpicture}'``.

The module allows easy creation of tikz pictures from Sage objects like graphs
and posets. Conversion of tikz pictures to pdf and png format based on
standalone LaTeX document class.

EXAMPLES::

    sage: from slabbe import TikzPicture
    sage: lines = []
    sage: lines.append(r'\begin{tikzpicture}')
    sage: lines.append(r'\draw[very thick,orange,->] (0,0) -- (1,1);')
    sage: lines.append(r'\end{tikzpicture}')
    sage: s = '\n'.join(lines)
    sage: t = TikzPicture(s)

Creation of a pdf in a temporary directory. The returned value is a string
giving the file path::

    sage: path_to_file = t.pdf(view=False)   # long time (2s)

Setting ``view=True``, which is the default, opens the pdf in a viewer.

::

    zage: t
    \documentclass[tikz]{standalone}
    \begin{document}
    \begin{tikzpicture}
    \draw[very thick,orange,->] (0,0) -- (1,1);
    \end{tikzpicture}
    \end{document}

Use ``print t`` to see the complete content of the file.

Adding a border avoids croping the vertices of a graph::

    sage: g = graphs.PetersenGraph()
    sage: s = latex(g)   # takes 3s but the result is cached
    sage: t = TikzPicture(s, standalone_config=["border=4mm"], usepackage=['tkz-graph'])
    sage: _ = t.pdf()    # not tested

If dot2tex Sage optional package and graphviz are installed, then the following
one liner works::

    sage: t = TikzPicture.from_graph(g)  # optional: dot2tex (3s)
    doctest:...: FutureWarning: This class/method/function is marked as experimental.
    It, its functionality or its interface might change without a formal deprecation.
    See http...20343 for details.

::

    sage: s = latex(transducers.GrayCode())
    sage: t = TikzPicture(s, usetikzlibrary=['automata'])
    sage: _ = t.pdf(view=False)  # long time (2s)

AUTHORS:

- Sébastien Labbé, initial version in slabbe-0.2.spkg, nov 2015.
"""
#*****************************************************************************
#       Copyright (C) 2015-2019 Sébastien Labbé <slabqc@gmail.com>
#
#  Distributed under the terms of the GNU General Public License version 2 (GPLv2)
#
#  The full text of the GPLv2 is available at:
#
#                  http://www.gnu.org/licenses/
#*****************************************************************************
from __future__ import absolute_import, print_function

from subprocess import run, PIPE
import os

try:
    from sage.misc.latex import have_program
except ImportError:
    from sage.misc.sage_ostools import have_program

from sage.misc.temporary_file import tmp_filename
from sage.structure.sage_object import SageObject

from sage.misc.decorators import rename_keyword
#from sage.misc.superseded import experimental

class Standalone(SageObject):
    @rename_keyword(standalone_options="standalone_config")
    def __init__(self, content, standalone_config=None, usepackage=None,
            usetikzlibrary=None, macros=None, use_sage_preamble=False):
        r"""
        See the class documentation for full information.

        EXAMPLES::

            sage: from slabbe import Standalone
            sage: content = "\\section{Intro}\n\nTest\n"
            sage: t = Standalone(content)

        ::

            sage: from slabbe import TikzPicture
            sage: s = "\\begin{tikzpicture}\n\\draw (0,0) -- (1,1);\n\\end{tikzpicture}"
            sage: t = TikzPicture(s)
        """
        self._content = content
        self._standalone_config = [] if standalone_config is None else standalone_config
        self._usepackage = [] if usepackage is None else usepackage
        self._usetikzlibrary = [] if usetikzlibrary is None else usetikzlibrary
        self._macros = [] if macros is None else macros
        if use_sage_preamble:
            from sage.misc.latex import _Latex_prefs
            for key in ['preamble', 'macros']:
                s = _Latex_prefs._option[key]
                if s: 
                    self._macros.append(s)
            from sage.misc.latex_macros import sage_latex_macros
            self._macros.extend(sage_latex_macros())

    def _latex_file_header_lines(self):
        r"""
        EXAMPLES::

            sage: latex.extra_preamble('')
            sage: from slabbe import TikzPicture
            sage: s = "\\begin{tikzpicture}\n\\draw (0,0) -- (1,1);\n\\end{tikzpicture}"
            sage: t = TikzPicture(s, standalone_config=["border=4mm"], usepackage=['tkz-graph'])
            sage: t._latex_file_header_lines()[:6]
            ['\\documentclass[tikz]{standalone}',
             '\\standaloneconfig{border=4mm}',
             '\\usepackage{tkz-graph}']
        """
        lines = []
        lines.append(r"\documentclass[tikz]{standalone}")
        for config in self._standalone_config:
            lines.append(r"\standaloneconfig{{{}}}".format(config))
        for package in self._usepackage:
            lines.append(r"\usepackage{{{}}}".format(package))
        lines.extend(self._macros)
        for library in self._usetikzlibrary:
            lines.append(r"\usetikzlibrary{{{}}}".format(library))
        return lines

    def _repr_(self):
        r"""
        Returns the first few and last few lines.

        EXAMPLES::

            sage: from slabbe import TikzPicture
            sage: g = graphs.PetersenGraph()
            sage: s = latex(g)
            sage: t = TikzPicture(s, usepackage=['tkz-graph'])
            sage: t
            \documentclass[tikz]{standalone}
            \usepackage{tkz-graph}
            \begin{document}
            \begin{tikzpicture}
            \definecolor{cv0}{rgb}{0.0,0.0,0.0}
            \definecolor{cfv0}{rgb}{1.0,1.0,1.0}
            \definecolor{clv0}{rgb}{0.0,0.0,0.0}
            \definecolor{cv1}{rgb}{0.0,0.0,0.0}
            ...
            65 lines not printed (3695 characters in total).
            ...
            \Edge[lw=0.1cm,style={color=cv6v8,},](v6)(v8)
            \Edge[lw=0.1cm,style={color=cv6v9,},](v6)(v9)
            \Edge[lw=0.1cm,style={color=cv7v9,},](v7)(v9)
            %
            \end{tikzpicture}
            \end{document}
        """
        lines = self._latex_file_header_lines()
        lines.append(r"\begin{document}")
        L = self._content.splitlines()
        if len(L) <= 10:
            lines.extend(L)
        else:
            lines.extend(L[:5])
            lines.append('...')
            lines.append('{} lines not printed ({} characters in total).'.format(len(L)-10, 
                                                           len(self._content)))
            lines.append('...')
            lines.extend(L[-5:])
        lines.append(r"\end{document}")
        return '\n'.join(lines)

    def _rich_repr_(self, display_manager, **kwds):
        """
        Rich Output Magic Method

        See :mod:`sage.repl.rich_output` for details.

        EXAMPLES::

            sage: from sage.repl.rich_output import get_display_manager
            sage: dm = get_display_manager()
            sage: dm.is_in_terminal()
            False

            sage: from slabbe import TikzPicture
            sage: lines = []
            sage: lines.append(r'\begin{tikzpicture}')
            sage: lines.append(r'\draw[very thick,orange,->] (0,0) -- (1,1);')
            sage: lines.append(r'\end{tikzpicture}')
            sage: s = '\n'.join(lines)
            sage: t = TikzPicture(s)
            sage: t._rich_repr_(dm)      # random result is Text in doctest
            OutputImagePng container

        Using vector svg instead of png::

            sage: dm.preferences.graphics = 'vector'
            sage: t._rich_repr_(dm)      # random result is Text in doctest
            OutputImageSvg container
            sage: dm.preferences.graphics = 'raster'
        """
        # Do not use rich output in the terminal
        if display_manager.is_in_terminal():
            return
        # Do not use rich output if not in IPython notebook (Jupyter)
        from sage.repl.rich_output.backend_ipython import BackendIPythonNotebook
        if not isinstance(display_manager._backend, BackendIPythonNotebook):
            return

        types = display_manager.types
        prefer_raster = (
            ('png', types.OutputImagePng),
        )
        prefer_vector = (
            ('svg', types.OutputImageSvg),
            ('pdf', types.OutputImagePdf),
        )
        graphics = display_manager.preferences.graphics
        if graphics == 'disable':
            return
        elif graphics == 'raster' or graphics is None:
            preferred = prefer_raster + prefer_vector
        elif graphics == 'vector':
            preferred = prefer_vector + prefer_raster
        else:
            raise ValueError('unknown graphics output preference')

        for format, output_container in preferred:
            if output_container in display_manager.supported_output():
                filename = getattr(self, format)(view=False, **kwds)
                from sage.repl.rich_output.buffer import OutputBuffer
                buf = OutputBuffer.from_file(filename)
                return output_container(buf)

    def __str__(self):
        r"""
        Returns the complete string.

        EXAMPLES::

            sage: from slabbe import TikzPicture
            sage: s = "\\begin{tikzpicture}\n\\draw (0,0) -- (1,1);\n\\end{tikzpicture}"
            sage: t = TikzPicture(s)
            sage: print(t)
            \RequirePackage{luatex85}
            \documentclass[tikz]{standalone}
            \begin{document}
            \begin{tikzpicture}
            \draw (0,0) -- (1,1);
            \end{tikzpicture}
            \end{document}
        """
        lines = []
        # LuaLaTeX, TeXLive 2016, standalone: undefined control sequence
        # https://tex.stackexchange.com/questions/315025
        # fixed in 2018, meanwhile, we add the fix here
        lines.append(r"\RequirePackage{luatex85}")
        lines.extend(self._latex_file_header_lines())
        lines.append(r"\begin{document}")
        lines.append(self._content)
        lines.append(r"\end{document}")
        return '\n'.join(lines)

    def content(self):
        r"""
        EXAMPLES::

            sage: from slabbe import TikzPicture
            sage: s = "\\begin{tikzpicture}\n\\draw (0,0) -- (1,1);\n\\end{tikzpicture}"
            sage: t = TikzPicture(s)
            sage: print(t.tikz_picture_code())
            \begin{tikzpicture}
            \draw (0,0) -- (1,1);
            \end{tikzpicture}
        """
        return self._content

    def pdf(self, filename=None, view=True, program=None):
        r"""
        Compiles the latex code with pdflatex and create a pdf file.

        INPUT:

        - ``filename`` -- string (default:``None``), the output filename. 
          If ``None``, it saves the file in a temporary directory.

        - ``view`` -- bool (default:``True``), whether to open the file in a
          pdf viewer. This option is ignored and automatically set to
          ``False`` if ``filename`` is not ``None``.

        - ``program`` -- string (default:``None``) ``'pdflatex'`` or
          ``'lualatex'``. If ``None``, it uses ``'lualatex'`` if it is
          available, otherwise ``'pdflatex'``.

        OUTPUT:

            string, path to pdf file

        EXAMPLES::

            sage: from slabbe import TikzPicture
            sage: lines = []
            sage: lines.append(r'\begin{tikzpicture}')
            sage: lines.append(r'\draw[very thick,orange,->] (0,0) -- (1,1);')
            sage: lines.append(r'\end{tikzpicture}')
            sage: s = '\n'.join(lines)
            sage: t = TikzPicture(s)
            sage: _ = t.pdf()    # not tested

        ::

            sage: from sage.misc.temporary_file import tmp_filename
            sage: filename = tmp_filename('temp','.pdf')
            sage: _ = t.pdf(filename)   # long time (2s)

        ACKNOWLEDGEMENT:

            The code was adapted and taken from the module :mod:`sage.misc.latex.py`.
        """
        # Set default program
        if program is None:
           if have_program('lualatex'):
               program = 'lualatex'
           else:
               program = 'pdflatex'

        # Check availability of programs
        if program == 'pdflatex' and not have_program(program):
            raise RuntimeError("PDFLaTeX does not seem to be installed. " 
                    "Download it from ctan.org and try again.")
        elif program == 'lualatex' and not have_program(program):
            raise RuntimeError("lualatex does not seem to be installed.")
        elif program not in ['pdflatex','lualatex']:
            raise ValueError("program(={}) should be pdflatex or lualatex".format(program))

        # set up filenames
        _filename_tex = tmp_filename('tikz_','.tex')
        with open(_filename_tex, 'w') as f:
            f.write(str(self))
        base, _filename_tex = os.path.split(_filename_tex)
        _filename, ext = os.path.splitext(_filename_tex)

        # running pdflatex or lualatex
        cmd = [program, '-interaction=nonstopmode', _filename_tex]
        cmd = ' '.join(cmd)
        run(cmd, shell=True, stdout=PIPE, stderr=PIPE, cwd=base, check=True)
        _filename_pdf = os.path.join(base, _filename+'.pdf')

        # move the pdf into the good location
        if filename:
            filename = os.path.abspath(filename)
            os.rename(_filename_pdf, filename)
            return filename

        # open the tmp pdf
        elif view:
            from sage.misc.viewer import pdf_viewer
            cmd = [pdf_viewer(), _filename_pdf]
            cmd = ' '.join(cmd)
            run(cmd, shell=True, cwd=base, stdout=PIPE, stderr=PIPE, check=True)

        return _filename_pdf

    def png(self, filename=None, density=150, view=True):
        r"""
        Compiles the latex code with pdflatex and converts to a png file.

        INPUT:

        - ``filename`` -- string (default:``None``), the output filename. 
          If ``None``, it saves the file in a temporary directory.

        - ``density`` -- integer, (default: ``150``), horizontal and vertical
          density of the image

        - ``view`` -- bool (default:``True``), whether to open the file in a
          png viewer. This option is ignored and automatically set to
          ``False`` if ``filename`` is not ``None``.

        OUTPUT:

            string, path to png file

        EXAMPLES::

            sage: from slabbe import TikzPicture
            sage: lines = []
            sage: lines.append(r'\begin{tikzpicture}')
            sage: lines.append(r'\draw[very thick,orange,->] (0,0) -- (1,1);')
            sage: lines.append(r'\end{tikzpicture}')
            sage: s = '\n'.join(lines)
            sage: t = TikzPicture(s)
            sage: _ = t.png()    # not tested

        ::

            sage: from sage.misc.temporary_file import tmp_filename
            sage: filename = tmp_filename('temp','.png')
            sage: _ = t.png(filename)      # long time (2s)

        ACKNOWLEDGEMENT:

            The code was adapted and taken from the module :mod:`sage.misc.latex.py`.
        """
        try:
            from sage.features.imagemagick import ImageMagick
        except ImportError:
            # This is deprecated in sagemath >=9.5
            from sage.misc.latex import have_convert
            if not have_convert():
                raise RuntimeError("convert (from the ImageMagick suite) does not "
                    "appear to be installed. Converting PDFLaTeX output to png "
                    "requires this program, so please install and try again. "
                    "Go to http://www.imagemagick.org to download it.")
        else:
            # This is how to do it in sagemath >=9.5
            ImageMagick().require()

        _filename_pdf = self.pdf(filename=None, view=False)
        _filename, ext = os.path.splitext(_filename_pdf)
        _filename_png = _filename+'.png'

        # convert to png
        cmd = ['convert', '-density',
               '{0}x{0}'.format(density), '-trim', _filename_pdf,
               _filename_png]
        cmd = ' '.join(cmd)
        run(cmd, shell=True, stdout=PIPE, stderr=PIPE, check=True)

        # move the png into the good location
        if filename:
            filename = os.path.abspath(filename)
            os.rename(_filename_png, filename)
            return filename

        # open the tmp png
        elif view:
            from sage.misc.viewer import png_viewer
            cmd = [png_viewer(), _filename_png]
            cmd = ' '.join(cmd)
            run(cmd, shell=True, stdout=PIPE, stderr=PIPE, check=True)

        return _filename_png

    def svg(self, filename=None, view=True):
        r"""
        Compiles the latex code with pdflatex and converts to a svg file.

        INPUT:

        - ``filename`` -- string (default:``None``), the output filename. 
          If ``None``, it saves the file in a temporary directory.

        - ``view`` -- bool (default:``True``), whether to open the file in
          a browser. This option is ignored and automatically set to
          ``False`` if ``filename`` is not ``None``.

        OUTPUT:

            string, path to svg file

        EXAMPLES::

            sage: from slabbe import TikzPicture
            sage: lines = []
            sage: lines.append(r'\begin{tikzpicture}')
            sage: lines.append(r'\draw[very thick,orange,->] (0,0) -- (1,1);')
            sage: lines.append(r'\end{tikzpicture}')
            sage: s = '\n'.join(lines)
            sage: t = TikzPicture(s)
            sage: _ = t.svg()    # not tested

        ::

            sage: from sage.misc.temporary_file import tmp_filename
            sage: filename = tmp_filename('temp','.svg')
            sage: _ = t.svg(filename)      # long time (2s)

        ACKNOWLEDGEMENT:

            The code was adapted and taken from the module :mod:`sage.misc.latex.py`.
        """
        if not have_program('pdf2svg'):
            raise RuntimeError("pdf2svg does not seem to be installed. " 
                    "Install it for example with ``brew install pdf2svg``"
                    " or ``apt-get install pdf2svg``.")

        _filename_pdf = self.pdf(filename=None, view=False)
        _filename, ext = os.path.splitext(_filename_pdf)
        _filename_svg = _filename+'.svg'

        # convert to svg
        cmd = ['pdf2svg', _filename_pdf, _filename_svg]
        cmd = ' '.join(cmd)
        run(cmd, shell=True, stdout=PIPE, stderr=PIPE, check=True)

        # move the svg into the good location
        if filename:
            filename = os.path.abspath(filename)
            os.rename(_filename_svg, filename)
            return filename

        # open the tmp svg
        elif view:
            from sage.misc.viewer import browser
            cmd = [browser(), _filename_svg]
            cmd = ' '.join(cmd)
            run(cmd, shell=True, stdout=PIPE, stderr=PIPE, check=True)

        return _filename_svg

    def tex(self, filename=None, content_only=False, include_header=None):
        r"""
        Writes the latex code to a file.

        INPUT:

        - ``filename`` -- string (default:``None``), the output filename.
          If ``None``, it saves the file in a temporary directory.
        - ``content_only`` -- bool (default:``False``) whether to include
          the header latex part. If ``True``, it prints only the
          content to the file.

        OUTPUT:

            string, path to tex file

        EXAMPLES::

            sage: from slabbe import TikzPicture
            sage: lines = []
            sage: lines.append(r'\begin{tikzpicture}')
            sage: lines.append(r'\draw[very thick,orange,->] (0,0) -- (1,1);')
            sage: lines.append(r'\end{tikzpicture}')
            sage: s = '\n'.join(lines)
            sage: t = TikzPicture(s)
            sage: _ = t.tex()

        Write only the tikzpicture without header and begin/end document::

            sage: _ = t.tex(content_only=True)

        Write to a given filename::

            sage: from sage.misc.temporary_file import tmp_filename
            sage: filename = tmp_filename('temp','.tex')
            sage: _ = t.tex(filename)

        """
        if filename is None:
            from sage.misc.temporary_file import tmp_filename
            filename = tmp_filename('tikz_', '.tex')
        else:
            filename = os.path.abspath(filename)

        if include_header is not None:
            content_only = not include_header
            from sage.misc.superseded import deprecation
            deprecation(20343, "When merging this code from slabbe into "
                    "SageMath the argument include_header=False was "
                    "replaced by content_only=True. Please update your code "
                    "before include_header option gets removed from SageMath.")

        if content_only:
            output = self.content()
        else:
            output = str(self)

        with open(filename, 'w') as f:
            f.write(output)

        return filename


class TikzPicture(Standalone):
    r"""
    Creates a TikzPicture embedded in a LaTeX standalone document class.

    INPUT:

    - ``code`` -- string, tikzpicture code starting with ``r'\begin{tikzpicture}'``
      and ending with ``r'\end{tikzpicture}'``
    - ``standalone_config`` -- list of strings (default: ``[]``),
      latex document class standalone configuration options.
    - ``usepackage`` -- list of strings (default: ``['amsmath']``), latex
      packages.
    - ``usetikzlibrary`` -- list of strings (default: ``[]``), tikz libraries
      to use.
    - ``macros`` -- list of strings (default: ``[]``), stuff you need for the picture.
    - ``use_sage_preamble`` -- bool (default: ``False``), whether to include sage
      latex preamble and sage latex macros, that is, the content of
      :func:`sage.misc.latex.extra_preamble()`,
      :func:`sage.misc.latex.extra_macros()` and
      :func:`sage.misc.latex_macros.sage_latex_macros()`.

    EXAMPLES::

        sage: from slabbe import TikzPicture
        sage: g = graphs.PetersenGraph()
        sage: s = latex(g)
        sage: t = TikzPicture(s, standalone_config=["border=4mm"], usepackage=['tkz-graph'])
        sage: _ = t.pdf(view=False)   # long time (2s)

    Here are standalone configurations, packages, tikz libraries and macros you
    may want to set::

        sage: options = ['preview', 'border=4mm', 'beamer', 'float']
        sage: usepackage = ['nicefrac', 'amsmath', 'pifont', 'tikz-3dplot',
        ....:    'tkz-graph', 'tkz-berge', 'pgfplots']
        sage: tikzlib = ['arrows', 'snakes', 'backgrounds', 'patterns',
        ....:      'matrix', 'shapes', 'fit', 'calc', 'shadows', 'plotmarks',
        ....:      'positioning', 'pgfplots.groupplots', 'mindmap']
        sage: macros = [r'\newcommand{\ZZ}{\mathbb{Z}}']
        sage: s = "\\begin{tikzpicture}\n\\draw (0,0) -- (1,1);\n\\end{tikzpicture}"
        sage: t = TikzPicture(s, standalone_config=options, usepackage=usepackage, 
        ....:        usetikzlibrary=tikzlib, macros=macros)
        sage: _ = t.pdf(view=False)   # long time (2s)
    """
    @classmethod
    def from_dot_string(cls, dotdata, prog='dot'):
        r"""
        Convert a graph to a tikzpicture using graphviz and dot2tex.

        .. NOTE::

            Prerequisite: dot2tex optional Sage package and graphviz must be
            installed.

        INPUT:

        - ``dotdata`` -- dot format string
        - ``prog`` -- string (default: ``'dot'``) the program used for the
          layout corresponding to one of the software of the graphviz
          suite: 'dot', 'neato', 'twopi', 'circo' or 'fdp'.

        EXAMPLES::

            sage: from slabbe import TikzPicture
            sage: G = graphs.PetersenGraph()
            sage: dotdata = G.graphviz_string()
            sage: tikz = TikzPicture.from_dot_string(dotdata) # optional dot2tex # long time (3s)
            sage: _ = tikz.pdf()      # not tested
            sage: dotdata = G.graphviz_string(labels='latex')
            sage: tikz = TikzPicture.from_dot_string(dotdata) # optional dot2tex # long time (3s)
            sage: _ = tikz.pdf()      # not tested

        ::

            sage: W = CoxeterGroup(["A",2])
            sage: G = W.cayley_graph()
            sage: dotdata = G.graphviz_string()
            sage: tikz = TikzPicture.from_dot_string(dotdata) # optional dot2tex # long time (3s)
            sage: _ = tikz.pdf()      # not tested
            sage: dotdata = G.graphviz_string(labels='latex')
            sage: tikz = TikzPicture.from_dot_string(dotdata) # optional dot2tex # long time (3s)
            sage: _ = tikz.pdf()      # not tested

        """
        import dot2tex
        tikz = dot2tex.dot2tex(dotdata,
                               format='tikz',
                               autosize=True,
                               crop=True,
                               figonly='True',
                               prog=prog).strip()
        return TikzPicture(tikz, standalone_config=["border=4mm"],
                           usetikzlibrary=['shapes'])

    @classmethod
    #@experimental(trac_number=20343)
    def from_graph(cls, graph, merge_multiedges=True,
            merge_label_function=tuple, **kwds):
        r"""
        Convert a graph to a tikzpicture using graphviz and dot2tex.

        .. NOTE::

            Prerequisite: dot2tex optional Sage package and graphviz must be
            installed.

        INPUT:

        - ``graph`` -- graph
        - ``merge_multiedges`` -- bool (default: ``True``), if the graph
          has multiple edges, whether to merge the multiedges into one
          single edge
        - ``merge_label_function`` -- function (default:``tuple``), a
          function to apply to each list of labels to be merged. It is
          ignored if ``merge_multiedges`` is not ``True`` or if the graph
          has no multiple edges.

        Other inputs are used for latex drawing with dot2tex and graphviz:

        - ``prog`` -- string (default: ``'dot'``) the program used for the
          layout corresponding to one of the software of the graphviz
          suite: 'dot', 'neato', 'twopi', 'circo' or 'fdp'.
        - ``edge_labels`` -- bool (default: ``True``)
        - ``color_by_label`` -- bool (default: ``False``)
        - ``rankdir`` -- string (default: ``'down'``)
        - ``subgraph_clusters`` -- (default: []) a list of lists of
          vertices, if supported by the layout engine, nodes belonging to
          the same cluster subgraph are drawn together, with the entire
          drawing of the cluster contained within a bounding rectangle.

        EXAMPLES::

            sage: from slabbe import TikzPicture
            sage: g = graphs.PetersenGraph()
            sage: tikz = TikzPicture.from_graph(g) # optional dot2tex
            sage: _ = tikz.pdf()      # not tested

        Using ``prog``::

            sage: tikz = TikzPicture.from_graph(g, prog='neato', color_by_label=True) # optional dot2tex # long time (3s)
            sage: _ = tikz.pdf()      # not tested

        Using ``rankdir``::

            sage: tikz = TikzPicture.from_graph(g, rankdir='right') # optional dot2tex # long time (3s)
            sage: _ = tikz.pdf()      # not tested

        Using ``merge_multiedges``::

            sage: alpha = var('alpha')
            sage: m = matrix(2,range(4)); m.set_immutable()
            sage: G = DiGraph([(0,1,alpha), (0,1,0), (0,2,9), (0,2,m)], multiedges=True)
            sage: tikz = TikzPicture.from_graph(G, merge_multiedges=True) # optional dot2tex
            sage: _ = tikz.pdf()      # not tested

        Using ``merge_multiedges`` with ``merge_label_function``::

            sage: fn = lambda L: LatexExpr(','.join(map(str, L)))
            sage: G = DiGraph([(0,1,'a'), (0,1,'b'), (0,2,'c'), (0,2,'d')], multiedges=True)
            sage: tikz = TikzPicture.from_graph(G, merge_multiedges=True,   # optional dot2tex
            ....:               merge_label_function=fn)            
            sage: _ = tikz.pdf()      # not tested

        Using subgraphs clusters (broken when using labels, see
        :trac:`22070`)::

            sage: S = FiniteSetMaps(5)
            sage: I = S((0,1,2,3,4))
            sage: a = S((0,1,3,0,0))
            sage: b = S((0,2,4,1,0))
            sage: roots = [I]
            sage: succ = lambda v:[v*a,v*b,a*v,b*v]
            sage: R = RecursivelyEnumeratedSet(roots, succ)
            sage: G = R.to_digraph()
            sage: G
            Looped multi-digraph on 27 vertices
            sage: C = G.strongly_connected_components()
            sage: tikz = TikzPicture.from_graph(G, merge_multiedges=False,   # optional dot2tex
            ....:                               subgraph_clusters=C)
            sage: _ = tikz.pdf()      # not tested

        An example coming from ``graphviz_string`` documentation in SageMath::

            sage: f(x) = -1 / x
            sage: g(x) = 1 / (x + 1)
            sage: G = DiGraph()
            sage: G.add_edges((i, f(i), f) for i in (1, 2, 1/2, 1/4))
            sage: G.add_edges((i, g(i), g) for i in (1, 2, 1/2, 1/4))
            sage: t = TikzPicture.from_graph(G)                           # optional -- dot2tex
            sage: _ = tikz.pdf()      # not tested
            sage: def edge_options(data):
            ....:     u, v, label = data
            ....:     options = {"color": {f: "red", g: "blue"}[label]}
            ....:     if (u,v) == (1/2, -2): options["label"]       = "coucou"; options["label_style"] = "string"
            ....:     if (u,v) == (1/2,2/3): options["dot"]         = "x=1,y=2"
            ....:     if (u,v) == (1,   -1): options["label_style"] = "latex"
            ....:     if (u,v) == (1,  1/2): options["edge_string"] = "->"
            ....:     if (u,v) == (1/2,  1): options["backward"]    = True
            ....:     return options
            sage: t = TikzPicture.from_graph(G, edge_options=edge_options)  # optional -- dot2tex
            sage: _ = tikz.pdf()      # not tested

        .. TODO:: improve the previous example

        """
        try:
            from sage.features.latex import pdflatex
        except ImportError:
            # This is deprecated in sagemath >=9.5
            from sage.misc.latex import have_pdflatex
            assert have_pdflatex(), "pdflatex does not seem to be installed"
        else:
            # This is how to do it in sagemath >=9.5
            pdflatex().require()

        from sage.features.graphviz import Graphviz
        Graphviz().require()

        # TODO: test the presence of dot2tex

        if merge_multiedges and graph.has_multiple_edges():
            from slabbe.graph import merge_multiedges
            graph = merge_multiedges(graph,
                    label_function=merge_label_function)

        default = dict(format='dot2tex', edge_labels=True,
                       color_by_label=False, prog='dot', rankdir='down')
        default.update(kwds)

        graph.latex_options().set_options(**default)
        tikz = graph._latex_()
        usepackage = ['amsmath']
        return TikzPicture(tikz, standalone_config=["border=4mm"],
                usepackage=usepackage)

    @classmethod
    #@experimental(trac_number=20343)
    def from_graph_with_pos(cls, graph, scale=1, merge_multiedges=True,
            merge_label_function=tuple):
        r"""
        Convert a graph with positions defined for vertices to a tikzpicture.

        INPUT:

        - ``graph`` -- graph (with predefined positions)
        - ``scale`` -- number (default:``1``), tikzpicture scale
        - ``merge_multiedges`` -- bool (default: ``True``), if the graph
          has multiple edges, whether to merge the multiedges into one
          single edge
        - ``merge_label_function`` -- function (default:``tuple``), a
          function to apply to each list of labels to be merged. It is
          ignored if ``merge_multiedges`` is not ``True`` or if the graph
          has no multiple edges.

        EXAMPLES::

            sage: from slabbe import TikzPicture
            sage: g = graphs.PetersenGraph()
            sage: tikz = TikzPicture.from_graph_with_pos(g)
            doctest:...: FutureWarning: This class/method/function is marked as experimental.
            It, its functionality or its interface might change without a formal deprecation.
            See http...20343 for details.

        ::

            sage: edges = [(0,0,'a'),(0,1,'b'),(0,1,'c')]
            sage: kwds = dict(format='list_of_edges', loops=True, multiedges=True)
            sage: G = DiGraph(edges, **kwds)
            sage: G.set_pos({0:(0,0), 1:(1,0)})
            sage: f = lambda label:','.join(label)
            sage: TikzPicture.from_graph_with_pos(G, merge_label_function=f)
            \documentclass[tikz]{standalone}
            \standaloneconfig{border=4mm}
            \begin{document}
            \begin{tikzpicture}
            [auto,scale=1]
            % vertices
            \node (node_0) at (0, 0) {0};
            \node (node_1) at (1, 0) {1};
            % edges
            \draw[->] (node_0) -- node {b,c} (node_1);
            % loops
            \draw (node_0) edge [loop above] node {a} ();
            \end{tikzpicture}
            \end{document}

        TESTS::

            sage: edges = [(0,0,'a'),(0,1,'b'),(0,1,'c')]
            sage: kwds = dict(format='list_of_edges', loops=True, multiedges=True)
            sage: G = DiGraph(edges, **kwds)
            sage: TikzPicture.from_graph_with_pos(G)
            Traceback (most recent call last):
            ...
            ValueError: vertex positions need to be set first
        """
        pos = graph.get_pos()
        if pos is None:
            raise ValueError('vertex positions need to be set first')

        if merge_multiedges and graph.has_multiple_edges():
            from slabbe.graph import merge_multiedges
            graph = merge_multiedges(graph,
                    label_function=merge_label_function)

        keys_for_vertices = graph._keys_for_vertices()

        lines = []
        lines.append(r'\begin{tikzpicture}')
        lines.append(r'[auto,scale={}]'.format(scale))

        # vertices
        lines.append(r'% vertices')
        for u in graph.vertices():
            line = r'\node ({}) at {} {{{}}};'.format(keys_for_vertices(u),
                                                      pos[u], u)
            lines.append(line)

        # edges
        lines.append(r'% edges')
        arrow = '->' if graph.is_directed() else ''
        for (u,v,label) in graph.edges():
            if u == v:
                # loops are done below
                continue
            if label:
                line = r'\draw[{}] ({}) -- node {{{}}} ({});'.format(arrow,
                                                    keys_for_vertices(u),
                                                    label,
                                                    keys_for_vertices(v))
            else:
                line = r'\draw[{}] ({}) -- ({});'.format(arrow,
                                                    keys_for_vertices(u),
                                                    keys_for_vertices(v))
            lines.append(line)

        # loops
        lines.append(r'% loops')
        for (u,v,label) in graph.loop_edges():
            line = r'\draw ({}) edge [loop above] node {{{}}} ();'.format(
                                              keys_for_vertices(u), label)
            lines.append(line)

        lines.append(r'\end{tikzpicture}')
        tikz = '\n'.join(lines)
        return TikzPicture(tikz, standalone_config=["border=4mm"])

    @classmethod
    def from_poset(cls, poset, **kwds):
        r"""
        Convert a poset to a tikzpicture using graphviz and dot2tex.

        .. NOTE::

            Prerequisite: dot2tex optional Sage package and graphviz must be
            installed.

        INPUT:

        - ``poset`` -- poset
        - ``prog`` -- string (default: ``'dot'``) the program used for the
          layout corresponding to one of the software of the graphviz
          suite: 'dot', 'neato', 'twopi', 'circo' or 'fdp'.
        - ``edge_labels`` -- bool (default: ``True``)
        - ``color_by_label`` -- bool (default: ``False``)
        - ``rankdir`` -- string (default: ``'down'``)

        EXAMPLES::

            sage: from slabbe import TikzPicture
            sage: P = posets.PentagonPoset()
            sage: tikz = TikzPicture.from_poset(P) # optional dot2tex # long time (3s)
            doctest:...: FutureWarning: This class/method/function is marked as experimental.
            It, its functionality or its interface might change without a formal deprecation.
            See http...20343 for details.
            sage: tikz = TikzPicture.from_poset(P, prog='neato', color_by_label=True) # optional dot2tex # long time (3s)

        ::

            sage: P = posets.SymmetricGroupWeakOrderPoset(4)
            sage: tikz = TikzPicture.from_poset(P) # optional dot2tex # long time (4s)
            sage: tikz = TikzPicture.from_poset(P, prog='neato') # optional dot2tex # long time (4s)
        """
        graph = poset.hasse_diagram()
        return cls.from_graph(graph, **kwds)

    def tikz_picture_code(self):
        r"""
        EXAMPLES::

            sage: from slabbe import TikzPicture
            sage: s = "\\begin{tikzpicture}\n\\draw (0,0) -- (1,1);\n\\end{tikzpicture}"
            sage: t = TikzPicture(s)
            sage: print(t.tikz_picture_code())
            \begin{tikzpicture}
            \draw (0,0) -- (1,1);
            \end{tikzpicture}
        """
        return self.content()

