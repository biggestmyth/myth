
firsteven =int(input (" even number:"))
firstodd =int(input ("odd number:"))
maxeven=firsteven
maxodd=firstodd
if(firstodd>firsteven):
    maxall=firstodd
    littleall=firsteven
else:
    maxall=firsteven
    littleall=firstodd
    
totaleven=firsteven
totalodd=firstodd
even20=0
evencounter=1
oddcounter=1
i=1
for i in range(4):
    
    a=int(input("any num:"))
    
    if(a>maxall):
        
        maxall=a
        
    if (a<littleall):
        
        littleall=a
        
    if(a%2==0):
        
        totaleven=totaleven+a
        evencounter=evencounter+1
        
        if(a>maxeven):
            
            maxeven=a
        if(20<a<60):
            even20=even20+1
    else:
        
        totalodd=totalodd+a
        oddcounter=oddcounter+1
        
        if(a>maxodd):
            
            maxodd=a

print("min:"+str(littleall))
print("max:"+str(maxall))
print("max odd:"+str(maxodd))
print("max even:"+str(maxeven))
print("avg odd:"+str(totalodd/oddcounter))
print("avg even:"+str(totaleven/evencounter))
print("numbers bitween 20, 60: "+str(even20)) 
