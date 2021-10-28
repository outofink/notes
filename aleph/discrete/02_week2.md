---
title: Discrete Math - Chapter 2
author: Moshe Krumbein
date: Fall 2021
header-includes: |
    \usepackage{bbold}
---

If we have two finite groups $A, B$, function $f: A \mapsto B$, and $C
\subseteq A, D \subseteq B$:

1. $|f(c)| \leq |C|$
2. $f$ is injective:
    a. $|f(C)|= |C|$
    b. $|f^{-1}(D)| = |D|$
3. $f$ is surjective:
    a. $|f^{-1}(D)| \geq |D|$
4. If $f$ is injective and $|A|=|B|$, then it is also surjective
4. If $f$ is surjective and $|A|=|B|$, then we've learned nothing new

## Composing Functions

Given groups $A, B, C$:

$$f: A \mapsto B, \quad g: B \mapsto C$$
$$g \circ f: A \mapsto C: \forall \; a \in A:$$
$$(g \circ f)(a) = g(f(a))$$

## Identity function

$$\mathrm{Id}_A: A \mapsto A$$
$$f \circ \mathrm{Id}_A: A \mapsto B$$
$$f \circ \mathrm{Id}_A: f$$
$$\mathrm{Id}_B \circ f: A \mapsto B$$
$$\mathrm{Id}_B \circ f: f$$

## Inverse function

Given $f: A \mapsto B, g: B \mapsto C$:

$g$ is the inverse of $f$ if:

$$g \circ f = \mathrm{Id}_A$$
$$f \circ g = \mathrm{Id}_B$$

If the previous is true, then $g = f^{-1}$

$n \in \mathbb{N}, [n] = \{1,2,\ldots, n\}$

# Permutations

A *permutation* is a (possible) rearrangement of objects. For example,
there are 6 permutations of the letters $a, b, c$:

$$abc, acb, bac, bca, cab, cba$$

Permutation on $[n]$ is $f: [n] \mapsto [n]$, for example $\mathrm{Id}_{[n]}$

$f: A \mapsto A$
$$f^2 = f \circ f: A \mapsto A$$
$$f^m = \underbrace{f \circ f \circ f \ldots}_{m \text{ times}}$$

If $f \circ g$ is bijective, it is a permutation.

$$\sigma^6 = \mathrm{Id}_{\sigma}$$
$$\sigma^{100} = \mathrm{Id}_{\sigma}$$


# Exercise

## Question 1

Given $f:A \mapsto B$, $C_1, C_2 \subseteq A$

1. If $C_1 \subseteq C_2$, then $f(C_1) \subseteq f(C_2)$.

Yes.

Suppose $a \in f(C_1) \implies b \in C_1$ such that $f(b)=a$. Since we also
know $b \in C_2$, therefore $f(b) \subseteq f(C_2) \implies f(C_1) \subseteq f(C_2)$.

2. If $f(C_1) \subseteq f(C_2)$, then $f(C_1) \subseteq f(C_2)$.

No.

We define $A=\{1,2\}, B=\{u\}$, $f(1)=f(2)=a$.

3. If $f$ is injective, and $f(C_1) \subseteq f(C_2)$ ,then $C_1 \subseteq
C_2$.

Suppose $c \in C_1, c \notin C_2$.

$f(c) \notin f(C_2)$

## Question 2

Let $f: A \mapsto B, g: B \mapsto C$. Prove that if $g \circ f$ is injective
then $f$ is also injective.

Suppose $a_1, a_2 \in A, a_1 \neq a_2$.

$$g \circ f(a_1) \neq g \circ f(a_2)$$
$$f(a_1) \neq f(a_2)$$

## Question 3

Let $f: A \mapsto B, g: B \mapsto A, h: B \mapsto A$

1. $g \circ f = \mathrm{Id}_A$ and $h \circ f = \mathrm{Id}_A$, then $g=h$.

False

2. $f \circ g = \mathrm{Id}_B$ and $h \circ f = \mathrm{Id}_A$, then $g=h$.

True
