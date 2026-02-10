import pandas as pd

def main():
    # I loaded the student dataset into a DataFrame
    df = pd.read_csv("student.csv")

    # I created grade_band based on the rules in the assignment
    # Low: grade <= 9, Medium: 10-14, High: >= 15
    def assign_band(grade):
        if grade <= 9:
            return "Low"
        elif grade <= 14:
            return "Medium"
        else:
            return "High"

    df["grade_band"] = df["grade"].apply(assign_band)

    # I grouped by grade_band to compute summary statistics
    summary = df.groupby("grade_band").agg(
        num_students=("grade", "count"),
        avg_absences=("absences", "mean"),
        pct_internet=("internet", "mean")  # mean of 0/1 gives proportion
    )

    # I converted the internet proportion into a percentage
    summary["pct_internet"] = summary["pct_internet"] * 100

    # I reset the index so grade_band becomes a regular column in the saved CSV
    summary = summary.reset_index()

    # I saved the grouped summary table to a CSV file
    summary.to_csv("student_bands.csv", index=False)

    # I printed the summary so I can visually confirm it looks correct
    print(summary)

if __name__ == "__main__":
    main()
