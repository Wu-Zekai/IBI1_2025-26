import matplotlib.pyplot as plt
expressions={'TP53':12.4,'EGFR':15.1,'BRCAC1':8.2,'PTEN':5.3,'ESR1':10.7}
print(expressions)
expressions['MYC']=1.6
print(expressions)
genes = list(expressions.keys())
values = list(expressions.values())
plt.bar(genes, values)
plt.xlabel('Genes')
plt.ylabel('Expression Levels')
plt.title('Gene Expression Levels')
plt.show()