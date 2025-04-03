import os
import pandas as pd
from collections import defaultdict


def display_node_info(session):
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

    # Load the calculated sums from the CSV file
    sums_df = pd.read_csv('output_folder/init_folder/nodes_from_graph_distances.csv', index_col='NODE_ID')

    numeric_attributes = defaultdict(list)

    for record in result:
        node = record["n"]
        labels = record["labels"]
        node_properties = record["node_properties"]
        relationship_type = record["relationship_type"]

        if current_node is None or node.id != current_node["Node ID"]:
            if current_node is not None:
                current_node.update(numeric_attributes)  # Add numeric attribute lists
                data.append(current_node)
            current_node = {
                "Node ID": node.id,
                "Labels": ', '.join(labels),
                **node_properties
            }
            numeric_attributes = defaultdict(list)  # Reset numeric attribute lists

        if relationship_type:
            # Replace the relationship counts with the corresponding values
            current_node[relationship_type] = int(sums_df.at[node.id, relationship_type])

        # Collect numeric attributes and their values
        for key, value in node_properties.items():
            if isinstance(value, list):
                numeric_attributes[key] += value
            else:
                current_node[key] = value

    if current_node is not None:
        current_node.update(numeric_attributes)  # Add numeric attribute lists
        data.append(current_node)

    # Create a DataFrame with all attributes and replace NaN with 0
    df = pd.DataFrame(data).fillna(0)

    # Convert lists to single values for columns containing lists
    for col in df.columns:
        if isinstance(df.at[0, col], list):
            df[col] = df[col].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else x)

    # Set Pandas display options to show all columns and rows
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # Save the DataFrame to a CSV file
    df.to_csv(f'output_folder/displayed_data.csv', index=False)
    print("CSV file 'displayed_data.csv' created successfully")
    print()

    # Create a folder to store individual label CSV files
    labeled_folder = f'output_folder/labeled_csv_files'
    os.makedirs(labeled_folder, exist_ok=True)

    # Create separate CSV files for nodes with each specific Label attribute
    for label in df['Labels'].explode().unique():
        label_df = df[df['Labels'].apply(lambda x: label in x)]

        # Check if all values in each relationship column are 0.0, and remove if true
        non_zero_columns = [col for col in label_df.columns if not all(label_df[col] == 0.0)]
        label_df = label_df[non_zero_columns]

        labeled_csv_file = f'{labeled_folder}/{label}_nodes.csv'
        label_df.to_csv(labeled_csv_file, index=False)
        print(f"CSV file '{labeled_csv_file}' created successfully for nodes with Label '{label}'")
        print()

    return df
