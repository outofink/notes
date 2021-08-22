---
title: Theorems
author: Moshe Krumbein
date: Spring 2021
---

# Theorems

## Intermediate value theorem

### Cauchy's mean value theorem

Given a function $f(x)$ which is continuous on the interval $[a, b]$, if $f(a)
\cdot f(b) < 0$, there exists at least one $f(x) = 0$ where $a<x<b$.

### General intermediate value theorem

Given a function $f(x)$ which is continuous on the interval $[a, b]$, there
exists at least one $x_1 \in [a,b]$ such that $f(a) \leq f(x_1) \leq f(b)$.

### Example

Prove that $x^3 + 2\sin(x) = 5$ has at least one solution.

$$
f(x) = x^3 +2\sin(x) - 5, x \in \mathbb{R}
$$

$$
\begin{array}{c|c}
\lim\limits_{x \to \infty} f(x) = \infty
&
\lim\limits_{x \to -\infty} f(x) = -\infty
\end{array}
$$

Therefore, as per the intermediate value theorem, there exists at least one
solution.

## Weierstrauss theorem

1. A function which is continuous in $[a,b]$ is bounded within that interval.
2. A function which is continuous in $[a,b]$ has within it a maximum and a
   minimum. In other words, there exists on the interval $x_1, x_2$ such that:
   $$\forall \; x \in [a,b] \;\exists\; f(x_1) \leq f(x) \leq f(x_2)$$

## Rolle's theorem

$f(x)$ is continuous on the interval $[a,b]$ and is differentiable on the
interval $(a,b)$. If $f(a)=f(b)$, then there exists $c \in (a,b)$ such that
$f'(c)=0$.

## Lagrange's theorem

Given a function $f(x)$ which is continuous on the interval $[a,b]$ and
differentiable on the interval $(a,b)$, there exists $c \in (a,b)$ such that
$f'(c) = \frac{f(b)-f(a)}{b-a}$.

## The Mean Value Theorem

If a function $f(x)$ is continuous on the closed interval $[a,b]$ and differentiable
on the open interval $(a,b)$, then there exists a point $c$ in the interval
$(a,b)$ such that $f'(c)$ is equal to the function's average rate of change
over $[a,b]$.

## Linear Approximation by Differentiation

$$f(x) \approx f(a) +f'(a)(x-a)$$
