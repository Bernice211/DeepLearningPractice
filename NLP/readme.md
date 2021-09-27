NLP走近自然语言处理
概念
日常对话、办公写作、日常上网
希望机器能像人一样去理解，以人类自然语言理解为载体的文本所包含的信息，并完成一些特定任务
内容
中文分词、词性标注、命名实体识别、关系抽取、关键词提取、信息抽取、依存分析、词嵌入。。。
应用
篇章理解、文本摘要、情感分析、知识图谱、文本翻译、问答系统、聊天机器人。。。


NLP WordEmbedding的概念和实现

背景
如何表示词语所包含的语义？

苹果？水果？Iphone?
苹果、梨子，这两个词相关吗？

语言的表示
符号主义：Bags-of-word,纬度高、过于系数、缺乏语义、模型简单(eg.苹果[1,0,0,0,0],梨子[0,1,0,0,0]),容易造成维数灾难
分布式表示：Word Embedding, 维度低、更为稠密，包含语义、训练复杂，维度有限，每个维度上都有确确实实的值，可以通过计算相似度来衡量两个词之间的关系（eg.苹果[0.1,0.4,0.2],梨子[0.2,0.1,0.5]）

Word Embedding
核心思想：语义相关的词语，具有相似的上下文环境，e.g. 苹果，梨子
所做的事情：将每个词语训练成词向量

时间
基于gensim包和中文维基百科
gensim:http://radimrehurek.com/gensim/models/word2vec.html
中文维基分词语料：https://pan.baidu.com/s/1o8wG9g2

#加载包
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

#训练模型
sentences=LineSentence('wiki.zh.word.text')
model=Word2Vec(sentences,size=128,window=5,min_count=5,workers=4)

#保存模型
model=Word2Vec.load("word_embedding_128)

#使用模型
items=model.most_similar(u'中国')
model.similarity(u'男人',u'女人')

