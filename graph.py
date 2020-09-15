import csv

indegree = {}
with open('heapdump.csv', newline='') as csvfile:
    ptr_reader = csv.reader(csvfile, delimiter=',')
    for row in ptr_reader:
        indegree[row[0]] = 1

with open('heapdump.csv', newline='') as csvfile:
    ptr_reader = csv.reader(csvfile, delimiter=',')
    for row in ptr_reader:
        for i in range(len(row)):
            col = row[i]
            if i != 1 and i != 0 and col in indegree:
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

# write 
with open('heapdump.csv', newline='') as inp:
    ptr_reader = csv.reader(inp)
    with open('forward_block.csv', 'w', newline='') as out:
        ptr_writer = csv.writer(out)
        for row in ptr_reader:
            if row[1] == '250' or row[1] == '252':
                ptr_writer.writerow(row)
