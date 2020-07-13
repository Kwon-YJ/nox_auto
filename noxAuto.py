# -*- coding: utf-8 -*- 
import pyautogui
import time


'''
# all process kill
pyautogui.click(x = 2220, y = 500, clicks=1)

# home button
pyautogui.click(x = 2220, y = 1350, clicks=1)
'''


# ckick_ = pyautogui.click(x = 2248, y = 448,clicks=1,interval=1)
# 네이처 스크롤 = 12
# 칠성 첫번째 스크롤 = 8
# 칠성 두번째 스크롤 = 11
# 아이템 매니아 스크롤 = 12


def scroll_down(number):
    time.sleep(2.5)
    for i in range(number):
        time.sleep(0.6)
        pyautogui.scroll(-100)

def click_folder(num):
    if num == 1:
        pyautogui.click(x = 1250, y = 418, clicks=1)
    if num == 2:
        pyautogui.click(x = 1550, y = 418, clicks=1)
    if num == 3:
        pyautogui.click(x = 1850, y = 418, clicks=1)
    if num == 4:
        pyautogui.click(x = 350, y = 650, clicks=1)
    else:
        print('err!')
        
def click_file(num):
    if num == 1:
        pyautogui.click(x = 850, y = 600, clicks=1)
    if num == 2:
        pyautogui.click(x = 1100, y = 600, clicks=1)
    if num == 3:
        pyautogui.click(x = 1350, y = 600, clicks=1)
    if num == 4:
        pyautogui.click(x = 850, y = 770, clicks=1)
    if num == 5:
        pyautogui.click(x = 1100, y = 770, clicks=1)
    if num == 6:
        pyautogui.click(x = 1350, y = 770, clicks=1)
    else:
        print('err!')

def exit_app():
    pyautogui.click(x = 2220, y = 500, clicks=1)







# 1. 네이처 컬렉션
click_folder(1)
click_file(1)
pyautogui.click(x = 1438, y = 1280, clicks=1)
pyautogui.click(x = 743, y = 113, clicks=1)
pyautogui.click(x = 811, y = 1117, clicks=1)
scroll_down(12)
pyautogui.click(x = 1066, y = 883, clicks=1)
pyautogui.click(x = 1265, y = 798, clicks=1)
pyautogui.click(x = 1331, y = 798, clicks=1)
exit_app()

# 2. MyBN
click_folder(1)
click_file(2)
exit_app()

# 3. 립합
click_folder(1)
click_file(3)
exit_app()

# 4. 교보문고
click_folder(1)
click_file(4)
pyautogui.click(x = 1225, y = 972, clicks=1)
pyautogui.click(x = 945, y = 844, clicks=1)
exit_app()
'''미완'''


# 5. 예스24NEB
click_folder(1)
click_file(5)
pyautogui.click(x = 736, y = 111, clicks=1)
pyautogui.click(x = 811, y = 555, clicks=1)
pyautogui.click(x = 1085, y = 1252, clicks=1)
exit_app()
'''미완'''

# 1. 하이마트
click_folder(2)
click_file(1)
pyautogui.click(x = 1263, y = 1093, clicks=1)
pyautogui.click(x = 790, y = 793, clicks=1)
pyautogui.click(x = 1280, y = 223, clicks=1)
pyautogui.click(x = 1093, y = 823, clicks=1)
pyautogui.click(x = 1112, y = 1054, clicks=1)
exit_app()

# 2. 칠성몰
click_folder(2)
click_file(2)
pyautogui.click(x = 1440, y = 204, clicks=1)
pyautogui.click(x = 1151, y = 1002, clicks=1)
pyautogui.click(x = 1097, y = 1121, clicks=1)
pyautogui.click(x = 1198, y = 873, clicks=1)
pyautogui.click(x = 1085, y = 1252, clicks=1)
exit_app()
'''스크롤'''


# 3. HPoint
click_folder(2)
click_file(3)
pyautogui.click(x = 1110, y = 1400, clicks=1)
pyautogui.click(x = 1087, y = 731, clicks=1)
'''미완'''
exit_app()

# 4. 아이템매니아
click_folder(2)
click_file(4)
pyautogui.click(x = 1280, y = 849, clicks=1)
pyautogui.click(x = 1077, y = 1272, clicks=1)
'''미완'''
exit_app()

# 5. 티몬
click_folder(2)
click_file(5)
pyautogui.click(x = 1289, y = 1401, clicks=1)
pyautogui.click(x = 950, y = 851, clicks=1)
pyautogui.click(x = 1381, y = 787, clicks=1)
pyautogui.click(x = 802, y = 613, clicks=1)
pyautogui.click(x = 1107, y = 674, clicks=1)
pyautogui.click(x = 984, y = 857, clicks=1)
exit_app()

# 6. 해피머니
click_folder(2)
click_file(6)
pyautogui.click(x = 1285, y = 1194, clicks=1)
pyautogui.click(x = 1441, y = 128, clicks=1)
pyautogui.click(x = 1310, y = 223, clicks=1)
pyautogui.click(x = 1409, y = 505, clicks=1)
pyautogui.click(x = 860, y = 581, clicks=1)
pyautogui.click(x = 1377, y = 353, clicks=1)
exit_app()

# 1. 지마켓
click_folder(3)
click_file(1)
pyautogui.click(x = 790, y = 666, clicks=1)
pyautogui.click(x = 1009, y = 189, clicks=1)
pyautogui.click(x = 1102, y = 656, clicks=1)
pyautogui.click(x = 1100, y = 959, clicks=1)
exit_app()

# 2. 인터파크
click_folder(3)
click_file(2)
pyautogui.click(x = 1384, y = 1050, clicks=1)
pyautogui.click(x = 951, y = 783, clicks=1)
pyautogui.click(x = 1040, y = 1315, clicks=1)
'''미완'''
exit_app()

# 3. 인터파크 투어
click_folder(3)
click_file(3)
pyautogui.click(x = 1214, y = 1063, clicks=1)
pyautogui.click(x = 1411, y = 1057, clicks=1)
pyautogui.click(x = 1095, y = 473, clicks=1)
exit_app()

# 4. 인터파크 도서
click_folder(3)
click_file(4)
pyautogui.click(x = 925, y = 757, clicks=1)
pyautogui.click(x = 1249, y = 585, clicks=1)
exit_app()

# 5. 지9
click_folder(3)
click_file(5)
pyautogui.click(x = 1457, y = 1405, clicks=1)
pyautogui.click(x = 1248, y = 341, clicks=1)
pyautogui.click(x = 1106, y = 731, clicks=1)
exit_app()

# 6. 해피포인트
click_folder(3)
click_file(6)
pyautogui.click(x = 753, y = 136, clicks=1)
pyautogui.click(x = 1277, y = 227, clicks=1)
pyautogui.click(x = 1436, y = 944, clicks=1)
pyautogui.click(x = 865, y = 1034, clicks=1)
pyautogui.click(x = 1103, y = 1086, clicks=1)
exit_app()

# 1. CJ 더마켓
click_folder(4)
click_file(1)
pyautogui.click(x = 940, y = 1289, clicks=1)
'''미완'''
exit_app()
