class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        for i in range(len(citations)):
            if i+1 > citations[i]:
                return i

        return len(citations)
	
	def hIndex_full(self, citations: List[int]) -> int:
        n = len(citations)
        hist = [0]*(n+1)
        for c in citations:
            if c >= n:
                hist[n]+=1
            else:
                hist[c]+=1

        csum = 0
        for i in range(n,-1,-1):
            csum += hist[i]
            if csum>=i:
                return i
        return 0