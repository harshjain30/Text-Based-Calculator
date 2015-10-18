prior = {"=":1,"*=":1,"/=":1,"+=":1,"-=":1,"+":2,"-":2,"*":3,"/":3,"++":4,"--":4}
variables = {}
post = []

def isNumber(s):
	for c in s:
		if not (c.isdigit() or c=="."):
			return False
	return True

def num(s):
	try:
		return int(s)
	except ValueError:
		return float(s)

def enpqueue(l,c,_i,i_,p):
	j = 0
	while j!=len(l) and p >= l[j][3]: j += 1
	l.insert(j,(c,_i,i_,p))

def opr(o,l,r):
	try:
		if o == "=":
			variables[l] = r
			return True

		if o == "++":
			if r == "":
				post.append(o+l)
				return variables[l]
			elif l == "":
				variables[r] += 1
				return variables[r]

		if o == "--":
			if r == "":
				post.append(o+l)
				return variables[l]
			elif l == "":
				variables[r] -= 1
				return variables[r]
		
		if type(r) is str:
			r = variables[r]
		if o == "*=":
			variables[l] *= r
			return True
		if o == "/=":
			variables[l] /= r
			return True
		if o == "+=":
			variables[l] += r
			return True
		if o == "-=":
			variables[l] -= r
			return True
		
		if type(l) is str:
			l = variables[l]
		if o == "*":
			return l*r
		if o == "/":
			return l/r
		if o == "+":
			return l+r
		if o == "-":
			return l-r
	except KeyError:
		print("Invalid input")
		exit()


def process(st,s,e,pq):
	if not pq:
		if st == None: return None
		cst = st[s:e+1].strip()
		if cst == "": return ""
		if isNumber(cst):
			return num(cst)
		else:
			return cst
	spl = pq.pop(0)
	pql = [t for t in pq if t[1]>=s and t[2]<spl[1]]
	pqr = [t for t in pq if t[1]>spl[2] and t[2]<=e]
	return opr(spl[0],process(st,s,spl[1]-1,pql),process(st,spl[2]+1,e,pqr))

def _process(s):
	pq = []
	i = 0
	n = len(s)
	while i < n:
		c = s[i]
		if c in prior:
			if i != n-1 and c+s[i+1] in prior:
				d = c+s[i+1]
				enpqueue(pq,d,i,i+1,prior[d])
				i += 1
			else:
				enpqueue(pq,c,i,i,prior[c])
		i += 1

	process(s,0,n-1,pq)


def main():
	s = input()
	l = []
	while s:
		l.append(s)
		s = input()

	for s in l:
		del post[:]
		_process(s)
		for p in post: _process(p)

	print(variables)

main()