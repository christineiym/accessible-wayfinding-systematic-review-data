"""Utilities for running the paper selection process.

Simply change paths for the input and output files for each stage of the paper selection process,
then run on the command line (after cd'ing to this directory) with the following command:

python -m part-2-paper-selection
"""


OUTPUT_TABLES: dict[str, list[str]] = {
    "stage 1": ["Exclusion_Stage_1"],
    "stage 2": ["Exclusion_Stage_2"],
    "analysis": [
        "Device_Classification",
        "Usage_Context",
        "Disability_of_Target_Population",
        "Technology_Type",
        "Data_Sources",
        "User_Involvement"
    ],
}

# queries
QUERY_TABLE_COLUMNS = """
    SELECT name FROM pragma_table_info(?);
"""
QUERY_PAPER_INFO = """
    SELECT paper_analysis_id, document_type, title, year, author, doi, abstract
        FROM All_Papers
        WHERE paper_analysis_id=?;
"""

# Steps:
# Stage 1: For each paper in all papers, input 0 or 1 for each category in Exclusion Stage 1.
# Stage 2: For each paper for which all criteria are 0 in Stage 1, input 0 or 1 for each category in Exclusion Stage 2.
# Duplicates: Mark duplicates in the table after identifying relationships.
# For each paper that passes Stage 2 AND is not a duplicate, enter criteria for each dimension table.


def main():
    print("test")


def run_stage(stage_name: str, record_id_list: list[str]):
    print("Begin")

    for table in OUTPUT_TABLES[stage_name]:
        # Get information on relevant table

        # Define relevant insertion query
        query_insertion = """"""

    i = 0
    while i < len(record_id_list):
        # Print selected information on the paper

        # Ask for input

        for table in OUTPUT_TABLES[stage_name]:
            # Insert into table
            print("placeholder")
        
        i += 1


if "__name__" == "main":
    main()