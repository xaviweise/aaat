# Generative Artificial Intelligence

Since the release in 2022 of Chat GPT, the field of Artificial Intelligence has been radically transformed. Chat GPT was based on the third version of the Generalized Pre-trained Transformer (GPT) model, a so-called large language model, with surprising capabilities for reasoning and conversation in a creative way. Since then, new versions of the model have been released, as well as competition in the space, with other providers catching up on the capabilities. Moreover, multi-modal so-called foundational models that extend their understanding beyond language to images and video, blending them. For instance, models like Stable Diffusion are able to convert text into highly realistic (although not necessarily consistent) images. This type of models, which mostly share a common neural-network architecture, the Transformer, that has boosted its capabilities together with a large number of parameters and training data, form the backbone of the emerging field of Generative Artificial Intelligence (Gen AI). In order to understand them and make an efficient use of them, particularly in business applications, it is convenient to understand their fundamentals. 

## What is Gen AI?

In simple conceptual terms, Gen AI consists on the application of generative probabilistic models to the domain of Artificial Intelligence. Let us understand each of these concepts to shed light on the term. 

### Artificial Intelligence

Considered the father of the field of Artificial Intelligence, the computer scientist John McCarthy coined the term and provided a simple but compelling definition: Artificial Intelligence is *"the Science and Engineering of Making Intelligent Machines"*. What what does it mean intelligence? In general, here we are referring to human capabilities for learning, reasoning, interpreting, understanding and adapting. 

It is key here to focus on the idea of "human intelligence". Human beings are the benchmark for Artificial Intelligence, as the famous test proposed by Alan Turing in 1949, the imitation game, clearly showcases. Here, a human evaluator tries to differentiate the human and the machine in a text transcript of a natural language conversation between them. The machine passes the test if the evaluator cannot tell them apart with certain confidence. There are naturally many domains where human intelligence is quite limited, for instance when working with raw datasets trying to generate statistical inferences. A Turing test where one of the participants is able to extract patterns from a billion lines dataset will provide a clear hit to the evaluator on who is the machine. And despite this relatively obvious fact, during the last decades the field of Machine Learning has been almost synonymous of Artificial Intelligence. 

This does not mean that Machine Learning has not been able to excel at some tasks that can be clearly labelled as human intelligence. The most impressive ones were propelled, though, by the use of artificial neural networks, which from the second decade of this century, thanks to improved algorithms for learning without over-fitting, and the availability of data and computing power, all blended together in the field of Deep Learning, started to pass or even beat human beings in specific tasks like object recognition in images, or playing games board games like Go. However, most of the applications of Machine Learning, at least in the business environment, have been on improving upon traditional statistical models, which are precisely good at learning patterns from large datasets. In these tasks, these systems can easily show super-human capabilities.

Despite the advances of Deep Learning in some human intelligence tasks, these systems where considered too specialized in their capabilities. Yes, they could excel humans in recognizing hand-written characters, but such system trained to do so would be later incapable of generalize the knowledge to even similar tasks like object recognition in images. In that sense, we can talk about *narrow* intelligence, limited to a specific task, and *general* intelligence, which can extrapolate knowledge acquired to perform a set of tasks to others for which it has not been specifically trained. The problem is that such capability of extrapolation is seemingly key even when Artificial Intelligence systems are to be applied in specific domains of knowledge. That was one of the learnings after the rise and fall of so-called expert AI systems in 80s of the previous century. These systems were based on a large corpus of rules compiled from experts in a specific field, the idea being that these systems could be used to reason about new problems in those domains. But they ended up becoming too complex to maintain and lacking those extrapolation capabilities that are key for the necessary bit of creativity needed to tackle new problems. 

In some sense, the philosophical theory of knowledge was already pointing out the problem since the Ancient Greece: to learn is to generate some abstractions in our minds, that extract regularities from what our senses perceive. Reasoning, then, is the combination of those abstractions to build further inferences or perform deductions. Neurologists now understand that human brains generate such abstractions by building or strengthening connections between neurons in our brains when exposed to regularities in perceptions. It does not come then as a surprise that the most successful machine models were built upon neural networks, that resemble at a high level the workings of the brain. They seemingly build their own abstractions as they are trained on a large number of data points, and have a sufficient scale to learn complex patterns coupled with mechanism for regularization, i.e. avoid to learn so well the patterns of the training data that will later not generalize to unseen datasets.

During the second decade of this century, the combination of neural networks increasingly large trained on increasing large datasets started to provide surprising examples of a sort of emergent behaviour in terms of capabilities: a sort of threshold in data and parameters from which capabilities would become akin or superior to humans. Such observations however did not anticipate that such neural network systems, when trained upon language datasets with the seemingly simple task of predicting the next work given the previous ones, would suddenly become shockingly good at probably the most central skills considered in the domain of human intelligence: general language interpretation and reasoning. 

It was not, though, without effort. The field of natural language processing (NLP) had been trying during years to build systems capable of generating realistic conversations by training statistical models to sequences of words. One of the main challenges was that those systems would quickly forget the context of the conversation, making sentences incoherent in their syntax and conversations that would jump randomly across topics. With the boom of Deep Learning, specific neural network architectures were built to try to address this shortcoming, such as *recurrent neural networks* and *long short term memory* (LSTM) cells. They improved upon previous systems, but did not provide major breakthroughs. The tipping point happened with the release of the paper "Attention is All You Need", by researchers from Google, in 2017. They introduced the Transformer architecture, which could have been easily seen as yet another proposal to try to fix the memory issue of sequential neural networks. However, conveniently fine-tuned, when applied to a vast corpus of text to learn a massive amount of neural weights, researchers witnessed an emerging behaviour in reasoning and understanding that still surprises any casual user of them. 

With the advent of such *Large Language Models (LMMs)*, the field of Artificial Intelligence has come back to its roots of building systems that target human capabilities.  Naturally, this has raised the interest of corporations across the world that have a lot of interest in gaining understanding of these models to automate and optimize tasks that few years back were thought exclusively to belong to the human domain. 


### Generative models

In the chapter on Bayesian theory, we already introduced the concept of generative probabilistic models in contrast to discriminative probabilistic models. At the heart is the way we try to use probabilistic models to perform inferences from datasets. Discriminative models focus on understanding the distribution of a subset of variables conditional to the other, i.e. the domain of so-called Supervised Learning using the Machine Learning terminology. In simple terms, if we have a dataset composed of two variables $X, Y$, a discriminative model seeks to understand the conditional distribution:

$$P(Y|X)$$

A generative model, however, tries to model the full dataset, akin to understanding the full data generation process, hence the name. It models the joint probability distribution:

$$P(X,Y)$$

A generative model is more general that a discriminative model, since correct modelling of the joint distribution allows us to derive the distribution of the discriminative model, by virtue of use of the product rule of probability:

$$P(Y|X) = \frac{P(X,Y)}{P(Y)}$$

A point to notice is that were we only interested in computing $P(Y|X)$, it might be more efficient to learn this directly distribution using any of the multiple available statistical or Machine Learning supervised models. Modelling the joint distribution is more complex and therefore the quality of the inferences of $P(Y|X)$ might suffer. However, having the full generative model allows us to solve a wider range of inferences than the discriminative model.

The previous argument can also work in reverse: if we learn all the relevant discriminative distributions separately, we have knowledge of the generative model, since:

$$P(X, Y) = P(Y|X) P(X)$$

We can generalize this result to a sequence of $N$ variables: 

$$P(X_1, ..., X_N) = P(X_1| X_2, .., X_N) P(X_2| X_3, ..., X_N) ... P(X_{N-1}|X_N) P(X_N)$$

where we have simply applied the product rule sequentially. 

This structure already provides a hint on the connection between generative models and Gen AI models, particularly Large Language Models, mentioned in the previous section. Statistical language models try to compute the distribution of words (or tokens, which are more granular building blocks to decompose language that perform better in practical tasks). For instance, given the sentence "the cat had blue ...", such models try to estimate the probability of any existing next word, conditional to the previous words, for instance:

$$P(\text{"eyes"}| \text{"the"}, \text{"cat"}, \text{"had"}, \text{"blue"})$$

In this case, a well estimated model needs to be able to compute such probability for any word in the English vocabulary. Of course a useful model would not be specifically trained to compute probabilities for this case. This means that it should be able to compute the probability of any other sequence, in particular $P(\text{"blue"}|\text{"the"}, \text{"cat"}, \text{"had"})$, $P(\text{"had"}|\text{"the"}, \text{"cat"})$, $P(\text{"cat"}| \text{"the"})$ and $P(\text{"the"})$. But using the previous equation this means that this model must be able to compute:

$$P(\text{"the"}, \text{"cat"}, \text{"had"}, \text{"blue"}, \text{"eyes"})$$

i.e. is a generative model for language. 

Having a generative model for human language opens up the possibility for multiple tasks. In particular, we can use it to generate language given some context of *prompt*. We can have an expert model that sticks to most likely facts by generating sequences taking the most likely word according to the model. Or we can build creative systems that sample the distribution according to the computed probabilities. A common practice to control the degree of creativity of these models is to transform the probability distribution for the next word or token into a Gibbs distribution. The motivation is the transformation:

$$P_i = e^{\log P_i} \rightarrow \hat{P}_i = \frac{e^{-s_i /T}}{Z}$$

where we have defined the scores $s_i = -\log P_i$ per word $i$ in the vocabulary, $T$ is an external parameter called the Temperature in analogy to statistical mechanics, where the Gibbs distribution was introduced, and $Z = \sum_i e^{-s_i /T}$ is a normalization constant, also called the partition function using the terminology of statistical mechanics. An insight into the Gibbs distribution is that it is the distribution that maximizes entropy when the average score is a constraint: let us assume unknown probabilities $P_i$ for each word $i$, but the average score is known: $\bar{s} = \sum_i p_i s_i$. The constrained optimization problem can be written using the Lagrangian:

$${\mathcal L} = \sum_i p_i \log p_i + \lambda_1 (\sum_i p_i - 1) + \lambda_2 (\sum_i p_i s_i - \bar{s})$$

where we also have the normalization constraint (all probabilities sum to one), and $\lambda_1, \lambda_2$ are Lagrange multipliers. The extreme of this function (which can be shown to be a maximum) is given by:

$$1 + \log \hat{p}_i + \lambda_1 + \lambda_2 s_i = 0 \rightarrow \hat{p}_i = e^{-(1 + \lambda_1 + \lambda_2 s_i)}$$

Applying now the normalization constraint we get the Gibbs distribution:

$$\hat{p}_i = \frac{e^{-\lambda_2 s_i}}{\sum_i e^{-\lambda_2 s_i }} \equiv \frac{e^{-s_i / T}}{Z}$$

where we have identified the temperature $T$ as the inverse of the Lagrange multiplier $\lambda_2$. By varying the temperature, we can control the degree of creativity:

* For $T\rightarrow 0$, all terms tend to zero but the one with the smaller score $s_i$ is the slowest, therefore we get $\hat{p_i} \rightarrow \delta_{i, i_{max}}$, where $i_{max}$ is the word with the lowest score, which is the largest probability since $s_i = -\log p_i$. In this case the model is less creative, sticking to the most likely next words

* For $T = 1$, we recover the original distribution of probabilities $\hat{p}_i = p_i$

* For $T \rightarrow \infty$ the exponential terms tend to $1$, so the distribution is uniform over all words once normalization is accounted. In this case, the model is random over the distribution of all possible words. 


### Gen AI models



## Large Language Models

### Traditional language modelling

N-grams, HMMs, first neural network architectures

### The Transformer Architecture

### Decoder-only models

### Fine-tuning models with RLHL 

### Reasoning models

## Working with Large Language Models

### Prompt Engineering

### Chain of Thought

### Retrieval - Augmented Generation (RAG)

### Agentic systems