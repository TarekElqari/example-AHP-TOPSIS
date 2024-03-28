# Car Evaluation Project

This Python project implements the Analytic Hierarchy Process (AHP) and 
Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) methods for car evaluation.
 The project consists of several Python files:

- `ahp.py`: Contains the implementation of the AHP method.
- `topsis.py`: Contains the implementation of the TOPSIS method.
- `visualise.py`: Contains a function for ranking visualization.
- `__init__.py`: The main file to run the AHP and TOPSIS methods.

## Usage

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Make sure you have Python installed on your machine.
4. Set up a virtual environment (optional but recommended).
5. Install the required dependencies by running:
    pip install -r requirements.txt

6. Run the __init__.py file to execute the AHP and TOPSIS methods:
    python __init__.py

## Project Structure

- `ahp.py`: Contains the AHP method implementation.
- `topsis.py`: Contains the TOPSIS method implementation.
- `visualise.py`: Contains a function for ranking visualization.
- `__init__.py`: The main file to execute the AHP and TOPSIS methods.
- `README.md`: This file containing project information.
- `requirements.txt`: A list of project dependencies.

## Dependencies

- `numpy`: Used for numerical computations.
- `matplotlib`: Used for visualization.

## Example Dataset

The example dataset represents the performance of different cars on three criteria: price,
fuel efficiency, and safety rating. Each row represents a criterion,
and each column represents a car. Criterion types are specified 
as 'min' for price (lower is better) and 'max' for fuel efficiency
and safety rating (higher is better).
