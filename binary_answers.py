# Answers to the Questions on Binary Tree


class BinaryTree(object):
    ''' Represents a binary tree '''

    class Node(object):
        ''' Represents a node in the binary tree '''

        def __init__(self, data):
            ''' Constructor for Node '''
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        ''' Constructor for Binary Tree '''
        self.root = None

    def insert(self, data):
        ''' Inserts nodes in Binary Tree '''
        insert_node = self.Node(data)
        # If there is no node insert the node at the root
        if self.root is None:
            self.root = insert_node
            return "Inserted at root"
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = insert_node
                        return "Inserted at left"
                        break
                    current = current.left

                if data > current.data:
                    # If the node is greater than its root node insert at right
                    if current.right is None:
                        current.right = insert_node
                        return "Inserted at right"
                        break
                    current = current.right

                else:				# If the node is already present in the tree
                    return "Already Exists"
    

    def print_left_view(self, root, level, max_level):
        ''' Prints the left side view of the root '''		
        if root == None:
            return 
			
        if max_level[0] < level:
            print(root.data)
            max_level[0] = level
        self.print_left_view(root.left, level+1, max_level)
        self.print_left_view(root.right, level+1, max_level)


    deepest_level = 0
    deep_right_node=None
    def deep_right(self, root):
	    ''' Calls the function deepest right node of the tree '''
	
        # Call the function with initial parameters
	    self.deepest_right_node(root, 0, True)   
        # Print the updated value after calling the function		
        print(self.deep_right_node)				  

    def deepest_right_node(self, root, level, isRight):
	    '''Recursive implementation to find deepest right node in tree'''
        if root == None:
            return
        self.deepest_right_node(root.right,level+1, True)  
        if isRight and self.deepest_level < level:
            self.deep_right_node = root.data
            self.deepest_level = level
        self.deepest_right_node(root.left,level, False)  
	 	
    def spiral_level_order(self, root):  
        '''
		   Prints the level order of tree in spiral format
		   eg.
		        1
				2    3
			  4   5 6   7
		  
			op:
				1
				3 2
				4 5 6 7

        '''		
        queue =[]
        if root != None:
            queue.append(root)
        leftToRight = True
        while len(queue)>0:           
            nextLevel = []
            while len(queue)>0:
                node = queue.pop()
                print(node.data, )
                if leftToRight:
                    if node.left != None:
                        nextLevel.append(node.left)
                    if node.right != None:
                        nextLevel.append(node.right)
                else:
                    if node.right != None:
                        nextLevel.append(node.right)
                    if node.left != None:
                        nextLevel.append(node.left)
            queue = nextLevel            
            leftToRight = not leftToRight

if __name__ == '__main__':

    tree = BinaryTree()
    tree.insert(10)
    tree.insert(2)
    tree.insert(6)
    tree.insert(12)    
    tree.insert(11)
    tree.insert(23)
    tree.insert(26)
    tree.insert(22)
    max_level = [0]
    root = tree.get_root
    tree.spiral_level_order(root)
	#tree.print_spiral()
    #print(tree.height(root))
    #tree.print_left_view(tree.get_root, 1, max_level)
    #tree.deep_right(tree.get_root)
    #tree.level_order()
