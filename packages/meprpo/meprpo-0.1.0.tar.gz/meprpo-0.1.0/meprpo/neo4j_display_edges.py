import pandas as pd
from collections import defaultdict
import os


def display_node_info_edges_counts(session):
    query = """
    MATCH (n)
    OPTIONAL MATCH (n)-[r]->(m)
    RETURN n, labels(n) as labels, properties(n) as node_properties, 
           type(r) as relationship_type
    ORDER BY n, relationship_type
    """
    result = session.run(query)
    data = []
    current_node = None
    relationship_counts = defaultdict(int)
    numeric_attributes = defaultdict(list)

    for record in result:
        node = record["n"]
        labels = record["labels"]
        node_properties = record["node_properties"]
        relationship_type = record["relationship_type"]

        if current_node is None or node.id != current_node["Node ID"]:
            if current_node is not None:
                current_node.update(relationship_counts)
                current_node.update(numeric_attributes)  # Add numeric attribute lists
                data.append(current_node)
            current_node = {
                "Node ID": node.id,
                "Labels": ', '.join(labels),
                **node_properties
            }
            relationship_counts = defaultdict(int)
            numeric_attributes = defaultdict(list)  # Reset numeric attribute lists

        if relationship_type:
            relationship_counts[f"{relationship_type}"] += 1
        else:
            # Collect numeric attributes and their values
            for key, value in node_properties.items():
                if isinstance(value, (int, float)):
                    numeric_attributes[key].append(value)

    if current_node is not None:
        current_node.update(relationship_counts)
        current_node.update(numeric_attributes)  # Add numeric attribute lists
        data.append(current_node)

    # Create a DataFrame with all attributes and replace NaN with 0
    df = pd.DataFrame(data).fillna(0)

    # Set Pandas display options to show all columns and rows
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # Save the DataFrame to a CSV file
    df.to_csv('output_folder/displayed_data_edges_counts.csv', index=False)
    print("CSV file 'displayed_data_edges_counts.csv' created successfully")

    # Create a folder to store individual labeled CSV files
    labeled_folder = 'output_folder/labeled_csv_files_edges_counts'
    os.makedirs(labeled_folder, exist_ok=True)

    # Create separate CSV files for nodes with each specific Label attribute
    for label in df['Labels'].explode().unique():
        label_df = df[df['Labels'].apply(lambda x: label in x)]

        # Check if all values in each relationship column are 0.0, and remove if true
        non_zero_columns = [col for col in label_df.columns if not all(label_df[col] == 0.0)]
        label_df = label_df[non_zero_columns]

        labeled_csv_file = f'{labeled_folder}/{label}_nodes_edges_counts.csv'
        label_df.to_csv(labeled_csv_file, index=False)
        print(f"CSV file '{labeled_csv_file}' created successfully for nodes with Label '{label}'")

    return df
