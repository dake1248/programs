from random import randint
import matplotlib.pyplot as plt

result=[]

for i in range(100):
	result.append(randint(1,7))
	
frequency=[]
frequencies=[]
for value in range(1,7):
	frequency=result.count(value)
	frequencies.append(frequency)
	
#x=[1,2,3,4,5,6]

hist=plt.bar()
hist.title="Fiture Title"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title='result'
hist.y_title='frequency of result'

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')
	