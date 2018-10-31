import sys;
import numpy as np;
from faker import Faker;

# python generate_files.py ADJACENCY_MATRIX_FILE

source_file = sys.argv[1]
source_file_name = source_file[:-4]

print("Processing "+source_file)

matrix = np.loadtxt(source_file, dtype=int, delimiter=',');

# Save relationships/edges to a file
relationship_pairs = np.argwhere(matrix == 1).astype('object')
relationship_pairs = np.insert(relationship_pairs, 2, "claims_dependent", axis=1)
relationship_pairs = np.insert(relationship_pairs, 0, np.array(["src", "dst", "relationship"]), axis=0)
edge_file = source_file_name+"-edges.csv"
np.savetxt(edge_file, relationship_pairs, delimiter=",", fmt="%s");
print("Edges saved to "+edge_file)

# Create vertices
vertices = np.arange(matrix.shape[0])
vertices = np.reshape(vertices, (-1, 1))

# Create some fake vertex attributes
fake = Faker()
names = [fake.name() for f in range(0, len(matrix))]
itins = [fake.itin() for f in range(0, len(matrix))]
eins = [fake.ein() for f in range(0, len(matrix))]
street_address = [fake.street_address() for f in range(0, len(matrix))]
city = [fake.city() for f in range(0, len(matrix))]
state = [fake.state() for f in range(0, len(matrix))]

vertices = np.insert(vertices.astype('object'), 1, names, axis=1)
vertices = np.insert(vertices, 1, itins, axis=1)
vertices = np.insert(vertices, 1, eins, axis=1)
vertices = np.insert(vertices, 1, street_address, axis=1)
vertices = np.insert(vertices, 1, city, axis=1)
vertices = np.insert(vertices, 1, state, axis=1)
vertices = np.insert(vertices, 0, np.array(["id", "name", "itin", "ein", "street_address", "city", "state"]), axis=0)
vertex_file = source_file_name+"-nodes.csv"
np.savetxt(vertex_file, vertices, delimiter=",", fmt="%s");
print("Nodes saved to "+vertex_file)
print("Processing complete. Two .csv files created in same directory as source file")
