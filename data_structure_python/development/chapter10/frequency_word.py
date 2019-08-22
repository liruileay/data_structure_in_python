def frequency(filename):
	freq = {}
	for piece in open(filename, encoding='utf-8').read().lower().split():
		word = ''.join(c for c in piece if c.isalpha())
		if word:
			freq[word] = 1 + freq.get(word, 0)
	max_word = 0
	max_count = 0
	for item in freq:
		if freq[item] > max_count:
			max_word = item
			max_count = freq[item]

	print(f'出现频率最高的是{max_word}')
	print(f'{max_word}出现的次数是{max_count}')


frequency('./frequency_word.py')
