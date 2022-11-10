from gensim.models import fasttext
from gensim.test.utils import datapath
import plotly.express as px
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd

# Load fasttext pre-trained model
wv = fasttext.load_facebook_vectors(datapath('/home/pc-bonito/Projects/fasttext-test/models/cc.ja.300.bin'))

vocab = [ '父', '母', '兄', '姉', '祖父', '祖母', '両親', '家族', '弟', '妹', '息子', '娘',
          '今日', '明日', '昨日', '来週', '今週', '先週', 'おととい', '来年', '去年',
          '月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日', '曜日',
          '春', '夏', '秋', '冬' ]

# Construct a dataframe for pca
data_matrix = np.zeros([300, len(vocab)])

i = 0
for word in vocab:
    word_emb = wv[word]

    data_matrix[:, i] = word_emb
    i+=1

df = pd.DataFrame(data_matrix, columns = vocab)

# Perform PCA
n_components = 3
pca = PCA(n_components=n_components)
components = pca.fit_transform(df)

# Projects vectors onto principal components
projection = np.zeros([n_components, len(vocab)])
i=0
for collumn in data_matrix.transpose():
    projection[:, i] = np.dot(components.transpose(), collumn)
    i+=1

# Plot scatter graph
fig = px.scatter_3d(projection.transpose(), x=0, y=1, z=2, color=vocab)
fig.show()