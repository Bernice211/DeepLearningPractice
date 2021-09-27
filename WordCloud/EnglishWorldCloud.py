from wordcloud import WordCloud
import matplotlib.pyplot as plt
 
#打开文本
text= open('constitution.txt').read()
#生成对象
wc=WordCloud().generate(text)

#显示词云
plt.imshow(wc,intepolation='bilinear')
plt.axis('off')
plt.show()

#保存到文件
wc.to_file('wordcloud.png')

# WordCloud()的可选参数
# font_path:可用于制定字体路径，包括otf和ttf
# width:词云的宽度，默认为400
# height:词云的高度，默认为200
# mask:蒙版，可用于定制词云的形状
# min_font_size:最小字号，默认为4
# max_font_size:最大字号，默认为词云高度
# max_words:词的最大数量，默认为200
# stopwords:将被忽略的停用词，如果不指定则使用默认的停用词词库
# backgroud_color:背景颜色，默认为black
# mode：默认为RGB模式，如果为RGBA模式且background_color设为none,则背景将透明
