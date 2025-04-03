from .neo4j_connector import connect_to_neo4j
from .neo4j_fetch_data import fetch_nodes_and_relationships
from .neo4j_fetch_paths import calculate_distances_and_sums
from .neo4j_display_distances import display_node_info
from .neo4j_calculate_correlations import calculate_correlations


# from .neo4j_display_edges import display_node_info_edges_counts


def neo4j_correlation_heatmaps(uri, username, password, include_kendall=False):
    neo4j_connector = connect_to_neo4j(uri, username, password)

    with neo4j_connector.driver.session() as session:
        fetch_nodes_and_relationships(session)
        calculate_distances_and_sums('output_folder/init_folder/nodes_and_relationships.csv',
                                     'output_folder/init_folder/node_to_node_distances.csv',
                                     'output_folder/init_folder/nodes_from_graph_distances.csv')
        display_node_info(session)
        # display_node_info_edges_counts(session)

        # Specify the folder containing individual label CSV files
        label_csv_folder = 'output_folder/labeled_csv_files'
        calculate_correlations(label_csv_folder, include_kendall)

        # label_csv_folder_edges_counts = 'output_folder/labeled_csv_files_edges_counts'
        # calculate_correlations(label_csv_folder_edges_counts, include_kendall)
