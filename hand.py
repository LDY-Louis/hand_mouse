import cv2
import mediapipe as mp
import pyautogui
import pyautogui as patg
import keyboard

patg.FAILSAFE = False
cap = cv2.VideoCapture(0)  # 调用摄像头
mphands = mp.solutions.hands
hands_solution = mphands.Hands(max_num_hands=1)  # 限制检测手的数量
Draw = mp.solutions.drawing_utils
handstyle = Draw.DrawingSpec(color=(0, 0, 255), thickness=3)  # 指定的特征点的样式
linestyle = Draw.DrawingSpec(color=(0, 255, 0), thickness=5)  # 指定连接线的样式
screenWidth, screenHeight = patg.size()  # 获取屏幕分辨率
size = (screenWidth, screenHeight)  # 得到屏幕分辨率元组
move = []
move1 = []
angle = []
size1 = ()
v1 = []
v2 = []  # 判断中指形态
v3 = []
v4 = []  # 判断无名指形态
v5 = []
v6 = []  # 判断小指形态
v7 = []
v8 = []  # 判断食指形态
t = 'no action'
z = ('左键点击：伸出中指，并弯曲无名指和小指\n右键点击：伸直中指、无名指和小指\n双击左键：伸直中指、无名指，并弯曲小指\nCtrl+a：伸直食指和小指\n'
     'Ctrl+c：伸直小指并弯曲食指\nCtrl+v：伸直中指和小指，弯曲无名指\n按 Q 键退出')
print(z)

while True:
    ret, img = cap.read()
    if ret:  # 摄像头是否开启正确

        img = cv2.flip(img, 1)
        imgHeight = img.shape[0]  # 获取视窗高度
        imgWidth = img.shape[1]  # 获取视窗宽度
        size1 = (imgWidth, imgHeight)  # 为之后的重新转换视窗大小做准备
        mpimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 将通过opencv采集到的图片从BRG格式转换为可读的RGB格式
        img = cv2.resize(img, size)  # 让窗口与屏幕分辨率相同
        result = hands_solution.process(mpimg)  # 检测画面中是否有手出现

        if result.multi_hand_landmarks:  # 手部特征点是否存在
            for i in result.multi_hand_landmarks:
                Draw.draw_landmarks(img, i, mphands.HAND_CONNECTIONS, handstyle, linestyle)  # 在画面中标出特征点并连接
                for j, lm in enumerate(i.landmark):  # 打印21个特征点的坐标
                    if j == 0:
                        v1.append([lm.x, lm.y])
                        v2.append([lm.x, lm.y])
                        v3.append([lm.x, lm.y])
                        v4.append([lm.x, lm.y])
                        v5.append([lm.x, lm.y])
                        v6.append([lm.x, lm.y])
                        v7.append([lm.x, lm.y])
                        v8.append([lm.x, lm.y])
                    elif j == 6:
                        v7.append([lm.x, lm.y])
                    elif j == 8:
                        v8.append([lm.x, lm.y])
                    elif j == 10:
                        v1.append([lm.x, lm.y])
                    elif j == 12:
                        v2.append([lm.x, lm.y])
                    elif j == 14:
                        v3.append([lm.x, lm.y])
                    elif j == 16:
                        v4.append([lm.x, lm.y])
                    elif j == 18:
                        v5.append([lm.x, lm.y])
                    elif j == 20:
                        v6.append([lm.x, lm.y])
                    if j == 8:  # 使用食指指尖作为控制鼠标移动的参数
                        move.append([lm.x, lm.y])

        l_0_10 = 0
        l_0_12 = 0
        l_0_14 = 0
        l_0_16 = 0
        l_0_18 = 0
        l_0_20 = 0
        l_0_6 = 0
        l_0_8 = 0
        if len(v1) == len(v2) == 2:
            l_0_10 = (v1[0][0] - v1[1][0]) ** 2 + (v1[0][1] - v1[1][1]) ** 2
            l_0_12 = (v2[0][0] - v2[1][0]) ** 2 + (v2[0][1] - v2[1][1]) ** 2
            v1.clear()
            v2.clear()
        if len(v3) == len(v4) == 2:
            l_0_14 = (v3[0][0] - v3[1][0]) ** 2 + (v3[0][1] - v3[1][1]) ** 2
            l_0_16 = (v4[0][0] - v4[1][0]) ** 2 + (v4[0][1] - v4[1][1]) ** 2
            v3.clear()
            v4.clear()
        if len(v5) == len(v6) == 2:
            l_0_18 = (v5[0][0] - v5[1][0]) ** 2 + (v5[0][1] - v5[1][1]) ** 2
            l_0_20 = (v6[0][0] - v6[1][0]) ** 2 + (v6[0][1] - v6[1][1]) ** 2
            v5.clear()
            v6.clear()
        if len(v7) == len(v8) == 2:
            l_0_6 = (v7[0][0] - v7[1][0]) ** 2 + (v7[0][1] - v7[1][1]) ** 2
            l_0_8 = (v8[0][0] - v8[1][0]) ** 2 + (v8[0][1] - v8[1][1]) ** 2
            v7.clear()
            v8.clear()


        if l_0_12 == l_0_10 and l_0_16 == l_0_14 and l_0_20 == l_0_18:
            t = 'no action'
        elif l_0_12 >= l_0_10 and l_0_16 >= l_0_14 and l_0_20 >= l_0_18:  # 中指、无名指和小指全部伸直，单击右键
            if t != 'click right':
                t = 'click right'
                c_x, c_y = pyautogui.position()
                pyautogui.click(c_x, c_y, button='right')
        elif l_0_12 >= l_0_10 and l_0_16 >= l_0_14 and l_0_20 <= l_0_18:  # 中指、无名指全部伸直，小指弯曲，双击左键
            if t != 'double click left':
                t = 'double click left'
                c_x, c_y = pyautogui.position()
                pyautogui.doubleClick(c_x, c_y, button='left')
        elif l_0_12 >= l_0_10 and l_0_16 <= l_0_14 and l_0_20 <= l_0_18:  # 中指伸直，无名指、小指弯曲，单击左键
            if t != 'click left':
                t = 'click left'
                c_x, c_y = pyautogui.position()
                pyautogui.click(c_x, c_y, button='left')

        elif l_0_12 <= l_0_10 and l_0_16 <= l_0_14 and l_0_20 >= l_0_18 and l_0_8 >= l_0_6:  # 中指、无名指弯曲，小指、食指伸直
            if t != 'ctrl+a':
                t = 'ctrl+a'
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('a')
                pyautogui.keyUp('a')
                pyautogui.keyUp('ctrl')
        elif l_0_12 <= l_0_10 and l_0_16 <= l_0_14 and l_0_20 >= l_0_18:  # 中指、无名指弯曲，小指伸直
            if t != 'ctrl+c':
                t = 'ctrl+c'
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('c')
                pyautogui.keyUp('c')
                pyautogui.keyUp('ctrl')
        elif l_0_12 >= l_0_10 and l_0_16 <= l_0_14 and l_0_20 >= l_0_18:  # 中指、小指伸直，无名指弯曲
            if t != 'ctrl+v':
                t = 'ctrl+v'
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('v')
                pyautogui.keyUp('v')
                pyautogui.keyUp('ctrl')
        elif l_0_12 <= l_0_10 and l_0_16 <= l_0_14 and l_0_20 <= l_0_18:  # 中指，无名指、小指弯曲
            t = 'no action'

        if len(move) == 2:  # 两帧进行一次移动
            x = move[0][0]
            y = move[0][1]
            move.clear()
            patg.moveTo(1.5 * x * screenWidth, 1.5 * y * screenHeight, 0.0001)  # 使用绝对坐标进行移动，可以有效实现降噪，提高稳定性，减小抖动影响

        cv2.putText(img, t, (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1, color=(0, 0, 255), thickness=3)
        img = cv2.resize(img, size1)  # 将窗口缩小为
        cv2.imshow('img', img)  # 将这一帧处理好的图片放到指定窗口
        cv2.waitKey(1)
        if keyboard.is_pressed('q'):
            break