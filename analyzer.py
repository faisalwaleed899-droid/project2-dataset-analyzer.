
import pandas as pd
from pathlib import Path


# ==========================================
# PROJECT 2: DATASET ANALYZER
# ==========================================

# Get the location of the project folder
PROJECT_DIR = Path(__file__).parent

# Get the location of the data folder
DATA_DIR = PROJECT_DIR / "data"


def analyze_dataset(file_path):
    """
    Load a CSV file and display a complete basic analysis.
    """

    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Display the project heading
        print("\n" + "=" * 50)
        print("             DATASET ANALYZER")
        print("=" * 50)

        print(f"\nFile Name: {file_path.name}")

        # ------------------------------------------
        # 1. DATASET INFORMATION
        # ------------------------------------------

        print("\n[1] DATASET INFORMATION")
        print("-" * 50)

        rows, columns = df.shape

        print(f"Number of rows    : {rows}")
        print(f"Number of columns : {columns}")
        print(f"Total cells       : {df.size}")

        # ------------------------------------------
        # 2. MISSING VALUES
        # ------------------------------------------

        print("\n[2] MISSING VALUES")
        print("-" * 50)

        missing_values = df.isnull().sum()
        total_missing = int(missing_values.sum())

        print(missing_values.to_string())
        print(f"\nTotal missing values: {total_missing}")

        if rows > 0 and columns > 0:
            missing_percentage = (
                total_missing / df.size
            ) * 100

            print(
                f"Missing data percentage: "
                f"{missing_percentage:.2f}%"
            )

        # ------------------------------------------
        # 3. NUMERICAL COLUMNS
        # ------------------------------------------

        numerical_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()

        print("\n[3] NUMERICAL COLUMNS")
        print("-" * 50)

        if numerical_columns:
            for column in numerical_columns:
                print(f"- {column}")
        else:
            print("No numerical columns found.")

        print(
            f"Total numerical columns: "
            f"{len(numerical_columns)}"
        )

        # ------------------------------------------
        # 4. CATEGORICAL COLUMNS
        # ------------------------------------------

        categorical_columns = df.select_dtypes(
            include=["object", "category", "string"]
        ).columns.tolist()

        print("\n[4] CATEGORICAL COLUMNS")
        print("-" * 50)

        if categorical_columns:
            for column in categorical_columns:
                print(f"- {column}")
        else:
            print("No categorical columns found.")

        print(
            f"Total categorical columns: "
            f"{len(categorical_columns)}"
        )

        # ------------------------------------------
        # 5. BASIC STATISTICS
        # ------------------------------------------

        print("\n[5] NUMERICAL STATISTICS")
        print("-" * 50)

        if numerical_columns:
            print(df[numerical_columns].describe().round(2))
        else:
            print("No numerical statistics available.")

        # ------------------------------------------
        # 6. CATEGORICAL STATISTICS
        # ------------------------------------------

        print("\n[6] CATEGORICAL STATISTICS")
        print("-" * 50)

        if categorical_columns:
            print(df[categorical_columns].describe().to_string())
        else:
            print("No categorical statistics available.")

        # ------------------------------------------
        # 7. DATA TYPES
        # ------------------------------------------

        print("\n[7] COLUMN DATA TYPES")
        print("-" * 50)

        print(df.dtypes.to_string())

        # ------------------------------------------
        # 8. COMPLETION MESSAGE
        # ------------------------------------------

        print("\n" + "=" * 50)
        print("         ANALYSIS COMPLETED SUCCESSFULLY")
        print("=" * 50)

    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path.name}' is empty.")

    except pd.errors.ParserError:
        print(
            f"Error: Could not parse '{file_path.name}'. "
            "Check whether it is a valid CSV file."
        )

    except UnicodeDecodeError:
        print(
            f"Error: Could not read the text encoding of "
            f"'{file_path.name}'."
        )

    except PermissionError:
        print(
            f"Error: Permission denied when reading "
            f"'{file_path.name}'."
        )

    except OSError as error:
        print(f"File error: {error}")


def main():
    """
    Find CSV files and let the user select one.
    """

    # Check whether the data folder exists
    if not DATA_DIR.exists():
        print("Error: The data folder does not exist.")
        print(f"Expected location: {DATA_DIR}")
        print("Please create a folder named 'data'.")
        return

    # Find all CSV files inside the data folder
    csv_files = sorted(DATA_DIR.glob("*.csv"))

    # Check whether any CSV files exist
    if not csv_files:
        print("No CSV files found!")
        print(f"Please add a CSV file to: {DATA_DIR}")
        return

    # Display available CSV files
    print("\nAvailable CSV files:")
    print("-" * 30)

    for index, file in enumerate(csv_files, start=1):
        print(f"{index}. {file.name}")

    # Ask the user to select a file
    while True:
        choice = input(
            "\nEnter the number of the CSV file to analyze: "
        ).strip()

        try:
            file_number = int(choice)

            if 1 <= file_number <= len(csv_files):
                selected_file = csv_files[file_number - 1]
                break

            print(
                f"Please enter a number from 1 to "
                f"{len(csv_files)}."
            )

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Analyze the selected CSV file
    analyze_dataset(selected_file)


# Run the program
if __name__ == "__main__":
    main()
