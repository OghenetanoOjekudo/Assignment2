import pandas as pd

def main():
    # I loaded the crime dataset into a DataFrame
    df = pd.read_csv("crime.csv")

    # I created the risk category based on ViolentCrimesPerPop
    df["risk"] = df["ViolentCrimesPerPop"].apply(
        lambda v: "HighCrime" if v >= 0.50 else "LowCrime"
    )

    # I grouped by risk and calculated the average unemployment rate
    avgUnemploymentByRisk = df.groupby("risk")["PctUnemployed"].mean()

    # I printed the results in a clear format
    highCrimeAvg = avgUnemploymentByRisk.get("HighCrime")
    lowCrimeAvg = avgUnemploymentByRisk.get("LowCrime")

    print("Average PctUnemployed by risk group:")
    print(f"HighCrime: {highCrimeAvg}")
    print(f"LowCrime: {lowCrimeAvg}")

if __name__ == "__main__":
    main()
