x=[1,2,3,0,2,-2,-1,1,2,-1]
y=[0,1,1,0,0,5,2,2,0,-2]
z=[1,3,2,2,-1,-1,0,3,3,-3]
n=len(x)
d1=(x[1]-x[0])**2
d2=(y[1]-y[0])**2
d3=(z[1]-z[0])**2
dd,ii,jj,ass=[],[],[],[]
i1, i2, j1, j2=0, 0, 1, 1
m1=(d1+d2+d3)**0.5
m2=(d1+d2+d3)**0.5

for i in range(0,n-1):
	for j in range(i+1,n):
		d1=x[i]-x[j]
		d2=y[i]-y[j]
		d3=z[i]-z[j]
		d=(d1**2+d2**2+d3**2)**0.5
		dd.append(d)
		ii.append(i)
		jj.append(j)
		if(m1<d):
			m1=d
			i1=i
			j1=j
		if(m2>d):
			m2=d
			i2=i
			j2=j
print("particle no=",i1,j1,"max =",m1)
print("particle no=",i2,j2,"min =",m2)

n=len(dd)	
for i in range(0,n-1):
	for j in range(i+1,n):
		if(dd[i]>dd[j]):
			dd[i],dd[j] = dd[j],dd[i]
			ii[i],ii[j] = ii[j],ii[i]
			jj[i],jj[j] = jj[j],jj[i]
for i in  range(n):
        print(ii[i],jj[i],dd[i])
				
		
		
		
		
		
		
		
				
