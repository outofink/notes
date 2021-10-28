---
title: Discrete Mathematics - Chapter 3
author: Moshe Krumbein
date: Fall 2021
header-includes: |
    \usepackage{pgfplots}
    \usepackage{gensymb}
---

# [Permutation](https://en.wikipedia.org/wiki/Permutation)

Permutation of $[n]$ is $f: [n] \mapsto [n]$ is surjective and injective.

We symbolize the *collection* of permutations of $[n]$: $S_n$ ($|S_n|=???$)

If $f, g \in S_n$, then $g \circ f: [n] \mapsto [n]$.

If $g \circ f$ is "one-to-one", then we see it's also "onto" $g \circ f \in
S_n$.


#### Claim:

If $f: A \to B$ is "one-to-one" and $g: B \to C$ is also "one-to-one", then $g
\circ f A \to C$ is also "one-to-one".

#### Proof:

Suppose $a_1, a_2 \in A$ such that $(g \circ f)(a_1)=(g \circ f)(a_2)$ (which
means $a_1=a_2$).

Given $g(f(a_1))=g(f(a_2))$ is "one-to-one" $\implies f(a_1)=f(a_2)$. $f$ is
also "one-to-one" $\implies a_1=a_2$.

Conclusion: $g \circ f$ is "one-to-one".

#### Definition:

Let $f: [n] \to [n]$ be the permutation of $f$, the minimal number of
permutations $k$ such that $f_k=\mathrm{Id}_{[n]}$.

We see that $k$ is the "lowest common multiple" of the lengths of the loops ???

# [Binary Relation](https://en.wikipedia.org/wiki/Binary_relation)

#### Definition:

Given two sets $A, B$, all subsets $R \subseteq A \times B$ is called "binary
relations" from $A$ to $B$. If $(a,b) \in R$ we symbolize relations as $aRb$.

#### Example:

$$A=B=\mathbb{R} \quad R=\{(x,x^2) \mid x \in A \}$$

#### Definition:

If $A=B$, then $R \subseteq A \times A$ is called *relation on $A$*.

#### Examples:

1. $A=\{2,3,4,5,8,12\}, R=\{(a,b) \mid a, b \in A, a | b \}$

$$R=\{(2,4), (2,8),(2,12),(2,2),(3,3),(3,12),\ldots \}$$

2. *Empty relation*: $R=\emptyset$
3. *Full (universal) relation*: $R = A \times A$

#### Definition:

Given set $A$, we'll define the *power set* as being all the subsets of $A$:

$$2^A = P(A) = \{B \mid B \subseteq A \}$$
$$|P(A)| = 2^{|A|}$$

4. $B = P(\{1,2,3\})$:

$$R=\{(A_1,A_2) \mid A_1, A_2 \in B, A_1 \subseteq A_2 \}$$

#### Characteristics of Binary Relations

1. $R$ is *reflexive* if for all $a \in A: (a,a) \in R$
2. $R$ is *irreflexive* if for all $a \in A: (a,a) \notin R$
3. $R$ is *symmetric* if for all $a,b \in A: (a,b) \in R \implies (b,a) \in R$
4. $R$ is *antisymmetric* if for all $a,b \in A: (a,b), (b,a) \in R \implies
   a=b$
5. $R$ is *transitive* if for all $a,b,c \in A: (a,b), (b,c) \in R \implies
   (a,c) \in R$

$A \neq \emptyset$ and not limited in size can have a relation that is
reflexive, symmetric and antisymmetric: $R =\{(a,a) \mid a \in A \}$.

#### Example:
$$
\begin{gathered}
    A \in \mathbb{Z} \\
    a|x-y \iff xRy \\
    (x,y), (y,z) \in R \implies (x,z) \in R \\
    (x,y) \in R \implies \exists t_1 \in \mathbb{Z}, x-y=2t_1 \\
    (y,z) \in R \implies \exists t_2 \in \mathbb{Z}, y-z=2t_2 \\
    x-z = x-y + y-z = 2t_1 + 2t_2 = 2(t_1 + t_2) \implies (x,z) \in R
\end{gathered}
$$

## Equivalence relation

#### Definition

$R$ is a *equivalence relation* on $A$ if $R$ is *reflexive*, *symmetric*, and
*transitive*.

$$
    A = \{1,2,3,4,5\} \\
$$

1. $R = \{(a,a) \mid a \in A \}$ - Identity relation
2. Everything is related to itself, and $1, 2$ relate to each other
3. Everything is related to itself, and $1, 2, 3$ relate to each other

We can see that there are closed groups (*closures*) within each of the relations: 1 has
five closed groups, 2 has four, and 3 has three.

#### Symbol

If $R$ is a equivalence relation on $A$ we sometimes symbolize $(x,y) \in R$ or
$x \sim y$

#### Definition

If $R$ is a equivalence relation on $A$ then for all $a \in A$ we will define
*equivalence closure*:

$$[a]_R = \{b \in A \mid (a,b) \in R$$

Given group $A$ the closure of $A$ is the collection $\{A_i\}_{i \in I}$:

1. $\forall i \in I, A_i \neq \emptyset$
2. $\forall i,j \in I, A_i \neq A_j \implies A_i \cap A_j = \emptyset$
3. $\displaystyle \bigcup_{i \in I}A_i=A$

##### Example:

$$
\begin{gathered}
    A = \mathbb{R} = \{(-\infty, -1), [-1,1], (1,\infty)\} \\
    B = \mathbb{N} = \{\{1,3,5,7,\ldots\},\{2,4,6,8,\ldots\}\}
\end{gathered}
$$

#### Claim:

If $R$ is a equivalence relation on $A$ then the collection of all the
equivalence closures:

$$\{[a]_R \mid a \in A \}$$

is a *partition* of $A$.

#### Proving the previous definition
1. For all $a \in A, (a,a) \in R$ because $R$ is reflexive, and therefore:

$$a \in [a]_R \implies [a]_R \neq \emptyset$$

3. For all $a \in A$

$$[a]_R \subseteq A \implies \bigcup_{a \in A}[a]_R \subseteq A$$

In the opposite direction: $a \in A$ then $a \in [a]_R$ (reflexive), therefore:

$$A \subseteq \bigcup_{a \in A}[a]_R \implies A = \bigcup_{a \in A}[a]_R$$

2. If for $a,b \in A$:
$$[a]_R \cap [b]_R = \emptyset \implies [a]_R=[b]_R$$

  i. Proving $(a,b),(b,a) \in R$:

  Given $c \in A$ such that $c \in [a]_R \cap [b]_R$.

  In other words, if $(c,b) \in R$ from *transitivity* we get that $(a,b) \in R$
  and using *symmetry* we get $(b,a) \in R$.

  ii. Proving $[a]_R=[b]_R$

  Proving $[a]_R \subseteq [b]_R$:

  Let $d \in [a]_R$, we need to prove $d \in [b]_R$

  Given $(a,d) \in R$ we need to prove $(b,d) \in R$

$$(b,a) \in R \underbrace{\implies}_{\text{transitivity}} (b,d) \in R
\implies d \in [b]_R \implies [a]_R \subseteq [b]_R$$

And the other way...

#### Symbol:

Equivalence closures: $A/R$
$$A/R  = \{[a]_R \mid a \in A\}$$

$D$ is the *representative set* if:
$$\forall a \in A: |D \cap [a]_R| = 1$$

#### Examples:

1. Identity relation
$$
\begin{gathered}
    \forall a \in A: [a]_R = \{a\} \\
    A/R=\{\{a\}\}_{a \in A} \\
    D=A
\end{gathered}
$$

2. Universal relation
$$
\begin{gathered}
    R = A \times A \\
    A/R = \{A\} \\
    \forall a \in A: D = \{a\}
\end{gathered}
$$

3.
$$
\begin{gathered}
    A  = \mathbb{Z} \\
    R = \{(x,y) \mid x,y \in A, 2 | x-y \} \\
    [0]_R = \{-4,-2,0,2,4,6,\ldots\} \\
    [1]_R = \{-3,-1,1,3,5,\ldots\} \\
    A/R = \{[0]_R, [1]_R \} \\
    D = \{0,1\} \\
    \text{ (or any two even/odd numbers)}
\end{gathered}
$$
