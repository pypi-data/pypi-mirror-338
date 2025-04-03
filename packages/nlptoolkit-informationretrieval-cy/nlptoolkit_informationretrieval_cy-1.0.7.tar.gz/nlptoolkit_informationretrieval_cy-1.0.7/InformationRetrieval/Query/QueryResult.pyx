from DataStructure.Heap.MinHeap cimport MinHeap
from InformationRetrieval.Query.QueryResultItem cimport QueryResultItem

cdef class QueryResult:

    def __init__(self):
        """
        Empty constructor for the QueryResult object.
        """
        self.__items = []

    cpdef add(self, int docId, float score = 0.0):
        """
        Adds a new result item to the list of query result.
        :param docId: Document id of the result
        :param score: Score of the result
        """
        self.__items.append(QueryResultItem(docId, score))

    cpdef int size(self):
        """
        Returns number of results for query
        :return: Number of results for query
        """
        return len(self.__items)

    cpdef list getItems(self):
        """
        Returns result list for query
        :return: Result list for query
        """
        return self.__items

    cpdef QueryResult intersectionFastSearch(self, QueryResult queryResult):
        """
        Given two query results, this method identifies the intersection of those two results by doing parallel iteration
        in O(N).
        :param queryResult: Second query result to be intersected.
        :return: Intersection of this query result with the second query result
        """
        cdef QueryResult result
        cdef int i, j
        cdef QueryResultItem item1, item2
        result = QueryResult()
        i = 0
        j = 0
        while i < self.size() and j < queryResult.size():
            item1 = self.__items[i]
            item2 = queryResult.__items[j]
            if item1.getDocId() == item2.getDocId():
                result.add(item1.getDocId())
                i = i + 1
                j = j + 1
            else:
                if item1.getDocId() < item2.getDocId():
                    i = i + 1
                else:
                    j = j + 1
        return result

    cpdef QueryResult intersectionBinarySearch(self, QueryResult queryResult):
        """
        Given two query results, this method identifies the intersection of those two results by doing binary search on
        the second list in O(N log N).
        :param queryResult: Second query result to be intersected.
        :return: Intersection of this query result with the second query result
        """
        cdef QueryResult result
        cdef int low, middle, high
        cdef bint found
        cdef QueryResultItem searched_item
        result = QueryResult()
        for searched_item in self.__items:
            low = 0
            high = queryResult.size() - 1
            middle = (low + high) // 2
            found = False
            while low <= high:
                if searched_item.getDocId() > queryResult.__items[middle].getDocId():
                    low = middle + 1
                elif searched_item.getDocId() < queryResult.__items[middle].getDocId():
                    high = middle - 1
                else:
                    found = True
                    break
                middle = (low + high) // 2
            if found:
                result.add(searched_item.getDocId(), searched_item.getScore())
        return result

    cpdef QueryResult intersectionLinearSearch(self, QueryResult queryResult):
        """
        Given two query results, this method identifies the intersection of those two results by doing exhaustive search
        on the second list in O(N^2).
        :param queryResult: Second query result to be intersected.
        :return: Intersection of this query result with the second query result
        """
        cdef QueryResult result
        result = QueryResult()
        for searched_item in self.__items:
            for item in queryResult.__items:
                if searched_item.getDocId() == item.getDocId():
                    result.add(searched_item.getDocId(), searched_item.getScore())
        return result

    def getBest(self, K: int):
        """
        The method returns K best results from the query result using min heap in O(K log N + N log K) time.
        :param K: Size of the best subset.
        """
        minHeap = MinHeap(K, lambda x1, x2: 1 if x1.getScore() > x2.getScore() else (0 if x1.getScore() == x2.getScore() else -1))
        i = 0
        while i < K and i < len(self.__items):
            minHeap.insert(self.__items[i])
            i = i + 1
        for i in range(K + 1, len(self.__items)):
            top_item = minHeap.delete()
            if isinstance(top_item, QueryResultItem) and top_item.getScore() > self.__items[i].getScore():
                minHeap.insert(top_item)
            else:
                minHeap.insert(self.__items[i])
        self.__items.clear()
        i = 0
        while i < K and not minHeap.isEmpty():
            self.__items.insert(0, minHeap.delete())
            i = i + 1

    def __repr__(self):
        return f"{self.__items}"
