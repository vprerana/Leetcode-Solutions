from collections import defaultdict
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build Adjacency List and Indegree Array
        adjList = defaultdict(list)  # {prerequisite: [courses that depend on it]}
        indegree = [0] * numCourses   # Number of prerequisites for each course

        for prerequisite, course in prerequisites: 
            adjList[prerequisite].append(course)  # Add course to the list of courses depending on the prerequisite
            indegree[course] += 1  # Increment the indegree of the dependent course

        # 2. Initialize Queue with Zero-Indegree Nodes (No Prerequisites)
        q = deque()  # Queue to hold courses with no remaining prerequisites
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)  # Add to queue if it has no dependencies

        # 3. Topological Sorting (Kahn's Algorithm)
        topo = []  # Array to store the topological order of courses
        while q:
            node = q.popleft()  # Take a course with no prerequisites from the queue
            topo.append(node)   # Add it to the topological order

            # Update neighbors' indegrees and add them to queue if ready
            for neighbor in adjList[node]: 
                indegree[neighbor] -= 1  # One less prerequisite for the neighbor
                if indegree[neighbor] == 0:  
                    q.append(neighbor)  # Add to queue if it has no more dependencies

        # 4. Check if a Valid Topological Order Exists
        # If the length of the topological order equals the number of courses, then all courses can be finished.
        # This indicates no cycles exist in the dependency graph.
        print(topo)  # You can comment this out if you don't want to see the topological order
        return len(topo) == numCourses  
