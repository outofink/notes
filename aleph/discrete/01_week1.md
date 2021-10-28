---
title: Discrete Math - Chapter 1
author: Moshe Krumbein
date: Fall 2021
header-includes: |
    \usepackage{bbold}
---

# Course details

The course is split up into three parts

1. [Set Theory](https://en.wikipedia.org/wiki/Set_theory) and
[Logic](https://en.wikipedia.org/wiki/Mathematical_logic)
2. [Combinatorics](https://en.wikipedia.org/wiki/Combinatorics)
3. [Graph Theory](https://en.wikipedia.org/wiki/Graph_theory)

## What is a "discrete set"?

A *discrete set* is one that has a specific individualized parts.

Discrete sets may be finite or infinite (countable).

## Types of questions:

[Birthday Problem](https://en.wikipedia.org/wiki/Birthday_problem)

A bunch of other examples...

## What is a *set*?

A *set* is a collection of objects.

A set of objects of does not have to contain objects of only one type.

A property of sets is that a set $A$ has a *binary relation* between between
itself and an object $o$. Either $A$ *contains* or *does not contain* $o$.

### Example:

$$
\begin{gathered}
    A=\{1,4,7,8\} \\
    B=\{a,b,c,d\} \\
    C=\{x,y,z\} \\
    \\
    1 \in A \\
    2 \notin A
\end{gathered}
$$

Additionally, a set that has multiple members of the same element is
equivalent to a set that has one one of the element, due to the property of
*binary relation*.

$$A = \{1,4,7,8\} = \{1,1,4,4,4,7,8\}$$

*Size of a set*: number of (by definition, distinct) elements in a set.

$$|A| = 4$$

$$
\begin{gathered}
    B = \{\{1,2,3\},4\} \\
    4 \in B \quad 1 \notin B
\end{gathered}
$$

## A conditional set: (such that)

$$\{ x \;|\; \text{such that } x \}$$

$$B = \{a \in A \;|\; a < 5 \}$$

### Example:

All of the whole numbers from 1 to 1000.

$$\{x \;|\; 1<x<1000, \text{ such that $x$ is whole }\}$$

Although the following set is small in size, it is easier to express it in
the following fashion instead of explicitly:

$$\{x \;|\; x^5-4x^3+7x^2-11x+\sqrt 2=0\}$$

### Dictionary (quantifiers):

$$
\begin{gathered}
    \forall = \text{for all} \\
    \exists = \text{exists}
\end{gathered}
$$

## Containment (Subset)

**Definition:** $B$ *contains* $A$ when all elements in $B$ are also in $A$.

$$B \subseteq A$$

Specifically if $A$ and $B$ are distinct:

$$B \subsetneq A$$

If two sets are *equivalent*: ($A \subseteq B, B \subseteq A$)

$$A=B$$

### Example:

$$
\begin{gathered}
    A = \{1,3,4, \{1\}, \{1,2\}\} \\
    |A| = 5 \\
    1 \in A \\
    \{1\} \in A \\
    \{1\} \subseteq A \\
    \text{ (because of the first element)} \\
    \{\{1\}\} \subseteq A \\
    \text{(because of the forth element)} \\
    \{1,2\} \in A \\
    \{1,2\} \nsubseteq A \\
    \{1\} \subseteq A \\
    \{1\} \subsetneq A \\
\end{gathered}
$$

### *Note:*

$A \in B$: the *element* $A$ is in *set* $B$.

$A \subseteq B$: the contents of *set* $A$ are all in *set* $B$.

## Special sets

$$
\begin{alignedat}{3}
    \emptyset  =& \{\}
        &- &\;\text{empty set} \\
    \mathbb{N} =& \{1,2,3,\mathellipsis\}
        &- &\;\text{natural numbers} \\
    \mathbb{Z} =& \{\mathellipsis,-2,-1,0,1,2,3,\mathellipsis\}
        &- &\;\text{whole numbers} \\
    \mathbb{Q} =& \left\{ \frac{m}{n} \;|\; m,n \in \mathbb{Z}, n \neq 0 \right\}
        &- &\;\text{rational numbers} \\
    \mathbb{R} \quad& &- &\;\text{real numbers} \\
\end{alignedat}
$$
$$
    \emptyset \subsetneq
    \mathbb{N} \subsetneq
    \mathbb{Z} \subsetneq
    \mathbb{Q} \subsetneq
    \mathbb{R}
$$

## Binary operations on sets

### Union

$$A \cup B = \{a \;|\; a \in B \text{ or } a \in A \}$$

### Intersection

$$A \cap B = \{a \;|\; a \in B \text{ and } a \in A \}$$

### Difference

$$A \setminus B = \{a \;|\; a \notin B \text{ and } a \in A \}$$

### Symmetrical difference

$$A \triangle B = (A \cup B) \setminus (A \cap B)$$

## Size of union of sets

$$|A \cup B| \overset{?}{=} |A| + |B|$$

#### Disjoint set:

$A$ and $B$ are *disjoint sets* if $A \cap B = \emptyset$.

If $A$ and $B$ are disjoint sets, then:

$$|A \cup B| = |A| + |B|$$

In general:

$$|A \cup B| = |A| + |B|- |A \cap B|$$

### Magnitude of union between three sets

$$|A \cup B \cup C| = |A| + |B| + |C|$$

When $A, B, C$ are *pairwise disjointed*.

### Algebraic properties

$$
\begin{gathered}
    \text{Commutative property:} \\
    A \cup B = B \cup A \\
    A \cap B = B \cap B \\
    \text{Associative property:} \\
    (A \cup B) \cup C = A \cup (B \cup C) \\
    (A \cap B) \cap C = A \cap (B \cap C) \\
    \text{Distributive property:} \\
    A \cup (B \cap C) = (A \cup B) \cap (A \cup C) \\
    A \cap (B \cup C) = (A \cap B) \cup (A \cap C) \\
\end{gathered}
$$

Given the sets $A_1, A_2. \mathellipsis, A_n$:
$$[n] = \{1,2,3, \mathellipsis, n\}, n \in \mathbb{N},\quad |[n]|=n$$
$$\bigcup_{i=1}^{n}A_i=A_1\cup A_2 \cup \mathellipsis \cup A_n = \{ x \;|\; \exists \; i \in [n] : x \in A_i \} $$
$$\bigcap_{i=1}^{n}A_i=A_1\cap A_2 \cap \mathellipsis \cap A_n = \{ x \;|\; \forall \; i \in [n] : x \in A_i \} $$

### Complement

For set $U$ where $A \subseteq U$:
$$A^c = U \setminus A$$

### De Morgan's laws:

Given sets $A,B$:
$$(A \cup B)^c=A^c \cap B^c$$
$$(A \cap B)^c=A^c \cup B^c$$

# Logic

#### Statement:

Every claim is either *true* and *false*: $\{T,F\}$

$$
\begin{gathered}
    1+1=2 \to T \\
    1+1=0 \to F
\end{gathered}
$$

## Logical relations

### Unary Operations

#### Negation:

| $P$ | $\neg P$ |
|:---:|:--------:|
|  T  |     F    |
|  F  |     T    |

### Binary Operations

| $P$ | $Q$ | $P \lor Q$ | $P \land Q$ | $P \to Q$ | $P\leftrightarrow Q$ |
|:---:|:---:|:----------:|:------------:|:---------:|:--------------------:|
|  T  |  T  |      T     |       T      |     T     |           T          |
|  T  |  F  |      T     |       F      |     F     |           F          |
|  F  |  T  |      T     |       F      |     T     |           F          |
|  F  |  F  |      F     |       F      |     T     |           T          |

### Complex statements

Combination of logical relations in one statement.

#### Example:

$$\neg p \to Q$$

### Relation between $\cup, \cap$ and $\lor \land$
$$P : x \in A \quad Q: x \in B$$
$$
\begin{gathered}
    P \lor Q : x \in A \cup B \\
    P \land Q: x \in A \cap B
\end{gathered}
$$

| $P$ | $Q$ | $\neg P$ | $\neg P \to Q$ |
|:---:|:---:|:--------:|:--------------:|
|  T  |  T  |     F    |        T       |
|  T  |  F  |     F    |        T       |
|  F  |  T  |     T    |        T       |
|  F  |  F  |     T    |        F       |

If two complex statements are made up of the same statements, then they are
*logically equivalent*. ($\iff$)

#### Example:

$$\neg (P \lor Q) \iff (\neg P) \land (\neg Q)$$

| $P$ | $Q$ | $P \lor Q$ | $\neg(P \lor Q)$ | $\neg P$ | $\neg Q$ | $(\neg P) \land (\neg Q)$ |
|:---:|:---:|:----------:|:----------------:|:--------:|:--------:|:--------------------------:|
|  T  |  T  |      T     |         F        |     F    |     F    |              F             |
|  T  |  F  |      T     |         F        |     F    |     T    |              F             |
|  F  |  T  |      T     |         F        |     T    |     F    |              F             |
|  F  |  F  |      F     |         T        |     T    |     T    |              T             |

$$P \to Q \iff \neg P \lor Q$$

| $P$ | $Q$ | $P \to Q$ | $\neg P$ | $\neg P \lor Q$ |
|:---:|:---:|:---------:|:--------:|:---------------:|
|  T  |  T  |     T     |     F    |        T        |
|  T  |  F  |     F     |     F    |        F        |
|  F  |  T  |     T     |     T    |        T        |
|  F  |  F  |     F     |     T    |        T        |

$$P \to Q \iff \neg Q \to \neg P$$

| $P$ | $Q$ | $P \to Q$ | $\neg P$ | $\neg Q$ | $\neg Q \to \neg P$ |
|:---:|:---:|:---------:|:--------:|:--------:|:-------------------:|
|  T  |  T  |     T     |     F    |     F    |          T          |
|  T  |  F  |     F     |     F    |     T    |          F          |
|  F  |  T  |     T     |     T    |     F    |          T          |
|  F  |  F  |     T     |     T    |     T    |          T          |

$$
\begin{gathered}
    x \in \emptyset \to x \in A \\
    \iff \\
    \neg (x \in A) \to \neg (x \in \emptyset) \\
    x \notin A \to x \notin \emptyset
\end{gathered}
$$

$$
\begin{gathered}
    1<2 \quad x<2 \\
    \text{We'll symbolize the statement $P$ with the variable $x$ for $P(x)$} \\
    \text{Example: }P: (\forall \; x \in \mathbb{N} \quad x<2)
\end{gathered}
$$

$$\forall \; x \in A \quad P(x)$$

Is true if every $P(x)$ is true, and will be false if even one $P(x)$ is false.

$$\exists \; x \in A \quad P(x)$$

Will be true if even one $P(x)$ is true, and will be false if all $P(x)$ is false.

Given $P(x), Q(x)$:

The following logical statements can be constructed:
$$
\begin{gathered}
    \forall \; x \in A \quad \forall \; y \in B \quad P(x) \land Q(y) \\
    \exists \; x \in A \quad \exists \; y \in B \quad P(x) \land Q(y) \\
    \exists \; x \in A \quad \forall \; y \in B \quad P(x) \land Q(y) \\
    \forall \; x \in A \quad \exists \; y \in B \quad P(x) \land Q(y) \\
\end{gathered}
$$

## Series

### Cartesian multiplication:

#### Definition:

Given two sets $A,B$:

$$A \times B = \{(a,b) \mid a \in A, b \in B\}$$

*Note:* The order of $A, B$ *does* matter.

If $A, B$ are *finite*:

$$|A \times B| = |A| \cdot |B|$$

#### The plane:

$$\mathbb{R} \times \mathbb{R} = \mathbb{R}^2 = \{(x,y) \mid x, y \in \mathbb{R}\}$$

If $A_1, \mathellipsis, A_n$ are sets:

$$X_{i=1}^{n} = A_1 \times \mathellipsis \times A_n = \{(a_1, \mathellipsis,
a_n) \mid \forall \; i \in [n], a_i \in A_i\}$$

If $A_1, \ldots A_n$ are finite:

$$|X_{i=1}^n A_i| = \prod_{i=1}^n |A_i|$$

#### Notes:

$$
\begin{gathered}
    A \times \emptyset = \emptyset \\
    A \times A = A^2 \\
    \underbrace{A_1 \times \ldots \times A_n}_{n\text{ times}} = A^n
\end{gathered}
$$

### Functions:

Given two sets $A, B$, function $f: A \mapsto B$, there $\forall \; a
in A$ that maps to $b \in B$.

$A$ is called the *domain* and $B$ is called the *range*.

$$f(a)=b$$

$a$ is *a source* of $b$, and $b$ is *the image* of $a$.

For $c \subset a$, the image of $c$ is:

$$f(C) = \left\{b \in B \mid a \in C : f(a) = b \right\} \subseteq B$$
$$=\{f(a) \mid a \in C\}$$

#### Example:

Given $f: A \mapsto B$:

$$\text{Im}f = f(A) \subseteq B$$

Given $D \subseteq B$, the source of $D$:

$$ f^{-1}(D) = \{a \in A \mid f(a) \in D\}$$

1.
$$A \subseteq U$$
$$\mathbb{1}: U \mapsto \{0,1\} (\chi)$$

$$\forall \; a \in U, \mathbb{1}_A(a) = \begin{cases}
    1 \quad a \in A \\
    0 \quad a \notin A
\end{cases}$$

2.
$$
\begin{gathered}
    A = \mathbb{Z}^k \quad B = \mathbb{Z} \\
    f((a_1, \ldots, a_n)) = a_3
\end{gathered}
$$

3. $$
\begin{gathered}
    \text{Given: }\{(a_1, \ldots, a_n)\} \subseteq \mathbb{Z}^k \\
    f: \underbrace{[n]}_{\{1,2,\ldots,n\}} \mapsto \mathbb{Z} \\
    \forall \; i \in [n] : f(i)= a_i
\end{gathered}
$$

### Claim:

Given: $f: A \mapsto B$, $D_1, D_2 \subseteq B$:

$$f^{-1}(D_1 \cap D_2) = f^{-1}(D_1) \cap f^{-1}(D_2)$$
$$a \in f^{-1}(D_1 \cap D_2) \iff f(a) \in D_1 \cap D_2$$

Given: $C_1, C_2 \subseteq A$:

$$f(C_1 \cap C_2) \neq f(C_1) \cap f(C_2)$$

### [Characteristics of functions](https://en.wikipedia.org/wiki/Bijection,_injection_and_surjection)

Given $f: A \mapsto B$:

$f$ is *injective* (one-to-one) if:

$$\forall \; a_1,a_2 \in A : a_1 \neq a_2 \; \exists \; f(a_1) \neq f(a_2)$$
$$\forall \; a_1,a_2 \in A \quad f(a_1) = f(a_2) \implies a_1 = a_2$$

$f$ is *surjective* (onto) if:

$$\text{Im}f = B$$

If *f* is injective: $|A| \leq |B|$.

If *f* is surjective: $|A| \geq |B|$.

If *f* is both injective and surjective, it is *bijective* (invertible) and: $|A| = |B|$.
