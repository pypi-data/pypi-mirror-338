import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def calculate_correlations(labeled_csv_folder, include_kendall=False):
    include_pearson = True
    include_spearman = True

    pdf_folder = 'output_folder/correlations_folder'
    os.makedirs(pdf_folder, exist_ok=True)

    for label_csv_file in os.listdir(labeled_csv_folder):
        if label_csv_file.endswith("_nodes.csv"):
            df = pd.read_csv(os.path.join(labeled_csv_folder, label_csv_file))

            # Set display options to show all columns and rows
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_rows', None)

            # Filter out Node ID and non-numeric columns
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
            numeric_columns = [col for col in numeric_columns if col != "Node ID"]

            # Create a DataFrame with only numeric columns (excluding "Node ID")
            numeric_df = df[numeric_columns].fillna(0)

            correlation_methods = {}
            if include_pearson:
                pearson_correlation = numeric_df.corr(method='pearson')
                correlation_methods["Pearson"] = pearson_correlation
                pearson_correlation.to_csv(f'{pdf_folder}/{label_csv_file}_correlations_pearson.csv')
                print(
                    f"CSV file '{pdf_folder}/{label_csv_file}_correlations_pearson.csv' created successfully for '{label_csv_file}'")
                print()

            if include_spearman:
                spearman_correlation = numeric_df.corr(method='spearman')
                correlation_methods["Spearman"] = spearman_correlation
                spearman_correlation.to_csv(f'{pdf_folder}/{label_csv_file}_correlations_spearman.csv')
                print(
                    f"CSV file '{pdf_folder}/{label_csv_file}_correlations_spearman.csv' created successfully for '{label_csv_file}'")
                print()

            if include_kendall:
                kendall_correlation = numeric_df.corr(method='kendall')
                correlation_methods["Kendall"] = kendall_correlation
                kendall_correlation.to_csv(f'{pdf_folder}/{label_csv_file}_correlations_kendall.csv')
                print(
                    f"CSV file '{pdf_folder}/{label_csv_file}_correlations_kendall.csv' created successfully for '{label_csv_file}'")
                print()

            with PdfPages(f'{pdf_folder}/{label_csv_file}_correlation_heatmaps_matrices.pdf') as pdf:
                for method_name, correlation_matrix in correlation_methods.items():
                    fig, ax = plt.subplots(figsize=(8, 6))

                    # Set vmin and vmax to ensure the color bar range is from -1 to 1
                    im = ax.matshow(correlation_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)

                    # Title indicating the correlation method and file name
                    plt.title(f'{method_name} Correlation Matrix - {label_csv_file}', fontsize=10)

                    # Calculate text size and rotation angle based on the number of attributes
                    num_attributes = len(numeric_columns)
                    text_size = 8 if num_attributes <= 5 else 6
                    rotation_angle = 0 if num_attributes <= 5 else 22.5

                    # Display correlation values in cells
                    for i in range(correlation_matrix.shape[0]):
                        for j in range(correlation_matrix.shape[1]):
                            ax.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}', ha='center', va='center',
                                    color='k', fontsize=text_size)  # Adjust the fontsize as needed

                    # Adjust x and y axis labels for better visibility
                    ax.set_xticks(np.arange(len(numeric_columns)))
                    ax.set_yticks(np.arange(len(numeric_columns)))

                    if num_attributes > 5:
                        ax.set_xticklabels(numeric_columns, fontsize=text_size, rotation=rotation_angle, ha="center")
                        ax.set_yticklabels(numeric_columns, fontsize=text_size, va="center")
                    else:
                        ax.set_xticklabels(numeric_columns, fontsize=text_size, rotation=0, ha="center")
                        ax.set_yticklabels(numeric_columns, fontsize=text_size, va="center")

                    fig.subplots_adjust(right=0.85)
                    cbar_ax = fig.add_axes([0.88, 0.15, 0.03, 0.7])
                    cbar = plt.colorbar(im, cax=cbar_ax)
                    cbar.ax.tick_params(labelsize=text_size)

                    pdf.savefig()
                    plt.close()

                    print(
                        f"PDF file '{pdf_folder}/{label_csv_file}_correlation_heatmaps_matrices.pdf' created successfully for {label_csv_file}")
                    print()
