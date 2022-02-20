# encoding:utf-8

# 逐字检查
def anagramSolution1(s1,s2):
	alist = list(s2)
	print(s1[0])
	pos1 = 0
	stillOK = True
	while pos1 < len(s1) and stillOK:
		pos2 = 0
		found = False
		while pos2 < len(alist) and not found:
			if s1[pos1] == alist[pos2]:
				found = True
			else:
				pos2 = pos2 + 1
		if found:
			alist[pos2] = None
		else:
			stillOK = False
		pos1 = pos1 + 1
	return stillOK

	'''
	外层循环遍历s1个字符，将内层循环执行n次
	O(n2)

	'''

# 排序比较

def anagramSolution2(s1,s2):
	alist1 = list(s1)
	alist2 = list(s2)

	alist1.sort()
	alist2.sort()
	pos = 0
	matches = True
	while pos < len(s1) and matches:
		if alist1[pos] == alist2[pos]:
			pos = pos + 1
		else:
			matches = False
	return matches

'''
O(nlogn)
'''

# 计数比较
# 对比两个词中每个字母出现的次数，如果26个字母出现的次数都相同个，两个字符为变位词
def anagramSolution3(s1,s2):
	c1 = [0] * 26
	c2 = [0] * 26
	print(c1,c2)
	for i in range(len(s1)):
		pos = ord(s1[i]) - ord('a')
		c1[pos] = c1[pos] + 1
	for i in range(len(s2)):
		pos = ord(s2[i]) - ord('a')
		c2[pos] = c2[pos] + 1
	print(c1,c2)
	j = 0
	stillOK = True
	while j < 26 and stillOK:
		if c1[j] == c2[j]:
			j = j + 1
		else:
			stillOK = False
	return stillOK

	'''
	T(n) = 2n + 26
	O(n)
	本算法依赖两个长度26的计数器，更需要存储空间，
	牺牲存储空间换取运行时间。
	'''

if __name__ == "__main__":
	value = anagramSolution1('abcd','dbca')
	print(value)

	value1 = anagramSolution2('abcd','dbca')
	print(value1)

	value2 = anagramSolution3('abc','cba')
	print(value2)












