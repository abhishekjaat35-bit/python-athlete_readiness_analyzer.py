## 👨‍💻 Author

**Abhishek Tomar**

Strength & Conditioning | Sports Performance | Sports Analytics | Python

---

## 📜 License

This project is licensed under the MIT License.

---

## 📌 Project Status

Completed ✅

# Athlete Readiness Analyzer

A Python sports-performance analytics project that combines athlete wellness indicators and training load to produce an educational readiness score.

## Objective

The system processes:

- Sleep
- Soreness
- Fatigue
- Stress
- Mood
- Training load

It produces:

- Wellness score
- Wellness percentage
- Training-load score
- Combined readiness score
- Readiness category
- Athlete ranking
- Team readiness summary
- Lowest-readiness session

## Data Flow

Athlete Data
↓
CSV
↓
Pandas
↓
Wellness Score
↓
Training Load Score
↓
Combined Readiness Score
↓
Readiness Classification
↓
Athlete Ranking
↓
CSV Reports

## Wellness Score

Sleep and mood are treated as positive indicators.

Soreness, fatigue and stress are treated as inverse indicators.

Formula:

Wellness Score =
Sleep
+ (6 - Soreness)
+ (6 - Fatigue)
+ (6 - Stress)
+ Mood

Maximum score = 25.

## Wellness Percentage

Wellness % = Wellness Score / 25 × 100

## Training Load Score

This educational model uses 800 AU as an upper reference point:

Training Load Score =
100 - (Training Load / 800 × 100)

Values below zero are clipped to zero.

## Combined Readiness

The readiness model uses:

- Wellness = 70%
- Training-load component = 30%

Formula:

Readiness =
(Wellness % × 0.70)
+
(Load Score × 0.30)

## Readiness Categories

| Score | Category |
|---:|---|
| ≥ 85% | High Readiness |
| 70–84.9% | Moderate Readiness |
| 55–69.9% | Low Readiness |
| < 55% | Very Low Readiness |

## Dataset

The included dataset contains 20 synthetic athlete-monitoring observations from four athletes.

Variables:

| Variable | Description |
|---|---|
| Athlete | Athlete identifier |
| Date | Monitoring date |
| Sleep | 1–5 rating |
| Soreness | 1–5 rating |
| Fatigue | 1–5 rating |
| Stress | 1–5 rating |
| Mood | 1–5 rating |
| Training_Load | Session training load in AU |

## Technologies

- Python
- Pandas
- CSV
- Functions
- Lambda functions
- DataFrames
- GroupBy
- Aggregation
- Sorting
- Data processing

## Installation

Install Pandas:

```bash
pip install pandas
---