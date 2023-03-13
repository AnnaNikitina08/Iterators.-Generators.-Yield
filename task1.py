list_of_lists = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]


class FlatIterator:
	def __init__(self, list_of_list):
		self.list_of_list = list_of_list
		self.n = -1

	def __iter__(self):
		self.list = []
		self.iter = iter(self.list)
		for elem in self.list_of_list:
			self.list.extend(elem)
		return self

	def __next__(self):
		self.n += 1
		if self.n == len(self.list):
			raise StopIteration
		return next(self.iter)


for item in FlatIterator(list_of_lists):
	print(item)

flat_list = [item for item in FlatIterator(list_of_lists)]
print(flat_list)


def test_1():
	list_of_lists_1 = [
         ['a', 'b', 'c'],
         ['d', 'e', 'f', 'h', False],
         [1, 2, None]
         ]

	for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
        ):
		assert flat_iterator_item == check_item

	assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
	test_1()
