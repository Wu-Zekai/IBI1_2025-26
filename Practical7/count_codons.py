import matplotlib.pyplot as plt # type: ignore
from collections import Counter

def get_user_input():
    """要求用户输入指定的终止密码子并验证"""
    valid_stops = ['TAA', 'TAG', 'TGA']
    while True:
        user_choice = input("请输入一个终止密码子 (TAA, TAG, TGA): ").strip().upper()
        if user_choice in valid_stops:
            return user_choice
        print(f"输入无效！请确保输入的是 {valid_stops} 中的一个。")

def get_upstream_codons(sequence, target_stop):
    """
    识别最长 ORF 并提取该终止子之前的所有密码子。
    '最长' 意味着寻找读码框内最后一个出现的 target_stop。
    """
    # 将序列按 3 个一组切分为密码子列表
    # 范围到 len-2 是为了确保最后不满 3 个碱基的剩余部分被忽略
    codons = [sequence[i:i+3] for i in range(0, len(sequence) - 2, 3)]
    
    # 找到所有匹配目标终止子的索引
    indices = [i for i, codon in enumerate(codons) if codon == target_stop]
    
    if not indices:
        return [] # 如果这个基因里没有用户要的那个终止子，返回空列表
    
    # 题目要求：考虑产生最长 ORF 的那个 (即索引最大的那个)
    longest_stop_idx = max(indices)
    
    # 返回该终止子之前的所有密码子
    return codons[:longest_stop_idx]

def process_fasta_and_count(filename, target_stop):
    """读取文件并汇总所有符合条件的基因的密码子计数"""
    total_counts = Counter()
    
    with open(filename, 'r') as f:
        header = None
        sequence_parts = []
        
        for line in f:
            line = line.strip()
            if not line: continue
            
            if line.startswith('>'):
                if header:
                    full_seq = "".join(sequence_parts).upper()
                    # 检查是否以 ATG 开始
                    if full_seq.startswith('ATG'):
                        upstream = get_upstream_codons(full_seq, target_stop)
                        total_counts.update(upstream)
                
                header = line
                sequence_parts = []
            else:
                sequence_parts.append(line)
        
        # 处理最后一个基因
        if header:
            full_seq = "".join(sequence_parts).upper()
            if full_seq.startswith('ATG'):
                upstream = get_upstream_codons(full_seq, target_stop)
                total_counts.update(upstream)
                
    return total_counts

def create_visual_report(counts, target_stop):
    """生成并保存饼图"""
    if not counts:
        print("未发现匹配数据，无法生成图表。")
        return

    # 准备数据：按出现次数从高到低排序，取前 30 个（可选，因为 64 个全放饼图太挤了）
    # 这里我们展示所有密码子，但调整字体
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    labels = [item[0] for item in sorted_items]
    sizes = [item[1] for item in sorted_items]

    plt.figure(figsize=(12, 12))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 7})
    plt.title(f"Codon Distribution Upstream of {target_stop} (Longest ORF)")
    
    # 保存文件
    output_file = f"codon_dist_{target_stop}.png"
    plt.savefig(output_file)
    print(f"\n统计报告已完成：")
    print(f"1. 详细计数已输出到控制台。")
    print(f"2. 饼图已保存为文件: {output_file}")

if __name__ == "__main__":
    # 请确保文件名正确
    FILENAME = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    
    # 步骤 1: 获取用户选择
    chosen_stop = get_user_input()
    
    # 步骤 2: 计算
    print(f"正在扫描文件并计算以 {chosen_stop} 结尾的最长 ORF...")
    codon_stats = process_fasta_and_count(FILENAME, chosen_stop)
    
    # 打印部分结果到屏幕
    print("\n各密码子出现频次 (前 10 名):")
    for codon, count in codon_stats.most_common(10):
        print(f"{codon}: {count}")
    
    # 步骤 3: 绘图并保存
    create_visual_report(codon_stats, chosen_stop)