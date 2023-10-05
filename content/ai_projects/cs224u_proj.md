---
layout: default # page
title: "cs224u project"
# permalink: /URL-PATH
---
# Project Overview: Prompt Tuning for Language Models

## Background
Prompt tuning allows language models to learn new tasks and capabilities without full fine-tuning, enabling more efficient and customizable training. This project explored prompt tuning through training and interpreting soft prompts on language understanding tasks.

## Methods
- Used the Bloomz 560M model and optimized soft prompts on examples for tasks like natural language inference.
- Analyzed the semantic meaning of soft prompts by finding nearest neighbor tokens.
- Evaluated stochasticity via multiple train runs and visualizing variance.
- Assessed zero-shot transferability by testing prompts on new datasets.

## Key Findings
- Soft prompts diverge more on complex tasks, suggesting prompts can improve on English descriptions.
- Semantic interpretability remains limited, though some key tokens persist.
- Significant stochasticity exists, with multiple distinct prompts achieving similar accuracy.
- Prompts encode more than just the task and allow some transferability.

## Takeaways
- Prompt tuning surpasses finetuning and provides embedding-level communication.
- Inner workings of prompts enable better design choices.
- There are opportunities to improve prompt interpretability.
- Prompts exhibit meaningful variance uncaptured by accuracy.

This provides an overview of the project's goals, techniques, results, and conclusions, highlighting the advantages of prompt tuning and areas for further research. The focus is on communicating the essence and impact to potential employers. Details can be expanded on in an interview.