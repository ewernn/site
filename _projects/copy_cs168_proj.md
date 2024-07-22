---
layout: default # page
title: "cs168 project"
# permalink: /URL-PATH
---

# Investigated Vector Similarity Search techniques

> Investigated benefits and tradeoffs (like precision vs. recall) of various low- and high-dimensional embedding similarity searches; Locally-Sensitive Hashing (LSH), KNN, PCA, dimension reduction/compression


### Techniques
- k-d trees: works well for low-dimensional embeddings (<25)
- but... **curse of dimensionality**; $O(n^2)$ compare time
- enter... LSH (locally sensitive hashing)!
	- first, define measure of similarity (cosine, euclidian) (how close data is in original space)
	- maps similar data to same buckets, and dissimilar data to different buckets
	- uses ***multiple hash functions*** (i.e. majority of hash functions agree is data is similar)
		- also, AND- and OR-construction to reduce false positive and negatives, respectively
- ANNOY builds forest of BSTs to perform ANN search (approx. nearest neighbors)
	- **non-random hyperplane splitting** $\rightarrow$ better with large data
- also mentioned is Faiss (Facebook AI Similarity Search), for 5-10x speedup on GPU

### Measures
- Jaccard Similarity: $J(A,B) = {|A\cap B|\over|A\cup B|}$ (for binary vectors; absence/presence of feature is key)
- $L_2$ Distance: $L_2(A,B) = \sqrt{\sum_i(a_i-b_i)^2}$ (not normalized; longer docs ~ larger distance)
- Cosine Similarity: $\cos(\theta)={A\cdot B\over ||A|| ||B||}$ (normalized over sequence length)

**Next steps:** VSS is widely used. LSH and optimized libraries like Faiss are critical at scale (beating O(n))
Now, focus is on getting better embeddings and hardware optimizations