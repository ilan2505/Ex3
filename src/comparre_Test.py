import unittest

from Ex3.src.GraphAlgo import GraphAlgo




class MyTestCase(unittest.TestCase):

    def test_center(self):

        self.Algo = GraphAlgo()
        self.Algo.load_from_json('../data/A1.json')
        self.Algo.centerPoint()

    def test_TSP(self):
        self.Algo = GraphAlgo()
        self.Algo.load_from_json('../data/1000Nodes.json')
        self.Algo.TSP([1, 2, 3])

    def test_shorted_path(self):
        self.Algo = GraphAlgo()
        self.Algo.load_from_json('../data/1000Nodes.json')
        self.Algo.shortest_path(1, 8)


if __name__ == '__main__':
    unittest.main()
