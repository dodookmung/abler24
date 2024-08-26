import os
import shutil

# 원본 폴더 경로
Data_folder = r'D:\데이터_전처리\Validation\딸기_정상_Val\딸기\정상'
# 라벨링 폴더 경로
Label_folder = r'D:\데이터_전처리\Validation\딸기_라벨링데이터_Validation\정상'
# 복사 폴더 경로
Data_copy_folder = r'D:\데이터_전처리\Validation\Nomal_validation'
# 라벨링 폴더 복사 경로
Label_copy_folder = r'D:\데이터_전처리\Validation\Label_validation\Nomal'

# 폴더 생성
if not os.path.exists(Data_copy_folder):
    os.makedirs(Data_copy_folder)
if not os.path.exists(Label_copy_folder):
    os.makedirs(Label_copy_folder)

# 파일 목록 PULL
file_list = os.listdir(Data_folder)
file_list1 = os.listdir(Label_folder)

# 솔팅 대상 파일 이름

#정상
file = "_1_0_0_1_" # 구성요소 3 4 5 6
# file = "_1_0_0_2_"
# file = "_1_0_0_3_"
# file = "_1_0_0_4_"
# file = "_1_0_0_5_"

# 잿빛곰팡이병
# file = "_1_1_a1_1_"
# file = "_1_1_a1_2_"
# file = "_1_1_a1_3_"
# file = "_1_1_a1_4_"
# file = "_1_1_a1_5_"

# 흰가루병
# file = "_1_1_a2_1_"
# file = "_1_1_a2_2_"
# file = "_1_1_a2_3_"
# file = "_1_1_a2_4_"
# file = "_1_1_a2_5_"


# 파일 셀렉
twelve_files = [f for f in file_list if file in f]
twelve_files1 = [f for f in file_list1 if os.path.splitext(f)[0] in twelve_files]
num_twelve_files = len(twelve_files)
print(f"해당 파일 개수: {num_twelve_files}")

# 1/50 비율 파일 복사
for i, file_name in enumerate(twelve_files):
    file_path, file_extension = os.path.splitext(file_name)
    if i % 50 == 0:
        try:
            Data_folder_path = os.path.join(Data_folder, file_name)
            Data_copy_folder_path = os.path.join(Data_copy_folder, file_name)
            shutil.copy(Data_folder_path, Data_copy_folder_path)
            print(f"파일 복사: {Data_folder_path} -> {Data_copy_folder_path}")
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {Data_folder_path}")
            continue

        try:
            Label_folder_path = os.path.join(Label_folder, file_path + '.json')
            Label_copy_folder_path = os.path.join(Label_copy_folder, file_path + '.json')
            shutil.copy(Label_folder_path, Label_copy_folder_path)
            print(f"파일 복사: {Label_folder_path} -> {Label_copy_folder_path}")
        except StopIteration:
            print(f"해당 파일을 찾을 수 없습니다: {Label_folder_path}")
            continue
