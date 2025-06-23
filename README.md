
# AgriSmart Crop Recommendation

AgriSmart is an intelligent crop recommendation system designed to assist farmers in selecting the most suitable crops based on soil and environmental conditions. The system uses machine learning algorithms to analyze parameters such as soil nutrients, pH, temperature, humidity, and rainfall to provide accurate crop suggestions.

---

## Features

- Predicts the best crop to grow based on:
  - Soil nutrients: Nitrogen (N), Phosphorus (P), Potassium (K)
  - pH level
  - Temperature
  - Humidity
  - Rainfall
- Machine learning-based predictive model
- Easy-to-use interface (CLI / Web / Mobile compatible)
- Scalable and customizable for various regions and datasets
- Future support for dynamic weather API integration

---

## Project Structure

```
AgriSmart/
├── data/               # Dataset files and data preprocessing scripts
├── models/             # Trained machine learning models and training code
├── app/                # Application code (API, web or CLI interface)
├── notebooks/          # Jupyter notebooks for exploration and experiments
├── requirements.txt    # List of Python dependencies
├── README.md           # Project documentation
└── LICENSE             # License information
```

---

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:

```bash
git clone https://github.com/rishikam23/AgriSmart-Crop-Recommendation-System/tree/main
cd AgriSmart
```

2. Create a virtual environment **(recommended)**:

```bash
python -m venv venv
source venv\Scripts\activate
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```
4.️ Run the application:

```bash
python app/main.py
```

---

## Model Details

- The system is built using supervised machine learning algorithms (e.g., Random Forest, Decision Tree, or SVM).
- Trained on agricultural datasets containing soil and environmental parameters with corresponding suitable crops.
- The model can be retrained with regional data for improved accuracy.

---

## Usage

Once the app is running:

- Enter soil nutrient values (N, P, K), pH, temperature, humidity, and rainfall.
- The system will output the most suitable crop for the given conditions.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- Inspired by Indian agricultural datasets and local farming practices.
- Uses open-source libraries including Scikit-learn, Pandas, NumPy, and Flask/FastAPI.
