#1---布
#2---石头
#3---剪刀
import random
computer = random.randint(1,3)
player = int(input('请输入:1---布 2---石头 3---剪刀'))
if (player == 1 and computer) or (player == 2 and computer == 3) or (player ==  3 and computer == 1):
	print('玩家胜')
elif player == computer:
	print('平局')
else:
	print('电脑赢了')
