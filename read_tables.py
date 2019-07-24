#import tabula


#tables = tabula.read_pdf("iso_documents/ISO1101.PDF", multiple_tables=True)
#for table in tables:
#    print(table)

#pdftotext - layout!!!!

#tabula.convert_into("iso_documents/ISO1101.PDF", "output.csv", output_format="csv", pages='all', multiple_tables=True)
#df = tabula.read_pdf("iso_documents/ISO1101.PDF", pages='all', multiple_tables=True)
#print(df)

"""def file_read(fname):
    content_array = []
    with open(fname) as f:
        # Content_list is the list that contains the read lines.
        for line in f:
            content_array.append(line.strip().replace(" ",""))
        print(content_array)"""


#file_read('drawings/5129275_Rev01-GV12.txt')

class UnionFind:
    def __init__(self):
        self.rank = {}
        self.parent = {}

    def find(self, element):
        if element not in self.parent: # leader elements are not in `parent` dict
            return element
        leader = self.find(self.parent[element]) # search recursively
        self.parent[element] = leader # compress path by saving leader as parent
        return leader

    def union(self, leader1, leader2):
        rank1 = self.rank.get(leader1,1)
        rank2 = self.rank.get(leader2,1)

        if rank1 > rank2: # union by rank
            self.parent[leader2] = leader1
        elif rank2 > rank1:
            self.parent[leader1] = leader2
        else: # ranks are equal
            self.parent[leader2] = leader1 # favor leader1 arbitrarily
            self.rank[leader1] = rank1+1 # increment rank

nodes = set()
groups = UnionFind()

with open('/home/bscheibel/PycharmProjects/dxf_reader/drawings/5129275_Rev01-GV12.txt') as f:
    for y, line in enumerate(f): # iterate over lines
        for x, char in enumerate(line): # and characters within a line
            if char != ' ':
                nodes.add((x, y)) # maintain a set of node coordinates

                # check for neighbors that have already been read
                neighbors = [(x-1, y-1), # up-left
                             (x, y-1),   # up
                             (x+1, y-1), # up-right
                             (x-1, y)]   # left
                for neighbor in neighbors:
                    if neighbor in nodes:
                        my_group = groups.find((x, y))
                        neighbor_group = groups.find(neighbor)
                        if my_group != neighbor_group:
                            groups.union(my_group, neighbor_group)

# finally, count the number of unique groups
number_of_groups = len(set(groups.find(n) for n in nodes))