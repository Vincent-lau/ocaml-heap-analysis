import csv

lval = {}
file_of_block = 'forward_block.csv'
file_of_graph = 'forward_block.gv'

with open(file_of_block, newline='') as inp:
    reader = csv.reader(inp)
    for row in reader:
        lval[row[0]] = 1

with open(file_of_block, newline='') as inp:
    reader = csv.reader(inp)
    with open(file_of_graph, 'w', newline='') as out:
        out.write("digraph G{\nnode[shape = record];\n")
        for row in reader:
            out.write('i{a1}[label = "<f0> i{a1} | <tag> {tag} | '.format(
                a1=row[0], tag=row[1]))
            for i in range(2, len(row)):
                col = row[i]
                if i == len(row) - 1:
                    out.write('<i{a}>"];'.format(a=row[i]))
                else:
                    out.write('<i{a}> | '.format(a=row[i]))
            out.write("\n")
            for i in range(2, len(row)):
                if row[i] in lval: 
                    # only addresses that appear on the lhs can be linked
                    out.write('"i{ptr}":i{child} -> "i{child}":f0\n'.format(
                        ptr=row[0], child=row[i]))
        out.write("}\n")
