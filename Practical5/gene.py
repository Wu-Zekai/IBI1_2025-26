import matplotlib.pyplot as plt
gene_expression = {
    'TP53': 12.4,
    'EGFR': 15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7
}


gene_expression['MYC'] = 11.6

print("Gene Expression Dictionary:")
print(gene_expression)
print("-" * 30)

total_expression = sum(gene_expression.values())
average_expression = total_expression / len(gene_expression)
print(f"Average gene expression level: {average_expression:.2f}")


gene_to_find = 'BRCA1'  

print(f"Searching for gene: {gene_to_find}")
if gene_to_find in gene_expression:
    print(f"The expression value for {gene_to_find} is {gene_expression[gene_to_find]}")
else:
    print(f"Error: The gene '{gene_to_find}' was not found in the dataset.")
print("-" * 30)


genes = list(gene_expression.keys())
values = list(gene_expression.values())

plt.figure(figsize=(10, 6))
plt.bar(genes, values, color='skyblue')
plt.xlabel('Gene Name')
plt.ylabel('Expression Value')
plt.title('Gene Expression Levels Across Sample')
plt.show()