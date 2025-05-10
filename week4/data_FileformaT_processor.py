import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.parquet'):
            self.data = pd.read_parquet(self.file_path)
        elif self.file_path.endswith('.txt'):
            self.data = self.load_text_file()
        else:
            raise ValueError("Unsupported file format. Please use CSV or Parquet.")
        print(f"Data loaded successfully from {self.file_path}")

    def load_text_file(self):
        # Reading and processing text file
        with open(self.file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
        
    def initial_processing(self):
        if self.data is None:
            raise ValueError("No data loaded.")
        
        print("Initial Data Summary:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        print("\nDescriptive Statistics:")
        print(self.data.describe())




def main():
    # Replace the file path below with your actual file path
    file_path = 'C:/Users/msi/MSE800/week4/Sample_data_2.parquet'  # or 'your_data_file.parquet'
    processor = DataProcessor(file_path)
    processor.load_data()
    processor.initial_processing()

if __name__ == "__main__":
    main()
