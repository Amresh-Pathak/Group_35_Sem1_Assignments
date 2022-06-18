# Insert into Binary Tree Function
def insert(rootNode, value):
    # Create a EmpNode for the empId value
    node = EmpNode(value)
    
    # if the rootNode is None, make the node as rootNode
    if not rootNode:
        rootNode = node
        return
    
    # if rootNode is not None, create a queue
    tempQ = queue.Queue()
    
    # enque the rootNode into the Queue
    tempQ.put(rootNode)
    
    # while the queue has a value
    while not tempQ.empty():
        
        # deque from the queue, and store it in root variable
        root = tempQ.get()
        
        # if the root has left, add root.left to queue
        if root.left:
            
            # enqueing left into the queue will make sure we traverse till the end of the queue in levels
            tempQ.put(root.left)
        
        # if root doesn't have left, set node in left position of root
        else:
            root.left = node
            
            # once inserted, we can return from the function
            return
        
        # if root has left, check if root has right, add root.right to queue
        if root.right:
            
            # enqueing right into the queue will make sure we traverse till the end of the queue in levels
            tempQ.put(root.right)
            
        # if root doesn't have right, set node in right position of root
        else:
            root.right = node
            
            # once inserted, we can return from the function
            return