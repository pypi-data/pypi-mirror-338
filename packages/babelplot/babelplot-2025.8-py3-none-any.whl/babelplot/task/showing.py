"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2022
SEE COPYRIGHT NOTICE BELOW
"""

import gzip
import os as osys
import sys as s
import tempfile as tmpf

from babelplot.constant.project import NAME
from babelplot.runtime.figure import SHOWN_FIGURES, UN_SHOWN_FIGURES
from PyQt6.QtCore import QUrl as url_t
from PyQt6.QtWebEngineWidgets import QWebEngineView as widget_t
from PyQt6.QtWidgets import QApplication as application_t


def ShowHTMLWithPyQt(html: str | bytes, uid: int, /) -> None:
    """"""
    if isinstance(html, bytes):
        html = gzip.decompress(html).decode()

    # The application must be instantiated in the same thread/process as the one running
    # exec().
    if (application := application_t.instance()) is None:
        application = application_t(s.argv)
    application.setApplicationName(f"{NAME}-{uid}")

    widget = widget_t()
    SetURLIfNeeded = lambda _: _SetURLIfNeeded(_, html, widget, application)
    widget.loadFinished.connect(SetURLIfNeeded)
    widget.setHtml(html)  # Now attempt to set HTML; If failure, then SetURLIfNeeded.

    widget.show()
    application.exec()


def ShowAllFigures(
    *,
    modal: bool = True,
) -> None:
    """"""
    n_figures = UN_SHOWN_FIGURES.__len__()
    while n_figures > 0:
        UN_SHOWN_FIGURES[0].Show(modal=modal and (n_figures == 1))
        n_figures -= 1

    assert UN_SHOWN_FIGURES.__len__() == 0

    if modal:
        WaitForAllFiguresToBeClosed()


def WaitForAllFiguresToBeClosed() -> None:
    """"""
    if SHOWN_FIGURES.__len__() == 0:
        return

    with_processes = tuple(_ for _ in SHOWN_FIGURES if _.showing_process is not None)
    for figure in with_processes:
        figure.showing_process.join()
        figure.AcknowledgeClosure()


def _SetURLIfNeeded(
    success: bool, html: str, widget: widget_t, application: application_t, /
) -> None:
    """
    From: https://doc.qt.io/qtforpython-6/PySide6/QtWebEngineWidgets/QWebEngineView.html
          #PySide6.QtWebEngineWidgets.PySide6.QtWebEngineWidgets.QWebEngineView.setHtml
        Content larger than 2 MB cannot be displayed...
        ...
        Thereby, the provided code becomes a URL that exceeds the 2 MB limit set by
        Chromium. If the content is too large, the loadFinished() signal is triggered
        with success=False.
    Solution: Use a temporary file (with html extension) and setUrl.
    """
    if success:
        return

    transfer = tmpf.NamedTemporaryFile(mode="w", suffix=".html", delete=False)
    with open(transfer.name, "w") as accessor:
        accessor.write(html)
    url = url_t.fromLocalFile(transfer.name)

    widget.setUrl(url)

    DeleteTemporaryFile = lambda: osys.remove(transfer.name)
    application.lastWindowClosed.connect(DeleteTemporaryFile)


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
