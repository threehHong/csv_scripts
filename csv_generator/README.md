# CSV Data Generator for pH Values

This script generates a CSV file containing simulated pH data. The file is named `pH.csv` and is stored in the specified folder path. The script uses the `random` library to generate random pH values between 0 and 14 (with two decimal places) for 30 columns, and creates a specified number of records.

### Features:

- Generates random pH values between 0 and 14.
- The script uses a progress bar (`tqdm`) to show the progress of data generation.
- The number of records to generate is configurable.

### How to Use:

1. Set the desired folder path where the CSV file will be stored (replace `"C:/"` in the `folder_path` variable).
2. Set the number of records to generate by changing the `num_records` variable.
3. Run the script, and the CSV file will be created in the specified folder.

### Example:

```python
folder_path = "C:/"
filename = os.path.join(folder_path, "pH.csv")
num_records = 236870
```

### Requirements:

- Python 3.x
- Libraries: `csv`, `random`, `os`, `time`, `tqdm`(pip install tqdm)

<br>

<br>

# pH 값 CSV 데이터 생성기

이 스크립트는 시뮬레이션된 pH 데이터를 포함하는 CSV 파일을 생성합니다. 파일 이름은 `pH.csv`이며 지정된 폴더 경로에 저장됩니다. 이 스크립트는 `random` 라이브러리를 사용하여 0과 14 사이의 무작위 pH 값을 생성하며(소수점 2자리), 30개의 열에 대해 지정된 수의 레코드를 생성합니다.

### 주요 기능:

- 0과 14 사이의 무작위 pH 값 생성.
- 데이터 생성 진행 상황을 표시하기 위해 `tqdm` 라이브러리를 사용하여 진행률 표시.
- 생성할 레코드 수는 설정 가능합니다.

### 사용 방법:

1. CSV 파일이 저장될 폴더 경로를 원하는 경로로 설정합니다 (예: `"C:/"`를 `folder_path` 변수에 지정).
2. 생성할 레코드 수를 `num_records` 변수로 설정합니다.
3. 스크립트를 실행하면 지정된 폴더에 CSV 파일이 생성됩니다.

### 예시:

```python
folder_path = "C:/"
filename = os.path.join(folder_path, "pH.csv")
num_records = 236870
```

### 필요 사항:

- Python 3.x
- 필요한 라이브러리: `csv`, `random`, `os`, `time`, `tqdm`(pip install tqdm)
