import jieba
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt

# 读取文本文件
with open('answers.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 从停用词文件中读取停用词
def load_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        stopwords = set(line.strip() for line in f if line.strip())
    return stopwords

# 加载停用词表
stopwords = load_stopwords('stop_words.txt')

words = jieba.cut(text)
filtered_words = [word for word in words if word not in stopwords and len(word.strip()) > 1]  # 过滤掉停用词
word_string = ' '.join(filtered_words)  # 用空格连接分词结果

# 生成词云
wordcloud = WordCloud(font_path='msyh.ttc', width=800, height=600, background_color='white').generate(word_string)

# 显示词云
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 关闭坐标轴显示
plt.show()

# 统计词频
word_counts = Counter(filtered_words)

# 按词频排序并输出前 20 个最常见的词
most_common_words = word_counts.most_common(100)
print("前 100 个最常见的词及其词频：")
for word, freq in most_common_words:
    print(f"{word}: {freq}")