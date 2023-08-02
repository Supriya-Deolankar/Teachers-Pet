from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

def vectorize(text):
  return TfidfVectorizer().fit_transform(text).toarray()

def similarity(doc1, doc2):
  return cosine_similarity([doc1,doc2])

def check_plagarism(s_vectors):
  plagarism_results = set()
  for i in range(0,len(s_vectors)):
    student_a, text_vector_a = s_vectors[i]
    for j in range(i+1,len(s_vectors)):
      student_b, text_vector_b = s_vectors[j]
      sim_score = similarity(text_vector_a, text_vector_b)[0][1]
      score = (student_a,student_b,sim_score)
      plagarism_results.add(score)
    return plagarism_results

@st.cache_data
def get_results(notes,s_names):
    vectors = vectorize(notes)
    s_vectors = list(zip(s_names,vectors))
    scores = check_plagarism(s_vectors)
    print(scores)
    results = []
    for data in scores:
        if data[2]>0.8:
            results.append(data)
    return results