from .neo4j_connector import connect_to_neo4j
from .neo4j_fetch_data import fetch_nodes_and_relationships
from .neo4j_fetch_paths import calculate_distances_and_sums
from .neo4j_display_distances import display_node_info
from .neo4j_display_edges import display_node_info_edges_counts
from .neo4j_calculate_correlations import calculate_correlations


def neo4j_correlation_heatmaps(uri, username, password, include_kendall=False, method='distances'):
    """
    Generate correlation heatmaps using either distances or edge counts.
    :param uri: Neo4j URI
    :param username: Neo4j Username
    :param password: Neo4j Password
    :param include_kendall: Include Kendall correlation
    :param method: 'distances' or 'edges'
    """
    neo4j_connector = connect_to_neo4j(uri, username, password)

    with neo4j_connector.driver.session() as session:
        fetch_nodes_and_relationships(session)

        if method == 'distances':
            calculate_distances_and_sums('output_folder/init_folder/nodes_and_relationships.csv',
                                         'output_folder/init_folder/node_to_node_distances.csv',
                                         'output_folder/init_folder/nodes_from_graph_distances.csv')
            display_node_info(session)
            label_csv_folder = 'output_folder/labeled_csv_files'

        elif method == 'edges':
            display_node_info_edges_counts(session)
            label_csv_folder = 'output_folder/labeled_csv_files_edges_counts'

        else:
            raise ValueError("Invalid method. Choose 'distances' or 'edges'.")

        calculate_correlations(label_csv_folder, include_kendall)
