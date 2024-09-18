"""
Algorytm korzysta z dwóch kopców - minheapa i maxheapa.
Przechowują one elementy tablicy w formacie (T[i], i).
Nazwę element "aktywnym" jeśli jest on w aktualnie rozpatrywanym oknie (rozmiaru
p). Minheap przechowuje k największych aktywnych elementów, a maxheap
przechowuje pozostałe k-p aktywnych elementów. Moga one także przechowywać
elementy spoza okna, są one pomijane przy wybieraniu elementów z owych kopców.

W każdej iteracji sprawdzam, który element wyszedł poza okno, znajduję, w
którym jest on kopcu, i na bazie tego przesuwam elementy między kopcami tak,
by zachować ten inwariant co do ilości elementów.
Po każdej iteracji pierwszy element w minheapie jest k-tym według wielkości
aktywnym elementem (bo nieaktywne elementy są w miarę możliwości usuwane),
więc dodaję go do sumy.

W każdej z O(n) iteracji wywołuję kilka razy funkcję clean() (do niej wrócę),
i O(1) razy wsadzam/wyjmuję coś do kopca, co w najgorszym przypadku ma
złożoność O(log n). Pomijając funkcję clean(), algorytm ma więc złożoność
O(n log n).
Przez cały czas działania algorytmu funkcja clean() wykona co najwyżej jedną
iterację na każdy element (nie może usunąć czegoś dwa razy), więc zużywa ona
O(n) czasu - więc łączny czas działania algorytmu to O(n log n).
Zużywa on O(n) pamięci.
"""

from zad2testy import runtests

def parent(i): return (i-1)//2

# oryginalnie miałem jedną klasę Heap, która w konstruktorze przyjmowała
# funkcję do porównywania elementów. było to całkiem zgrabne ale trochę wolne.
# rozdzieliłem ją na dwie klasy i przyśpieszyłem program o około 20%... kosztem
# wyglądu. wiem że mogłem użyć np. Maxheap jako Minheap negując argumenty,
# ale wedlug mnie też by to zbyt piękne nie było
class Maxheap:
	def __init__(self):
		self.a = []

	def heapify(self, i):
		a = self.a
		n = len(self.a)
		while True:
			max_ind = i
			l = 2*i + 1
			r = 2*i + 2
			if l < n and not (a[max_ind] >= a[l]): max_ind = l
			if r < n and not (a[max_ind] >= a[r]): max_ind = r
			if max_ind == i: break
			a[i], a[max_ind] = a[max_ind], a[i]
			i = max_ind

	def push(self, v):
		a = self.a
		a.append(v)
		i = len(a)-1
		while i != 0 and not (a[parent(i)] >= a[i]):
			a[i], a[parent(i)] = a[parent(i)], a[i]
			i = parent(i)

	def pop(self):
		a = self.a
		ret = a[0]
		if len(a) > 1:
			a[0] = a.pop()
			self.heapify(0)
		else:
			a.pop()
		return ret

	def top(self): return self.a[0]
	def __len__(self): return len(self.a)
	def __str__(self): return f"<{', '.join([str(s) for s in self.a])}>"

class Minheap:
	def __init__(self):
		self.a = []

	def heapify(self, i):
		a = self.a
		n = len(self.a)
		while True:
			max_ind = i
			l = 2*i + 1
			r = 2*i + 2
			if l < n and not (a[max_ind] <= a[l]): max_ind = l
			if r < n and not (a[max_ind] <= a[r]): max_ind = r
			if max_ind == i: break
			a[i], a[max_ind] = a[max_ind], a[i]
			i = max_ind

	def push(self, v):
		a = self.a
		a.append(v)
		i = len(a)-1
		while i != 0 and not (a[parent(i)] <= a[i]):
			a[i], a[parent(i)] = a[parent(i)], a[i]
			i = parent(i)

	def pop(self):
		a = self.a
		ret = a[0]
		if len(a) > 1:
			a[0] = a.pop()
			self.heapify(0)
		else:
			a.pop()
		return ret

	def top(self): return self.a[0]
	def __len__(self): return len(self.a)
	def __str__(self): return f"<{', '.join([str(s) for s in self.a])}>"

def clean(heap, start):
	while len(heap) != 0 and heap.top()[1] < start:
		heap.pop()

def ksum(T, k, p):
	n = len(T)
	assert k <= p <= n

	top = Minheap() # k największych elementów, (T[i], i)
	bot = Maxheap() # reszta,                   (T[i], i)

	for i in range(p):   top.push((T[i], i))
	for _ in range(p-k): bot.push(top.pop())

	tally = 0
	tally += top.top()[0]

	# inwariant: w kopcu "górnym" powinno być k aktywnych elementów,
	#            a w kopcu dolnym p-k aktywnych elementów
	# assert len([(v, i) for v, i in top.a if 0 <= i]) == k
	# assert len([(v, i) for v, i in bot.a if 0 <= i]) == p-k
	

	for i in range(p, n):
		start = i-p+1
		print(top.__str__())
		print("========")
		print(bot.__str__())
		print("++++++++")

		#assert len(bot) == 0 or len(top) == 0 or bot.top() <= top.top()

		# remove T[i-p]
		if top.top() <= (T[i-p], i-p):
			# top is lacking
			# assert len([(v, i) for v, i in top.a if start <= i]) == k-1
			# assert len([(v, i) for v, i in bot.a if start <= i]) == p-k

			clean(bot, start)
			bot.push((T[i], i))
			top.push(bot.pop())
		else:
			# bot is lacking
			# assert len([(v, i) for v, i in top.a if start <= i]) == k
			# assert len([(v, i) for v, i in bot.a if start <= i]) == p-k-1

			top.push((T[i], i))
			clean(top, start)
			bot.push(top.pop())

		clean(top, start)
		# assert len([(v, i) for v, i in top.a if start <= i]) == k
		# assert len([(v, i) for v, i in bot.a if start <= i]) == p-k

		tally += top.top()[0]
	return tally

# zmien all_tests na True zeby uruchomic wszystkie testy


T =  [7, 9, 1, 5, 8, 6, 2, 12,44,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,41,5,78,223,667,123,675,555,1245,1234,4343,322,111,257,434,23,999,443,121,551,553,421,567,123,672,567,678,886,865,434,678,677,764,887,886,865,543,345,35,78,11,326,57,3,4]
k =  69
p =  100


print(ksum(T,k,p))
    

#runtests( ksum, all_tests=False )
