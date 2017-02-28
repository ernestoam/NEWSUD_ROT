import pandas as pd
df = pd.read_csv("/Users/ernestomartinez/Documents/Winter17/Math180/minstep.csv")
for i in range(0,91):
	link = df.Link_Type[i] # link
	tempnewsud = df.NEWSUD_format[i] # tempnewsud
	n = df.step_number[i] # length of tempnewsud
	newsudrot = [] # list of rotations
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]		
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]			
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]			
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]			
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]		
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]					
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]		
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]				
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]		
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]					
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]		
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]			
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]
		else:
			tempnewsud = tempnewsud			
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]		
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]		
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]	
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]		
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]			
	else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]
		else:
			tempnewsud = tempnewsud			
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]
		else:
			tempnewsud = tempnewsud			
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]					
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]		
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]				
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]	
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]	
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]			
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]	
		else:
			tempnewsud = tempnewsud		
	newsudrot.append(tempnewsud)
	for j in range(0,n-1):
		if tempnewsud[j] =='N':
			tempnewsud = tempnewsud[:j] + 'U' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='n':
			tempnewsud = tempnewsud[:j] + 'u' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='E':
			tempnewsud = tempnewsud[:j] + 'N' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='e':
			tempnewsud = tempnewsud[:j] + 'n' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='W':
			tempnewsud = tempnewsud[:j] + 'S' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='w':
			tempnewsud = tempnewsud[:j] + 's' + tempnewsud[j+1:]
		elif tempnewsud[j] =='S':
			tempnewsud = tempnewsud[:j] + 'D' + tempnewsud[j+1:]						
		elif tempnewsud[j] =='s':
			tempnewsud = tempnewsud[:j] + 'd' + tempnewsud[j+1:]			
		elif tempnewsud[j] =='U':
			tempnewsud = tempnewsud[:j] + 'E' + tempnewsud[j+1:]
		elif tempnewsud[j] =='u':
			tempnewsud = tempnewsud[:j] + 'e' + tempnewsud[j+1:]
		elif tempnewsud[j] =='D':
			tempnewsud = tempnewsud[:j] + 'W' + tempnewsud[j+1:]					
		elif tempnewsud[j] =='d':
			tempnewsud = tempnewsud[:j] + 'w' + tempnewsud[j+1:]
		else:
			tempnewsud = tempnewsud
	newsudrot.append(tempnewsud)	
print(newsudrot)
