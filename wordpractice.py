import random
import glob



# CMD颜色
import ctypes,sys
STD_OUTPUT_HANDLE = -11
GREEN = 0x0a
RED = 0x0c
BLUE = 0x09
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool

def resetColor():
    set_cmd_text_color(RED | GREEN | BLUE)

def colorPrint(mess,color):
    set_cmd_text_color(color)
    print(mess)
    resetColor()




# 打印单词全信息
def show(arr):
    print(arr[0])
    for i in range(1,len(arr)):
        print(arr[i][0],end=':')
        print(','.join(arr[i][1]))




# 选择训练文件
def select():
    file_list=glob.glob('*.txt')
    leng=len(file_list)
    print('--------------------------------------------------------------------')
    print('--------------------------------------------------------------------')
    print('--------------------------- 选择训练章节 ---------------------------')
    for i in range(leng):
        print('{}.  {}'.format(i,file_list[i]))
    print('--------------------------------------------------------------------')
    print('--------------------------------------------------------------------')
    
    try:
        file_name=file_list[int(input('选择：'))]
    except:
        file_name=file_list[int(input('输入有误，重新输入：'))]
    print()
    return file_name




# 单词转换为数组
file_name=select()
wordalist=[]
with open(file_name) as f:
    while True:
        wordly=[]
        word = f.readline()[:-1]
        if word=='$':
            break
        wordly.append(word)
        while True:
            infos=[]
            info=f.readline()
            if info=='\n' or info=='':
                break
            lis=list(map(str,info.split()))

            infos.append(lis[0])
            infos.append(lis[1:])
            wordly.append(infos)
        wordalist.append(wordly)




# 训练部分
length_i=len(wordalist)
n=0;ok_num=0;error=0;
temp_word=[]
try:
    while True:
        note_length=len(temp_word)

        if note_length>4:   # 达到累计错误限度，开始复习
            for _ in range(note_length):
                i,j,k,l=temp_word[_]
                print(wordalist[i][j][k][l], '--->：')
                user = input()
                if user == wordalist[i][0]:
                    ok_num += 1
                    colorPrint('            ☜(ˆ▽ˆ)----bingo!',GREEN)
                    show(wordalist[i])
                elif user == 'now_rate':
                    print('{}%'.format(ok_num / n * 100))
                elif user=='delect':
                    wordalist.pop(i)
                    print('删除成功！')
                else:
                    error += 1
                    colorPrint('            ☹-----error!',RED)
                    show(wordalist[i])
                    while True:
                        if input('  请再拼写一遍：')==wordalist[i][0]:
                                                        break
                    point = [i, j, k, l]
                    temp_word.append(point)
                print()
                print()
                print()
            temp_word=[]

        # 正常训练
        n=n+1
        i=random.randint(0,length_i-1)

        length_j = len(wordalist[i])
        j=random.randint(1,length_j-1)

        length_k = len(wordalist[i][j])
        k=random.randint(1,length_k-1)

        length_l = len(wordalist[i][j][k])
        l=random.randint(0,length_l-1)

        print(wordalist[i][j][k][l],'--->：')
        user=input()
        if user==wordalist[i][0]:
            ok_num+=1
            colorPrint('            ☜(ˆ▽ˆ)----bingo!',GREEN)
            show(wordalist[i])
        elif user=='now_rate':
            print('{}%'.format(ok_num/n*100))
        elif user=='delect':
            wordalist.pop(i)
            print('删除成功！')
        else:
            error+=1
            colorPrint('            ☹-----error!',RED)
            show(wordalist[i])
            while True:
                if input('  请再拼写一遍：')==wordalist[i][0]:
                                        break
            point=[i,j,k,l]
            temp_word.append(point)
        print()
        print()
        print()
except:
    show(wordalist[i])
    input()






