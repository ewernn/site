---
layout: default # page
title: "cs224u project"
# permalink: /URL-PATH
---
*Prompt tuning and semantic interpretation with an LLM*
**Trained and interpreted soft prompts for language understanding tasks using prompt-tuning, a PEFT (Parameter Efficient Finetuning) method. Improves prompting by revising prompt at an embedding level rather than the english level. Found soft prompt diverges more on harder-to-describe tasks, implying English task description is suboptimal, and prompting on an embedding-level can provide greater accuracy (approaching finetuning accuracy).  Analyzed stochasticity and zero-shot transferability of soft prompts.**
## Notes
prompt tuning: simple and effective finetuning method (PEFT method)
	-train prompt parameters for a task instead of giving task description
	-can beat finetuning
testing hypotheses:
1. explore semantic meaning of soft prompts
2. stochasticity of training (Var of accuracy across different train runs)
3. zero-shot task transferability
benefits:
- don't have to think up a perfect prompt. just give it examples
- expands prompting capabilities beyond just English (models think more complexly)

<font style="color:gray"> Found soft prompt diverges more on harder-to-describe tasks, implying English task description is suboptimal, and prompting on an embedding-level can provide greater accuracy. prompt-tuning is often able to beat finetuning because it let's gradient descent find an optimal prompt. gradient descent talks to the machine on an embedding level that English cannot </font> 

### methods
model: `bloomz-560m`
###### train soft prompt
1. start with description of task ("Does hypothesis entail or neutral about premise?")
2. embed prompt
3. optimize prompt on examples
##### a) semantic interpretability
soft-prompt size `(n, 1024)` for `n` trainable tokens
for each token, find `k` nearest tokens (cosine distance) in `bloomz-560m`'s dictionary
- results: 
	- looked at top-3 similar tokens for each soft prompt token
	- a few key words didn't change during training (important to result)
	- sometimes a token would be in another language like Chinese
	- model likes to be explicitly told to be accurate
##### b) Stochasticity
trained each task 4 times for 50 epochs (`Adam` optimizer randomly initializes momentum vectors)
project all 16 `(n,1024)` soft prompts into 2D using t-SNE
- results:
	- more complicated tasks deviate more from original prompt
	- all 4 train runs for each task resulted in equidistant t-SNE distances
##### c) zero-shot task transferability
1. subtract prompt embeddings (B-A) to find similarity between tasks (Frobenius norm)
2. get accuracy of RTE's soft prompt on WSC's validation set
- see if there is a relation between soft-prompt-similarity and task-transferability
- results
	- obviously, the more different, the less transferrable
	- most soft prompt transfer improved accuracy versus no prompt (90% of transfers)

prefix tuning: prepends trainable parameters to the hidden states of all transformer blocks

<font style="color:green">Text Color</font>
<font style="color:green">Text Color</font>


## Takeaways
- understanding inner workings of prompts $\rightarrow$ better design choices
- in 3 of 4 tasks, token for "accurate" appeared in soft prompt, implying model likes to be explicitly told to be accurate
- word "entailed" persisted thru training (important tokens don't change)
- less semantic meaning than we thought, highlighting interpretability problem
- there are many/infinite soft prompts that get the same accuracy (stochasticity)
- transferability (soft prompts encode more than just task, such as "be accurate")



## Questions still
refresh on similarity metrics like cosine