import os
import pandas as pd

START_NODE_COL = "START_NODE"
RELATIONSHIP_COL = "RELATIONSHIP"
END_NODE_COL = "END_NODE"


def fetch_nodes_and_relationships(session, csv_filename='nodes_and_relationships.csv'):
    query = """
    MATCH (start)-[r]->(end)
    RETURN ID(start) as START_NODE, type(r) as RELATIONSHIP, ID(end) as END_NODE
    """
    results = session.run(query)

    data = [
        record
        for record in results
    ]

    # Create a folder to store individual label CSV files
    output_folder = 'output_folder'
    os.makedirs(output_folder, exist_ok=True)

    init_folder = f'{output_folder}/init_folder'
    os.makedirs(init_folder, exist_ok=True)

    # Save to CSV
    nar = pd.DataFrame(data, columns=[START_NODE_COL, RELATIONSHIP_COL, END_NODE_COL])
    nar.to_csv(f'{init_folder}/{csv_filename}', index=False)
    print(f"CSV file '{csv_filename}' created successfully")
    print()

    return data
