# 🎯 CareerFit AI

### AI-Powered Career Readiness, Job-Fit & Salary Analysis System

CareerFit AI is a Machine Learning-based application that analyzes a candidate's career profile and provides an estimated salary, job-fit score, skill-gap analysis, and personalized career recommendations.

The project combines a Machine Learning regression model with a career recommendation layer and an interactive Streamlit dashboard.

---

##  Project Overview

Choosing the right job role can be difficult for students and early-career professionals because they may not know:

- How well their current profile matches a target role
- Which skills they are missing
- What salary they can expect based on their profile
- What areas they should improve

CareerFit AI addresses these problems by analyzing candidate information such as education, experience, skills, certifications, industry, company size, location, and remote-work preference.

---

##  Key Features

###  Salary Prediction
Predicts an estimated salary using a trained Machine Learning regression model.

###  Job Fit Score
Calculates how closely a candidate's skills and experience align with a selected job role.

###  Skill Gap Analysis
Identifies important skills that the candidate currently lacks for the selected role.

###  Career Recommendations
Provides actionable suggestions based on the candidate's profile and identified skill gaps.

### Interactive Dashboard
Built using Streamlit to provide an easy-to-use interface for entering candidate information and viewing results.

###  Model Evaluation
The Machine Learning model is evaluated using:

- Mean Absolute Error (MAE)
- R² Score

---

##  System Architecture

```text
                 Job Market Dataset
                         │
                         ▼
                Data Preprocessing
                         │
              ┌──────────┴──────────┐
              │                     │
       Numerical Features     Categorical Features
              │                     │
              │              One-Hot Encoding
              │                     │
              └──────────┬──────────┘
                         ▼
               Random Forest
                  Regression
                         │
                         ▼
                Salary Prediction
                         │
                         ▼
              CareerFit Analyzer
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
     Job Fit Score   Skill Gap    Recommendations
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                 Streamlit Dashboard
