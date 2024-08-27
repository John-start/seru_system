# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置 Seaborn 样式
sns.set(style="whitegrid")

# 读取 CSV 文件
df = pd.read_csv('适应度汇总.csv')

# 创建一个图表对象和子图
plt.figure(figsize=(12, 8))

# 绘制算法1的适应度曲线
plt.plot(df['序号']+1, df['无邻域搜索'], 
        color='#397fc7', 
        #  marker='o', 
        alpha = 0.7,
        linestyle='--', 
        linewidth=3, 
        markersize=8, 
        label='Genetic Algorithm')

# 绘制算法2的适应度曲线
plt.plot(df['序号']+1, df['有邻域搜索'], 
        color='#bf1d2d', 
        #  marker='s', 
        alpha = 0.7,
        linestyle='--', 
        linewidth=3, 
        markersize=8, 
        label='Genetic algorithm with neighborhood search')

# 添加图表标题和轴标签
plt.xlabel('Generation', fontsize=14)
plt.ylabel('The kernel of total weighted completion time', fontsize=14)

# 设置坐标轴刻度的字体大小
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# 添加网格线
plt.grid(True, which='both', linestyle='-', linewidth=0.7, alpha=0.7)

# 显示图例
plt.legend(fontsize=12)

# 显示图表
plt.tight_layout()
plt.show()



