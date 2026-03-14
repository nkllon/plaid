from pathlib import Path

from pyshacl import validate
from rdflib import Graph


ROOT = Path("/Volumes/lemon/codex/plaid")
DATA = ROOT / "model" / "security_package.ttl"
ONTOLOGY = ROOT / "model" / "security_ontology.ttl"
SHAPES = ROOT / "model" / "security_shapes.ttl"


def main() -> None:
    data_graph = Graph()
    data_graph.parse(ONTOLOGY)
    data_graph.parse(DATA)

    shapes_graph = Graph()
    shapes_graph.parse(SHAPES)

    conforms, _, report = validate(
        data_graph,
        shacl_graph=shapes_graph,
        inference="rdfs",
        abort_on_first=False,
        allow_infos=False,
        allow_warnings=False,
    )
    print(report)
    raise SystemExit(0 if conforms else 1)


if __name__ == "__main__":
    main()
