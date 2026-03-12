import pandas as pd

# load dataset
df = pd.read_csv("startups_dataset.csv")

# extract startup names
startups = df["Startup Name"].dropna().unique()

# save them to file
with open("startups.txt", "w", encoding="utf-8") as f:
    for startup in startups:
        f.write(startup.strip() + "\n")

print("Startup names extracted successfully.")
print(f"Total startups found: {len(startups)}")