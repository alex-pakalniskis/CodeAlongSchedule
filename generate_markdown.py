import pandas as pd
from config import *

def generate():
    try:
        # Read downloaded data
        df = pd.read_csv(schedule_local_csv_name)
        df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y").dt.date

        # Filter session data by before/after today
        past_sessions = df[df["Date"] < today].copy().reset_index()
        upcoming_sessions = df[df["Date"] >= today].copy().reset_index()

        # Populate speaker info
        markdown = ""
        for ms in markdown_strings_speaker_info:
            markdown += ms

        # Add upcoming sessions data
        markdown += f"""## Upcoming sessions\n"""
        markdown += f"""\n"""
        markdown += f"""| Day | Time | Topic | \n"""
        markdown += f"""| --- | --- | --- | \n"""
        
        for _ , row in upcoming_sessions.iterrows():
            markdown += f"""| {row["Date"]} | {row["Time"]} | [{row["Topic"]}]({row["Link"]}) | \n"""
        markdown += f"""\n"""

        # Add repo information
        for ms in markdown_strings_multisession_repos:
            markdown += ms

        # Add make a suggestion information
        for ms in markdown_strings_request_content:
            markdown += ms

        # Add past sessions data
        markdown += f"""## Past sessions\n"""
        markdown += f"""\n"""
        markdown += f"""| Day | Time | Topic | \n"""
        markdown += f"""| --- | --- | --- | \n"""

        for _ , row in past_sessions.iterrows():
            markdown += f"""| {row["Date"]} | {row["Time"]} | [{row["Topic"]}]({row["Link"]}) | \n"""
        markdown += f"""\n"""

        # Save markdown file
        with open(schedule_local_markdown_name, "w") as f:
            f.write(markdown)


    except Exception as e:
        print(e)


def main():
    generate()

if __name__ == "__main__":
    main()
