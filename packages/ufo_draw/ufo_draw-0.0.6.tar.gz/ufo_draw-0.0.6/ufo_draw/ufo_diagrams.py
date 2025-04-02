from typing import List

from feynml.interface import qgraf as iqgraf
from feynmodel.interface.qgraf import (
    feynmodel_to_qgraf,
    list_particle_names,
    qgraf_to_feynmodel,
)
from feynmodel.interface.ufo import load_ufo_model
from pyfeyn2.feynmandiagram import FeynML
from pyqgraf import qgraf
from xsdata.formats.dataclass.parsers import XmlParser


def list_particles(path) -> List[str]:
    fm = load_ufo_model(path)
    return list_particle_names(fm)


# TODO use own topology generator
def generate_diagrams_qgraf(
    path: str,
    inparticles: List[str],
    outparticles: List[str],
    loops: int = 0,
    inmomenta: List[str] = None,
    outmomenta: List[str] = None,
    loop_momentum: str = "l",
    filter=None,
) -> FeynML:
    """Generate FeynML diagrams from a UFO model."""
    if inmomenta is None:
        inmomenta = [f"p{i}" for i, p in enumerate(inparticles)]
    if outmomenta is None:
        outmomenta = [f"p{i+len(inparticles)}" for i, p in enumerate(outparticles)]
    # sanity check
    assert len(inmomenta) == len(inparticles)
    assert len(outmomenta) == len(outparticles)
    # Dress particles with momentum
    # TODO handle different names for particles
    inp = [f"{a}[{b}]" for a, b in zip(inparticles, inmomenta)]
    outp = [f"{a}[{b}]" for a, b in zip(outparticles, outmomenta)]
    # Load the UFO
    fm = load_ufo_model(path)
    # convert to feynmodel
    qgrafmodel = feynmodel_to_qgraf(fm, True, False)
    # print(qgrafmodel)
    if filter is not None:
        nq = ""
        # loop lines in the model
        for l in qgrafmodel.splitlines():
            hit = False
            for f in filter:
                # if the line is in the filter
                if f in l:
                    # add it to the new model
                    hit = True
            if not hit:
                nq += l + "\n"
        # overwrite the model
        qgrafmodel = nq
    # print(qgrafmodel)

    # Run pyQGRAF
    xml_string = qgraf.run(
        ",".join(inp),
        ",".join(outp),
        loops=loops,
        loop_momentum=loop_momentum,
        model=qgrafmodel,
        style=iqgraf.get_style(),
    )

    # Load FeynML
    parser = XmlParser()
    fml = parser.from_string(xml_string, FeynML)
    # Return list of diagrams
    return fml
