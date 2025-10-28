# MLOps

### 🎯 Goals of the project

### 👣 Steps

#### Step 1: Setup GitHub Repository

- Create a GitHub repository
- Clone the repository to you local machine

#### Step 2: Create a project structure

- Create a folder structure comparable to:
  
  ```
    mlops-demo/
    │
    ├── data/
    │   └── sample.csv
    ├── src/
    │   ├── train.py
    │   └── predict.py
    ├── requirements.txt
    └── README.md
  ```

#### Step 3: Setup dependencies

- Write the dependencies in the requirements.txt file
  
  ```
  pandas
  scikit-learn
  joblib
  ```

- Create a virtual environment and install the dependencies:
  
  ```py
  python -m venv mlops
  .\mlops\Scripts\activate
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```

#### Step 4: Create a pipeline YAML file
- In VS Code, create a folder `.github/workflows`.
- Inside, create a YAML file, e.g., `mlops-pipeline.yml`.
  ```yaml
  name: MLOps Pipeline

  on:
    push:
      paths:
        - 'data/**'       # trigger only when data changes
        - 'src/**'        # trigger only when source code changes

    jobs:
      retrain:
        runs-on: ubuntu-latest

        steps:
        - name: Checkout repository
            uses: actions/checkout@v3

        - name: Set up Python
            uses: actions/setup-python@v4
            with:
            python-version: '3.13.7'

        - name: Install dependencies
            run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
  ```
#### Step 5: Implement train.py
- Read the dataset
- Split the dataset in features and label and train and testset
- Create the model
- Use the test data to calculate MSE and r-squared
- Save the model

#### Step 6: Extend the pipeline to execute the script and save the model as an artifact
  ```yaml
    - name: Train model
      run: python src/train.py

    - name: Upload model artifact
        uses: actions/upload-artifact@v4
        with:
          name: linear-model-${{ github.run_id }}-${{ github.run_number }}
          path: models/
  ```
#### Step 7: Download the model from GitHub
After your GitHub Actions pipeline runs successfully, you can find your model artifact in a few places:     

  1. Actions tab → Specific workflow run: Go to your repository → Actions tab → click on the specific workflow
  run → scroll down to the "Artifacts" section at the bottom of the page
  2. Direct artifact download: The artifact will be named linear-model-{run_id}-{run_number} (e.g.,
  linear-model-123456789-1)
  3. Via GitHub API: You can also access artifacts programmatically using the GitHub REST API

  The artifact will contain the models/ directory with your linear_model.pkl file inside it. Note that GitHub       
  automatically zips artifacts, so you'll download a ZIP file containing your model.

  Important: GitHub artifacts have a retention period (default 90 days for public repos, configurable for
  private repos), after which they're automatically deleted.