import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# --------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------

DATA_PATH = "data/job_salary_prediction_dataset.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())


# --------------------------------------------------
# 2. SELECT FEATURES
# --------------------------------------------------

features = [
    "experience_years",
    "education_level",
    "job_title",
    "skills_count",
    "industry",
    "company_size",
    "location",
    "remote_work",
    "certifications"
]

target = "salary"


# --------------------------------------------------
# 3. REMOVE MISSING VALUES
# --------------------------------------------------

df = df[features + [target]].dropna()

print("\nAfter removing missing values:")
print(df.shape)


# --------------------------------------------------
# 4. INPUT AND OUTPUT
# --------------------------------------------------

X = df[features]
y = df[target]


# --------------------------------------------------
# 5. CATEGORICAL / NUMERICAL FEATURES
# --------------------------------------------------

categorical_features = [
    "education_level",
    "job_title",
    "industry",
    "company_size",
    "location",
    "remote_work"
]

numerical_features = [
    "experience_years",
    "skills_count",
    "certifications"
]


# --------------------------------------------------
# 6. PREPROCESSING
# --------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical_features
        )
    ],
    remainder="passthrough"
)


# --------------------------------------------------
# 7. MODEL
# --------------------------------------------------

model = RandomForestRegressor(
    n_estimators=20,
    random_state=42,
    n_jobs=-1
)


# --------------------------------------------------
# 8. COMPLETE PIPELINE
# --------------------------------------------------

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# --------------------------------------------------
# 9. TRAIN TEST SPLIT
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# --------------------------------------------------
# 10. TRAIN
# --------------------------------------------------

print("\nTraining model...")

pipeline.fit(X_train, y_train)

print("Training completed!")


# --------------------------------------------------
# 11. EVALUATION
# --------------------------------------------------

predictions = pipeline.predict(X_test)

mae = mean_absolute_error(
    y_test,
    predictions
)

r2 = r2_score(
    y_test,
    predictions
)

print("\nMODEL PERFORMANCE")
print("-------------------------")
print("MAE:", round(mae, 2))
print("R2 Score:", round(r2, 4))


# --------------------------------------------------
# 12. SAVE MODEL
# --------------------------------------------------

joblib.dump(
    pipeline,
    "model/salary_model.pkl"
)

print("\nModel saved successfully!")
print("Location: model/salary_model.pkl")
