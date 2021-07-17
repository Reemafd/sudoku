# sudoku
def AC3(csp):
#queue.Queue Constructor for a FIFO queue. 
#maxsize is an integer that sets the upper bound limit on the number of items that can be placed in the queue.  
#Put item into the queue. If optional args block is true and timeout is None (the default), block if necessary, until a free slot is available.                             
	q = queue.Queue()
That participate in consistent XIJ X
	for arc in csp.constraints:
		q.put(arc)

	i = 0
#Select and delete (XI,XJ) from queue. 
	while not q.empty():
		(Xi, Xj) = q.get()

		i = i + 1 
#remove_inconsistent_values
#Remove inconsistent values and return true if I remove a value
		if Revise(csp, Xi, Xj):
			if len(csp.values[Xi]) == 0:
				return False
			for Xk in (csp.peers[Xi] - set(Xj)):
				q.put((Xk, Xi))
	#display(csp.values)
	return True
#working of the revise algorithm
def Revise(csp, Xi, Xj):
	revised = False
	values = set(csp.values[Xi])

	for x in values:
		if not isconsistent(csp, x, Xi, Xj):
			csp.values[Xi] = csp.values[Xi].replace(x, '')
			revised = True 

	return revised
