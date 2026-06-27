(generative_ai)=
# Generative Artificial Intelligence

## Introduction

This chapter introduces the foundations and applications of Generative Artificial Intelligence (Gen AI), with an emphasis on the mathematical and architectural principles that make modern AI systems capable of language understanding, reasoning, and autonomous action.

Section {ref}`sec:gai_whatisgenai` establishes the conceptual underpinnings: the history of AI and the notion of general intelligence, the distinction between discriminative and generative probabilistic models, the role of temperature in controlling generation, and a taxonomy of generative systems. Section {ref}`sec:gai_llm` develops the theory of large language models, from early n-gram approaches to the Transformer architecture — deriving the scaled dot-product attention mechanism, multi-head attention, positional encodings, and the decoder-only causal design used in modern language models. Section {ref}`sec:gai_training` covers the three-phase training pipeline: unsupervised pre-training on next-token prediction, supervised fine-tuning with low-rank adaptation (LoRA), and post-training alignment via reinforcement learning from human feedback (RLHF) and direct preference optimisation (DPO). Sections {ref}`sec:gai_reasoning` and {ref}`sec:gai_memory` discuss chain-of-thought reasoning and context management strategies. Section {ref}`sec:gai_evaluation` covers evaluation metrics (perplexity, benchmarks) and safety guardrails.

The second half of the chapter moves from language models to systems that act. Section {ref}`sec:gai_kb` covers knowledge bases, ontologies, and retrieval-augmented generation (RAG), deriving the cosine similarity retrieval formula and the augmented generation objective. Section {ref}`sec:gai_agentic` defines the AI agent as a formal tuple, derives the ReAct reasoning loop, and surveys tools and function calling. Section {ref}`sec:gai_patterns` catalogs the key agentic design patterns — reflection, planning, parallelisation, human-in-the-loop, and learning. Section {ref}`sec:gai_multiagent` classifies multi-agent system topologies (linear, supervisor, hierarchical, actor-critic, DAG, swarm) and their communication protocols. Section {ref}`sec:gai_evals` discusses evaluation of agentic systems.

The chapter builds on the Bayesian foundations of chapter {ref}`intro_bayesian` (Gibbs distribution, conjugate updates) and the causal framework of chapter {ref}`intro_causal` (do-operator, tool selection as causal intervention).

(sec:gai_whatisgenai)=
## What is Gen AI?

In simple terms, Generative AI consists of training sophisticated *generative probabilistic models* on large corpora of data and applying them to tasks traditionally associated with intelligence — such as content generation and reasoning — thereby constituting *Artificial Intelligence* systems. Let us understand each of these concepts to shed light on the term.

(sec:gai_ai)=
### Artificial Intelligence

Considered the father of the field of Artificial Intelligence, the computer scientist John McCarthy coined the term and provided a simple but compelling definition: Artificial Intelligence is *"the Science and Engineering of Making Intelligent Machines"*. What does it mean for a machine to be intelligent? In general, here we are referring to human capabilities for learning, reasoning, interpreting, understanding, and adapting.

It is key here to focus on the idea of "human intelligence". Human beings are the benchmark for Artificial Intelligence, as the famous test proposed by Alan Turing in 1950, the Imitation Game, clearly showcases. Here, a human evaluator tries to differentiate the human and the machine in a text transcript of a natural language conversation between them. The machine passes the test if the evaluator cannot tell them apart with certain confidence. There are naturally many domains where human intelligence is quite limited — for instance when working with raw datasets trying to generate statistical inferences. A Turing test where one of the participants is able to extract patterns from a billion-line dataset will provide a clear hint to the evaluator on who is the machine. And despite this relatively obvious fact, during the last decades the field of Machine Learning was almost synonymous with Artificial Intelligence.

This does not mean that Machine Learning has not been able to excel at tasks that can be clearly labelled as human intelligence. The most impressive ones were propelled, though, by the use of artificial neural networks which, from the second decade of this century, thanks to improved algorithms for learning without overfitting and the availability of data and computing power, blended together in the field of *Deep Learning* and started to match or even beat human beings in specific tasks like object recognition in images or playing board games like Go. However, most business applications of Machine Learning improved upon traditional statistical models, which are precisely good at learning patterns from large datasets — domains where machines can easily show super-human capabilities.

Despite the advances of Deep Learning in some human intelligence tasks, these systems were considered too specialised in their capabilities. Yes, they could excel at recognising handwritten characters, but a system trained for that purpose would be incapable of generalising its knowledge to even similar tasks like object recognition in images. In that sense, we can talk about *narrow* intelligence, limited to a specific task, and *general* intelligence, which can extrapolate knowledge acquired to perform a set of tasks to others for which it has not been specifically trained. The problem is that such capability of extrapolation is seemingly key even when AI systems are applied in specific domains. That was one of the lessons learned after the rise and fall of so-called expert AI systems in the 1980s. These systems were based on a large corpus of rules compiled from domain experts. They ended up becoming too complex to maintain and lacking the extrapolation capabilities needed for the necessary bit of creativity to tackle genuinely new problems.

In some sense, the philosophical theory of knowledge was already pointing out the problem since Ancient Greece: to learn is to generate abstractions or ideas in our minds that extract regularities from what our senses perceive. Reasoning, then, is the combination of those abstractions to build further inferences or perform deductions. Neuroscientists now understand that human brains generate such abstractions by building or strengthening connections between neurons when exposed to regularities in perceptions. It does not come as a surprise, then, that the most successful machine models were built upon neural networks, which resemble at a high level the workings of the brain. They seemingly build their own abstractions as they are trained on a large number of data points, provided they have sufficient scale to learn complex patterns coupled with mechanisms for regularisation — that is, avoiding learning the patterns of training data so well that they fail to generalise to unseen data {cite:p}`goodfellow2016deep`.

During the second decade of this century, the combination of increasingly large neural networks trained on increasingly large datasets started to provide surprising examples of *emergent behaviour*: a sort of threshold in data and parameters beyond which capabilities would become akin or superior to humans {cite:p}`brown2020language`. Such observations, however, did not anticipate that neural network systems, when trained upon language datasets with the seemingly simple task of predicting the next word given the previous ones, would become shockingly good at probably the most central skill considered in the domain of human intelligence: general language interpretation and reasoning.

It was not without effort. The field of natural language processing (NLP) had been trying for years to build systems capable of generating realistic conversations by training statistical models on sequences of words. One of the main challenges was that those systems would quickly forget the context of a conversation, making sentences incoherent in their syntax and conversations that would jump randomly across topics. With the boom of Deep Learning, specific architectures such as *recurrent neural networks* and *long short-term memory* (LSTM) cells {cite:p}`hochreiter1997long` were built to address this shortcoming. They improved upon previous systems but did not provide major breakthroughs. The tipping point happened with the release of the paper "Attention Is All You Need" by {cite:t}`vaswani2017attention`. They introduced the Transformer architecture, which, when applied to a vast corpus of text to learn a massive number of neural weights, exhibited an emerging behaviour in reasoning and understanding that still surprises casual users today.

With the advent of such *large language models*, the field of AI has come back to its roots of building systems that target human capabilities. Naturally, this has raised the interest of corporations across the world eager to automate and optimise tasks that, just a few years back, were thought to belong exclusively to the human domain.

(sec:gai_genmodels)=
### Generative models

In the chapter on Bayesian theory ({ref}`intro_bayesian`), we already introduced the concept of generative probabilistic models in contrast to discriminative probabilistic models. At the heart is the way we use probabilistic models to perform inferences from datasets. Discriminative models focus on understanding the distribution of a subset of variables conditional on the others — the domain of so-called supervised learning in machine learning terminology. In simple terms, if we have a dataset composed of two variables $X, Y$, a discriminative model seeks to understand the conditional distribution:

$$P(Y|X)$$

A generative model, however, tries to model the full dataset, akin to understanding the full data generation process — hence the name. It models the joint probability distribution:

$$P(X,Y)$$

A generative model is more general than a discriminative model, since correct modelling of the joint distribution allows us to derive the conditional distribution by the product rule of probability:

$$P(Y|X) = \frac{P(X,Y)}{P(Y)}$$

A point to notice is that were we only interested in computing $P(Y|X)$, it might be more efficient to learn this distribution directly using supervised models. Modelling the joint distribution is more complex and therefore the quality of inferences of $P(Y|X)$ might suffer. However, having the full generative model allows us to solve a wider range of inferences than a discriminative model.

The previous argument can also work in reverse: if we learn all relevant discriminative distributions separately, we have knowledge of the generative model, since:

$$P(X, Y) = P(Y|X) P(X)$$

We can generalise this result to a sequence of $N$ variables:

$$P(X_1, \ldots, X_N) = P(X_1| X_2, \ldots, X_N) P(X_2| X_3, \ldots, X_N) \cdots P(X_{N-1}|X_N) P(X_N)$$

where we have simply applied the product rule sequentially.

This structure already provides a hint on the connection between generative models and large language models. Statistical language models try to compute the distribution of words (or *tokens*, which are more granular building blocks of language that perform better in practice). For instance, given the sentence "the cat had blue ...", such models try to estimate the probability of any possible next word conditional on the previous words, for instance:

$$P(\text{"eyes"}| \text{"the"}, \text{"cat"}, \text{"had"}, \text{"blue"})$$

A useful model should be able to compute such a probability for any word in the vocabulary. In particular $P(\text{"blue"}|\text{"the"}, \text{"cat"}, \text{"had"})$, $P(\text{"had"}|\text{"the"}, \text{"cat"})$, $P(\text{"cat"}| \text{"the"})$ and $P(\text{"the"})$, so that by the chain rule the model computes the full joint:

$$P(\text{"the"}, \text{"cat"}, \text{"had"}, \text{"blue"}, \text{"eyes"})$$

i.e., it is a generative model for language.

Having a generative model for human language opens up the possibility for multiple tasks. We can use it to generate text given some context or *prompt*. We can produce an expert model that sticks to the most likely facts by taking the highest-probability token at each step, or a creative system that samples from the full distribution. A common practice to control the degree of creativity is to transform the probability distribution for the next token into a Gibbs distribution. The motivation is the transformation:

$$P_i = e^{\log P_i} \rightarrow \hat{P}_i = \frac{e^{-s_i /T}}{Z}$$

where we define the scores $s_i = -\log P_i$ per token $i$, $T$ is an external parameter called **temperature** in analogy to Statistical Physics, and $Z = \sum_i e^{-s_i /T}$ is the normalisation constant. As discussed in {ref}`intro_bayesian`, the Gibbs distribution is the one that maximises entropy subject to a fixed average score. By varying the temperature we control the degree of creativity:

- For $T\rightarrow 0$, all terms tend to zero, but the one with the smallest score $s_i$ is the slowest. Therefore $\hat{P}_i \rightarrow \delta_{i, i_{\max}}$, where $i_{\max}$ is the token with the lowest score, i.e. the highest probability. The model is *deterministic* and sticks to the most likely next tokens.
- For $T = 1$, we recover the original distribution $\hat{P}_i = P_i$.
- For $T \rightarrow \infty$, all exponential terms tend to $1$, so the distribution becomes uniform over the vocabulary. The model generates tokens at random.

(sec:gai_taxonomy)=
### Taxonomy of generative AI systems

Large language models represent one — albeit dominant — class within a broader taxonomy of generative AI systems, all sharing the same fundamental principle of modelling a joint distribution over high-dimensional data {cite:p}`goodfellow2016deep`:

- **Language models**: model the distribution $P(\mathbf{w}_{1:T})$ over sequences of tokens. The generated output is text (or code, structured data, reasoning traces). Their principal architecture is the Transformer, discussed in section {ref}`sec:gai_transformer`.

- **Diffusion models**: model images, audio, or video by learning to reverse a gradual noising process. Starting from a data point $\mathbf{x}_0$, a Markov chain adds Gaussian noise over $T$ steps to produce $\mathbf{x}_T \approx \mathcal{N}(\mathbf{0}, I)$. A neural network $\epsilon_\theta(\mathbf{x}_t, t)$ learns to predict and remove the noise at each step, so that generation proceeds by sampling $\mathbf{x}_T$ and iteratively denoising.

- **Multimodal models**: model joint distributions over more than one modality (text + image, text + audio), enabling cross-modal generation and understanding.

In all cases, the generative model is parameterised by a neural network $\theta$ and trained by maximising the likelihood of observed data — equivalently, minimising a divergence between the model distribution and the empirical distribution of training data.

(sec:gai_llm)=
## Large Language Models

(sec:gai_traditional_lm)=
### Traditional language modelling

Early statistical language models were based on the *n-gram* assumption: the probability of the next word depends only on the previous $n-1$ words (the Markov property of order $n-1$). The bigram ($n=2$) model is:

$$P(w_t | w_1, \ldots, w_{t-1}) \approx P(w_t | w_{t-1})$$

Parameters are estimated from corpus frequencies: $\hat{P}(w_t|w_{t-1}) = \frac{c(w_{t-1}, w_t)}{c(w_{t-1})}$ where $c(\cdot)$ counts co-occurrences. The limitation is *data sparsity*: most n-grams are unobserved in any finite corpus, requiring smoothing techniques (Laplace, Kneser-Ney) to assign non-zero probabilities to unseen sequences.

The fundamental limitation is that n-gram models cannot capture long-range dependencies — information more than $n$ tokens away is discarded — and the number of parameters grows exponentially with $n$ (order $|V|^n$ where $|V|$ is the vocabulary size).

*Hidden Markov Models* (HMMs) introduced latent states representing coarser semantic categories, allowing a compact representation of longer dependencies, but still relied on Markov assumptions and manual feature engineering for language tasks.

The first *neural* language models represented words as dense vectors (embeddings) in $\mathbb{R}^d$ and parameterised $P(w_t|w_{t-n+1:t-1})$ with a feed-forward network. This provided better generalisation through shared representations but still had a fixed context window. Recurrent neural networks (RNNs) extended the context by maintaining a hidden state $\mathbf{h}_t = f(\mathbf{h}_{t-1}, \mathbf{x}_t)$ — in principle, $\mathbf{h}_t$ encodes all past information. In practice, gradients vanish over long sequences, making it extremely difficult to retain information over more than a few dozen tokens. Long short-term memory cells {cite:p}`hochreiter1997long` addressed vanishing gradients with gating mechanisms, but the fundamental problem of sequential computation — each step depending on the previous — remained.

(sec:gai_transformer)=
### The Transformer architecture

The Transformer {cite:p}`vaswani2017attention` discarded the sequential recurrence in favour of a fully parallel **self-attention** mechanism that allows every token to attend directly to every other token in the sequence, regardless of distance. This design choice made it possible to train on massive corpora using highly parallelised hardware and to capture long-range dependencies without gradient degradation.

**Embedding and positional encoding.** A sequence of $n$ tokens is first mapped to a matrix $\mathbf{X} \in \mathbb{R}^{n \times d}$ by an embedding table, where $d$ is the model dimension. Since attention is permutation-invariant, explicit positional information must be injected. The original paper added sinusoidal positional encodings:

$$PE_{(i, 2k)} = \sin\!\left(\frac{i}{10000^{2k/d}}\right), \qquad PE_{(i, 2k+1)} = \cos\!\left(\frac{i}{10000^{2k/d}}\right)$$

for position $i$ and dimension index $k$. These have the property that the encoding of position $i + \delta$ can be expressed as a linear function of the encoding at position $i$, enabling the model to learn relative positions. More recent architectures use *rotary positional embeddings* (RoPE) that encode relative position within the attention computation itself, improving extrapolation to sequences longer than those seen during training.

**Scaled dot-product attention.** The core operation maps a sequence of queries $Q \in \mathbb{R}^{n\times d_k}$, keys $K \in \mathbb{R}^{n\times d_k}$, and values $V \in \mathbb{R}^{n\times d_v}$ to an output:

$$\boxed{\mathrm{Attn}(Q, K, V) = \mathrm{softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right) V}$$

The term $QK^T \in \mathbb{R}^{n\times n}$ is the *attention score matrix*: entry $(i,j)$ measures the compatibility of query $i$ with key $j$. Dividing by $\sqrt{d_k}$ prevents the dot products from growing large in magnitude for high-dimensional embeddings, which would push the softmax into a near-one-hot regime and cause gradient saturation. After the softmax, each output row is a convex combination of the value vectors — a *soft lookup* that retrieves information from all positions, weighting them by relevance to the current query.

The three matrices $Q$, $K$, $V$ are linear projections of the same input:
$$Q = \mathbf{X} W_Q, \quad K = \mathbf{X} W_K, \quad V = \mathbf{X} W_V$$
with learnable weight matrices $W_Q, W_K \in \mathbb{R}^{d\times d_k}$ and $W_V \in \mathbb{R}^{d\times d_v}$.

**Multi-head attention.** Running a single attention head forces the model to mix all types of information in a single representation. Multi-head attention runs $h$ attention heads in parallel, each with its own projections, and concatenates the results:

$$\mathrm{MHA}(\mathbf{X}) = \mathrm{concat}(\mathrm{head}_1, \ldots, \mathrm{head}_h) W_O$$
$$\mathrm{head}_i = \mathrm{Attn}(\mathbf{X}W_{Q_i}, \mathbf{X}W_{K_i}, \mathbf{X}W_{V_i})$$

Different heads can learn to attend to different types of relationships simultaneously — syntactic agreement, coreference, topic coherence — allowing the model to represent the same token in multiple relational contexts.

**Feed-forward sublayer.** Each Transformer layer also contains a position-wise feed-forward network:

$$\mathrm{FFN}(\mathbf{x}) = \sigma(\mathbf{x}W_1 + \mathbf{b}_1)W_2 + \mathbf{b}_2$$

where $\sigma$ is a non-linear activation (originally ReLU; GELU is now standard). The inner dimension is typically $4d$, making this the layer responsible for most of the model's parameters.

**Layer normalisation and residual connections.** Each sublayer is wrapped in a residual connection {cite:p}`goodfellow2016deep` and layer normalisation:

$$\mathbf{x} \leftarrow \mathrm{LN}(\mathbf{x} + \mathrm{sublayer}(\mathbf{x}))$$

$$\mathrm{LN}(\mathbf{x}) = \gamma \odot \frac{\mathbf{x} - \mu}{\sigma} + \beta$$

Residual connections allow gradients to flow directly through the depth of the network, enabling training of very deep models. Layer normalisation stabilises the distribution of activations at each sublayer.

A complete Transformer language model stacks $L$ such layers, followed by a linear projection to the vocabulary dimension and a softmax, yielding a probability distribution over the next token at each position.

```{figure} figures/gai_transformer_block.png
:name: fig:gai_transformer_block
:width: 9in
:align: center

Structure of a single Transformer decoder block. Input embeddings (with positional encoding) pass through masked multi-head self-attention, followed by a position-wise feed-forward network. Each sublayer is wrapped with a residual connection and layer normalisation. The attention score matrix visualises which tokens attend to which (lighter = stronger attention).
```

(sec:gai_decoder_only)=
### Decoder-only language models

The original Transformer was designed for sequence-to-sequence tasks (e.g., machine translation) using an encoder-decoder architecture. For generative language modelling, the decoder-only variant has become the dominant design {cite:p}`brown2020language`. It consists of the same stacked decoder blocks but without an encoder or cross-attention sublayer.

The key feature of the decoder is *causal masking*: entry $(i,j)$ of the attention score matrix is set to $-\infty$ (before softmax) whenever $j > i$, preventing token $i$ from attending to future positions $i+1, \ldots, n$. This enforces the autoregressive property: the model can only use information from past tokens to predict the current one, which is consistent with the training objective of next-token prediction.

At generation time, the model operates autoregressively: given a prompt $w_1, \ldots, w_k$, it samples $w_{k+1}$ from the distribution $P_\theta(w_{k+1}|w_{1:k})$, appends it to the context, and repeats. This generates one token at a time, but the attention scores can be partially cached (**KV cache**) across steps, making generation significantly more efficient.

**Scaling.** The number of parameters in a Transformer scales roughly as $12 d^2 L$ (ignoring embedding parameters). Empirical scaling laws {cite:p}`kaplan2020scaling` established that loss decreases predictably as a power law in both model size $N$ and training tokens $D$, with the optimal allocation of a compute budget $C$ given by $C \approx 6ND$ FLOP. The *Chinchilla* scaling laws {cite:p}`hoffmann2022training` refined this, showing that prior large models were significantly under-trained: optimal training requires roughly 20 training tokens per model parameter, $D \approx 20N$.

(sec:gai_training)=
### Training of large language models

Training a large language model proceeds in three phases: pre-training on a vast unsupervised corpus, supervised fine-tuning for instruction following, and post-training alignment with human preferences.

(sec:gai_pretraining)=
#### Pre-training

Pre-training optimises the **language modelling objective**: given a corpus of token sequences $\{w_1, \ldots, w_T\}$, minimise the negative log-likelihood of each token given its causal context:

$$\mathcal{L}_{\mathrm{PT}}(\theta) = -\frac{1}{T}\sum_{t=1}^T \log P_\theta(w_t | w_1, \ldots, w_{t-1})$$

This is equivalent to minimising the cross-entropy between the empirical token distribution and the model distribution, and directly related to perplexity (section {ref}`sec:gai_evaluation`). The model learns grammar, factual knowledge, reasoning patterns, and stylistic conventions purely from the statistical structure of text.

Pre-training corpora typically include web-crawled text, books, code repositories, and scientific articles — often trillions of tokens. The enormous scale of data and model size means that gradient-based optimisation (typically Adam or a variant) must run for weeks to months on thousands of accelerators. Techniques such as mixed-precision training (FP16/BF16), gradient checkpointing, and model parallelism across GPUs are standard practice.

(sec:gai_sft)=
#### Supervised fine-tuning

After pre-training, the model knows how to complete text but does not necessarily follow instructions or maintain a helpful conversational style. *Supervised fine-tuning* (SFT) adapts the model on a curated dataset of (instruction, desired response) pairs, training the same next-token objective but restricted to this smaller, higher-quality dataset {cite:p}`ouyang2022training`.

Full fine-tuning updates all parameters — expensive for multi-billion-parameter models. **Low-rank adaptation (LoRA)** {cite:p}`hu2022lora` provides an efficient alternative. The key observation is that when adapting to a new task, the weight update $\Delta W$ occupies a low-dimensional subspace. LoRA decomposes the update as:

$$W = W_0 + \Delta W = W_0 + BA$$

where $W_0 \in \mathbb{R}^{d \times k}$ is the frozen pre-trained weight, $B \in \mathbb{R}^{d \times r}$, $A \in \mathbb{R}^{r \times k}$, and $r \ll \min(d,k)$ is the rank. Only $A$ and $B$ are trained, reducing trainable parameters from $dk$ to $r(d+k)$, typically a 100–1000$\times$ reduction. At inference time, the decomposition can be merged back into a single weight matrix $W$, incurring zero additional latency.

(sec:gai_alignment)=
#### Post-training alignment

The final phase ensures that the model's outputs align with human values: being helpful, honest, and avoiding harmful outputs. The dominant approach has been **Reinforcement Learning from Human Feedback (RLHF)** {cite:p}`ouyang2022training`.

RLHF proceeds in two steps. First, a *reward model* $r_\phi(x, y)$ is trained on preference data: for a given prompt $x$, human annotators compare two model responses $y_w$ (preferred) and $y_l$ (rejected). The reward model is fitted by minimising the negative log-likelihood of the Bradley-Terry preference model:

$$\mathcal{L}_\mathrm{RM} = -\mathbb{E}_{(x, y_w, y_l)}\bigl[\log\sigma\bigl(r_\phi(x, y_w) - r_\phi(x, y_l)\bigr)\bigr]$$

where $\sigma$ is the sigmoid function. Second, the language model $\pi_\theta$ is optimised against the reward model while staying close to the reference policy $\pi_\mathrm{ref}$ (the SFT model), via the objective:

$$\mathcal{L}_\mathrm{RL} = \mathbb{E}_{(x,y)\sim\pi_\theta}\bigl[r_\phi(x,y)\bigr] - \beta\, D_\mathrm{KL}\bigl(\pi_\theta \| \pi_\mathrm{ref}\bigr)$$

The KL divergence penalty, controlled by $\beta > 0$, prevents reward hacking — the tendency for the optimised policy to find degenerate outputs that score high on the learned reward model but are incoherent or harmful.

**Direct Preference Optimisation (DPO)** {cite:p}`rafailov2023direct` eliminates the need for a separate reward model. It exploits the fact that the optimal policy for the RLHF objective can be expressed in closed form:

$$\pi^*(y|x) \propto \pi_\mathrm{ref}(y|x)\exp\!\left(\frac{r(x,y)}{\beta}\right)$$

Substituting this expression into the reward model likelihood and rearranging, DPO directly optimises:

$$\mathcal{L}_\mathrm{DPO} = -\mathbb{E}_{(x,y_w,y_l)}\left[\log\sigma\!\left(\beta\log\frac{\pi_\theta(y_w|x)}{\pi_\mathrm{ref}(y_w|x)} - \beta\log\frac{\pi_\theta(y_l|x)}{\pi_\mathrm{ref}(y_l|x)}\right)\right]$$

This is a single-stage supervised loss on preference pairs, considerably simpler to implement than the two-stage RLHF pipeline.

(sec:gai_reasoning)=
### Reasoning and chain-of-thought

A key observation in scaling language models is that reasoning capability improves not only by increasing model size but by allowing the model to produce *intermediate reasoning steps* before the final answer. **Chain-of-thought (CoT)** prompting {cite:p}`wei2022chain` demonstrates this: including a sequence of natural-language reasoning steps in the prompt (or training data) leads to dramatic improvements on multi-step mathematical and logical tasks.

Formally, rather than modelling $P(a|q)$ — the probability of answer $a$ given question $q$ — chain-of-thought models $P(a|q, c)$ where $c = (c_1, \ldots, c_K)$ is a chain of $K$ intermediate reasoning tokens, and the full joint is:

$$P(a, c_1, \ldots, c_K | q) = P(a | q, c_1, \ldots, c_K)\prod_{k=1}^K P(c_k | q, c_1, \ldots, c_{k-1})$$

This connects to the broader principle of *test-time compute scaling*: allocating more computation at inference time (producing more tokens for reasoning before the answer) consistently improves accuracy at the cost of latency. More advanced approaches include **tree-of-thought** search over the space of reasoning paths, and **Monte Carlo tree search** over reasoning trajectories scored by an outcome reward model — essentially applying the planning ideas of chapter {ref}`stochastic_optimal_control` to language generation.

(sec:gai_memory)=
### Context and memory management

The self-attention mechanism attends over the entire *context window* — the sequence of tokens the model can process in a single forward pass. For most models this is in the range of $10^4$ to $10^6$ tokens, which is sufficient for many tasks but falls short of the requirements for very long conversations, codebases, or document collections.

Several complementary strategies manage memory at different time scales:

- **Rolling context window**: keep the most recent $n_{\max}$ tokens in the context, dropping the oldest. Simple but loses early conversation history.
- **Compaction / summarisation**: periodically summarise older context segments with a dedicated summarisation call, replacing them with a compressed representation. Trades fidelity for length.
- **Retrieval-augmented context**: store information in an external index (section {ref}`sec:gai_rag`) and retrieve relevant passages on demand. Scales to arbitrary amounts of knowledge without filling the context window.
- **External memory stores**: maintain structured stores of *episodic memory* (past conversation turns), *semantic memory* (facts and knowledge), and *procedural memory* (tools, code), which agents can read and write explicitly during task execution {cite:p}`albada2024building`.

The distinction between in-context memory (the context window) and external persistent memory is analogous to working memory versus long-term memory in cognitive science: the context window is fast and immediately accessible but limited and ephemeral, while external stores are slower to access but unbounded and persistent.

(sec:gai_evaluation)=
### Evaluation and safety

**Perplexity** is a metric to evaluate probabilistic language models. It is closely related to cross-entropy and offers a more interpretable score. The idea is to quantify the degree to which an estimated probability distribution for the data is *perplexed* (i.e., surprised) when it sees new data supposedly coming from the same generative process. The perplexity of a model that assigns probability $p(x_i)$ to a test sample $D = \{x_1, \ldots, x_N\}$:

$$PP(D) = b^{-\frac{1}{N}\sum_{i=1}^N \log_b p(x_i)}$$

where $b$ is the base for the logarithm (typically $b = 2$ or $b = e$). We can see immediately how this relates to the likelihood $L(D)$:

$$PP(D) = \left(\prod_i p(x_i) \right)^{-1/N} = L(D)^{-1/N}$$

By inverting the likelihood and normalising to the sample length, we obtain a metric that: (i) has an interpretation in terms of surprise — data that has higher probability under the model is less surprising; and (ii) is comparable across datasets of different lengths.

Perplexity is also related to the cross-entropy between the model and the empirical distribution:

$$H(\hat{p}, p) = -\sum_x \hat{p}(x) \log_b p(x) = -\frac{1}{N} \sum_i \log_b p(x_i)$$

which can be decomposed using the Kullback-Leibler divergence as $H(\hat{p}, p) = H(\hat{p}) + D_\mathrm{KL}(\hat{p} \| p)$, confirming that perplexity is minimised when model and empirical distributions agree. A uniformly random model over $K$ outcomes yields $PP(D) = K$, providing a natural baseline: perplexity should be compared to the vocabulary size to gauge model quality.

For sequence models, applying the chain rule:

$$PP(D) = b^{-\frac{1}{N}\sum_{t=1}^N \log_b p(s_t|s_1, \ldots, s_{t-1})}$$

A perplexity score of $PP$ means the model has an equivalent uncertainty to a random guess among $PP$ tokens — the smaller this is relative to the actual vocabulary size, the better the model.

**Task benchmarks.** Perplexity measures how well a model fits its training distribution but does not directly measure downstream capabilities. Standard benchmarks evaluate models on tasks such as reading comprehension, mathematical reasoning, coding, and common-sense inference using accuracy, F1, or pass rate as metrics. Benchmark design requires careful controls against training set contamination — if benchmark examples appeared in pre-training data, performance measures memorisation rather than generalisation.

**Safety and guardrails.** Alignment-trained models can still be prompted to produce harmful outputs through adversarial inputs (*jailbreaks*). Safety systems typically combine: (i) input classifiers that detect harmful prompts before reaching the model; (ii) output classifiers that filter model responses; (iii) constitutional AI approaches that train the model to self-critique and revise outputs against a set of principles; and (iv) red-teaming — systematic adversarial testing by humans or automated systems to discover failure modes before deployment.

(sec:gai_kb)=
## Knowledge bases and retrieval

Language models acquire factual knowledge implicitly through pre-training weights, but this knowledge is static (frozen at the training cutoff), opaque (not directly inspectable), and can be unreliable for specific facts, especially those that change over time. *Knowledge bases* provide an explicit, queryable, updatable store of structured knowledge that can be combined with language models.

(sec:gai_ontologies)=
### Ontologies and knowledge graphs

An *ontology* is a formal specification of concepts, categories, and relationships within a domain — a schema for knowledge. A *knowledge graph* instantiates an ontology with specific entities and their relationships, typically stored as a set of (subject, predicate, object) triples: for example, (AAPL, *isListedOn*, NASDAQ), (AAPL, *sector*, Technology). Querying a knowledge graph via SPARQL or graph traversal produces precise, auditable answers with full provenance.

*Wiki-style knowledge bases* combine human-curated ontologies with structured data (infoboxes, categories) and free text, providing a hybrid between structured knowledge graphs and unstructured documents. They are excellent for factual, encyclopaedic knowledge and provide the ground-truth signal for many NLP benchmarks.

The limitation of fully structured knowledge bases is the *knowledge acquisition bottleneck*: manually curating and maintaining triples at scale is extremely labour-intensive. This motivates retrieval from unstructured text, described next.

(sec:gai_rag)=
### Retrieval-augmented generation

**Retrieval-Augmented Generation (RAG)** {cite:p}`lewis2020retrieval` addresses the limitations of static model knowledge by dynamically retrieving relevant documents from an external corpus at inference time and augmenting the model's context with the retrieved content.

```{figure} figures/gai_rag_pipeline.png
:name: fig:gai_rag_pipeline
:width: 9in
:align: center

RAG pipeline. Documents are chunked and encoded into a dense vector index (offline). At query time, the user's question is encoded with the same embedding model; the $k$ nearest neighbours are retrieved and concatenated with the query to form an augmented prompt; the language model generates a grounded answer.
```

The pipeline has two phases:

**Offline indexing.** A corpus of documents $\mathcal{D} = \{d_1, \ldots, d_M\}$ is chunked into passages of roughly 256–512 tokens. Each passage is encoded by a *text embedding model* $f_\phi$ into a dense vector $\mathbf{e}_j = f_\phi(d_j) \in \mathbb{R}^D$. These vectors are stored in a *vector index* supporting approximate nearest-neighbour (ANN) search — data structures such as hierarchical navigable small worlds (HNSW) or product quantisation enable sub-linear query time over millions of vectors.

**Online retrieval and generation.** At query time, the user's query $q$ is encoded as $\mathbf{e}_q = f_\phi(q)$, and the $k$ most relevant passages are retrieved by cosine similarity:

$$d_1^*, \ldots, d_k^* = \arg\!\max_{d \in \mathcal{D}} \;\frac{\mathbf{e}_q \cdot \mathbf{e}_d}{\|\mathbf{e}_q\|\|\mathbf{e}_d\|}$$

The retrieved passages are prepended to the query in the prompt, and the language model generates a response conditioned on both the query and the retrieved evidence:

$$P_\theta(a | q, d_1^*, \ldots, d_k^*)$$

The key advantage is that factual knowledge now lives in the retrieval corpus, not the model weights. Updating knowledge requires only re-indexing the corpus — no expensive retraining. Responses can be traced back to source passages, improving interpretability and enabling fact-checking.

**Advanced RAG patterns.** The basic single-shot RAG pipeline can be extended in several directions: *iterative retrieval* performs multiple retrieval-generation cycles, using intermediate outputs to reformulate the query; *hybrid retrieval* combines dense embedding similarity with sparse keyword matching (BM25) for complementary coverage; *reranking* applies a cross-encoder model to re-score and filter retrieved passages before generation.

(sec:gai_kb_agents)=
### Knowledge base agents

Rather than relying on static offline indexing, *knowledge base agents* maintain, organise, and query the knowledge base dynamically as part of an agentic workflow (section {ref}`sec:gai_agentic`). Such an agent can:

- **Ingest** new documents, extract entities and relationships, and add them to the knowledge graph or vector index.
- **Reconcile** conflicting information from multiple sources, using the language model's reasoning capability to adjudicate.
- **Synthesise** new knowledge entries from retrieved passages, generating structured summaries that improve future retrievals.

This closes the loop between generation and knowledge management, creating a knowledge base that evolves continuously with new information rather than requiring batch reindexing.

(sec:gai_agentic)=
## Agentic AI

A language model receiving a prompt and generating a response is a *reactive* system: it produces one output per input, with no persistent state between calls. *Agentic AI* refers to systems in which a language model acts as the cognitive core of an agent that perceives its environment, maintains memory across steps, selects and executes actions via tools, and pursues goals over extended multi-step workflows {cite:p}`gulli2024agentic`. Agency is not a binary property but a spectrum determined by the autonomy, time horizon, and number of decisions involved.

(sec:gai_agent_def)=
### The AI agent

Formally, we define an AI agent as a tuple $(\mathcal{O}, \mathcal{A}, \mathcal{M}, \pi_\theta, \mathcal{G})$:

- $\mathcal{O}$: the *observation space* — text, tool outputs, retrieved documents, structured data.
- $\mathcal{A}$: the *action space* — tool calls, memory operations, messages to other agents, or direct responses to the user.
- $\mathcal{M}$: the *memory system* — context window, external memory stores, and knowledge bases.
- $\pi_\theta$: the *policy* — the language model parameterised by $\theta$ that maps the current state to the next action.
- $\mathcal{G}$: the *goal* — a natural language task description or objective function that the agent is trying to satisfy.

The agent operates in a loop. At each step $t$, the agent has a *state* $s_t = (g, h_t)$ where $g \in \mathcal{G}$ is the goal and $h_t = (o_1, a_1, o_2, a_2, \ldots, o_{t-1}, a_{t-1}, o_t)$ is the full history of observations and actions. The policy selects the next action $a_t \sim \pi_\theta(\cdot | s_t)$, the action is executed in the environment, and the new observation $o_{t+1}$ is received. This has the structure of a Markov Decision Process (MDP), but the state and action spaces are high-dimensional and the policy is a neural network rather than a tabular function.

**The ReAct pattern** {cite:p}`yao2023react` interleaves *reasoning* and *acting* within a single generation: the model produces a *thought* (a chain-of-thought reasoning trace), an *action* (a tool call), and incorporates the *observation* (the tool's output) into the next step:

```
Thought: I need to find the current price of the EUR/USD pair.
Action:  get_price("EURUSD")
Observation: 1.0823
Thought: I now have the price. I will compare it with the fair value estimate.
...
```

```{figure} figures/gai_agent_loop.png
:name: fig:gai_agent_loop
:width: 8in
:align: center

The ReAct agent loop. The language model core alternates between reasoning (producing a chain-of-thought trace) and acting (issuing a tool call). The tool's output is observed and appended to the context for the next reasoning step. The loop terminates when the model generates a final answer.
```

(sec:gai_tools)=
### Tools and function calling

Tools extend the agent's action space beyond text generation to include executable operations in the real world: web search, database queries, code execution, API calls, file read/write. The mechanism by which the model selects and invokes tools is **function calling**.

In function calling, available tools are described to the model as structured schemas (name, description, parameter types, required/optional). The model generates a structured action object — rather than free text — specifying which function to call and with what arguments. A dispatcher routes this action to the corresponding implementation, executes it, and returns the result as an observation.

The **Model Context Protocol (MCP)** is an emerging open standard for this interface, providing a uniform schema for tool definition and invocation that decouples the tool implementations from the agent framework. This allows tool ecosystems to be built independently of any specific model or orchestration library, improving composability and portability.

From the agent's perspective, the key property of any tool is its *signature*: the preconditions (what inputs it requires) and postconditions (what it returns and what side effects it has). Effective agents must select tools that satisfy the current step's preconditions and whose postconditions advance the goal.

(sec:gai_patterns)=
### Agentic design patterns

Single-agent behaviour can be structured through a small number of recurring *design patterns* that encapsulate different problem-solving strategies {cite:p}`gulli2024agentic` {cite:p}`albada2024building`.

**Reflection.** After generating an initial response or plan, the agent explicitly critiques it — identifying weaknesses, errors, or missing elements — and then revises. The critique and revision can be implemented either within a single prompt (self-critique) or by having a separate *critic* model evaluate the generator's output. Reflection improves the quality of outputs on tasks where the model's initial response is likely to be suboptimal, such as long-form writing or complex reasoning.

**Planning.** Rather than acting greedily (taking the immediately best action at each step), the agent first produces a structured *plan* decomposing the goal into a sequence of sub-goals. This corresponds to hierarchical decomposition of the MDP: the high-level policy operates over sub-goals, while lower-level policies handle the execution of each sub-goal. The plan may be revised as new observations arrive, implementing a *closed-loop* planning-execution cycle.

**Parallelisation.** Independent sub-tasks can be dispatched to separate agent instances running concurrently, aggregating results when all have completed. This is analogous to map-reduce: a *map* step fans out work to parallel agents; a *reduce* step aggregates their outputs. Parallelisation is particularly effective for tasks that require gathering information from multiple independent sources.

**Human-in-the-loop.** At specified decision points, the agent pauses and requests human confirmation or correction before proceeding. This is essential for tasks with irreversible consequences (executing a trade, sending a communication, modifying a production system). The agent framework must support asynchronous execution — suspending state, notifying the human, and resuming when input is received.

**Learning and self-improvement.** The agent updates its own memory, instructions, or prompts based on feedback from completed tasks. This can range from simply storing successful tool-use examples in an episodic memory that is retrieved in future tasks (in-context learning) to more sophisticated fine-tuning of the model weights on successful trajectories. At the most advanced end, the agent learns to improve its own prompts and strategies, implementing a meta-learning loop.

**Deep research.** A compound pattern that combines planning, retrieval, tool use, and reflection to perform systematic multi-step research on a complex question. The agent decomposes the question into search queries, retrieves and reads sources, synthesises findings, identifies gaps, and iterates until a comprehensive answer is formed. This is one of the most commercially valuable agentic applications.

(sec:gai_multiagent)=
### Multi-agent systems

For sufficiently complex tasks, a single agent may be insufficient — the task may exceed the context window, require parallel execution, or benefit from specialised expertise in different sub-domains. *Multi-agent systems* coordinate multiple language model agents, each with its own specialisation, tools, and memory, to collectively accomplish shared goals {cite:p}`albada2024building`.

The *communication protocol* between agents defines how agents exchange information. The **A2A (Agent-to-Agent) protocol** is a standardised message format for structured inter-agent communication, analogous to MCP for tool calling: it decouples agent implementations from the orchestration layer, enabling heterogeneous agents to collaborate through a common interface.

Agent systems are characterised by their *topology* — the graph structure of communication and control relationships. The main topologies are illustrated in {numref}`fig:gai_agent_topologies`.

```{figure} figures/gai_agent_topologies.png
:name: fig:gai_agent_topologies
:width: 9in
:align: center

Agent topologies. (a) **Linear / pipeline**: each agent processes the output of its predecessor; suitable for sequential transformation tasks. (b) **Supervisor / hub-and-spoke**: a central orchestrator decomposes the task and dispatches sub-tasks to specialised worker agents; suitable for hierarchical task decomposition. (c) **Hierarchical**: a tree of supervisors enabling multi-level decomposition for very complex tasks. (d) **Actor-critic**: one agent proposes actions while another evaluates and critiques them before execution; implements reflection at the system level. (e) **DAG (directed acyclic graph)**: dependencies between tasks are captured as a graph; tasks are executed as soon as their predecessors complete, maximising parallelism. (f) **Swarm**: agents communicate peer-to-peer without a central coordinator; coordination emerges from local interactions; suitable for large-scale parallel exploration tasks.
```

**Linear / pipeline topology** (Figure {numref}`fig:gai_agent_topologies`a) chains agents sequentially: agent $A_1$ produces output that becomes the input to $A_2$, and so on. This is appropriate when the task can be decomposed as a series of transformations (e.g., retrieve → extract → summarise → format).

**Supervisor / hub-and-spoke topology** ({numref}`fig:gai_agent_topologies`b) has a single orchestrator agent that decomposes a goal into sub-tasks, assigns each sub-task to a worker agent, and aggregates the results. The orchestrator maintains the global state and the plan; workers are stateless and specialised. This is the most common pattern in practice because it mirrors human team structures and is easy to reason about.

**Hierarchical topology** ({numref}`fig:gai_agent_topologies`c) extends the supervisor pattern to multiple levels: a top-level orchestrator delegates to mid-level orchestrators, each of which manages a team of workers. This scales to very complex, large-scope tasks.

**Actor-critic topology** ({numref}`fig:gai_agent_topologies`d) pairs a generative *actor* agent that proposes plans or outputs with a critical *evaluator* agent that scores or critiques them. This implements the reflection design pattern at the system level — the critique is independent of the actor, reducing self-serving bias in self-critique. The actor is iteratively refined by the evaluator's feedback.

**DAG topology** ({numref}`fig:gai_agent_topologies`e) represents the task as a directed acyclic graph of sub-tasks with dependencies. Each sub-task is executed by an agent as soon as all its predecessors have completed, maximising parallelism. This is appropriate when the dependency structure is known in advance (i.e., can be planned before execution).

**Swarm topology** ({numref}`fig:gai_agent_topologies`f) places agents in a peer-to-peer network with no central coordinator. Agents communicate via shared blackboards or broadcast messaging; global coordination emerges from local interactions. Swarms scale to large numbers of agents and are robust to individual agent failures, but global behaviour is harder to predict and debug.

The choice of topology is driven by the task structure, the required level of verification, the need for parallelism, and the criticality of individual agent failures. In practice, hybrid topologies combining elements of several patterns are common.

(sec:gai_evals)=
### Evaluation of agentic systems

Evaluating agentic systems is significantly harder than evaluating single-turn language models. The unit of evaluation is no longer a single response but an entire *trajectory* — the sequence of thoughts, actions, observations, and final output produced over a multi-step task.

**Task success rate** is the primary end-to-end metric: the fraction of tasks for which the agent achieves the stated goal, as determined by automated verification (where possible) or human judgement. Defining success precisely is non-trivial — partially completed tasks, correct outputs achieved via incorrect reasoning, and tasks with subjective quality dimensions all require careful rubric design.

**Step-level metrics** evaluate the quality of individual decisions within a trajectory: tool selection accuracy, plan coherence, retrieval relevance (precision/recall of retrieved passages), and reasoning soundness. Step-level metrics are more diagnostic than task-level metrics but require ground-truth annotation of intermediate steps.

**Trajectory quality.** Good task performance should not come at the cost of unnecessarily long or wasteful trajectories. Trajectory efficiency metrics include the number of tool calls per task, the fraction of redundant or incorrect actions, and the total token cost.

**Safety and alignment.** Agentic systems that take actions in the real world require additional safety evaluation: *refusal rate* on clearly harmful task requests, *escalation rate* (fraction of ambiguous tasks for which the agent appropriately requests human confirmation), and *harm rate* (fraction of trajectories that produce harmful side effects). Safety evaluation relies heavily on adversarial testing — red-teaming the agent with challenging, edge-case, or malicious inputs to surface failure modes before deployment.

**Evals as automated test suites.** The emerging best practice is to construct *evals*: curated suites of tasks with automated scoring functions, analogous to unit tests in software engineering. Well-designed eval suites catch regressions when the model, tools, or prompt templates are changed, providing a continuous quality gate for agentic systems in production.

## Exercises

1. **Temperature and entropy.** Consider a vocabulary of $K = 5$ tokens with log-probabilities $(-0.2, -0.5, -1.0, -1.5, -3.0)$ (base $e$). (a) Compute the raw probabilities $P_i$ and verify they sum to 1. (b) Compute the Gibbs-temperature-adjusted probabilities $\hat{P}_i$ for $T = 0.5$, $T = 1$, and $T = 2$. (c) Compute the entropy $H = -\sum_i \hat{P}_i \log \hat{P}_i$ at each temperature and describe the trend.

2. **Attention mechanism.** Given a sequence of $n = 3$ tokens with $d = 4$, $d_k = 2$, and the matrices $\mathbf{X} = \begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\end{pmatrix}$, $W_Q = W_K = I_2$ (the first two columns of the $4\times2$ identity extension), and $V = \mathbf{X}$ (identity mapping): (a) Compute $Q$, $K$, and the unnormalised attention scores $QK^T/\sqrt{d_k}$. (b) Apply the softmax row-wise to obtain the attention weights. (c) Compute the output $\mathrm{Attn}(Q,K,V)$ and interpret which positions each output attends to most strongly.

3. **Perplexity benchmark.** A trigram language model assigns log-probabilities to a held-out sentence of 100 tokens, yielding a sum of log-probabilities (base 2) of $-350$. (a) Compute the perplexity. (b) If the vocabulary size is $K = 10{,}000$, interpret the result relative to the random-guessing baseline. (c) A second model achieves perplexity 80 on the same test set. What is the ratio of their cross-entropies?

4. **LoRA parameter count.** A weight matrix $W_0 \in \mathbb{R}^{4096 \times 4096}$ is adapted using LoRA with rank $r$. (a) Express the number of trainable parameters in $A$ and $B$ as a function of $r$. (b) For $r \in \{4, 8, 16, 32\}$, compute the percentage of parameters trained relative to full fine-tuning. (c) What rank would be needed to reduce training parameters by a factor of 100?

5. **RAG retrieval.** A query has embedding $\mathbf{e}_q = (1, 0, 1)^T/\sqrt{2}$ (normalised). Three document embeddings are $\mathbf{e}_1 = (1, 0, 0)^T$, $\mathbf{e}_2 = (1, 1, 0)^T/\sqrt{2}$, $\mathbf{e}_3 = (0, 1, 1)^T/\sqrt{2}$. (a) Compute the cosine similarity of the query with each document. (b) Rank the documents by relevance. (c) Describe a scenario in which sparse keyword matching (BM25) would retrieve a different document as the top result, illustrating why hybrid retrieval is useful.

6. **Agent topology design.** A trading desk wants to build an agentic system to: (i) scan news feeds for earnings announcements; (ii) assess the impact of each announcement on the relevant stock and sector; (iii) generate a research summary; and (iv) route the summary for human review before any position is taken. (a) Which topology from {numref}`fig:gai_agent_topologies` best fits this task? Justify your answer. (b) Identify at least two agentic design patterns from section {ref}`sec:gai_patterns` that should be incorporated. (c) Describe how you would evaluate the system's performance, specifying both task-level and step-level metrics.

7. **DPO objective.** Given a reference model $\pi_\mathrm{ref}$ and a preference triple $(x, y_w, y_l)$ where $\log\pi_\mathrm{ref}(y_w|x) = -2.0$ and $\log\pi_\mathrm{ref}(y_l|x) = -1.0$ (the less preferred response is more likely under the reference), and the trained model assigns $\log\pi_\theta(y_w|x) = -1.5$ and $\log\pi_\theta(y_l|x) = -1.8$. With $\beta = 0.1$: (a) Compute the DPO argument inside the sigmoid. (b) Compute the DPO loss contribution from this triple. (c) Interpret: is the model making progress toward preferring $y_w$ over $y_l$ relative to the reference?
