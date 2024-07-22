---
layout: default # page
title: "cs224r project"
# permalink: /URL-PATH
---
# Training Robotic arm w/ visual encoder and model free reinforcement learning
> Forked Microsoft's VRL3 reinforcement learning framework to improve sample efficiency.
> 
> Replaced basic image encoder with VC-1, a foundation model trained specifically for Embodied AI for 5x increased sample efficiency.
> 
> Added RLPD (Reinforcement Learning from Prior Data) to improve robustness during exploration and increase online finetuning sample efficiency by 1.5x

objective: solve/(improve sample efficiency) D4RL's Franka kitchen (4 consecutive tasks)
what we did: we combined VC-1 with VRL3 to improve sample efficiency further (50%?)

### VC-1 notes:
- ...is a vision foundation model transformer (ViT) for Embodied AI
- trained with MAE, so it's useful for reconstructing images, which is useful downstream to extract features for tasks such as object rearrangement
- bridges domain gap sim->real
- by finetuning, VC-1 focuses much more on end-effector and object outlines
### VRL3 notes
([link](https://sites.google.com/nyu.edu/vrl3))
Stages:
1) Pretrain image encoder on ImageNet
2) Offline RL
	- **finetune encoder** and **train actor/critic network** on expert demonstrations
	- critical stage b/c of sparse reward
3) Online RL (RLPD)

Visual learning is hard
1) visual input
2) sparse reward
3) high-D action space
Only 3 relevant hyperparams: $\alpha$ (policy, Q-networks), exploration action noise, and $\alpha_{encoder} \sim \frac{\alpha}{10}$ 
Stage Transitions
- 1 -> 2: CCE (conv. channel expansion) to allow first encoder to take in multiple frames
- 2 -> 3: Safe Q: set max-Q value to smoothly transition

### VCRL differences
- VC-1 takes in 224x224 instead of 64x64, so we upscaled images by 3.5x
- Use calibrated Q-learning (Cal-QL) instead of off-policy actor-critic algo 'DrQv2'


### Takeaways
- got great at navigating and understanding large codebases
- learned good practice for production-level code
- sample efficiency is great (cost, time, capability)
	- off-policy is for data reuse is great
	- visual pretraining makes visual input tractable
- offline expert demonstrations are necessary
- in stage 2
	- learning representation+task(conservative RL) > learning just representation
	- We (bad idea) switched from actor-critic to Cal-QL because action space is large. Over-estimation in OOD data
- in stage 3
	- RLPD samples 50% offline and 50% online expert demos (sample randomly before)
	- mitigate overestimating Q-values
		- 1 actor 10 critics 😈 to average out, and avoid blowup from stochasticity
		- also, layer norm
- We showed that eval on Franka completed 3 of 4 tasks after 1.5M steps, showing promise
- We also observed 5x improved sample efficiency by switching from IL to BC during pretraining
- Immersed within production-level RL framework and codebase
- Improved sample efficiency a lot with VC-1 instead of ResNet18



