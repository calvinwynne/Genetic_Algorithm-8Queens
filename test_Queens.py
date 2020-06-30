import unittest
import Queens as master_queen



class test_GeneticQueen(unittest.TestCase):
    
    test_q1 = master_queen.Genetic_Queen(verbose=False, show_board=False, show_score=True)

    def test_populate(self):
        self.assertEqual(self.test_q1.populate([0, 0, 0, 0, 0, 0, 0, 0]), (0, [0, 0, 0, 0, 0, 0, 0, 0]))
        self.assertEqual(self.test_q1.populate([1, 2, 3, 4, 5, 6, 7, 8]), (28, [1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertEqual(self.test_q1.populate([1, 0, 3, 5, 0, 3, 7, 1]), (8, [1, 0, 3, 5, 0, 3, 7, 1]))
        self.assertEqual(self.test_q1.populate([1, 2, 3, 5, 5, 3, 7, 1]), (16, [1, 2, 3, 5, 5, 3, 7, 1]))
        self.assertEqual(self.test_q1.populate([1, 2, 3, 5, 5, 3, 4, 1]), (13, [1, 2, 3, 5, 5, 3, 4, 1]))
    

    def test_generateChromozomes(self):
        self.assertEqual(self.test_q1.generateChromozomes( ([28, [1, 2, 3, 4, 5, 6, 7, 8]], (8 , [1, 0, 3, 5, 0, 3, 7, 1]))  ), ((22, [1, 2, 3, 4, 5, 3, 7, 8]), (8 , [1, 0, 3, 5, 0, 6, 7, 1])) )
        self.assertEqual(self.test_q1.generateChromozomes( ([16, [1, 2, 3, 5, 5, 3, 7, 1]], (13, [1, 2, 3, 5, 5, 3, 4, 1])) ), ((13, [1, 2, 3, 5, 5, 3, 4, 1]), (13, [1, 2, 3, 5, 5, 3, 7, 1])) )
        self.assertEqual(self.test_q1.generateChromozomes( [(8 , [1, 0, 3, 5, 0, 3, 7, 1]), (13, [1, 2, 3, 5, 5, 3, 4, 1])] ), ((8, [1, 0, 3, 5, 5, 3, 4, 1]),  (11, [1, 2, 3, 5, 0, 3, 7, 1])) )
        

    def test_Mutation(self):
        parent_pts1 = 28
        parent_pts2 = 8
        (child_pts1, child1) , (child_pts2, child2)  = self.test_q1.Mutation(  ([28, [1, 2, 3, 4, 5, 6, 7, 8]], (8 , [1, 0, 3, 5, 0, 3, 7, 1]))  )
        self.assertLessEqual( child_pts1, parent_pts1)
        self.assertLessEqual( child_pts2, parent_pts2)
        parent_pts1 = 8
        parent_pts2 = 13
        (child_pts1, child1) , (child_pts2, child2)  = self.test_q1.Mutation(  [(8 , [1, 0, 3, 5, 0, 3, 7, 1]), (13, [1, 2, 3, 5, 5, 3, 4, 1])]  )
        self.assertLessEqual( child_pts1, parent_pts1)
        self.assertLessEqual( child_pts2, parent_pts2)


    def test_generategen1(self):
        self.assertLessEqual(len(self.test_q1.generateGen1()), 100)

    def test_checkWon(self):
        self.assertEqual(self.test_q1.check_won( ((0 , [4, 8, 1, 3, 6, 2, 7, 5]), (1 , [1, 0, 3, 5, 0, 3, 7, 1])) ), ("Won",( 0 , [4, 8, 1, 3, 6, 2, 7, 5])))
        self.assertEqual(self.test_q1.check_won( ((1 , [4, 8, 1, 3, 6, 2, 7, 5]), (1 , [1, 0, 3, 5, 0, 3, 7, 1])) ), "Continue")

if __name__ == "__main__":
    unittest.main()
