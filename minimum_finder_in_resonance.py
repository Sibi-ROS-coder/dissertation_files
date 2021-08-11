import numpy as np
with open('ALL2.txt','r') as f:
    lines = f.readlines()

count_line = 0
def find_minimum(epi,line_numbers):
    a =np.zeros([5000,2])
    line_number = line_numbers +2
    fn_count = 0
    i = 0
    for line in lines:
        b = line.split()
        if(fn_count>=line_number):
            if(b!='#Parameters' and len(b)==2):
                a[i,:] = b
                i = i+1
            else:
                break
        fn_count = fn_count + 1
    index = np.argmin(a[:,1])
    print(epi,a[index,0],a[index,1])
    return a[index,0],a[index,1]

for line in lines:
    dummy1 = line.split()
    if(dummy1[0]=='#"Frequency'):
        dummy = line.split()
        # print(dummy)
        dum2 =dummy[4].strip().split('=')
        dum3 = str(dum2[1])
        dum4 = dum3.split(')')
        dum5 = float(dum4[0])
        epsilon_ = dum5
        one,two = find_minimum(epsilon_,count_line)
    count_line = count_line + 1