import pandas as pd
import sys
import os
from PIL import Image

for i in range(20000):  
    
    file = f'your_file_name{i}.png'
    if os.path.isfile(file):
        df = pd.read_table(f'./your_file_name{i}.txt',sep=' ')

        val=list(df.columns)
        try:           # 예외사항이 발생하면 넘기기 위해 continue 사용
            val=list(map(float, val))
        except:
            continue
        val[1]=1-val[1]  # y 축 대칭 변환.

        sys.stdout = open(f"WIN_20210512_11_33_22_Pro.mp4_00000{i}_rev.txt",'w')
        print(int(val[0]),end=' ')
        print(val[1],end=' ')
        print(val[2],end=' ')
        print(val[3],end=' ')
        print(val[4])    # 여기서는 공백만들면 yolo가 인식못함, 소수점 6자리가 아니여도 괜찮음

        image = Image.open(f"your_file_name{i}.PNG")

            # image.show()
        FlipImage = image.transpose(Image.FLIP_LEFT_RIGHT)
        

        FlipImage.save(f"your_file_name{i}_rev.png",'png')
    else:
        continue