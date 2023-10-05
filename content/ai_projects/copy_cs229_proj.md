---
layout: default # page
title: "cs229 project"
# permalink: /URL-PATH
---
*Finetuned Convolutional Neural Net (CNN) to play GeoGuessr (image classification)*
**Finetuned ResNet50 by replacing the last 9 (of 50) layers and classifying on 20 different countries (from 38k Google Streetview screenshots). Ran data augmentation and hyperparameter tuning to achieve 72.5% classification accuracy.**

**METHOD:** 
	Finetuned ResNet50 by removing last layer, freezing weights, adding 20-class fully connected layer (softmax(log($\hat{y}$))), and retraining on data
**METHOD 2:** 
	also unfreeze last **stage**.
	ResNet has 4 stages with 16 blocks total. Each block has 3 layers (2 1x1xC, 1 3x3x1)
**HYPERPARAMETER TUNING:** 
	sampled $\alpha_{lr}, \texttt{batch\_size}, \alpha_{\text{Haversine}}, \gamma_{decay}$ 
	picked 4 values for each, and sampled randomly 30 times, running 10 epochs
	then, ran 40 epochs on optimal hyperparams
**DATA:** 
	50k (224,224,3) normalized Google street view images
	augment: flip, rotate, crop
**TRAINING**: 
	custom loss function to *express* visual similarity of geometrically-close countries
	$\text{loss}(y, \hat y) = \sum_i -y^{(i)}\log \hat y^{(i)}$ + $\alpha \sum_i d_{\text{Haversine}}(\hat y^{(i)} - y^{(i)})$ 
**RESULTS:** 
	40.3% classification accuracy with feature extraction
	58.5% classification accuracy with finetuning (CE loss)
	72.5% classification accuracy with finetuning (custom loss)
