import pandas as pd


print("=" * 75)
print("                ATHLETE READINESS ANALYZER")
print("=" * 75)


# ------------------------------------------
# Load Data
# ------------------------------------------

data = pd.read_csv("athlete_readiness_data.csv")

data["Date"] = pd.to_datetime(data["Date"])


# ------------------------------------------
# Wellness Score
# ------------------------------------------

def calculate_wellness_score(
    sleep,
    soreness,
    fatigue,
    stress,
    mood
):
    return (
        sleep
        + (6 - soreness)
        + (6 - fatigue)
        + (6 - stress)
        + mood
    )


# ------------------------------------------
# Readiness Classification
# ------------------------------------------

def classify_readiness(score):

    if score >= 85:
        return "High Readiness"

    elif score >= 70:
        return "Moderate Readiness"

    elif score >= 55:
        return "Low Readiness"

    else:
        return "Very Low Readiness"


# ------------------------------------------
# Calculate Wellness
# ------------------------------------------

data["Wellness_Score"] = data.apply(
    lambda row: calculate_wellness_score(
        row["Sleep"],
        row["Soreness"],
        row["Fatigue"],
        row["Stress"],
        row["Mood"]
    ),
    axis=1
)


# ------------------------------------------
# Wellness Percentage
# ------------------------------------------

data["Wellness_Percent"] = (
    data["Wellness_Score"] / 25
) * 100


# ------------------------------------------
# Training Load Score
# ------------------------------------------
# Educational model:
# 800 AU represents the upper reference point.
# Higher training load = lower load score.

data["Load_Score"] = (
    100 - (data["Training_Load"] / 800 * 100)
).clip(lower=0)


# ------------------------------------------
# Combined Readiness Score
# ------------------------------------------
# Wellness = 70%
# Training-load component = 30%

data["Readiness_Score"] = (
    data["Wellness_Percent"] * 0.70
    + data["Load_Score"] * 0.30
)


# ------------------------------------------
# Readiness Category
# ------------------------------------------

data["Readiness_Category"] = (
    data["Readiness_Score"]
    .apply(classify_readiness)
)


# ------------------------------------------
# Daily Results
# ------------------------------------------

print("\n" + "=" * 75)
print("DAILY READINESS RESULTS")
print("=" * 75)

display_columns = [
    "Athlete",
    "Date",
    "Wellness_Score",
    "Training_Load",
    "Wellness_Percent",
    "Load_Score",
    "Readiness_Score",
    "Readiness_Category"
]

print(
    data[display_columns].to_string(
        index=False,
        formatters={
            "Wellness_Percent": "{:.1f}%".format,
            "Load_Score": "{:.1f}".format,
            "Readiness_Score": "{:.1f}".format
        }
    )
)


# ------------------------------------------
# Athlete Summary
# ------------------------------------------

athlete_summary = (
    data.groupby("Athlete")
    .agg(
        Sessions=("Athlete", "count"),
        Average_Wellness=("Wellness_Score", "mean"),
        Average_Training_Load=("Training_Load", "mean"),
        Average_Readiness=("Readiness_Score", "mean"),
        Minimum_Readiness=("Readiness_Score", "min"),
        Maximum_Readiness=("Readiness_Score", "max")
    )
    .reset_index()
)


print("\n" + "=" * 75)
print("ATHLETE READINESS SUMMARY")
print("=" * 75)

print(
    athlete_summary.to_string(
        index=False,
        formatters={
            "Average_Wellness": "{:.1f}".format,
            "Average_Training_Load": "{:.1f}".format,
            "Average_Readiness": "{:.1f}%".format,
            "Minimum_Readiness": "{:.1f}%".format,
            "Maximum_Readiness": "{:.1f}%".format
        }
    )
)


# ------------------------------------------
# Athlete Ranking
# ------------------------------------------

ranking = athlete_summary.sort_values(
    "Average_Readiness",
    ascending=False
)


print("\n" + "=" * 75)
print("ATHLETE READINESS RANKING")
print("=" * 75)

for position, (_, athlete) in enumerate(
    ranking.iterrows(),
    start=1
):

    print(
        f"{position}. "
        f"{athlete['Athlete']:<10} "
        f"{athlete['Average_Readiness']:.1f}%"
    )


# ------------------------------------------
# Team Summary
# ------------------------------------------

team_wellness = data["Wellness_Score"].mean()

team_training_load = data["Training_Load"].mean()

team_readiness = data["Readiness_Score"].mean()


print("\n" + "=" * 75)
print("TEAM READINESS SUMMARY")
print("=" * 75)

print(
    f"Average Wellness Score : "
    f"{team_wellness:.1f}/25"
)

print(
    f"Average Training Load  : "
    f"{team_training_load:.1f} AU"
)

print(
    f"Average Team Readiness : "
    f"{team_readiness:.1f}%"
)


# ------------------------------------------
# Readiness Distribution
# ------------------------------------------

distribution = (
    data["Readiness_Category"]
    .value_counts()
)


print("\n" + "=" * 75)
print("READINESS DISTRIBUTION")
print("=" * 75)

for category, count in distribution.items():

    print(
        f"{category:<20} : "
        f"{count} sessions"
    )


# ------------------------------------------
# Lowest Readiness Session
# ------------------------------------------

lowest = data.loc[
    data["Readiness_Score"].idxmin()
]


print("\n" + "=" * 75)
print("LOWEST READINESS SESSION")
print("=" * 75)

print(f"Athlete   : {lowest['Athlete']}")
print(f"Date      : {lowest['Date'].date()}")
print(f"Readiness : {lowest['Readiness_Score']:.1f}%")
print(f"Category  : {lowest['Readiness_Category']}")


# ------------------------------------------
# Export Results
# ------------------------------------------

data.to_csv(
    "athlete_readiness_results.csv",
    index=False
)

athlete_summary.to_csv(
    "athlete_readiness_summary.csv",
    index=False
)


# ------------------------------------------
# Final Output
# ------------------------------------------

print("\n" + "=" * 75)
print("ANALYSIS COMPLETE")
print("=" * 75)

print("Files created:")
print("1. athlete_readiness_results.csv")
print("2. athlete_readiness_summary.csv")

print("\n" + "=" * 75)
print("MONITOR • ANALYZE • RECOVER • PERFORM")
print("=" * 75)