---
title:  Linear Algebra - Chapter 1
author: Moshe Krumbein
date: Fall 2021
---

# Intro

There are two properties of vectors: *magnitude* and *direction*.

An object that only has a magnitude is called a *scalar*, and an object that
only has a direction is called an *angle*.

#### Examples of scalars:

temperature, weight, volume

#### Examples of vectors:

force, velocity

$$\mathbb{R}^n\left\{\begin{bmatrix}
    x_1\\x_2\\ \vdots \\ x_n
\end{bmatrix} \Huge \mid x_1, x_2, \mathellipsis x_n \in \mathbb{R}\right\}$$

## Equivalence between vectors

$$\vec u = \vec u \iff \left(x_1 = y_1 \wedge x_2 = y_2, \wedge \mathellipsis
\wedge x_m = y_m\right)$$


This only works when $\vec x, \vec y$ are both in $\mathbb{R}^n$

## Adding vectors

$\vec v, \vec u$ are both vectors in $\mathbb{R}^n$ and $\lambda \in
\mathbb{R}$ is a scalar.

$$\vec u + \vec v = \begin{bmatrix}
    x_1 + y_1 \\
    x_2 + y_2 \\
    \vdots \\
    x_n + y_n
\end{bmatrix}$$

Technically, it would be more accurate to write $\vec u \oplus \vec v$ because
we're adding vectors and not scalars, but we understand what $+$ is in context.

$$\vec u + \vec v = \vec v + \vec u$$


$$\vec u, \vec v \in \mathbb{R}^n \implies \vec u + \vec v \in \mathbb{R}^n
\wedge \lambda \cdot \vec u \in \mathbb{R}^n$$

If $\vec u \in \mathbb{R}^n$ and $\vec v \in \mathbb{R}^m$, $\vec u + \vec v$
is *undefined*.

## Multiplying vectors with scalars

$$
\lambda \cdot \vec u = \begin{bmatrix}
    \lambda u_1 \\
    \lambda u_2 \\
    \vdots \\
    \lambda u_n
\end{bmatrix}
$$

# [Linear Combination](https://en.wikipedia.org/wiki/Linear_combination)

Given $m,n \in \mathbb{N}$ and $\vec u_1, \vec u_2, \mathellipsis \vec u_n$ in
$\mathbb{R}^m$, and $\vec v \in \mathbb{R}^m$.

$$
\exists \; \lambda_1,\mathellipsis \lambda_n \in \mathbb{R}
\text{ s.t. } \vec v = \sum_{i=1}^{n} \lambda_i \vec u_i
:= \lambda_1 \vec u_1, \mathellipsis, \lambda_n \vec u_n
$$

$\vec v$ is a linear combination.

#### Example:

$$\begin{bmatrix}
    3\\1
\end{bmatrix} = 1 \cdot \begin{bmatrix}
    3\\2
\end{bmatrix} + 2 \cdot \begin{bmatrix}
    0\\\frac{1}{2}
\end{bmatrix}$$

#### Example 1:

Is $\begin{bmatrix}
    1\\2\\3
\end{bmatrix}$ a linear combination of $\begin{bmatrix}
    0\\1\\-5
\end{bmatrix}, \begin{bmatrix}
    -1\\-1\\2
\end{bmatrix}, \begin{bmatrix}
    1\\1\\2
\end{bmatrix}$ ?

$$\lambda_1 \begin{bmatrix}
    0\\1\\-5
\end{bmatrix} + \lambda_2 \begin{bmatrix}
    -1\\-1\\2
\end{bmatrix} + \lambda_3 \begin{bmatrix}
    1\\1\\2
\end{bmatrix} = \begin{bmatrix}
    1\\2\\3
\end{bmatrix}$$

$$
- \lambda_1 + \lambda_3 = 1 \mid
\lambda_1 - \lambda_2 + \lambda_3 = 2 \mid
-5 \lambda_1 + 2 \lambda_2 + 2 \lambda_3 = 3
$$
$$\lambda_1 = 1 \quad \lambda_2 = 1.5 \quad \lambda_3 = 2.5$$

#### Example 2:

$$\begin{bmatrix}
    0\\2\\1
\end{bmatrix}, \begin{bmatrix}
    1\\-1\\1
\end{bmatrix} = \vec u_1, \vec u_2$$

$$
\lambda_1 \begin{bmatrix}
    0\\2\\1
\end{bmatrix}+ \lambda_2 \begin{bmatrix}
    1\\-1\\1
\end{bmatrix} = \begin{bmatrix}
    \lambda_2 \\
    2 \lambda_2 - \lambda_1 \\
    \lambda_1 + \lambda_2
\end{bmatrix}
$$

$$
\begin{bmatrix}
    x\\y\\z
\end{bmatrix} = \begin{bmatrix}
    \lambda_2 \\
    2 \lambda_1 - \lambda_2 \\
    \lambda_1 + \lambda_2
\end{bmatrix}
$$

$$\begin{gathered}
    \lambda_2 = x \\
    \lambda_1 = \frac{x+y}{2}
\end{gathered}$$

Therefore:
$$\begin{bmatrix}
    x\\y\\\frac{y+3x}{2}
\end{bmatrix}$$

For all $\{\vec u_1, \vec u_2,\ \mathellipsis \vec u_n\}$, $0 \cdot u_1, 0
\cdot u_1 \mathellipsis = \vec 0$. This is called its *trivial combination*.

If I wanted to symbolize $n$ vectors $\vec u$ in $\mathbb{R}^m$:

$$\vec u_1 = \begin{bmatrix}
    a_{1,1}\\a_{2,1}\\ \vdots \\ a_{m,1}
\end{bmatrix}, \vec u_2 = \begin{bmatrix}
    a_{1,2}\\a_{2,2}\\ \vdots \\ a_{m,2}
\end{bmatrix}, \mathellipsis, \vec u_n = \begin{bmatrix}
    a_{1,n} \\ a_{2,n} \\ \vdots \\ a_{m,n}
\end{bmatrix}$$


The number of elements  is $m$ and the number of vectors is $n$.

# [Gaussian Elimination (row reduction)](https://en.wikipedia.org/wiki/Gaussian_elimination)

$$
    \left[
    \begin{array}{ccccc|c}
        4 & -1 & -3 & 0 & 8 & 8 \\
        1 & 1 & -7 & 2 & 3 & 5 \\
        -5 & 2 & 0 & 0 & -7 & -7 \\
        2 & 0 & -4 & 1 & 4 & 5
    \end{array}\right]
    \begin{array}{c}
        ~ \\
        ~ \\
        ~
    \end{array}
$$

Also known as *Gauss-Jordan reduction*. In short, Gauss goes from from
top-right to bottom-left simplifying the matrix, and Jordan goes back the other
way, simplifying the columns.
