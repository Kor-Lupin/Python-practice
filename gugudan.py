import pandas as pd
dan_i = [1,2,3,4,5,6,7,8,9]

gugudan_dict = {}
for i in range(9):
    a = [0] * 9
    for j in range(9):
        a[j] = ('{} x {} = {}'.format(j+1,i+1,(i+1)*(j+1)))
        gugu_c = ('{}단'.format(i+1))
        gugudan_dict[gugu_c] = a
        
gugudan = pd.DataFrame(gugudan_dict, index = dan_i)
print(gugudan)

              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              