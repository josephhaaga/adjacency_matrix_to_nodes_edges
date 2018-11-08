# Adjacency Matrix to Nodes/Edges

Convert an adjacency matrix [from `graph_generator`](https://github.com/josephhaaga/graph_generator) into node and edge csv files for easy ingest into DataFrames/GraphFrames.

GeneratePeopleAndCompanies.ipynb is a standalone notebook for generating node and edge csv files. No adjacency matrix input is required.

## Requirements
`pip install numpy` 

`pip install faker`

## To Run

`python generate_files.py PATH_TO_ADJACENCY_MATRIX.csv`
