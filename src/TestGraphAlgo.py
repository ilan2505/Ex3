import unittest
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase, GraphAlgo):

    def test_center(self):

        self.Algo = GraphAlgo()
        self.Algo.load_from_json('../data/A1.json')
        self.assertEqual(self.Algo.centerPoint(), (8, 9.925289024973141))

    def test_TSP(self):
        self.Algo = GraphAlgo()
        self.Algo.load_from_json('../data/A1.json')
        self.assertEqual(self.Algo.TSP([1,2,3]), ([1,2,3], 2.8647559158521916))

    def test_shorted_path(self):
        self.Algo = GraphAlgo()
        self.Algo.load_from_json('../data/A1.json')
        self.assertEqual(self.Algo.shortest_path(1,8), (6.204771159825874, [1, 2, 6, 7, 8]))


if __name__ == '__main__':
    MyTestCase()
    pass
