
import jieba.analyse

content=u'中国特色社会主义是我们党领导的伟大事业，全面推进党的建设新的伟大工程，是这一伟大事业取得胜利的关键所在。党坚强有力，事业才能兴旺发达，国家才能繁荣稳定，人民才能幸福安康。党的十八大以来，我们党坚持党要管党、从严治党、凝心聚力、直击积弊、扶正祛邪，党的建设开创新局面，党风政风呈现新气象。习近平总书记围绕从严管党治党提出一系列新的重要思想，为全面推进党的建设新的伟大工程进一步指明了方向。'

# keywords=jieba.analyse.extract_tags(content,topK=20,withWeight=True,allowPOS=())#填入'n','nr','ns'进行词性的过滤，如果什么都不填就默认不进行词性的过滤
# for item in keywords:
#     print(item[0],item[1])

keywords=jieba.analyse.textrank(content,topK=20,withWeight=True,allowPOS=('ns','n','vn','v'))#填入'n','nr','ns'进行词性的过滤，如果什么都不填就默认不进行词性的过滤
for item in keywords:
    print(item[0],item[1])


