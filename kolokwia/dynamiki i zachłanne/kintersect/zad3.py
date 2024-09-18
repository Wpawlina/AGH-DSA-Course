from zad3testy import runtests
from heapq import heappop, heappush
 
def make_tab_of_events(A):
    tab=[]
    for i in range(len(A)):
        tab.append((A[i][0],1,A[i][1]))
        tab.append((A[i][1],-1,None))
    return tab
 
def kintersect( A, k ):
    tab=make_tab_of_events(A)
    tab.sort(key=lambda x: x[0])
    res_list=[]
    heap=[]
    cnt=0
    maxi=-1
    start_res=-1
    end_res=-1
    for i in range(len(tab)):
        if tab[i][1]==1:
            cnt+=1
            heappush(heap,tab[i][2])
            start=tab[i][0]
        if cnt>=k:
            end=heappop(heap)
            if end-start>maxi:
                maxi=end-start
                start_res=start
                end_res=end
            cnt-=1
    for i in range(len(A)):
        if start_res>=A[i][0] and end_res<=A[i][1]:
            res_list.append(i)
    return res_list




def kintersect2( A, k ):
	n = len(A)
	longest = 0
	res_spans = []

	if k == 1:
		for i in range(n):
			if A[i][1] - A[i][0] > longest:
				longest = A[i][1] - A[i][0]
				res_spans = [i]
	else:
		for i in range(n):
			A[i] = A[i], i
		A.sort(key=lambda tup: tup[0][1], reverse=True)

		for i in range(n):
			spans = [A[i][1]]
			for j in range(n):
				if i == j or A[j][0][0] > A[i][0][0]: continue
				spans.append(A[j][1])
				if len(spans) == k: break

			if len(spans) < k: continue

			length = min(A[i][0][1], A[j][0][1]) - A[i][0][0]
			if length > longest:
				longest = length
				res_spans = spans

	return res_spans

runtests( kintersect )