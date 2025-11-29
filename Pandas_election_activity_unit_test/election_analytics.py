import pandas as pd
import matplotlib.pyplot as plt
import os

def load_election_data(filepath):
    """
    loads the csv data into a pandas dataframe.
    handles error if file is missing or format is wrong.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"error: the file '{filepath}' was not found.")

    # the data uses semicolons ';' as separators, not commas
    try:
        df = pd.read_csv(filepath, sep=';')
        return df
    except Exception as e:
        print(f"error reading csv: {e}")
        return None

def plot_candidate_histogram(df, candidate_name):
    """
    plots a histogram showing the distribution of vote fractions
    for a specific candidate across all recorded counties.
    """
    # filter data for the specific candidate
    subset = df[df['candidate'] == candidate_name]

    if subset.empty:
        print(f"no data found for candidate: {candidate_name}")
        return

    # plotting logic
    plt.figure(figsize=(10, 6))
    plt.hist(subset['fraction_votes'], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'distribution of vote share: {candidate_name}')
    plt.xlabel('fraction of votes (0.0 to 1.0)')
    plt.ylabel('frequency (count of counties)')
    plt.grid(axis='y', alpha=0.5)
    
    # save the plot to a file
    filename = f"{candidate_name.replace(' ', '_')}_histogram.png"
    plt.savefig(filename)
    print(f"histogram saved as {filename}")
    # plt.show() # uncomment if running locally with a screen

def compare_two_candidates(df, candidate1, candidate2):
    """
    compares the total votes of two candidates.
    """
    # group by candidate and sum their votes
    summary = df.groupby('candidate')['votes'].sum()

    if candidate1 not in summary or candidate2 not in summary:
        print("error: one or both candidates not found.")
        return

    votes1 = summary[candidate1]
    votes2 = summary[candidate2]

    print(f"\n--- comparison ---")
    print(f"{candidate1}: {votes1:,} votes")
    print(f"{candidate2}: {votes2:,} votes")
    
    if votes1 > votes2:
        print(f"leader: {candidate1}")
    else:
        print(f"leader: {candidate2}")

def main():
    # define file path
    csv_file = 'US-2016-primary.csv'
    
    # load data
    df = load_election_data(csv_file)
    
    if df is not None:
        print("data loaded successfully.")
        print(f"columns: {df.columns.tolist()}")
        
        # task 1: plot histogram for donald trump
        plot_candidate_histogram(df, "Donald Trump")
        
        # task 2: plot histogram for hillary clinton
        plot_candidate_histogram(df, "Hillary Clinton")

        # task 3: compare two candidates
        compare_two_candidates(df, "Bernie Sanders", "Hillary Clinton")

if __name__ == "__main__":
    main()