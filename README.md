# 📊 Machine Learning Experiment Tracking with MLflow & DagsHub

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/MLflow-MLOps-0194E2?style=for-the-badge&logo=mlflow&logoColor=white">

<img src="https://img.shields.io/badge/DagsHub-Remote%20Tracking-4CAF50?style=for-the-badge">

<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">

</p>

<p align="center">

<a href="https://github.com/Anujku007/mlflowexperiments">
<img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github">
</a>

<a href="https://dagshub.com/Anujku007/mlflowexperiments.mlflow">
<img src="https://img.shields.io/badge/DagsHub-MLflow%20Tracking-blue?style=for-the-badge">
</a>

</p>

---

# 📖 Overview

This project demonstrates the fundamentals of **MLflow**, an open-source platform for managing the **Machine Learning lifecycle**, along with **DagsHub**, a collaborative platform for remote experiment tracking.

The project focuses on understanding how machine learning experiments are managed in real-world MLOps workflows. It explores tracking model parameters, logging evaluation metrics, storing model artifacts, and maintaining reproducible experiments using MLflow, while synchronizing experiment data to DagsHub.

Rather than building a production-ready machine learning application, this repository is designed to provide hands-on experience with the tools and workflow commonly used in modern Machine Learning Operations (MLOps).

---

# ⭐ Project Highlights

- 📊 MLflow Experiment Tracking
- ☁ Remote Experiment Tracking with DagsHub
- 📈 Parameter Logging
- 📉 Metrics Logging
- 📦 Model Artifact Management
- 🔄 Experiment Comparison
- 📚 Reproducible Machine Learning Workflow
- 🚀 Introduction to MLOps

---

# 🌐 Remote Experiment Tracking

This project integrates **MLflow** with **DagsHub**, enabling remote storage and management of machine learning experiments.

Using DagsHub, experiment runs, parameters, metrics, and artifacts are synchronized automatically, making it easier to organize, compare, and reproduce machine learning experiments across different environments.

### MLflow Tracking Repository

**🔗 https://dagshub.com/Anujku007/mlflowexperiments.mlflow**

Example configuration:

```python
import dagshub

dagshub.init(
    repo_owner="Anujku007",
    repo_name="mlflowexperiments",
    mlflow=True
)

import mlflow

with mlflow.start_run():
    mlflow.log_param("parameter name", "value")
    mlflow.log_metric("metric name", 1)
```

---

# 🛠 Tech Stack

## Programming Language

- Python

## MLOps

- MLflow
- DagsHub

## Machine Learning

- Scikit-learn

## Data Processing

- Pandas
- NumPy

## Visualization

- Matplotlib

## Development Tools

- Git
- GitHub
- VS Code
- Jupyter Notebook

---

# 📂 Project Structure

```text
mlflowexperiments/
│
├── app.py
├── mlflow.db
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🏗️ MLflow Workflow

```text
                    Dataset
                       │
                       ▼
              Data Preprocessing
                       │
                       ▼
               Model Training
                       │
                       ▼
               MLflow Tracking
                       │
         ┌─────────────┼─────────────┐
         │             │             │
         ▼             ▼             ▼
    Parameters      Metrics      Artifacts
         │             │             │
         └─────────────┼─────────────┘
                       │
                       ▼
         DagsHub Remote Tracking Server
                       │
                       ▼
            Compare Experiment Runs
```

---

# 📈 MLflow Features

### ✔ Experiment Tracking

Track multiple machine learning runs with complete experiment history.

### ✔ Parameter Logging

Store hyperparameters used during model training.

### ✔ Metric Logging

Track evaluation metrics such as:

- RMSE
- MAE
- R² Score
- Accuracy (depending on the model)

### ✔ Artifact Management

Store trained models, plots, and additional experiment outputs.

### ✔ Remote Tracking

Synchronize experiment runs with DagsHub for centralized access and collaboration.

### ✔ Reproducibility

Maintain reproducible machine learning workflows by preserving parameters, metrics, and artifacts.

---

# 📚 What I Learned

Through this project, I gained practical experience in:

- Understanding the Machine Learning lifecycle
- Using MLflow for experiment tracking
- Logging parameters and evaluation metrics
- Managing model artifacts
- Comparing experiment runs
- Integrating MLflow with DagsHub
- Remote experiment management
- Building reproducible ML workflows
- Fundamentals of MLOps

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Anujku007/mlflowexperiments.git
```

Navigate to the project

```bash
cd mlflowexperiments
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python app.py
```

Launch the MLflow UI

```bash
mlflow ui
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 💡 Skills Demonstrated

- Machine Learning Lifecycle
- MLflow
- DagsHub
- MLOps Fundamentals
- Experiment Tracking
- Parameter Logging
- Metrics Logging
- Model Artifact Management
- Remote Experiment Tracking
- Reproducible Machine Learning
- Python

---

# 📚 Key Takeaways

This project helped me understand:

- The complete Machine Learning lifecycle
- Importance of experiment tracking
- Logging parameters and metrics
- Managing model artifacts
- Comparing multiple experiments
- Remote tracking with DagsHub
- Reproducible machine learning pipelines
- Core concepts of MLOps

---

# 🚀 Future Improvements

- MLflow Model Registry
- Docker Integration
- Kubernetes Deployment
- CI/CD Pipeline
- DVC Integration
- BentoML Model Serving
- AWS Deployment
- Complete End-to-End MLOps Pipeline

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 👨‍💻 Author

**Anuj Kumar**

💻 Passionate about Machine Learning, Deep Learning, NLP, and MLOps.

**GitHub:** https://github.com/Anujku007

---

# ⭐ Support

If you found this repository useful, please consider giving it a ⭐ Star.

Your support motivates future open-source contributions.

---

# 📜 License

This project is licensed under the **MIT License**.

---

<p align="center">
Built with ❤️ using Python, MLflow & DagsHub
</p>