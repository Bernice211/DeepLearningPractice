#加载包
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

from gensim.models import word2vec
import time

#训练模型
# t0=int(time.time())
# sentences=word2vec.LineSentence('wiki.zh.word.text')
# model=word2vec.Word2Vec(sentences,vector_size=128,window=5,min_count=5,workers=4)
# print('训练耗时 %d s' % (int(time.time())-t0))

#保存模型
#model.save('word_embedding_128')

#使用模型
model=word2vec.Word2Vec.load('word_embedding_128')
#相关词
items=model.wv.most_similar('数学') #默认返回前十个最相关的词
for i,item in enumerate(items):
    print(i,item[0],item[1])
#语义类比
print('='*20)
items=model.wv.most_similar(positive=['纽约','中国'],negative=['北京'])
for i in enumerate(items):
    print(i,item[0],item[1])
#不相关词
print('='*20)
print(model.wv.doesnt_match(['早餐','午餐','晚餐','手机']))
#计算相关度
print('='*20)
print(model.wv.similarity('男人','女人'))

