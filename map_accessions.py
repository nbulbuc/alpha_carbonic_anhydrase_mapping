import pandas as pd

input_ids_file = "ca_positive_ids.txt"        # one accession per line
metadata_file = "bac120_metadata_r226.tsv"         # GTDB metadata file
taxonomy_file = "bac120_taxonomy.tsv"         # GTDB taxonomy file
output_file = "ca_with_taxonomy.csv"          # output CSV

# Load input list
with open(input_ids_file) as f:
    ids = [line.strip() for line in f if line.strip()]

# Load GTDB metadata & taxonomy
metadata_df = pd.read_csv(metadata_file, sep="\t")
taxonomy_df = pd.read_csv(taxonomy_file, sep="\t", names=["accession", "taxonomy"])

# Merge metadata & taxonomy
merged = pd.merge(metadata_df, taxonomy_df, left_on="accession", right_on="accession", how="inner")

# Filter to only accessions in our list
filtered = merged[merged["accession"].isin(ids)]

# Save to CSV
filtered.to_csv(output_file, index=False)

print(f"Saved {len(filtered)} records to {output_file}")