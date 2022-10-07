import pandas as pd
from config import schedule_remote_csv_path, schedule_local_csv_name

def download():
    try:
        df = pd.read_csv(schedule_remote_csv_path)
        df.to_csv(schedule_local_csv_name, index=None)
    except Exception as e:
        print(e)

def main():
    download()

if __name__ == "__main__":
    main()
