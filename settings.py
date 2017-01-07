# settings.py

def init():
	global window, width, height, vectors, showLineSegments, interpolationNumber, selectedT, splitLine, degreeOffset
	window = 0
	width, height = 1000, 700
	vectors = []
	showLineSegments = False
	interpolationNumber = 100
	selectedT = 0.5
	splitLine = False
	degreeOffset = 0

	global uK, vK, uKnots, vKnots, points, weights, uRes, vRes
	uK = 3
	vK = 3
	uRes = 3
	vRes = 3

	uKnots = []
	vKnots = []

	points = [[ [200, 300, 100], [200, 450, 1], [200, 560, 3], [200, 650, 5] ],
	         [ [300, 200, 4], [340, 300, -200], [370, 500, -200], [300, 600, 4] ],
	         [ [400, 200, 5], [430, 400, -200], [430, 500, -200], [440, 700, 2] ],
	         [ [500, 200, 5], [520, 400, 0], [530, 500, 3], [560, 600, 220] ]]

	weights = [[2, 3, 1, 3],
	         [5, 10, 10, 6],
	         [2, 10, 10, 3],
	         [2, 4, 2, 2] ]

def getVectorEndpoints(points, vectors):
	endPoints = []
	for i in range(min(len(points), len(vectors))):
		endPoints.append([points[i][0] + vectors[i][0], points[i][1] + vectors[i][1]])
	return endPoints

def convertVectorEndpointToVector(vectorEndpoint, point):
	return vectorEndpoint[0] - point[0], vectorEndpoint[1] - point[1]