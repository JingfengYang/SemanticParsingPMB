from __future__ import unicode_literals, print_function, division
from io import open
import argparse

parser = argparse.ArgumentParser(description='Test')
parser.add_argument('-r1', type=int, default=1)
parser.add_argument('-r2', type=int, default=2)
parser.add_argument('-gold', type=str, default='dev.test')
args = parser.parse_args()

for idx in range(args.r1, args.r2):
	readerTest = open(str(idx)+'.test', 'r', encoding='utf-8')
	readerGold = open(args.gold, 'r', encoding='utf-8')
	linesTest = []
	linesGold = []
	sentence = []
	for line in readerTest:
		if line.strip() == '':
			linesTest.append(sentence)
			sentence = []
		else:
			sentence.append(line.strip())
	sentence = []
	for line in readerGold:
		if line.strip() == '':
			linesGold.append(sentence)
			sentence = []
		else:
			sentence.append(line.strip())
	readerTest.close()
	readerGold.close()

	totalGold = 0
	totalTest = 0
	right = 0
	if not len(linesTest) == len(linesGold):
		print(len(linesTest),len(linesGold))
	assert (len(linesTest) == len(linesGold))
	for i, (test, gold) in enumerate(zip(linesTest, linesGold)):
		testSet = set(test)
		goldSet = set(gold)
		rightSet = testSet.intersection(goldSet)
		totalGold += len(goldSet)
		totalTest += len(testSet)
		right += len(rightSet)

	precision = right / totalTest
	recall = right / totalGold
	print(str(idx)+': p %.10f, r: %.10f, f: %.10ff ' % (precision, recall, 2 * precision * recall / (precision + recall)))

