"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2022
SEE COPYRIGHT NOTICE BELOW
"""

import dataclasses as d
import typing as h

from babelplot.task.showing import ShowHTMLWithPyQt
from babelplot.type.dimension import dim_e
from babelplot.type.figure import figure_t as base_figure_t
from babelplot.type.frame import frame_t as base_frame_t
from babelplot.type.plot import plot_t as base_plot_t
from babelplot.type.plot_type import plot_e, plot_function_h
from bokeh.embed import file_html as HTMLofBackendContent  # noqa
from bokeh.layouts import column as NewBackendColLayout  # noqa
from bokeh.layouts import grid as NewBackendGridLayout  # noqa
from bokeh.layouts import row as NewBackendRowLayout  # noqa
from bokeh.models.renderers import GlyphRenderer as backend_plot_t  # noqa
from bokeh.plotting import figure as backend_figure_t  # noqa
from bokeh.resources import INLINE  # noqa

# from bokeh.layouts import LayoutDOM as backend_content_t  # noqa

NAME = "bokeh"


backend_frame_t = backend_figure_t


@d.dataclass(slots=True, repr=False, eq=False)
class plot_t(base_plot_t): ...


@d.dataclass(slots=True, repr=False, eq=False)
class frame_t(base_frame_t):

    def _NewPlot(
        self,
        plot_function: plot_function_h,
        *args,
        title: str | None = None,  # If _, then it is swallowed by kwargs!
        **kwargs,
    ) -> plot_t:
        """"""
        output = plot_t(
            title=title,
            property=kwargs.copy(),
            backend_name=self.backend_name,
        )

        output.raw = plot_function(self.raw, *args, **kwargs)

        return output


@d.dataclass(slots=True, repr=False, eq=False)
class figure_t(base_figure_t):
    layout: h.Any = None

    _BackendShow = ShowHTMLWithPyQt

    def _NewBackendFigure(self, *args, **kwargs) -> backend_figure_t:
        """"""
        return backend_figure_t(*args, **kwargs)

    def _NewFrame(
        self,
        row: int,
        col: int,
        *args,
        title: str | None = None,
        dim: dim_e = dim_e.XY,
        **kwargs,
    ) -> frame_t:
        """"""
        output = frame_t(
            title=title,
            dim=dim,
            backend_name=self.backend_name,
        )

        output.raw = backend_frame_t(*args, title=title, **kwargs)

        return output

    def AdjustLayout(self) -> None:
        """"""
        n_rows, n_cols = self.shape
        arranged_frames = [n_cols * [None] for _ in range(n_rows)]
        for frame, (row, col) in zip(self.frames, self.locations):
            arranged_frames[row][col] = frame.raw
        arranged_frames: list[list[backend_frame_t]]

        if n_rows > 1:
            if n_cols > 1:
                layout = NewBackendGridLayout(arranged_frames)
            else:
                column = [_row[0] for _row in arranged_frames]
                layout = NewBackendColLayout(column)
        else:
            layout = NewBackendRowLayout(arranged_frames[0])

        self.layout = layout

    def AsHTML(self) -> str:
        """"""
        return HTMLofBackendContent(self.layout, INLINE)


PLOTS = plot_e.NewPlotsTemplate()
PLOTS[plot_e.SCATTER][1] = backend_frame_t.scatter


TRANSLATIONS = {
    "color_face": "fill_color",
}


"""
COPYRIGHT NOTICE

This software is governed by the CeCILL  license under French law and
abiding by the rules of distribution of free software.  You can  use,
modify and/ or redistribute the software under the terms of the CeCILL
license as circulated by CEA, CNRS and INRIA at the following URL
"http://www.cecill.info".

As a counterpart to the access to the source code and  rights to copy,
modify and redistribute granted by the license, users are provided only
with a limited warranty  and the software's author,  the holder of the
economic rights,  and the successive licensors  have only  limited
liability.

In this respect, the user's attention is drawn to the risks associated
with loading,  using,  modifying and/or developing or reproducing the
software by the user in light of its specific status of free software,
that may mean  that it is complicated to manipulate,  and  that  also
therefore means  that it is reserved for developers  and  experienced
professionals having in-depth computer knowledge. Users are therefore
encouraged to load and test the software's suitability as regards their
requirements in conditions enabling the security of their systems and/or
data to be ensured and,  more generally, to use and operate it in the
same conditions as regards security.

The fact that you are presently reading this means that you have had
knowledge of the CeCILL license and that you accept its terms.

SEE LICENCE NOTICE: file README-LICENCE-utf8.txt at project source root.

This software is being developed by Eric Debreuve, a CNRS employee and
member of team Morpheme.
Team Morpheme is a joint team between Inria, CNRS, and UniCA.
It is hosted by the Centre Inria d'Université Côte d'Azur, Laboratory
I3S, and Laboratory iBV.

CNRS: https://www.cnrs.fr/index.php/en
Inria: https://www.inria.fr/en/
UniCA: https://univ-cotedazur.eu/
Centre Inria d'Université Côte d'Azur: https://www.inria.fr/en/centre/sophia/
I3S: https://www.i3s.unice.fr/en/
iBV: http://ibv.unice.fr/
Team Morpheme: https://team.inria.fr/morpheme/
"""
