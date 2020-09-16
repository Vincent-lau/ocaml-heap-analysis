import csv

indegree = {}
with open('heapdump.csv', newline='') as csvfile:
    ptr_reader = csv.reader(csvfile, delimiter=',')
    for row in ptr_reader:
        indegree[row[0]] = 0

with open('heapdump.csv', newline='') as csvfile:
    ptr_reader = csv.reader(csvfile, delimiter=',')
    for row in ptr_reader:
        for i in range(2, len(row)):
            col = row[i]
            if col in indegree:
                indegree[col] += 1

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
        if row[1] == '250' and len(row) == 6:
            rope_children.add(row[4])
            rope_children.add(row[5])

with open('heapdump.csv', newline='') as inp:
    ptr_reader = csv.reader(inp)
    with open('forward_block.csv', 'w', newline='') as out:
        ptr_writer = csv.writer(out)
        for row in ptr_reader:
            if row[1] == '250' and len(row) == 6 or \
            row[1] == '252' and row[0] in rope_children:
                ptr_writer.writerow(row)
