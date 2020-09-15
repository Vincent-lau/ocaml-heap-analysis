all:
	python3 graph.py
	python3 dot-graph.py
	dot -Tpdf -o forward_block.pdf forward_block.gv
