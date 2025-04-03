import csv
import pandas as pd
from queue import Queue
from collections import defaultdict


class GraphDistanceCalculator:
    def __init__(self, csv_file_path):
        self.sums = None
        self.df = pd.read_csv(csv_file_path)
        self.unique_nodes = self.get_unique_nodes()
        self.unique_relationships = self.get_unique_relationships()
        self.distances = self.calculate_distances()

    def get_unique_nodes(self):
        start_nodes = self.df["START_NODE"].unique()
        end_nodes = self.df["END_NODE"].unique()
        return sorted(pd.unique(pd.concat([pd.Series(start_nodes), pd.Series(end_nodes)])))

    def get_unique_relationships(self):
        return pd.Series(pd.unique(self.df["RELATIONSHIP"]))

    def calculate_distances(self):
        distances = {}
        for relationship in self.unique_relationships:
            distances[relationship] = {}
            for node in self.unique_nodes:
                distances[relationship][node] = self.calculate_distance(node, relationship)

        return distances

    def calculate_distance(self, start_node, relationship):
        graph = self.get_graph(relationship)
        distance = {node: float('inf') for node in self.unique_nodes}
        distance[start_node] = 0

        q = Queue()
        q.put(start_node)

        while not q.empty():
            node = q.get()
            for neighbor in graph[node]:
                if distance[neighbor] == float('inf'):
                    distance[neighbor] = distance[node] + 1
                    q.put(neighbor)

        return distance

    def get_graph(self, relationship):
        graph = defaultdict(list)
        for _, row in self.df[self.df["RELATIONSHIP"] == relationship].iterrows():
            graph[row["START_NODE"]].append(row["END_NODE"])
        return graph

    def save_distances_to_csv(self, output_file):
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["RELATIONSHIP", "NODE_ID"] + [f"VALUE_{i}" for i in
                                                           range(1, len(next(iter(self.distances.values()))) + 1)])
            for relationship, distances in self.distances.items():
                for node, values in distances.items():
                    row = [relationship, node] + list(values.values())
                    writer.writerow(row)

    def save_sums_to_csv(self, output_file):
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["NODE_ID"] + list(self.distances.keys()))

            for node in self.unique_nodes:
                row = [node] + [self.sums[relationship][node] for relationship in self.distances.keys()]
                writer.writerow(row)

    def calculate_sums(self):
        # Výpočet súčtov z vypočítaných vzdialeností
        self.sums = {}
        for relationship, distances in self.distances.items():
            self.sums[relationship] = {}
            for node, values in distances.items():
                non_zero_values = [value for value in values.values() if value != float('inf') and value != 0]
                count_non_zero_values = len(non_zero_values)
                sum_of_non_zero_values = sum(non_zero_values) if count_non_zero_values > 0 else 0

                # Divide the sum by the count of non-zero values
                self.sums[relationship][
                    node] = sum_of_non_zero_values / count_non_zero_values if count_non_zero_values > 0 else 0

        return self.sums


def calculate_distances_and_sums(csv_file_path, output_distances, output_sums):
    calculator = GraphDistanceCalculator(csv_file_path)
    calculator.save_distances_to_csv(output_distances)
    calculator.calculate_sums()
    calculator.save_sums_to_csv(output_sums)
    return calculator
