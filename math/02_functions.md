---
title: Functions
date: Fall 2020
author: Moshe Krumbein
---

# What's a function?

A function is a binary relation between two sets that associates every element
of the first set to exactly one element of the second set.

Domain are the possible values of $x$ and range is the possible values of $y$.

For example:

$$
\begin{gathered}
    f:D \to E \\
    D \in \mathbb{R},E \in \mathbb{R}
\end{gathered}
$$

# Natural domain

$$
\begin{gathered}
    y=\frac{x^2 -5x +7}{x^2 -4} \\
    \mathbb{R}\backslash \{-2,2\}
\end{gathered}
$$

# Definitions

*Natural domain* - the maximum set of values for which the function is defined

*Injective function (one-to-one)* - each value in range has at most one
corresponding value as part of the domain

*Surjective function* - where every value in the range has at least one
value in the domain

If a function is both injective and surjective, it is an *invertible function*
such that exists an *inverse function* such that:

$$f:X \to Y, \quad \exists! \; g:Y \to X$$
$$f(x)=y \iff g(y)=x$$

It can also be written as $f^{-1}(x)$.

The *image* of a function is the set of all output values it may produce.

# Composing functions

$$f: A \to B, \quad g:C \to D$$

$$f \circ g : C \to B \iff D \subseteq A$$
$$(f \circ g)(x) = f(g(x))$$

$$g \circ f : A \to D \iff B \subseteq C$$
$$(g \circ f)(x) = g(f(x))$$

If we compose a function with its inverse, it always returns $x$.

$$\pagebreak$$

# Simple transformations
If $(a,b)$ is on the graph $y=f(x)$, then:

$$
\begin{alignedat}{2}
    &(a,b+n) \quad &\exists \in \quad &y = f(x)+n \\
    &(a-n,b) \quad &\exists \in \quad &y = f(x+n) \\
    &(a,b \cdot n) \quad &\exists \in \quad &y = f(x) \cdot n \\
    &\left(\frac{a}{n},b\right) \quad &\exists \in \quad &y = f(x \cdot n) \\
    &(a,-b) \quad &\exists \in \quad &y = -f(x) \\
    &(-a,b) \quad &\exists \in \quad &y = f(-x) \\
    &(a,|b|) \quad &\exists \in \quad &y = |f(x)| \\
    &(|a|,b) \quad &\exists \in \quad &y = f(|x|) \\
\end{alignedat}
$$

# Evenness of function

Given $y=f(x) \quad f: D \to E$:

If:

1. If $a \in D$ then $-a \in D$
2. For all $f(a) = f(-a):a \in D$

Then the function is *even*.

If:

1. If $a \in D$ then $-a \in D$
2. For all $-f(a) = f(-a):a \in D$

Then the function is *odd*.

$$\break$$

The sum of *odd* parts in a function is *odd*.

The sum of *even* parts in a function is *even*.

$$\break$$

$$y=f(x), f:D \to E$$
$$\text{Given: $a \in D$ then $-a \in D$}$$

All functions such be broken down into the sum of an even and an odd component:

$$g(x)=\frac{f(x)+f(-x)}{2} \text{ is even.}$$
$$h(x)=\frac{f(x)-f(-x)}{2} \text{ is odd.}$$

$$f(x)=g(x)+h(x)$$

$$\break$$

# Graphing quadratic functions

$$(A \pm B)^2 = A^2 \pm 2AB + B^2$$
$$Ax^2 + Bx + C$$
$$y=A\left(\left(x+\frac{B}{2A}\right)^2 + \frac{4AC-B^2}{4A}\right)$$
$$\Delta = B^2 - 4AC$$
$$y=A\left(\left(x+\frac{B}{2A}\right)^2 + \frac{-\Delta}{4A}\right)$$
$$\left(-\frac{B}{2A}, -\frac{\Delta}{4A}\right)$$

# Periodicity

$$y=f(x), f: D \to E $$

Is a *periodic function* if of period $T$:

1. For each $x \in D$, then $x \pm T \in D$
1. For each $x \in D$, then $f(x)=f(x+T)$

From 1 we see that for $x \in D$ for each $k \in \mathbb{Z}$:
$$x \pm kT \in D$$
From 2 we see that for $x \in D$ for each $k \in \mathbb{Z}$:
$$f(x+kT) = f(x)$$

The *minimum period* is the smallest period in a given function.

*Integer part $([x])$ *- the integer that has the largest absolute value less than or
equal to the absolute value of $x$.
$$D= \mathbb{R}, \text{Im}=\mathbb{Z}$$

*Fractional part $(\{x\} = x- [x])$ *- the decimal part of a positive number or
one minus the decimal part of a negative number
$$D = \mathbb{R}, \text{Im}=[0,1)$$

$f(x)= \{x\}$ is periodic with the period $T=1$.

# Transformations on periodic functions

If $y=f(x)$ is periodic, and $T$ is the minimum period, then:

$$
\begin{alignedat}{2}
    &y=f(x+n) \quad & \to \quad &T \\
    &y=Mf(x)  \quad & \to \quad &T \\
    &y=-f(x)  \quad & \to \quad &T \\
    &y=f(x+n) \quad & \to \quad &T \\
    &y=f(mx)  \quad & \to \quad &\frac{T}{m} \\
    &y=f(-x)  \quad & \to \quad &T \\
\end{alignedat}
$$

If $f(x)$ is a periodic function with a minimum period of $T$ and $g(x)$ is any
function, then $g(f(x))$ is a periodic function with a period of $T$ (though it
may not be the minimum).

If $y=f(x)$ is a periodic function with a minimum period of $T_1$ and $y=g(x)$ is a
periodic function with a period of $T_2$ then $y=f(x)+g(x)$ is a periodic
function with period of the least common multiple of $(T_1, T_2)$.

# Inverse trigonometric functions

# $\sin$ and $\arcsin$
$$f (x)=\sin    x \quad f:\left[-\frac{\pi}{2},\frac{\pi}{2}\right] \to [-1,1]$$
$$f'(x)=\arcsin x \quad f:[-1,1] \to \left[-\frac{\pi}{2},\frac{\pi}{2}\right]$$

$$\sin(\arcsin x) = x \quad x \in [-1,1]$$
$$\arcsin(\sin x) = x \quad x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$$

# $\cos$ and $\arccos$

$$f (x)=\cos    x \quad f:[0,\pi] \to [-1,1]$$
$$f'(x)=\arccos x \quad f:[-1,1] \to [0,\pi]$$

$$\cos(\arccos x) = x \quad x \in [-1,1]$$
$$\arccos(\cos x) = x \quad x \in [0,\pi]$$

# $\tan$ and $\arctan$

$$f (x)=\tan    x \quad f:\left(-\frac{\pi}{2},\frac{\pi}{2}\right) \to \mathbb{R}$$
$$f'(x)=\arctan x \quad f:\mathbb{R} \to \left(-\frac{\pi}{2},\frac{\pi}{2}\right)$$

$$
\begin{alignedat}{2}
    &\sin (\arcsin x) = x \quad &x& \in [-1,1] \\
    &\cos (\arccos x) = x \quad &x& \in [-1,1] \\
    &\tan (\arctan x) = x \quad &x& \in \mathbb{R} \\
    \\
    &\arcsin (\sin x) = x \quad &x& \in \left[-\frac{\pi}{2},\frac{\pi}{2}\right] \\
    &\arcsin (\cos x) = x \quad &x& \in [0,\pi] \\
    &\arctan (\tan x) = x \quad &x& \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right) \\
\end{alignedat}
$$

# Additional identities

$$\cos(\arcsin x) = \sqrt{1-\sin^2(\arcsin(x))} = \sqrt{1-x^2}$$
$$\sin(\arccos x) = \sqrt{1-\cos^2(\arccos(x))} = \sqrt{1-x^2}$$

$$\tan(\arccos x) = \frac{\sqrt{1-x^2}}{x}$$
