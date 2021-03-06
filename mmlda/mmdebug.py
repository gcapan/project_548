from lda import LDA, _doc_update, _slice_doc_update
import pickle
import numpy as np

np.seterr(divide="raise")

from data.datafile import AADataFile
dfile = pickle.load(open("data/datafile.pkl"))

dt = dfile.DT
te = dfile.TE

f = te.toarray().argmax(axis=1)

lda = LDA(K=10, n_jobs=8, nr_em_epochs=20)

perp, b, g, e = lda.fit(dt, f)