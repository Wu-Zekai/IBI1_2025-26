# Pseudocode:
# 1. Define total population n = 91.
# 2. Set initial infected individuals to 5.
# 3. Set growth rate to 0.4 (40%).
# 4. Use a counter for days, starting at day 1.
# 5. Use a while loop that runs as long as infected individuals < 91.
# 6. Inside loop: Calculate new infections, increment day counter, and print status.
# 7. Stop once everyone is infected and report the total days taken.
#initial number a=5
a=5
#days
b=1
#all students n=91
#if a>n stop
#else a=a*1.4 keep increasing b by 1
print("days:",b,"people:",a)
while a<91:
	a=a*1.4
	b=b+1
	print("days:",b,"people:",a) 
