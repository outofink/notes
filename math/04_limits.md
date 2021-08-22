---
title: Limits
date: Fall 2020
author: Moshe Krumbein
---

# Neighborhood

The _neighborhood_ of a value is an open set of values surrounding the
target value.

i.e. the neighborhood of $5$ could be $(4.99999, 5.00001)$

The smallest positive value is denoted as $\delta$ such that $5 \in
(5-\delta,5+\delta)$

$$\delta, \epsilon > 0$$

$$ a \text{ is an interior point of } I \iff I \subset (a-\delta,a+\delta)$$

It is possible to approximate the limit by using numbers very close to the
limit (I.e. instead of $1$, input $0.99999999$ or $1.00000001$)

# Basics

$$\lim\limits_{x \to a} f(x) =b$$

For all $\epsilon > 0$ there exists $\delta > 0$ such that for all $a-\delta<x<a+\delta$
there exists $b-\epsilon<f(x)<b-\epsilon$.

It is possible to take the limit from the left ($\lim\limits_{x \to a^-}{f(x)}=b$)
or the right ($\lim\limits_{x \to a^+}{f(x)}=b$).

Even though the limit from the left and the right both exist, if they both
don't approach the same value, the limit does not exist.

# Calculating limits

If $a$ is an internal value to the domain of the function $f(x)$, then:
$$\lim\limits_{x \to a} f(x) = f(a)$$

For example, $\lim\limits_{x \to 0} \sqrt{x}$ does not exist even though
$\sqrt{0}$ exists, because the domain doesn't have a neighborhood of values
surrounding $0$ from both sides.

If given $y=f(x), y=g(x)$, where $\lim\limits_{x \to a} f(x) =
b_1$ and $\lim\limits_{x \to a} g(x) =b_2$, then:
$$\lim\limits_{x \to a} (f(x) \pm g(x)) = b_1 \pm b_2 \tag{1}$$
$$\lim\limits_{x \to a} (f(x) \cdot g(x)) = b_1 \cdot b_2 \tag{2}$$
$$\lim\limits_{x \to a} \left(\frac{f(x)}{g(x)}\right) = \frac{b_1}{b_2}, \quad b \neq 0 \tag{3}$$

Given $\lim\limits_{x \to a} f(x) = b$ and $\lim\limits_{x \to a} g(x) =c$, then:
$$\lim\limits_{x \to a} (g \circ f)(x) = c$$

Given $\lim\limits_{x \to a} f(x) = b$ and $\lim\limits_{x \to a} g(x) =+\infty$, then:
$$\lim\limits_{x \to a} (f(x) + g(x)) = +\infty$$

$$
\lim\limits_{x \to a} (f(x) \cdot g(x)) = \begin{cases}
    +\infty, &\quad b>0 \\
    -\infty, &\quad b<0 \\
    \text{indeterminate}, &\quad b=0
\end{cases}
$$

$$\lim\limits_{x \to a} \frac{1}{g(x)} = 0$$

# Indeterminates

Given $\lim\limits_{x \to a} f(x) = 0$ and $\lim\limits_{x \to a} g(x) = 0$,
then:

$$\lim\limits_{x \to a} \frac{f(x)}{g(x)} = \frac{0}{0} = \;? \tag{1}$$

Given $\lim\limits_{x \to a} f(x) = +\infty$ and $\lim\limits_{x \to a} g(x) = +\infty$,
then:

$$\lim\limits_{x \to a} \frac{f(x)}{g(x)} = \frac{+\infty}{+\infty} = \;? \tag{2}$$

Given $\lim\limits_{x \to a} f(x) = +\infty$ and $\lim\limits_{x \to a} g(x) = +\infty$,
then:

$$\lim\limits_{x \to a} (f(x)-g(x)) = \infty - \infty = \;? \tag{3}$$

Given $\lim\limits_{x \to a} f(x) = +\infty$ and $\lim\limits_{x \to a} g(x) = 0$,
then:

$$\lim\limits_{x \to a} \frac{f(x)}{g(x)} = \frac{\infty}{0} = \;? \tag{4}$$

# Workarounds

$$\lim\limits_{x \to a} f(x) = b+$$

1. $\lim\limits_{x \to a} f(x) = b$
2. $\delta > 0, a-\delta < x < a+ \delta : f(x) \ge b$

If $b>0$:
$$\frac{b}{0^+} = +\infty$$
$$\frac{b}{0^-} = -\infty$$

For example:

$$\lim\limits_{x \to \pi^+} \frac{x}{\sin x} = \frac{\pi^+}{0^-} = -\infty$$

$$
\lim\limits_{x \to 0^+} \frac{\log x}{x} = \frac{-\infty}{0^+} = -\infty
\cdot \frac{1}{0^+} = -\infty \cdot (+\infty) = -\infty
$$

$$
\lim\limits_{x \to 0^+} (\log^2 x + \log x -5) = \lim\limits_{x \to 0^+} (\log x)(\log x + 1) - 5
= (-\infty)(-\infty) - 5 = +\infty
$$

# Limit as $x \to \infty$

$$y=f(x) \quad (a, +\infty) \subset D$$
$$\lim\limits_{x \to +\infty} f(x) = b$$

For each $\epsilon>0$, exists N such that for every $x>N$ exists $b-\epsilon<f(x)<b+\epsilon$.

$$y=f(x) \quad (-\infty, a) \subset D$$
$$\lim\limits_{x \to -\infty} f(x) = b$$

For each $\epsilon>0$, exists N such that for every $x<N$ exists $b-\epsilon<f(x)<b+\epsilon$.

## Polynomials

$$\text{Example: }\lim\limits_{x \to +\infty} \frac{-x^2 +3x -7 }{5x^2 -x -11}$$

We factor out the largest factor (in our example $x^2$) and solve:

$$=\lim\limits_{x \to +\infty} \frac{x^2(-1+\frac{3}{x}-\frac{7}{x^2})}{x^2(5 - \frac{1}{x} - \frac{11}{x^2})}$$
$$=-\frac{1}{5}$$

# "Sandwich Rule" (Squeeze Theorem)

$$\text{Given: } \lim\limits_{x \to a} f(x) = b \quad \lim\limits_{x \to a} g(x) = b$$
$$\text{If: } g(x) \leq h(x) \leq f(x)$$
$$\text{Then: } \lim\limits_{x \to a} h(x) = b$$

Given functions $q(x)$ and $p(x)$:

1. $\lim\limits_{x \to a} p(x) = 0$
2. $m \leq q(x) \leq n \quad (m, n \in \mathbb{R})$

$$\lim\limits_{x \to a} q(x) \cdot p(x) = 0$$

## Example

$$\lim\limits_{x \to +\infty} \frac{\sin x}{x}=\lim\limits_{x \to +\infty} \sin x \cdot \frac{1}{x}$$
$$\text{Because: } -1 \leq \sin x \leq 1$$
$$\lim\limits_{x \to -\infty} \sin x \cdot \frac{1}{x} = 0$$

$$\lim\limits_{x \to +\infty} \frac{3x^3-5x^2+\cos(x^5-3x)}{2x^3-5x-\sin(\sqrt{x})}=\frac{3}{2}$$

# Solving $\lim\limits_{x \to 0} \frac{\sin x}{x}$

For values $x \in \left(0,\frac{\pi}{2}\right)$:
$$\sin x < x < \tan x$$
Therefore:
$$\frac{1}{\sin x} > \frac{1}{x} > \frac{1}{\tan x} \; || \cdot \sin x$$
$$1 > \frac{\sin x}{x} > \cos x$$

$$\lim\limits_{x \to 0} \frac{\sin x}{x}$$
$$1 > \frac{\sin x}{x} > 1$$
$$\lim\limits_{x \to 0} \frac{\sin x}{x} = 1$$

## Generalization

$$\lim\limits_{x \to 0} \frac{\sin ax}{x} = a$$
$$\lim\limits_{x \to 0} \frac{\sin ax}{\sin bx} = \frac{a}{b}$$

## limit as $x \to \pi$

$$\lim\limits_{x \to \pi} \frac{\sin 5x}{\sin 2x}$$
$$=\lim\limits_{t \to 0} \frac{\sin (5t + 5 \pi)}{\sin (2t + 2 \pi)}$$
$$=\lim\limits_{t \to 0} \frac{-\sin 5t}{\sin 2t} = -\frac{5}{2}$$

## Why we use radians

For small values of $x$, $\sin x$ and $\tan x$ approach $x$.

# Defining $e$

$$\lim\limits_{x \to +\infty} \left(1+\frac{1}{x}\right)^x = 2.718281828 \ldots =e$$
$$=\lim\limits_{x \to 0} (1+x)^{\frac{1}{x}}$$

# Continuity

Function $y=f(x)$ is _continuous_ at the point $x=a$ given:

1. Exists $b = \lim\limits_{x \to a-} f(x)$
1. Exists $c = \lim\limits_{x \to a+} f(x)$
1. $b=c=f(a)$

## Elementary functions

$$y = c, x^n, a^x, |x|, \sin x, \cos x, \tan x, \arcsin x, \arccos x, \arctan x$$

If $f(x)$ and $g(x)$ are _elementary_ functions then:

$$
\begin{array}{c|c}
\begin{gathered}
    y=f(x)+g(x) \\
    y=f(x)-g(x) \\
    y=f(x) \cdot g(x) \\
    y=f(g(x))
\end{gathered}
&
\begin{gathered}
    y=\frac{f(x)}{g(x)} \\
    y=f(x)^{g(x)} \\
    y=\log_{f(x)}{g(x)} \\
\end{gathered}
\end{array}
$$

are all elementary functions.

If $a$ is an interior point of $f(x)$, then $f(x)$ at point $a$.

The exception being _piecewise_ functions.

# Piecewise functions

$$
f(x) = \begin{cases}
    x-5, \quad &x \ge 3 \\
    8-2x, \quad &x < 3
\end{cases}
$$

If $\lim\limits_{x \to a+} f(x) = b$, $\lim\limits_{x \to a-} f(x) = b$, and
$f(a) = b$, then the function is continuous at point $a$.

In the example above, the function would not be continuous at point $3$,
because the limit from the left and the limit from the right are not equal.

However the function

$$
f(x) = \begin{cases}
    x-5, \quad &x \ge 3 \\
    -8-2x, \quad &x < 3
\end{cases}
$$

is continuous at $x=3$ because the limit from the left, right, and at $3$ are all equal.

# Discontinuity

## Removable discontinuity

1. $\lim\limits_{x \to a+} f(x) =b$
1. $\lim\limits_{x \to a-} f(x) =b$
1. $f(a) = c$ or does not exist

### Examples

$$f(x)=\frac{x^2-4}{x-2} \tag{1}$$
$$\lim\limits_{x \to 2-} f(x) = \lim\limits_{x \to 2+} f(x) = 4$$

$$
f(x) = \begin{cases}
    \frac{\sin 4x}{x},  \quad &x > 0 \\
    4+ e^{\frac{1}{x}}, \quad &x < 0
\end{cases}\tag{2}
$$

$$\lim\limits_{x \to 0-} f(x) = \lim\limits_{x \to 0+} f(x) = 4$$

## Step/jump discontinuity (type 1)

1. $\lim\limits_{x \to a+} f(x) =b$
1. $\lim\limits_{x \to a-} f(x) =c$
1. $b \neq c$

### Examples

$$f(x) = x \sqrt{\frac{1}{x^2}} \tag{1}$$

$$
\begin{array}{c|c}
\lim\limits_{x \to 0+} f(x) =  1 & \lim\limits_{x \to 0-} f(x) = -1
\end{array}
$$

$$
f(x) = \begin{cases}
    \frac{\sin(x-1)}{x-1}, \quad &x < 1 \\
    x^{\frac{1}{x-1}},     \quad &x > 1
\end{cases} \tag{2}
$$

$$
\begin{array}{c|c}
\lim\limits_{x \to 1-} f(x) = 1 & \lim\limits_{x \to 1+} f(x) = 1
\end{array}
$$

## Asymptotic discontinuity (type 2)

The limit from at least one side is infinity or does not exist.

### Examples

$$f(x) = \frac{x^2 -5x +6}{x^2-4} \tag{1}$$
$$\lim\limits_{x \to -2} \frac{x-3}{x+2}$$

$$
\begin{array}{c|c}
\lim\limits_{x \to -2^-} \frac{x-3}{x+2} = \frac{-5}{0^-} = +\infty \&
\lim\limits_{x \to -2^+} \frac{x-3}{x+2} = \frac{-5}{0^+} = -\
\end{array}
$$

$$f(x) = e^{-\frac{1}{x}} \tag{2}$$

$$
\begin{array}{c|c}
\lim\limits_{x \to 0^+} e^{-\frac{1}{x}} = e^{-\frac{1}{0^+}} = 0 &
\lim\limits_{x \to 0^-} e^{-\frac{1}{x}} = e^{-\frac{1}{0^-}} = +\infty
\end{array}
$$

# Intermediate value theorem

Given $f(a)>0$ and $f(b)<0$ and $y=f(x)$ is continuous, there exists at least
one $c \in (a,b)$ such that $f(c) = 0$.
$$f(a) \cdot f(b) < 0$$
$$\exists \;c \in (a,b) \to f(c) = 0$$

$$Ax^5 +Bx^2+Cx+D=0 \;|| :A \quad A \neq 0$$
$$x^3 + \frac{B}{A}x^2 + \frac{C}{A}x + \frac{D}{A} = 0$$
$$\frac{B}{A} =a, \frac{C}{A} =b, \frac{D}{A}=c$$
$$f(x)=x^3+x^2+bx+c=0$$

$$
\begin{array}{c|c}
\lim\limits_{x \to +\infty} f(x) = +\infty & \lim\limits_{x \to -\infty} f(x) = -\infty
\end{array}
$$

$$\forall n \exists b \to x>b, f(x) >0$$

$$\lim\limits_{x \to +\infty} f(x) = +\infty: \exists a \forall x>a \exists f(x)>0$$
