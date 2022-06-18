import queue

class EmpNode:
    def __init__ (self, empId):
        self.empId = empId
        self.attctr = 1
        self.left = None
        self.right = None

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

def nodeOperation(rootNode: EmpNode, operation: str, params={}):
    # creating a dummy dictionary for the output
    out = {'count':0, 'increase_count':False, 'search': None, 'inFreezer': 0, 'nodes': []}
    
    # if rootNode is None, we can exit
    if not rootNode:
        return

    # creating a temporary queue for traversing in levels
    tempQ = queue.Queue()

    # enque rootNode to queue
    tempQ.put(rootNode)

    # while queue is not empty
    while not tempQ.empty():

        # deque the node and store it in root variable
        root = tempQ.get()

        # based on the required operation, 
        # we will run respective code
         
        # traversing through list 
        if operation == 'traverse':
            
            # count number of employees
            out['count'] += 1
            print(root.empId, " - ", root.attctr)
        
        # increasing scan_count for specific employee  
        if operation == 'increase_count':

            # if the employee id of the root matches 
            # with the node provided in params
            if int(root.empId) == int(params['increase_node']):

                # increase the counter and set increase_count to True
                root.attctr += 1
                out['increase_count'] = True

                # after increasing, we don't need to traverse, 
                # so breaking the loop
                break

        # searching for a element in list
        if operation == 'search':

            # if the employee id of the root matches 
            # with the node provided in params
            if int(root.empId) == int(params['search']):

                # set the search key with root value
                out['search'] = root

                # after finding the element, 
                # we can break the loop
                break

        # check how many employees are in Freezer
        if operation == 'inFreezer':

            # if the scan_count is odd, 
            # it means the employee is inside the freezer room
            if root.attctr%2 != 0:
                out['inFreezer'] += 1
            
            # here we don't break because 
            # we need to traverse through the whole list

        # check how many employees are
        if operation == 'freq_visit':
            if root.attctr >= params['freq']:
                out['nodes'].append(root)
        if operation == 'range':
            if ((int(root.empId) >= params['low']) and (int(root.empId) < params['high'])):
                out['nodes'].append(root)
        
        if root.left:
            tempQ.put(root.left)
        if root.right:
            tempQ.put(root.right)
    return out

if __name__ == "__main__":
    inp = open('./inputPS07.txt', 'r')
    instructions = str(inp.read()).split('\n')
    inp.close()

    out = open('./test_final_outputPS07.txt', 'w')
    bt = None
    for instruction in instructions:
        pre = instruction.split(':')[0]
        if pre not in ['inFreezer', 'checkEmp', 'freqVisit', 'range', '']:
            # pre = int(pre)
            if not bt:
                bt = EmpNode(pre)
            else:
                present = nodeOperation(rootNode=bt, operation='increase_count', params={'increase_node': pre})['increase_count']
                if not present:
                    insert(rootNode=bt, value=pre)
        else:
            if pre == 'inFreezer':
                count = nodeOperation(rootNode=bt, operation='traverse')['count']
                out.write(f"Total number of employees recorded today: {count}\n")
                freezer_count = nodeOperation(rootNode=bt, operation='inFreezer')['inFreezer']
                out.write(f"Total number of employees inside Freezer: {freezer_count}\n")
            
            if pre == 'checkEmp':
                emp = int(instruction.split(':')[-1])
                node = nodeOperation(rootNode=bt, operation='search', params={'search': emp})['search']
                if not node:
                    out.write(f"Employee id {emp} did not swipe today.\n")
                else:
                    out.write(f"Employee id {node.empId} swiped {node.attctr} times today and is currently {'outside' if node.attctr%2==0 else 'inside'} freezer room\n")
            if pre == 'freqVisit':
                num = int(instruction.split(':')[-1])
                nodes = nodeOperation(rootNode=bt, operation='freq_visit', params={'freq': num})['nodes']
                if nodes:
                    out.write(f"Employees that swiped more than {num} times today are:\n")
                    for node in nodes:
                        out.write(f"{node.empId}, {node.attctr}\n") 
            if pre == 'range':
                low = int(instruction.split(':')[-2])
                high = int(instruction.split(':')[-1])
                nodes = nodeOperation(rootNode=bt, operation='range', params={'low': low, 'high': high})['nodes']
                if nodes:
                    out.write(f"Range: {low} to {high} Employee swipe:\n")
                    for node in nodes:
                        out.write(f"{node.empId}, {node.attctr}, {'in' if node.attctr%2 != 0 else 'out'}\n")
                        
    out.close()