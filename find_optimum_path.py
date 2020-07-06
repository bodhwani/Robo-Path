from collections import deque
from collections import defaultdict
import time
import queue as Q 



def take_input(filename):
	file1 = open(filename,"r")
	input1 = (file1.readlines())
	algo = input1[0]
	colum_row = input1[1].split(" ")
	landing_position = input1[2].split(" ")
	max_elevation = input1[3]
	n_target = input1[4]
	target_values = []
	matrix_values = []

	for i in range(int(n_target)):
		target_values.append(input1[i+5].split(" "))
	for j in range(int(colum_row[1])):
		matrix_values.append(input1[j+i+6].split(" "))
	file1.close()

	return algo, colum_row[0], colum_row[1],landing_position, max_elevation, n_target, target_values,matrix_values

filename = ""
input_list = take_input(filename)
print(input_list)
#taking input values
algo = input_list[0]
column = int(input_list[1])
row = int(input_list[2])
landing_position_values = [int(x) for x in input_list[3]]
max_elevation = int(input_list[4])
n_target = int(input_list[5])
target_values_string = input_list[6]

#converting into integers values
target_values = []
for i in target_values_string:
	temp = []
	temp.append(int(i[0]))
	temp.append(int(i[1]))
	target_values.append(temp)


#taking matrix values and converting into integer values
matrix_values = [[0 for c in range(column)] for r in range(row)]
matrix_values_string = input_list[7]
for r in range(row):
	for c in range(column):
		matrix_values[r][c] = int(matrix_values_string[r][c])
print(matrix_values)
def safeDistance(a,b):
	if(abs(a-b) <= max_elevation):
		return True
	else:
		return False

def computeElevationDistance(a,b):
	return abs(a-b)


def BFS(M, start_pos, goal):
	print("start_pos = ", start_pos)
	print("goal = ", goal)
	queue = deque([[start_pos]])
	print(queue)
	visited = set([start_pos])
	while queue:
		path = queue.popleft()

		x, y = path[len(path)-1]
		if ([x,y] == goal):
			return path
		for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1, y+1), (x+1, y-1), (x-1, y-1), (x-1, y+1)):
			if 0 <= x2 < width and 0 <= y2 < height:
				if ((x2, y2) not in visited):
					if(safeDistance(M[y2][x2], M[y][x])):
						queue.append(path + [(x2, y2)])
						visited.add((x2, y2))


def computeHeuristicCost(ny,nx,gy,gx):
	xd = abs(nx-gx)
	yd = abs(ny-gy)
	return 10*(xd + yd) - (6)*min(xd,yd)

	
def UCS(M, start_pos, goal):

	path = ((start_pos[0], start_pos[1]),)
	cost_dictionary = {}
	cost, sd,dd = 0,0,0
	temp = ()
	cost_dictionary[start_pos] = 0
	temp_queue = Q.PriorityQueue()
	visited = set([start_pos])
	n_loops = 0
	while bool(cost_dictionary):
		n_loops = n_loops + 1
		if(len(temp_queue.queue) != 0):
			path = temp_queue.get()[1]
			cost = cost_dictionary[path]
		if(start_pos in cost_dictionary):
			del cost_dictionary[start_pos]
		else:
			del cost_dictionary[path]
		x, y = path[-1]

		if((x,y) == start_pos):
			pass
		else:
			if((x,y) in visited):
				continue

		visited.add((x,y))		
		if ([x,y] == goal):
			return path
		for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1, y+1), (x+1, y-1), (x-1, y-1), (x-1, y+1)):
			if 0 <= x2 < width and 0 <= y2 < height:
				if ((x2, y2) not in visited):
					if(safeDistance(M[y2][x2], M[y][x])):
						temp = path + ((x2,y2),)
						if(abs(x2-x) + abs(y2-y) == 2):
							g_cost = (cost  + 14)	
						else:
							g_cost = (cost  + 10)
						f_cost = g_cost
						temp_queue.put((f_cost, temp))
						cost_dictionary[temp] = g_cost
				else:
					continue

def A_STAR(M, start_pos, goal):

	path = ((start_pos[0], start_pos[1]),)
	cost_dictionary = {}
	cost, sd,dd = 0,0,0
	temp = ()
	cost_dictionary[start_pos] = 0
	temp_queue = Q.PriorityQueue()
	visited = set([start_pos])
	n_loops = 0
	while bool(cost_dictionary):
		n_loops = n_loops + 1
		if(len(temp_queue.queue) != 0):
			path = temp_queue.get()[1]
			cost = cost_dictionary[path]
		if(start_pos in cost_dictionary):
			del cost_dictionary[start_pos]
		else:
			del cost_dictionary[path]
		x, y = path[-1]

		if((x,y) == start_pos):
			pass
		else:
			if((x,y) in visited):
				continue
		visited.add((x,y))		
		if ([x,y] == goal):
			return path
		for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1, y+1), (x+1, y-1), (x-1, y-1), (x-1, y+1)):
			if 0 <= x2 < width and 0 <= y2 < height:
				if ((x2, y2) not in visited):
					if(safeDistance(M[y2][x2], M[y][x])):
						temp = path + ((x2,y2),)
						elevation_cost = computeElevationDistance(M[y2][x2], M[y][x])
						heuristic_cost = computeHeuristicCost(y2,x2, goal[0], goal[1])
						if(abs(x2-x) + abs(y2-y) == 2):
							g_cost = (cost + elevation_cost + 14)	
						else:
							g_cost = (cost + elevation_cost + 10)
						f_cost = g_cost + heuristic_cost
						temp_queue.put((f_cost, temp))
						cost_dictionary[temp] = g_cost
				else:
					continue

width, height = column, row
all_paths = []

fp = open("output.txt", "w")

if(algo[0:2] == "BF"):
	for value in target_values:
		path = BFS(matrix_values, tuple(landing_position_values), value)
		if path:
			for x,y in path:
				fp.write('%s,%s ' % (x,y))
			fp.write("\n")
			
		else:
			fp.write('FAIL')
			fp.write("\n")

elif(algo[0:2] == "UC"):
	for value in target_values:
		path = UCS(matrix_values, tuple(landing_position_values), value)
		if path:
			for x,y in path:
				fp.write('%s,%s ' % (x,y))
			fp.write("\n")
			
		else:
			fp.write('FAIL')
			fp.write("\n")

elif(algo[0] == "A"):
	for value in target_values:
		path = A_STAR(matrix_values, tuple(landing_position_values), value)
		if path:
			for x,y in path:
				fp.write('%s,%s ' % (x,y))
			fp.write("\n")
			
		else:
			fp.write('FAIL')
			fp.write("\n")
else:
	fp.write('FAIL')
	fp.write("\n")

fp.close()