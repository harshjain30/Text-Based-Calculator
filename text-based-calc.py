prior = {"=":1,"+=":1,"-=":1,"+":2,"-":2,"*":3,"/":3,"++":4,"--":4}
variables = {}
post = []

def enpqueue(l,c,_i,i_,p):
	j = 0
	while j!=len(l) and p >= l[j][3]: j += 1
	l.insert(j,(c,_i,i_,p))

def opr(o,l,r):
	print(o,l,r)

	if o == "=":
		variables[l] = r
		return True

	if o == "++":
		if r == "":
			post.append(o+l)
			#print(post)
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



def process(st,s,e,pq):
	if st == None: return None
	cst = st[s:e+1].strip()
	if cst == "": return ""
	if cst.isdigit():
		return int(cst)
	elif len(cst) == 1:
		return cst #strictly single-character variables, otherwise define variables
	print(pq)
	for i,t in enumerate(pq):
		if t[1] >= s and t[2] <= e:
			return opr(t[0],process(st,s,t[1]-1,pq[:i]+pq[i+1:]),process(st,t[2]+1,e,pq[:i]+pq[i+1:]))

def _process(s):
	#print(s)
	pq = []
	i = 0
	n = len(s)
	#if s[0] not in prior: variables[s[0]] = 0
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