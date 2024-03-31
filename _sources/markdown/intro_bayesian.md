(intro_bayesian)=
# Introduction to Bayesian Modelling

## Bayesian probability vs frequentist statistics

Statistics is about reasoning in situations where it is not possible to argue with certainty. The main tool of statistics is probability, which was already used qualitatively since the ancient Greek but would be
formalized by de Moivre's in the 18th century as a ratio of possible outcomes for a certain event denoted $A$:

$$P(\textrm{event A}) = \frac{\#\textrm{outcomes where A happens}}{\#\textrm{total number of outcomes}}$$

This definition was suitable for situations like dice games where 1) the outcomes are countable, 2) there is a symmetry in each outcome, in the sense that they can be considered equiprobable.

This limitation would motivate several thinkers to consider alternative ways to compute probabilities. One emerging school lead by the work of Bernoulli would explore the link between probabilities of events and the
relative frequency of observation of this event in repeatead observations. This would be the foundation of the so-called frequentist school of probability and statistics, which eventually would motivate
philosophers like Venn or statisticians like Fisher to make frequencies the definition of probabilities. Such a departure was slightly at odds with Bernoulli, who simply proposed that frequencies could be a way to compute probabilities in specific set-ups. However, the appeal of
frequencies to define probability laid in their apparent objectivity, which was in contrast with a parallel school of thought started by reverend Bayes also in the 18th century, and formalized and extended by Laplace, where probabilities were considered degrees of belief, and
therefore always had an element of subjectivity from the observer. The advantage of such Bayesian way of thinking about probability is that it would make it available to many other setups apart from games of chance
or repeated experiments, reconciling it with the intuitive way our brains think about uncertainty, where probability can be perfectly defined for events that only happen once, as tomorrow's weather or a
candidate winning an election, or scientific hypothesis that are validated using observational data but cannot be repeated in a controlled lab setup, as happens in astronomical science.

Precisely is in the scientific contexts where some of the first obvious issues with the frequentist approach would become apparent. Take for instance an example discussed in [@SilviaBayesian] in detail, entailing
the estimation of the mass of Saturn. The mass of Saturn is not a random variable, it is (at our time measurement scales) a constant. The frequentist definition cannot be used directly on the mass of Saturn,
but still some sort of \"statistical\" estimation is needed since the observations from orbital data are noisy. Laplace would precisely use Bayesian probability to make a (surprisingly good) estimation of this
quantity.

The way for the frequentist school to circumvent this issue was to introduce the concept of a statistic, a random variable that can be related to the magnitude we want to estimate, for example the mass of
Saturn, which we assume is actually not directly observable. The statistic combines the information from the different measurements or observations, and if correctly built, under certain hypothesis it
converges to the value of the magnitude we want to estimate. Since it is a random variable we can apply the theory of frequentist probability. This is the origin of the actual subject of Statistics, and was quite
developed by Galton, Pearson, Neyman and Fisher, among others. They would introduce distinct features of Statistics such as the concept of statistical relevance and hypothesis testing, maximum likelihood
estimation and inferential statistics.

However, the issue with this classical statistics is the lack of a coherent methodology to choose the statistic, which in the end tends to look a bit like a series of cookbook recipes. It also hides in some way
the difficulty of properly defining what is a random variable under the statistic. Randomness is an elusive concept that in most cases (Quantum Mechanics aside) reflects lack of detailed understanding of the process
analysed, like in measurement errors. We are not that far then from here to coming back to the original concept of probability as representing a degree of belief or partial knowledge.

On the other hand, one of the main critics regarding Bayesian probability was the fact that in some sense a degree of belief is perceived as subjective, depending on each person, and not objective.
There was also no particular reason to think that degrees of belief could be framed within the mathematical rules of probability theory. A breakthrough would come in the 20th century with the work of Richard Cox and later Edwin T. Jaynes. In 1946, Richard Cox would give a step
forward in the understanding of Bayesian probability by trying to derive quantitative rules necessary for logical and consistent reasoning in terms of degrees of belief. He started by associating a real number to
our degree of belief in a proposition: the larger the number, the larger the degree of belief. Then he introduced consistency rules using logical
reasoning:

-   If we specify how much we believe a proposition X is true, we are implicitly specifying how much we believe it is false

-   If we specify how much we believe a proposition Y is true, and then how much another proposition X is true, given that Y is true, then we are implicitly specifying how much we believe both X and Y to be true

Then, using Boolean logic and ordinary algebra, he found that consistency constraints this real numbers associated to our degree of belief to follow the rules of probability theory: 

$$\begin{aligned}
P(X) + P(\bar{X}) = 1 \; \textrm{(sum rule)} \\  
P(X,Y) = P(X|Y) P(Y)  \; \textrm{(product rule)}
\end{aligned}$$

where ̄X denotes the proposition that X is false. Therefore, if we are bound to use the rules of logical reasoning, we can see that our degrees of belief can be rigorously mapped to probability theory.

These rules are just the basic building blocks from probability theory. Many other results can be derived from them, for instance the infamous Bayes' theorem, which is a simple consequence of the product rule. Since
we can write the product rule either way in terms of X or Y:

$$P(X,Y) = P(X|Y) P(Y) = P(Y|X) P(X)$$ 

Then:
$$P(X|Y) = \frac{P(Y|X) P(X)}{P(Y)}$$ 

which is Bayes's theorem. We also could derive the marginalization rule: 

$$P(X) = \int P(X,Y) dY$$ 

by taking the continuum limit starting from a discrete and complete set of events. We leave it as an exercise for the interested reader.

The work of Cox was continued in the eighties of the same century by Jaynes, who would tackle the other controversial point of Bayesian theory, namely the subjectivity in the definition of probability. Such
subjectivity disappears if we introduce the set of information available into the problem. Bayesian probabilities can be made objective once we
agree on the information available when we formulate them. We can formalize this by introducing the set of information available, $I$ into the definition of the probabilities, namely: 

$$P(X|I)$$ 

If two different rational observers agree on the information set available, then their
quantification of probability should match. As we will see, such information set typically makes it way into the computation of probabilities via so-called prior probabilities.

For a more extensive discussion on the frequentist vs bayesian debate, reference [@ClaytonBernoulli] is a good starting point. The very book from Jaynes [@Jaynes] is also a good reference who has inspired a generation of Bayesian thinkers, but is less suitable as an introduction
to the topic. As pointed out in these books, in the end the Bayesian definition of probability is the more general one, and definitions based on counting outcomes or measuring frequencies can be seen as specific
cases of the formula applicable to particular set-ups. Still, those definitions hold only under certain assumptions made by the person computing the odds or making the observations, assumptions that the
Bayesian paradigm make explicit instead of hiding them to provide an illusion of objectivity. For example, when we repeatedly throw a coin an measure relative frequencies of heads and tails, we are assuming that
such experiment generates independent observations, i.e. that the environment is effectively stationary and that initial conditions when throwing the coin are so sensitive to the outcome as to consider them a
source of randomness; we are also considering that the same coin has been used through the experiment, and so on. Those might seem obvious assumptions, but they are implicit in the computation of probabilities
as frequencies.

## Example: estimating the probability of heads in a coin toss experiment

A great way to understand the differences between frequentist probability / classical statistics and Bayesian probability is by looking at an example. We will use both methodologies to estimate the
probability of getting heads or tails in a simulated coin, modelled as a Bernoulli random variable. Every time we get heads (H) we score 1 and for tails (T) we score 0.

ADD DISCUSSION BEST POINT ESTIMATION POSTERIOR MEAN VS MODE VS MEDIAN
FROM JAYNES
