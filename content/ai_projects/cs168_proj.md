---
layout: default # page
title: "cs168 project"
# permalink: /URL-PATH
---
# Exploration of Vector Similarity Search Techniques

## Overview:
Delved into the nuances of low- and high-dimensional embedding similarity searches. Assessed the benefits and tradeoffs such as precision versus recall, exploring methods including LSH, KNN, PCA, and dimension reduction techniques.

## Key Insights:
- **k-d trees**: Effective for low-dimensional embeddings (<25). However, limited by the curse of dimensionality, resulting in $O(n^2)$ comparison time.
- **Locally-Sensitive Hashing (LSH)**: Utilized multiple hash functions to classify similar data into the same buckets. Enhanced performance using AND- and OR-constructions to mitigate false positives/negatives.
- **ANNOY**: Built using a forest of binary search trees for approximate nearest neighbors. Leveraged non-random hyperplane splitting for superior performance with large datasets.
- **Faiss (Facebook AI Similarity Search)**: Recognized for delivering 5-10x speedup on GPU.

## Evaluation Metrics:
- **Jaccard Similarity**: Useful for binary vectors, focusing on the absence or presence of features.
- **$L_2$ Distance**: Effective for unnormalized data where longer sequences equate to larger distances.
- **Cosine Similarity**: Offers normalization over sequence length.

## Conclusions and Future Work:
Vector Similarity Search (VSS) holds pivotal importance. Techniques like LSH and optimized libraries, such as Faiss, demonstrate superiority at scale. Current endeavors pivot towards refining embeddings and advancing hardware optimizations.