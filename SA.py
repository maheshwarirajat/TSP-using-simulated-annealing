# Modules
import math
import numpy as np
import matplotlib.pyplot as plt

# calulate length between two points

def length (n1,n2):
	return math.sqrt((n1[0]-n2[0])**2 + (n1[1]-n2[1])**2)


# calculate total length to traverse all points

def total_length(arr,n):
	l=length(arr[0],arr[n-1])
	for i in range(n-1):
		l+= length(arr[i],arr[i+1])
	return l
		

	
	
# two_opt optimization for simulated annealing, using a random probabilty function to do selection

def two_opt_optimization(sol_arr,t,n):
	
	# picking two pair of consecutive integers, making sure they are not same
	ai =np.random.randint(0,n-1)
	bi =(ai+1)%n 
	ci =np.random.randint(0,n-1)
	di =(ci+1)%n
	
	if ai != ci and bi != ci:
		a =sol_arr[ai]
		b =sol_arr[bi]
		c =sol_arr[ci]
		d =sol_arr[di]
		
		# old lengths
		ab =length(a,b)
		cd =length(c,d)
		# new lengths, if accepted by our probability function
		ac =length(a,c)
		bd =length(b,d)
		
		diff = ( ab + cd ) - ( ac + bd )
		
		p = 0
		# for negative diff-> we'll use boltzman probabilty distribution equation-> P(E)=exp(-E/kT)
		if diff < 0:
			# k is considered to be 1
			p = math.exp( diff/t )
			
		# we'll sometimes skip the good solution
		elif diff > 0.05 :
			p = 1
			
		#print p	
		if(np.random.random() < p ):
			
			new_arr = range(0,n)
			new_arr[0]=sol_arr[ai]
			i = 1
			
			while bi!= ci:
				
				new_arr[i]=sol_arr[ci]
				i = i+1
				ci = (ci-1)%n
				
			new_arr[i]=sol_arr[bi]
			i = i+1
			
			while ai!= di:
				new_arr[i] =sol_arr[di]
				i = i+1
				di =(di+1)%n
				
				
			# animate this frame	
			#animate()
			
			return new_arr
			
	return sol_arr
				
				
# Simmulated Annealing algorithm----------------------------------------------	
	
def sa_algorithm (input_data):
	
	#length of input_data
	n=len(input_data)
	
	#creating a base solution
	sol_arr=input_data
	
	#plot initial solution
	#plt.axis([-100,1100,-100,1100])
	#plt.plot(input_data[:,0],input_data[:,1],'ro')
	
	#initial temperature
	t = 100
	
	#current length
	min_l=total_length(sol_arr,n)
	
	i=0
	best_arr=[]
	
	while t>0.1:
		
		i= i+1
		
		#two_opt method- for optimization
		sol_arr=two_opt_optimization(sol_arr,t,n)
		
		#after 200 steps restart the process until the temperature is less than 0.1
		if i>=200 :
				
			i=0
			current_l=total_length(sol_arr,n)
			
			#because input size is approx. 200 i'm keeping the cooling schedule slow
			t = t*0.9995
			#print t
			
			if current_l < min_l:
				print current_l
				min_l=current_l
				best_arr=sol_arr[:]
	
	return best_arr
				
			 
		
	
	
	
	
