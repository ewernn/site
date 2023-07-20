---
layout: notes
title: "nanda_transformer"
---
#### [[*]](https://youtu.be/bOYE6E8JrtU){:target="_blank"} What is a transformer?

### How a transformer block works, algebraically

* $$A$$ attention: "where do I move information from?"
* $$x$$: residual stream
* $$W_v$$: values of prompt tokens, "what info do I move to my current position"
* $$W_o$$: head --> residual stream
* $$A,x$$ are **activations**, $$W_o,W_v$$ are **parameters**

### $$A ~~~ x ~~~ W_v^T ~~~ W_o^T$$

### $$(A ~ (x ~ W_v^T)) ~ W_o^T$$

shapes $$(p_{dest},p_{source})\times(p_{source},d_{model})\times(d_{model}, d_{head})\times(d_{head},d_{model})$$

note on hopeless intution for values:values are kinda meaningless; they are just a low-rank intermediate state in part of a larger $$d_{model} \times d_{model}$$ matrix $$W_{ov} = W_o W_v$$.
<!-- residual stream = context vector -->

##### me trying to explain how a transformer works
1. input text is embedded (most simply, a one-hot vector of length $$d_{dictionary}$$)
    * embedding is a lookup table mapping tokens to vectors
2. embedded text is run through series of blocks, with a residual stream carrying the word past each layer
    * each block runs attention on input, and sends this through an MLP
        * context vector: for *each* of the input tokens, **attention** is run on it's prior (causal) tokens
        * then, the `context_window_length` context vectors are passed through MLP, which outputs `softmax(log(logits))`
            * note that `softmax` and `log` don't change dimension, and `logits` is a vector with an entry for each token in the dictionary
        * a 100% confident prediction would be if the MLP output a one-hot vector
3. the `softmax`'ed vectors are sampled to generate a next-token prediction

* multihead attention: if `d_{embedding} = 512` and `n_heads = 8`, then each attention head operates in a subspace of size `512/8 = 64`


## useful comments

**model attends to context vectors, not tokens**: In mech interp, high activation on a full stop doesn't mean the full stop was highly relevant; it means that the model compressed info about setence into the full-stop's residual stream. Keep in mind, each token's residual stream is a function of all previous tokens, so the model doesn't need to look at each token individually.