INP_GRAPH=forward_block.gv
OUT_GRAPH=forward_block.pdf

all:
	make linear csvs graph

linear: test_linear.ml
	make clean
	../ocaml/install/bin/ocamlc -o test_linear test_linear.ml
	OCAMLHEAPDUMP="heapdump.csv" ../ocaml/install/bin/ocamlrun ./test_linear

csvs: heapdump.csv
	python3 graph.py
	python3 dot-graph.py

graph: ${INP_GRAPH}
	dot -Tpdf -o ${OUT_GRAPH} ${INP_GRAPH}

clean:
	rm -f *.csv *.gv *.pdf test_linear.cm* test_linear
