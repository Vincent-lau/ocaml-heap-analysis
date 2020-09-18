import csv

indegree = {}
with open('heapdump.csv', newline='') as inp:
    ptr_reader = csv.reader(inp)
    for row in ptr_reader:
        col = row[0]
        if col in indegree:
            indegree[col] += 1
        else:
            indegree[col] = 1


# write the pointers that are not linear and their ref_count
with open('ref_count.csv','w', newline='') as inp:
    ptr_writer = csv.writer(inp)
    for ptr in indegree:
        if indegree[ptr] > 1:
            ptr_writer.writerow([ptr, indegree[ptr]])

# write blocks that are not linear
with open('heapdump.csv', newline='') as inp:
    ptr_reader = csv.reader(inp)
    with open('nonlinear_block.csv', 'w', newline='') as out:
        ptr_writer = csv.writer(out)
        for row in ptr_reader:
            col = row[0]
            if indegree[col] > 1:
                ptr_writer.writerow(row)

# write blocks related to ropes
rope_children = set()
with open('heapdump.csv', newline='') as inp:
    ptr_reader = csv.reader(inp)
    for row in ptr_reader:
        if row[1] == '250' and len(row) == 7:
            rope_children.add(row[4])
            rope_children.add(row[5])

with open('heapdump.csv', newline='') as inp:
    ptr_reader = csv.reader(inp)
    with open('forward_block.csv', 'w', newline='') as out:
        ptr_writer = csv.writer(out)
        for row in ptr_reader:
            if row[1] == '250' and len(row) == 7 or \
            row[1] == '252' and row[0] in rope_children or \
            len(row) == 9 and row[3] in rope_children:
                ptr_writer.writerow(row)
