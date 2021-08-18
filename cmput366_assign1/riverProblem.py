"""
Solution stub for the River Problem.

Fill in the implementation of the `River_problem` class to match the
representation that you specified in problem XYZ.
"""


from searchProblem import Search_problem, Arc

class River_problem(Search_problem):
    def start_node(self):
        """returns start node"""
        #TODO
        #return (None,)
        # n is start node, means there is no animals on the right
        return ('n')
    
    def is_goal(self,node):
        """is True if node is a goal"""
        #TODO
        #return len(node) % 2 == 0 # dummy goal, state has two items in it
        # If node == ('fox', 'grain', 'hen'), then we get the goal
        return (node == ('fox', 'grain', 'hen'))

    def neighbors(self,node):
        """returns a list of the arcs for the neighbors of node"""
        #TODO
        #return [Arc(node, node+(None,), 1, 'ADD-NONE')]  
        
        # Start node
        # We have 4 ways to go
        if (node == ('n')):
            return [Arc(('n'), ('hen'), 1, 'Farmer takes hen to the right'), Arc(('n'), ('grain'), 1, 'Farmer takes grain to the right'), Arc(('n'), ('fox'), 1, 'Farmer takes fox to the right'), Arc(('n'), ('nn'), 1, 'Farmer doesn’t bring things across the river')]
        
        # Farmer doesn’t bring things across the river and animals on the left bank of the river eat each other
        # No ways
        elif (node == ('nn')):
            return []
        
        # Grain Node
        # No ways
        elif (node == ('grain')):
            return []
        
        # Fox Node
        # No ways        
        elif (node == ('fox')):
            return [] 
        
        # Hen Node
        # We have 4 ways to go       
        elif (node == ('hen')):
            return [Arc(('hen'), ('hen', 'fox'), 2, 'Farmer takes fox to the right'), Arc(('hen'), ('hen', 'grain'), 2, 'Farmer takes grain to the right'), Arc(('hen'), ('fox'), 2, 'Farmer brings back hen and takes fox to the right'), Arc(('hen'), ('grain'), 2, 'Farmer brings back hen and takes grain to the right')]
        
        # Fox and grain Node
        # We have 3 ways to go          
        elif (node == ('fox', 'grain')):
            return [Arc(('fox', 'grain'), ('fox', 'grain', 'hen'), 2, 'Farmer takes hen to the right'), Arc(('fox', 'grain'), ('hen', 'grain'), 2, 'Farmer brings back fox and takes hen to the right'), Arc(('fox', 'grain'), ('hen', 'fox'), 2, 'Farmer brings back grain and takes hen to the right')]     
        
        # Hen and fox Node
        # We have 3 ways to go              
        elif (node == ('hen', 'fox')):
            return [Arc(('hen', 'fox'), ('hen', 'grain'), 2, 'Farmer brings back fox and takes grain to the right'), Arc(('hen', 'fox'), ('fox', 'grain'), 2, 'Farmer brings back hen and takes grain to the right'), Arc(('hen', 'fox'), ('grain'), 2, 'Fox eats hen and farmer takes grain to the right')] 
        
        # Hen and grain Node
        # We have 3 ways to go         
        elif (node == ('hen', 'grain')):
            return [Arc(('hen', 'grain'), ('hen', 'fox'), 2, 'Farmer brings back grain and takes fox to the right'), Arc(('hen', 'grain'), ('fox', 'grain'), 2, 'Farmer brings back hen and takes fox to the right'), Arc(('hen', 'grain'), ('fox'), 2, 'Hen eats grain and farmer takes fox to the right')]         

    def heuristic(self,n):
        """Gives the heuristic value of node n."""
        #TODO
        #return 0
        # Heuristic function is 2 * (The animals on the left side of the river) - 1
        # Suppose the last position of the farmer is on the right side of the river
        # Thus, no matter which side of river the farmer is now, we have a heuristic function:
        return 2 * (3 - len(n)) - 1
    
