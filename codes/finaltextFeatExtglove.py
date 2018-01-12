#FeatureExtract
#Extract
# Read the query file
#
#
# from keras.applications.vgg16 import VGG16
# from keras.preprocessing import image
# from keras.applications.vgg16 import preprocess_input
import numpy as np
# from keras.preprocessing import image
# import json
# import skipthoughts
import pickle
# import penseur
import sys

# %matplotlib inline
import os, argparse
import cv2, spacy, numpy as np
from keras.models import model_from_json
from keras.optimizers import SGD
from sklearn.externals import joblib
import sys
import os

print(sys.path)


def get_question_features(question):
    ''' For a given question, a unicode string, returns the time series vector
    with each word (token) transformed into a 300 dimension representation
    calculated using Glove Vector '''
    word_embeddings = spacy.load('en', vectors='en_glove_cc_300_1m_vectors')
    tokens = word_embeddings(question)
    question_tensor = np.zeros((1, len(tokens), 300))
    for j in xrange(len(tokens)):
            question_tensor[0,j,:] = tokens[j].vector
#     print(question_tensor.shape())
    return question_tensor
# question = u"What vehicle is in the picture?"
# question_features = get_question_features(question)
# print(question_features.flatten().shape)
# if isinstance(question_features,np.ndarray):
#     print('yes')
#modelSent= skipthoughts.load_model()
# sys.path = ['', '/home/subha/anaconda3/envs/python2/bin', '/home/subha/anaconda3/envs/python2/lib/python2.7/site-packages/distribute-0.6.19-py2.7.egg', '/home/subha/anaconda3/envs/python2/lib/python2.7/site-packages/StarCluster-0.95.6-py2.7.egg', '/home/subha/anaconda3/envs/python2/lib/python2.7/site-packages/iso8601-0.1.12-py2.7.egg', '/home/subha/anaconda3/envs/python2/lib/python2.7/site-packages/scp-0.10.2-py2.7.egg', '/home/subha/anaconda3/envs/python2/lib/python2.7/site-packages/optcomplete-1.2_devel-py2.7.egg', '/home/subha/anaconda3/envs/python2/lib/python2.7/site-packages/iptools-0.6.1-py2.7.egg', '/home/subha/anaconda3/envs/python2/lib/python2.7/site-packages/workerpool-0.9.4-py2.7.egg', '/home/subha/anaconda3/envs/python2/lib/python2.7/site-packages/paramiko-2.2.1-py2.7.egg', '/home/subha/anaconda3/envs/python2/lib/python2.7/site-packages/backports.weakref-1.0rc2.dev4_ge88e083-py2.7.egg', '/home/subha/anaconda3/envs/python2/lib/python2.7/site-packages/setuptools-19.2-py2.7.egg', '/home/subha/ReferralExp/ObjectRetreival/natural-language-object-retrieval', '/home/subha/caffe/python', '/home/subha/caffe/distribute/python', '/home/subha/python', '/srv/share/gpu_lock', '/home/subha/anaconda3/envs/python2/lib/python27.zip', '/home/subha/anaconda3/envs/python2/lib/python2.7', '/home/subha/anaconda3/envs/python2/lib/python2.7/plat-linux2', '/home/subha/anaconda3/envs/python2/lib/python2.7/lib-tk', '/home/subha/anaconda3/envs/python2/lib/python2.7/lib-old', '/home/subha/anaconda3/envs/python2/lib/python2.7/lib-dynload', '/home/subha/.local/lib/python2.7/site-packages', '/home/subha/anaconda3/envs/python2/lib/python2.7/site-packages/Sphinx-1.5.1-py2.7.egg', '/home/subha/anaconda3/envs/python2/lib/python2.7/site-packages', '/home/subha/anaconda3/envs/python2/lib/python2.7/site-packages/IPython/extensions', '/home/subha/.ipython']+ sys.path
# # sys.path.append('/home/subha/RefExpCVPR2018/penseur')
# # p = penseur.Penseur()
# #
# # # model = VGG16(weights='imagenet', include_top=False)
# # with open('/home/subha/ReferralExp/ObjectRetreival/natural-language-object-retrieval/data/metadata/referit_query_dict.json') as fp:
# #     d = json.load(fp)
#
# #print(d)
# #1. list of sentences
# #2. list of numpy arrays
# #3. skip thought vectors
# # train=[]
# # dev=[]
# # sentences=[]
# # imgFeatures=[]
# # skipThought=[]
# #
# # img_id=[]
# # caption=[]
textFeatures=[]
sentences=[]
with open("/home/subha/RefExpCVPR2018/penseur/captions.txt","rb") as fp:
    cap = pickle.load(fp)
with open("/home/subha/RefExpCVPR2018/penseur/img_id.txt","rb") as fp1:
    imgId = pickle.load(fp1)

for c,i in zip(cap,imgId):
    print('loading')
    for sen in c:

        try:
            # print(sen)
            f= get_question_features(sen)
            f=f.flatten()
            textFeatures.append(f)
            with open("/home/subha/RefExpCVPR2018/penseur/textFeaturescacheLSTM/text_"+i+ ".txt","wb+") as fp2:
                pickle.dump(f,fp2)

            sentences.append(sen)
        except:
            print('no')
            pass


# for key, value in d.iteritems():
#     img_id.append(key)
#     caption.append(value)
# print(len(img_id))
# print(len(caption))
#print(caption)
#print('Extracting')
#textFeatures= skipthoughts.encode(modelSent,caption)
# for i in range(len(caption)):
#     print(i)
#     # img = image.load_img('/home/subha/ReferralExp/ObjectRetreival/natural-language-object-retrieval/data/resized_imcrop/'+img_id[i]+'.png'
#     # , target_size=(224, 224))
#     # x=image.img_to_array(img)
#     # x = np.expand_dims(x,axis=0)
#     # x = preprocess_input(x)
#     # features=model.predict(x)
#     # imgFeatures.append(features)
#     sentences.append(caption[i])
#     #print(sentences)
#     textFeatures=skipthoughts.encode(modelSent,[caption[i]])
#     skipThought.append(textFeatures)
#print(caption[0])
with open("textFeaturesLSTM.txt","wb+") as fp:
    pickle.dump(textFeatures,fp)
with open("sentences.txt","wb+") as fp1:
    pickle.dump(sentences,fp1)
# print(sentences,imgFeatures,skipThought)
