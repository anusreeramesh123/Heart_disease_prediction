# CardioSense — Heart Disease Prediction

## Description

CardioSense is a web application built with Flask that predicts the likelihood of heart disease based on user-inputted medical parameters. It uses a pre-trained machine learning model to analyze inputs such as age, sex, chest pain type, blood pressure, cholesterol levels, and other cardiac indicators to provide a prediction.

## Features

- **Interactive Web Interface**: Clean, responsive UI with dark and light theme options.
- **Real-time Prediction**: Instant results based on machine learning model.
- **Input Validation**: Ensures data is entered correctly before prediction.
- **Machine Learning Powered**: Utilizes a trained model for accurate predictions.

## Installation

1. Ensure you have Python 3.7+ installed.
2. Clone or download this repository to your local machine.
3. Navigate to the project directory.
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Make sure the model files (`best_model_heart.pkl` and `heart_encoder.pkl`) are present in the root directory. If not, you may need to train or obtain them separately.

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```
2. Open your web browser and go to `http://127.0.0.1:5000/`.
3. Fill in the patient data form with the required medical parameters.
4. Click "Predict" to get the heart disease prediction result.

### Input Parameters

The application requires the following inputs:
- Age
- Sex (0 for female, 1 for male)
- Chest pain type (0-3)
- Resting blood pressure
- Serum cholesterol
- Resting electrocardiographic results (0-2)
- Maximum heart rate achieved
- Exercise induced angina (0 or 1)
- ST depression induced by exercise
- Slope of the peak exercise ST segment (0-2)
- Number of major vessels colored by fluoroscopy (0-3)
- Thalassemia (0-2)

## Dependencies

- Flask==2.3.3
- numpy==1.24.3
- joblib==1.3.2
- scikit-learn==1.3.0

## Troubleshooting

- **Model files missing**: Ensure `best_model_heart.pkl` and `heart_encoder.pkl` are in the project root.
- **Import errors**: Verify all dependencies are installed via `pip install -r requirements.txt`.
- **Port issues**: If port 5000 is in use, modify the `app.run()` call in `app.py` to use a different port.
- **Prediction errors**: Check that all form fields are filled with valid numeric values.

## License

This project is for educational purposes. Please consult medical professionals for actual health advice.

## Contributing

Feel free to submit issues or pull requests for improvements.