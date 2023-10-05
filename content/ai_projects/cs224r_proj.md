---
layout: default # page
title: "cs224r project"
# permalink: /URL-PATH
---
# Efficiency-Boosted Robotic Reinforcement Learning via VC-1 Visual Encoding

## Objective:
Enhance sample efficiency in D4RL's Franka kitchen's sequential robotic arm tasks using a modified VRL3 reinforcement learning framework.

## Key Implementation:
- **Forked VRL3 Framework**: Incorporated VC-1, a vision foundation model transformer (ViT) for Embodied AI, leading to a 5x surge in sample efficiency.
- **VC-1 Enhancements**: Tailored for object rearrangement, bridging the simulation-to-reality gap and emphasizing on end-effector and object outlines.
- **VRL3 Modifications**: Transformed the VRL3 stages by integrating RLPD for robust exploration and a 1.5x efficiency bump in online fine-tuning. Replaced off-policy actor-critic algorithm 'DrQv2' with calibrated Q-learning (Cal-QL).
- **Image Processing**: Scaled images by 3.5x to match VC-1's 224x224 input dimensions.

## Findings & Takeaways:
- **Enhanced Navigability**: Mastery in comprehending and modifying extensive codebases, aligned with production-level code practices.
- **Sample Efficiency**: Crucial for cost, time, and capability; benefits derived from off-policy data reuse and visual pretraining.
- **Optimization Insights**: During stage 2, a combination of representation learning and conservative RL outperformed sole representation learning. In stage 3, RLPD's sample split (50% offline and 50% online expert demonstrations) was vital.
- **Evaluation**: The adapted model completed 3 of the 4 tasks in 1.5M steps, endorsing its potential.

## Conclusions:
The integration of VC-1 within the VRL3 framework substantially elevated the sample efficiency of model-free reinforcement learning for robotic arm tasks. This project encapsulates a significant step towards practical, sample-efficient reinforcement learning in real-world robotic applications.