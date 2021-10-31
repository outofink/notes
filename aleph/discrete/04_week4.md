---
title: Discrete Math - Chapter 4
author: Moshe Krumbein
date: Fall 2021
header-includes: |
    \usepackage{pgfplots}
    \usepackage{gensymb}
---

# Binary Relations

*Definition:* $R \subseteq A \times A$

*Relations* are made up of pair from set $A$ that fulfill certain parameters.

*Equivalence Relation*: A binary relation that is *reflexive*[^reflexive], *symmetric*[^symmetric], and
*transitive*[^transitive].

[^reflexive]:  $R$ is *reflexive* if $\forall \; a \in A: (a,a) \in R$
[^symmetric]: $R$ is *symmetric* if $\forall \; a,b \in A: (a,b) \in R \implies (b,a) \in R$
[^transitive]: $R$ is *transitive* if $\forall \; a,b,c \in A: (a,b), (b,c) \in R \implies (a,c) \in R$

#### Example:

$$A = \mathbb{Z} \times \mathbb{Z} \backslash \{0\}$$
$$R=\{(m_1,n_1),(m_2,n_2) \mid m_1n_2=m_2n_1\}$$

To prove that this relation is an equivalence relation, we have to prove that
it is reflexive, symmetric and transitive.

# [Partial Ordered Relations](https://en.wikipedia.org/wiki/Partially_ordered_set#Partial_order_relation)

Given relation $R$ on a set, then we say the $R$ is a partial ordered relation
is $R$ is *reflexive*, *antisymmetric*[^antisymmetric], and *transitive*. In this case we say
that $A$ is a *partial ordered set*.

[^antisymmetric]: $R$ is *antisymmetric* if $\forall \; a,b \in A: (a,b), (b,a) \in R \implies
   a=b$

#### Definition:

Partial Ordered relation exists for all $\forall \: x,y \in R \;\exists\; (x,y)
\in R$ or $(y,x) \in R$ is called a *linear order*.

Suppose that $R$ is a partial ordered relation on $A$:

$$(a,b) \in R \quad a \leq_R b$$

$x \in A$ is called the *maximum* if $\forall \; y \in A$ , if $(x,y) \in R$,
then $x=y$. ($x$ has no arrows going out of it except for to itself).

$x \in A$ is called the *minimum* if $\forall \; y \in A$ , if $(y,x) \in R$,
then $x=y$. ($x$ has no arrows going to it except for to itself).

## [Hasse Diagram](https://en.wikipedia.org/wiki/Hasse_diagram)

We'll say that pair $(x,y) \in R$ is "required" in a Hasse diagram if $x \neq y$,
and therefore:

$$\forall z \in A (x,z),(z,y) \in R \implies z=x \text{ or } z=y$$

Essentially, we can get rid of all arrows that represent transitive and
reflexively because they are assumed.

#### Claim:

If $R$ is a linear ordered relation on $A$ then there exists in $A$ only one
maximum and minimum.

#### Proof:

Using proof by contradiction, if $x,y \in A$ minimums such that $x \neq y$ ...
