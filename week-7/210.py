class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create adjacency list and track indegrees
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        # Build the graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        # Initialize queue with courses having no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        
        # Process courses level by level
        while queue:
            curr = queue.popleft()
            order.append(curr)
            
            # Reduce indegree of neighbors
            for next_course in graph[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        # Return order if all courses can be completed, empty list otherwise
        return order if len(order) == numCourses else []
