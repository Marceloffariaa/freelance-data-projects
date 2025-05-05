# Data Merge Pipeline

This project demonstrates a simple ETL (Extract, Transform, Load) data pipeline that merges data from two different sources: a JSON file and a CSV file. It performs column mapping, combines datasets, and outputs a unified dataset in CSV format.

## 📌 Use Case

This pipeline simulates a scenario where two branches of the same company store product information in different formats and need to consolidate their data for analysis.

## 🛠 Technologies Used

- Python 3.10+
- `csv` module (standard)
- `json` module (standard)

## 📂 Project Structure

```
data-merge-pipeline/
├── data_merge_pipeline.py              # Main script (ETL steps)
├── data_merge_pipeline_class.py       # Class for data handling
├── data_raw/                           # Input files (CSV and JSON)
├── data_processed/                     # Output folder for merged file
└── README.md                           # Project documentation
```

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Marceloffariaa/freelance-data-projects.git
cd freelance-data-projects/data-merge-pipeline
```

2. Make sure you have Python 3.10+ installed.

3. Add your input files to the `data_raw` folder:
   - `dados_empresaA.json`
   - `dados_empresaB.csv`

4. Run the pipeline:

```bash
python data_merge_pipeline.py
```

5. The merged data will be saved to:

```
data_processed/merged_data.csv
```

## 🧠 Key Functionalities

- Read and parse CSV and JSON files
- Rename columns using a defined mapping
- Merge data from both sources
- Export results to a structured CSV file

## ✅ Example Output

```csv
Product Name,Product Category,Product Price (R$),Stock Quantity,Store,Sale Date
Notebook,Gaming,5500.00,12,São Paulo,2023-03-02
...
```

## 👨‍💻 Author

**Marcelo Faria**  
Data Engineer & Freelancer  
[LinkedIn](https://www.linkedin.com/in/seu-perfil) – [GitHub](https://github.com/Marceloffariaa)

---

📬 *Feel free to fork this project or contact me for collaboration opportunities!*
