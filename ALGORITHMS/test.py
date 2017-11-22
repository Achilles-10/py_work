import unittest

from insertion_sort import *
from bubble_sort import *
from selection_sort import *
from merge_sort import *
from quick_sort import *


class SortsTestCase(unittest.TestCase):
	"""test all these algorithms"""

	def test_insertion_sort(self):
		list = [3, 1, 4, 5, 9, 2, 6, 8, 7]
		insertion_sort_ascend(list)
		self.assertEqual(list, [1, 2, 3, 4, 5, 6, 7, 8, 9])

	def test_merge_sort(self):
		list = [3, 1, 4, 5, 9, 2, 6, 8, 7]
		list = merge_sort_ascend(list)
		self.assertEqual(list, [1, 2, 3, 4, 5, 6, 7, 8, 9])

	def test_bubble_sort(self):
		list = [3, 1, 4, 5, 9, 2, 6, 8, 7]
		bubble_sort_ascend(list)
		self.assertEqual(list, [1, 2, 3, 4, 5, 6, 7, 8, 9])

	def test_selection_sort(self):
		list = [3, 1, 4, 5, 9, 2, 6, 8, 7]
		selection_sort_ascend(list)
		self.assertEqual(list, [1, 2, 3, 4, 5, 6, 7, 8, 9])

	def test_quick_sort(self):
		list = [3, 1, 4, 5, 9, 2, 6, 8, 7]
		qucik_sort_ascend(list, 0, 8)
		self.assertEqual(list, [1, 2, 3, 4, 5, 6, 7, 8, 9])


unittest.main()
