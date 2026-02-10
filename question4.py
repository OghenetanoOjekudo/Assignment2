import pandas as pd

def main():
    # I loaded the CSV file into a pandas DataFrame
    df = pd.read_csv("student.csv")

    # I created a filter using the conditions from the assignment
    highEngagementFilter = (
        (df["studytime"] >= 3) &
        (df["internet"] == 1) &
        (df["absences"] <= 5)
    )

    # I applied the filter to get only the high engagement students
    highEngagement = df[highEngagementFilter].copy()

    # I saved the filtered data into a new CSV file (without the index column)
    highEngagement.to_csv("high_engagement.csv", index=False)

    # I calculated how many students were saved
    numSaved = len(highEngagement)

    # I calculated the average grade (only if at least one student matched)
    if numSaved > 0:
        avgGrade = highEngagement["grade"].mean()
        print("Number of students saved:", numSaved)
        print("Average grade:", avgGrade)
    else:
        print("Number of students saved:", numSaved)
        print("Average grade: N/A (no students matched the filter)")

if __name__ == "__main__":
    main()
