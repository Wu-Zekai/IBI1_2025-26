#读取文件
#file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
#检索是否有in frame stop codons
#import re
#stop_genes = re.findall(r'>.*\n((?:ATG)*?(?:TAA|?:TAG|?:TGA))', file.read())
#!/usr/bin/env python3
# stop_codons.py
# 识别酵母基因中所有框内终止密码子，输出到新 FASTA 文件
# 输出格式：>基因名: 终止密码子1 终止密码子2 ...

import re

def parse_fasta(file_path):
    """读取 FASTA 文件，逐条返回 (header, sequence) 元组"""
    with open(file_path, 'r') as f:
        header = None
        seq_parts = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                if header is not None:
                    yield header, ''.join(seq_parts)
                header = line[1:]   # 去掉 '>'
                seq_parts = []
            else:
                seq_parts.append(line)
        if header is not None:
            yield header, ''.join(seq_parts)

def get_gene_name(header):
    """从 FASTA 标题行提取基因名（第一个空格前的部分）"""
    return header.split()[0]

def find_inframe_stop_codons(dna_seq):
    """
    在 DNA 序列中查找所有框内终止密码子。
    框内定义：从任意 ATG 开始，每3个碱基一组，直到遇到终止密码子（TAA, TAG, TGA）。
    返回找到的终止密码子集合（去重）。
    """
    stop_codons = {'TAA', 'TAG', 'TGA'}
    found = set()
    n = len(dna_seq)
    # 遍历所有可能的起始位置
    for i in range(n - 2):
        if dna_seq[i:i+3] == 'ATG':
            # 从起始位置后第3个碱基开始，步长3
            for j in range(i+3, n-2, 3):
                codon = dna_seq[j:j+3]
                if codon in stop_codons:
                    found.add(codon)
                    break   # 该起始位点只取第一个终止密码子
    return found

def main():
    input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    output_file = 'stop_genes.fa'

    with open(output_file, 'w') as out:
        for header, dna_seq in parse_fasta(input_file):
            stop_set = find_inframe_stop_codons(dna_seq)
            if stop_set:
                gene_name = get_gene_name(header)
                # 将终止密码子排序后以空格分隔
                stop_str = ' '.join(sorted(stop_set))
                # 输出格式：>基因名: 终止密码子1 终止密码子2 ...
                out.write(f'>{gene_name}: {stop_str}\n')
                # 输出原始 DNA 序列，每行 60 个碱基
                for i in range(0, len(dna_seq), 60):
                    out.write(dna_seq[i:i+60] + '\n')
                out.write('\n')   # 记录间空一行（可选）

    print(f"处理完成，结果已保存至 {output_file}")

if __name__ == '__main__':
    main()

