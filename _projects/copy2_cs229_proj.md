---
layout: default # page
title: "cs229 project"
# permalink: /URL-PATH
---
# Fine-tuning CNN for GeoGuessr Classification using Google Streetview Images

## Objective: 
Enhanced a pre-trained ResNet50 model to classify Google Streetview images into 20 distinct countries with a focus on boosting performance through modified architectures and custom loss functions.

## Model Development:
Adapted ResNet50 by removing the last layer, freezing initial weights, and adding a new 20-class output layer.
Introduced an additional training strategy by unfreezing the last stage of ResNet, which consists of 16 blocks with a 3-layer structure each.

## Data & Augmentation:
Utilized a dataset of 50,000 normalized Google Streetview images (224x224x3).
Augmentation techniques: Flipping, rotation, and cropping for enhanced generalization.

## Training Strategy:
Hyperparameter Optimization: Systematically sampled learning rate ($\alpha_{lr}$), batch size, Haversine weight ($\alpha_{\text{Haversine}}$), and decay factor ($\gamma_{decay}$). Randomly sampled combinations over 30 iterations, followed by an extended 40-epoch training on the optimal set.
Custom Loss Function: Combined cross-entropy with a Haversine distance-based term to account for visual similarities among geographically proximate countries.

## Performance Results:
Feature extraction method yielded 40.3% accuracy.
Fine-tuning with standard cross-entropy achieved 58.5% accuracy.
Incorporating the custom loss function led to a substantial improvement, reaching 72.5% classification accuracy.
