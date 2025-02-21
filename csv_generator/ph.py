import csv
import random
import os
import time
from tqdm import tqdm  # Import tqdm for progress bar (tqdm 임포트트)

# CSV file name and save path (CSV 파일명 및 저장 경로)
folder_path = "C:/"  # Enter the desired folder path here (저장 경로 입력력)
filename = os.path.join(folder_path, "pH.csv")
num_records = 236870 # Number of records to generate (생성할 레코드 수수)

# Create the folder if it doesn't exist (폴더가 존재하지 않으면 생성성)
os.makedirs(folder_path, exist_ok=True)

# Record the start time of the task (작업 시작 시간 기록록)
start_time = time.time()
print(f"Start time: {time.ctime(start_time)}")

# Create CSV file (CSV 파일 생성성)
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "PH_1", "PH_2", "PH_3", "PH_4", "PH_5", "PH_6", "PH_7", "PH_8", "PH_9", "PH_10", "PH_11", "PH_12", "PH_13", "PH_14", "PH_15", "PH_16", "PH_17", "PH_18", "PH_19", "PH_20", "PH_21", "PH_22", "PH_23", "PH_24", "PH_25", "PH_26", "PH_27", "PH_28", "PH_29", "PH_30",   
    ])
    
    # Use tqdm to show progress bar (tqdm을 사용해서 진행률 표시시)
    for _ in tqdm(range(num_records), desc="Generating Data", unit="record"):
        writer.writerow([
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
            round(random.uniform(0, 14.0), 2), 
        ])

# Record the end time of the task (작업 종료 시간 기록)
end_time = time.time()
print(f"End time: {time.ctime(end_time)}")

# Calculate the total time taken (총 소요 시간 계산)
elapsed_time = end_time - start_time
print(f"Total time taken: {elapsed_time:.2f} seconds")

print(f"{filename} file has been created")
