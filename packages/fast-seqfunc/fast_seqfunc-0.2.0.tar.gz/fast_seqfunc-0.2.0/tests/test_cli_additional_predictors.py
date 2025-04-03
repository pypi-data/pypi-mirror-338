"""Tests for CLI functionality with additional predictors."""

import shutil
import tempfile
from pathlib import Path

import pandas as pd
import pytest
from typer.testing import CliRunner

from fast_seqfunc.cli import app
from fast_seqfunc.synthetic import generate_dataset_with_predictors


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    tmp_dir = tempfile.mkdtemp()
    yield tmp_dir
    # Clean up after tests
    shutil.rmtree(tmp_dir)


@pytest.fixture
def dataset_with_predictors(temp_dir):
    """Generate a dataset with sequences and additional predictors."""
    # Create a dataset with sequences, additional predictors, and target values
    data = pd.DataFrame(
        {
            "sequence": ["ACDEFGHIKLM", "NOPQRSTUVWX", "YZACDEFGHIK", "LMNOPQRSTUV"],
            "pH": [6.5, 7.0, 7.5, 8.0],
            "temperature": [25, 30, 35, 40],
            "buffer_type": ["phosphate", "tris", "phosphate", "tris"],
            "function": [0.45, 0.62, 0.78, 0.34],
        }
    )

    # Save to CSV in the temp directory
    data_path = Path(temp_dir) / "data_with_predictors.csv"
    data.to_csv(data_path, index=False)

    return data_path


@pytest.fixture
def large_synthetic_dataset(temp_dir):
    """Generate a larger synthetic dataset with sequences and additional predictors."""
    # Use synthetic data generator to create a more robust dataset
    data = generate_dataset_with_predictors(
        task="nonlinear_composition",  # Nonlinear regression task
        count=100,  # 100 samples
        noise_level=0.2,  # Add some noise
        num_numeric_predictors=2,  # Add 2 numeric predictors
        num_categorical_predictors=1,  # Add 1 categorical predictor
        correlation_strength=0.7,  # Strong correlation with target
    )

    # Rename columns to more descriptive names for CLI tests
    data = data.rename(
        columns={
            "predictor1": "concentration",
            "predictor2": "pH",
            "categorical_pred1": "buffer_type",
        }
    )

    # Save to CSV in the temp directory
    data_path = Path(temp_dir) / "large_synthetic_data.csv"
    data.to_csv(data_path, index=False)

    return data_path


@pytest.mark.slow
def test_cli_regression_with_predictors(dataset_with_predictors, temp_dir):
    """Test CLI with regression task including additional predictors."""
    runner = CliRunner()
    output_dir = Path(temp_dir) / "outputs"
    model_path = output_dir / "model.pkl"

    # Train model with additional predictors
    result = runner.invoke(
        app,
        [
            "train",
            str(dataset_with_predictors),
            "--sequence-col",
            "sequence",
            "--target-col",
            "function",
            "--embedding-method",
            "one-hot",
            "--model-type",
            "regression",
            "--output-dir",
            str(output_dir),
            "--model-filename",
            "model.pkl",
            "--additional-predictors",
            "pH,temperature",
        ],
    )

    assert result.exit_code == 0
    assert model_path.exists()

    # Make predictions
    predictions_dir = Path(temp_dir) / "prediction_outputs"
    predictions_path = predictions_dir / "predictions.csv"
    result = runner.invoke(
        app,
        [
            "predict-cmd",
            str(model_path),
            str(dataset_with_predictors),
            "--sequence-col",
            "sequence",
            "--output-dir",
            str(predictions_dir),
            "--predictions-filename",
            "predictions.csv",
        ],
    )

    assert result.exit_code == 0
    assert predictions_path.exists()

    # Verify predictions file has expected columns
    predictions_df = pd.read_csv(predictions_path)
    assert "sequence" in predictions_df.columns
    assert "prediction" in predictions_df.columns


@pytest.mark.slow
def test_cli_with_categorical_predictors(dataset_with_predictors, temp_dir):
    """Test CLI with categorical additional predictors."""
    runner = CliRunner()
    output_dir = Path(temp_dir) / "outputs_categorical"
    model_path = output_dir / "model.pkl"

    # Train model with categorical predictor
    result = runner.invoke(
        app,
        [
            "train",
            str(dataset_with_predictors),
            "--sequence-col",
            "sequence",
            "--target-col",
            "function",
            "--embedding-method",
            "one-hot",
            "--model-type",
            "regression",
            "--output-dir",
            str(output_dir),
            "--model-filename",
            "model.pkl",
            "--additional-predictors",
            "buffer_type",
        ],
    )

    assert result.exit_code == 0
    assert model_path.exists()

    # Make predictions
    predictions_dir = Path(temp_dir) / "prediction_cat_outputs"
    predictions_path = predictions_dir / "predictions.csv"
    result = runner.invoke(
        app,
        [
            "predict-cmd",
            str(model_path),
            str(dataset_with_predictors),
            "--sequence-col",
            "sequence",
            "--output-dir",
            str(predictions_dir),
            "--predictions-filename",
            "predictions.csv",
        ],
    )

    assert result.exit_code == 0
    assert predictions_path.exists()


@pytest.mark.slow
def test_cli_with_multiple_predictors(dataset_with_predictors, temp_dir):
    """Test CLI with multiple additional predictors of different types."""
    runner = CliRunner()
    output_dir = Path(temp_dir) / "outputs_multiple"
    model_path = output_dir / "model.pkl"

    # Train model with multiple predictors
    result = runner.invoke(
        app,
        [
            "train",
            str(dataset_with_predictors),
            "--sequence-col",
            "sequence",
            "--target-col",
            "function",
            "--embedding-method",
            "one-hot",
            "--model-type",
            "regression",
            "--output-dir",
            str(output_dir),
            "--model-filename",
            "model.pkl",
            "--additional-predictors",
            "pH,temperature,buffer_type",
        ],
    )

    assert result.exit_code == 0
    assert model_path.exists()

    # Make predictions
    predictions_dir = Path(temp_dir) / "prediction_multi_outputs"
    predictions_path = predictions_dir / "predictions.csv"
    result = runner.invoke(
        app,
        [
            "predict-cmd",
            str(model_path),
            str(dataset_with_predictors),
            "--sequence-col",
            "sequence",
            "--output-dir",
            str(predictions_dir),
            "--predictions-filename",
            "predictions.csv",
        ],
    )

    assert result.exit_code == 0
    assert predictions_path.exists()


@pytest.mark.slow
def test_cli_missing_predictor_error(dataset_with_predictors, temp_dir):
    """Test CLI behavior when a predictor is missing in prediction data."""
    runner = CliRunner()
    output_dir = Path(temp_dir) / "outputs_error"
    model_path = output_dir / "model.pkl"

    # Train model with pH predictor
    result = runner.invoke(
        app,
        [
            "train",
            str(dataset_with_predictors),
            "--sequence-col",
            "sequence",
            "--target-col",
            "function",
            "--embedding-method",
            "one-hot",
            "--model-type",
            "regression",
            "--output-dir",
            str(output_dir),
            "--model-filename",
            "model.pkl",
            "--additional-predictors",
            "pH",
        ],
    )

    assert result.exit_code == 0
    assert model_path.exists()

    # Create prediction data without pH
    data = pd.DataFrame(
        {
            "sequence": ["ACDEFGHIKLM", "NOPQRSTUVWX"],
            "temperature": [25, 30],
            "function": [0.45, 0.62],
        }
    )

    missing_path = Path(temp_dir) / "missing_predictor.csv"
    data.to_csv(missing_path, index=False)

    # Make predictions (should fail)
    predictions_dir = Path(temp_dir) / "prediction_error_outputs"
    result = runner.invoke(
        app,
        [
            "predict-cmd",
            str(model_path),
            str(missing_path),
            "--sequence-col",
            "sequence",
            "--output-dir",
            str(predictions_dir),
            "--predictions-filename",
            "predictions.csv",
        ],
    )

    # Should exit with an error
    assert result.exit_code != 0
    assert "Missing required predictor column" in result.stdout


@pytest.mark.slow
def test_cli_backwards_compatibility(dataset_with_predictors, temp_dir):
    """Test CLI backward compatibility with models trained without predictors."""
    runner = CliRunner()
    output_dir = Path(temp_dir) / "outputs_compatibility"
    model_path = output_dir / "model.pkl"

    # Train model without additional predictors
    result = runner.invoke(
        app,
        [
            "train",
            str(dataset_with_predictors),
            "--sequence-col",
            "sequence",
            "--target-col",
            "function",
            "--embedding-method",
            "one-hot",
            "--model-type",
            "regression",
            "--output-dir",
            str(output_dir),
            "--model-filename",
            "model.pkl",
        ],
    )

    assert result.exit_code == 0
    assert model_path.exists()

    # Create prediction data with only sequences
    data = pd.DataFrame(
        {
            "sequence": ["ACDEFGHIKLM", "NOPQRSTUVWX"],
        }
    )

    sequence_path = Path(temp_dir) / "sequences_only.csv"
    data.to_csv(sequence_path, index=False)

    # Make predictions with sequences only
    predictions_dir = Path(temp_dir) / "prediction_compat_outputs"
    predictions_path = predictions_dir / "predictions.csv"
    result = runner.invoke(
        app,
        [
            "predict-cmd",
            str(model_path),
            str(sequence_path),
            "--sequence-col",
            "sequence",
            "--output-dir",
            str(predictions_dir),
            "--predictions-filename",
            "predictions.csv",
        ],
    )

    assert result.exit_code == 0
    assert predictions_path.exists()


@pytest.mark.slow
def test_cli_with_large_synthetic_dataset(large_synthetic_dataset, temp_dir):
    """Test CLI with a larger synthetic dataset including additional predictors."""
    runner = CliRunner()
    output_dir = Path(temp_dir) / "outputs_large_synthetic"
    model_path = output_dir / "model.pkl"

    # Read data to get column names
    data = pd.read_csv(large_synthetic_dataset)

    # Train model with all predictors
    result = runner.invoke(
        app,
        [
            "train",
            str(large_synthetic_dataset),
            "--sequence-col",
            "sequence",
            "--target-col",
            "function",
            "--embedding-method",
            "one-hot",
            "--model-type",
            "regression",
            "--output-dir",
            str(output_dir),
            "--model-filename",
            "model.pkl",
            "--additional-predictors",
            "concentration,pH,buffer_type",
        ],
    )

    assert result.exit_code == 0
    assert model_path.exists()

    # Make predictions on the same dataset
    predictions_dir = Path(temp_dir) / "prediction_large_synthetic"
    predictions_path = predictions_dir / "predictions.csv"
    result = runner.invoke(
        app,
        [
            "predict-cmd",
            str(model_path),
            str(large_synthetic_dataset),
            "--sequence-col",
            "sequence",
            "--output-dir",
            str(predictions_dir),
            "--predictions-filename",
            "predictions.csv",
        ],
    )

    assert result.exit_code == 0
    assert predictions_path.exists()

    # Verify predictions
    predictions_df = pd.read_csv(predictions_path)
    assert len(predictions_df) == len(data)
    assert "sequence" in predictions_df.columns
    assert "prediction" in predictions_df.columns

    # Create a split dataset for testing generalization
    train_data = data.iloc[:80]
    test_data = data.iloc[80:]

    train_path = Path(temp_dir) / "train_large_synthetic.csv"
    test_path = Path(temp_dir) / "test_large_synthetic.csv"

    train_data.to_csv(train_path, index=False)
    test_data.to_csv(test_path, index=False)

    # Train on split data
    split_output_dir = Path(temp_dir) / "outputs_split_synthetic"
    split_model_path = split_output_dir / "model.pkl"

    result = runner.invoke(
        app,
        [
            "train",
            str(train_path),
            "--sequence-col",
            "sequence",
            "--target-col",
            "function",
            "--embedding-method",
            "one-hot",
            "--model-type",
            "regression",
            "--output-dir",
            str(split_output_dir),
            "--model-filename",
            "model.pkl",
            "--additional-predictors",
            "concentration,pH,buffer_type",
            "--test-data",
            str(test_path),
        ],
    )

    assert result.exit_code == 0
    assert split_model_path.exists()
