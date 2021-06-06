--- 
title: Definite Integrals 
author: Moshe Krumbein 
date: Spring 2021
---

# Definite Integrals

## Riemann sum

### Definition

Let $[a,b]\rightarrow \mathbb{R}$ be a function defined on a closed interval
$[a,b]$ of the real numbers, $\mathbb{R}$, and

$$P=\left\{[x_{0},x_{1}],[x_{1},x_{2}],\dots ,[x_{n-1},x_{n}]\right\}$$

be a partition of I, where

$$a=x_{0}<x_{1}<x_{2}<\cdots <x_{n}=b$$

A Riemann sum $S$ of $f$ over $I$ with partition $P$ is defined as

$$S=\sum _{i=1}^{n}f(x_{i}^{*})\,\Delta x_{i}$$

where $\Delta x_{i}=x_{i}-x_{i-1}$ and $x_{i}^{*}\in [x_{i-1},x_{i}]$. One
might produce different Riemann sums depending on which $x_{i}^{*}$'s are
chosen. In the end this will not matter, if the function is Riemann integrable,
when the difference or width of the summands $\Delta x_{i}$ approaches zero.

$$\int_{a}^{b}f(x)dx = \lim\limits_{n \to \infty} \frac{b-a}{n}
\sum_{k=1}^{n}f\left(a+\frac{k}{n}(b-a)\right)$$

## Newton-Leibniz Theorem

$$\int_{a}^{b} f(x)dx = F(x) \Big|_a^b = F(b) - F(a)$$

## Characteristics

1. If $a<b$ and $f(x)>$ or $a<b$ and $f(x)>0$ then $\int_{a}^{b}f(x)dx<0$.

    If $a<b$ and $f(x)<$ or $a>b$ and $f(x)>0$ then $\int_{a}^{b}f(x)dx>0$.

2. $\int_{a}^{b}f(x)dx = \int_{a}^{c}f(x)dx + \int_{c}^{b}f(x)dx$

3. $\int_{a}^{a}f(x)dx = 0$

4. $\int_{a}^{b}f(x)dx = -\int_{b}^{a}f(x)dx$

5. $\int_{-a}^{a} f(x)dx = 0$ where $f(x)$ is an odd function

6. $\int_{-a}^{a} f(x)dx = 2\int_{0}^{a}f(x)dx$ where $f(x)$ is an even
   function

## Definite integrals using partial fractions

$$\int_{a}^{b}uv'dx = \Big[uv\Big]_{x=a}^{x=b} - \int_{a}^{b}u'vdx$$

# Applications of Integrals

## Area between curves

If $f$ and $g$ are continuous and $f(x) \ge g(x)$, the area between them is:

$$\int[f(x)-g(x)]dx$$

Naturally, if the shape of the area forms a familiar geometric shape it is
preferable to do the geometric calculation rather than the integral.

# Volumes of Solids of Revolutions

How to find the volume of a function rotated around the $x$-axis.

## Method of Disks

The volume of a disk is $\pi r^2 h$ so for a function we get between $a$ and
$b$ we get:

$$\lim\limits_{n \to \infty} f(x)\pi \cdot
\frac{b-a}{n}\sum_{k=1}^{n}f^2\left(a+\frac{b-a}{n}k\right)$$ $$\boxed{V=\pi
\int_{a}^{b}f^2(x)dx}$$

### Example

$$f(x)=\sqrt x, 1 \leq x \leq 3, \text{rotated around the $x$-axis.}$$ $$V =
\pi \int_{1}^{3}(\sqrt x)^dx=\pi \frac{x^2}{2}\Big|_{x=1}^{x=3}=\boxed{4\pi}$$

## Rotation around a shifted axis

$$f(x)=\sqrt x, 1 \leq x \leq 3, \text{rotated around $y=1$.}$$ $$V = \pi
\int_{1}^{3}R^2(x)dx= \pi \int_{1}^{3} (\sqrt x - 1)^2dx$$

## Area of washers

The area of the larger circle minus the area of the smaller circle

$$V= \pi \int_{a}^{b} (R^2-r^2)dx$$

# Fundamental theorem of calculus

## Part 1

### Definition

$f(x)$ is continuous om the closed interval $[a,b]$ and differentiable on the
open interval $(a,b)$, then the function $F(x)$ can be expressed as:

$$F(x) = \int_{a}^{b} f(x)dx, \quad a \leq x, \leq b$$

Therefore:

$$F'(x) = \frac{d}{dx}F(x)=f(x)$$

### Proof

$$F'(x) = \lim\limits_{h \to 0} \frac{F(x+h) -F(x)}{h}$$ $$=\lim\limits_{h \to
0}  \frac{1}{h}\left[\int_{a}^{x+h}f(u)dx + \int_{x}^{a}f(u)du\right]$$
$$=\lim\limits_{h \to 0} \frac{1}{h} \int_{x}^{x+h}f(u)du$$
$$\int_{x}^{x+h}f(u)du \approx f(x) \cdot h$$ $$\lim\limits_{h \to 0}
\int_{x}^{x+h}f(u)du = \lim\limits_{h \to 0} \frac{1}{h} \cdot h$$
$$=\lim\limits_{h \to 0} f(x) = f(x)$$ $$ \blacksquare$$

#### Indefinite integrals

$$F(x)=\int_{a}^{x}f(u)du, G(x)=\int_{b}^{x}f(u)du$$ $$F'(x)=G'(x)=f(x)$$

Functions whose derivatives are equal differ only by a constant:

$$F(x)= \int_{x}^{x}f(u)du =
\int_{a}^{b}f(u)du+\int_{b}^{x}f(u)du=\int_{a}^{b}f(u)du+ G(x) = C + G(x)$$

#### General anti-derivatives

$$\int_{a}^{x}f(u)du + C = \int f(x)dx$$

## Part 2

> *How do we calculate that constant?*

Given a function $f(x)$ continuous on $[a,b]$ and differentiable on $(a,b)$,
then:

$$\int_{a}^{b} f(x)dx= F(b)-F(a)$$

Where $F(x)$ is the anti-derivative of $f(x)$

Which is essentially a proof of Newton-Leibniz theorem

### Proof

Let $F(x)$ and $G(x)$ be anti-derivatives of $f(x)$ such that:

$$G(x)= \int_{a}^{x}f(u)du \implies F(x)=G(x)+C$$

Therefore:

$$G(a)= \int_{a}^{a}f(u)du = 0 \implies F(a) = G(a) + C = C$$ $$G(x) =
\int_{a}^{x}f(u)du = F(x)-C = F(x)-F(x)$$ $$G(b) =
\int_{a}^{b}f(u)du=F(b)-F(a)$$ $$\blacksquare$$

## Derivative of anti-derivative theorem - Leibniz's Rule

If functions $f(x)$ and $g(x)$ are differentiable and the function $f(u)$ is
continuous on $g(x) < u < h(x)$, then:

$$\frac{d}{dx} \int_{g(x)}^{h(x)}f(u)du = f(h(x)) \cdot h'(x) = f(g(x) \cdot
g'(x)$$

### Proof

$$F(x) = \int_{0}^{x}f(u)du$$ $$\int_{g(x)}^{h(x)}f(u)du=
\int_{g(x)}^{0}f(u)du+\int_{0}^{h(x)}f(u)du$$ $$ = -\int_{0}^{h(g)}f(u)du +
\int_{0}^{h(x)}f(u)du$$ $$=F(h(x))- F(g(x))$$

$$\frac{d}{dx}(I) = \frac{d}{dx}\left[F(h(x)-F(g(x)))\right]$$
$$=F'(h(x))h'(x)-F'(g(x))g'(x)$$ $$ = f(h(x))h'(x)- f(g(x))g'(x)$$
$$\blacksquare$$

### Examples

1.

$$\frac{d}{dx}\int_{5}^{\sin x}t^2dt = \sin^2(x) \cdot (\sin x)' - 5^2 \cdot
(5)'$$ $$=\sin^2x \cdot \cos x$$

2.

$$\frac{d}{dx} \int_{x^3}^{3}\arctan t dt = \arctan 3 \cdot (3)' - \arctan(x^3)
\cdot (x^3)'$$ $$=-3x^2 \arctan x^3$$

### Applications

$$\lim\limits_{x \to 0} \frac{1}{x^3}\int_{0}^{x}\frac{t^2}{t^4+1}dt =
\left("\frac{0}{0}"\right)$$ $$\to \lim\limits_{x \to 0}
\frac{\frac{d}{dx}\int_{0}^{x}\frac{t^2}{t^4+1}dt}{\frac{d}{dx}(x^3)}$$
$$=\lim\limits_{x \to 0} \frac{\frac{x^2}{x^3+1}}{3x^2} = \lim\limits_{x \to 0}
\frac{1}{3(x^4+1)} = \boxed{\frac{1}{3}}$$

### Applications in investigating functions

1. Find the extreme points in the function: $$F(x) = \int_{0}^{x}\frac{\sin
t}{t}dt, \quad x > 0$$

$$\frac{d}{dx}F(x)=\frac{d}{dx}\int_{0}^{x}\frac{\sin t}{t}dt = \frac{\sin
x}{x} = 0$$

$$\max F(x) \to x = (2k+1)\pi$$ $$\min F(x) \to x = 2k\pi$$

2. $\displaystyle F(x) = \int_{0}^{x}t^2 \sqrt{2-t}\;dt$

Find:

1. The domain of $F(x)$
2. For $x$ where $F(x)>0$
3. ... $F(x)<0$
4. ... $F(x)=0$

Answer:

1. The domain of $f(x)$ is $2-x \geq 0, \to x \leq 2$ 2.

> $F'(x)= \frac{d}{dx}\int_{-3}^{x}t^2 \sqrt{t-2}\;dt$

> $=x^2 \sqrt{x-2} > 0 \quad\quad \forall\; x \leq 2$

> $F(-3) = \int_{-3}^{-3}T^2\sqrt{T-2} = 0$

3-4.

> When $x<-3   : F(x)<0$

> When $-3<x<2 : F(x)>0$

> When $x=-3   : F(x)=0$

# Improper integrals

1. If $f$ is continuous on $[a, \infty)$, then: $$\int_{a}^{\infty} f(x)dx =
\lim\limits_{b \to \infty} \int_{a}^{b} f(x)dx \tag{1}$$

1. If $f$ is continuous on $(-\infty, b]$, then: $$\int_{-\infty}^{b} f(x)dx =
\lim\limits_{a \to -\infty} \int_{a}^{b} f(x)dx \tag{2}$$

1. If $f$ is continuous on $(a, b]$, then: $$\int_{a}^{b} f(x)dx =
\lim\limits_{c \to a^+} \int_{c}^{b} f(x)dx \tag{3}$$

1. If $f$ is continuous on $[a, b)$, then: $$\int_{a}^{b} f(x)dx =
\lim\limits_{c \to b^-} \int_{a}^{c} f(x)dx \tag{4}$$

In each case, if the limit is finite we say that the improper integral
**converges** and the limit is the value of the improper integral. If the
integral fails to exist the improper integral **diverges**.

Basically, whichever part is undefined is replaced with a limit.

$$\begin{gathered} \int_{2}^{\infty}\frac{1}{x^p}dx = \lim\limits_{b \to
\infty} \int_{1}^{b}\frac{1}{x^p}dx \\ = \lim\limits_{b \to \infty}
\left[\frac{x^{p-1}}{p-1}\right]_{x=1}^{x=b}\\ = \lim\limits_{b \to \infty}
\frac{1}{1-p}\left[b^{1-p}-1\right] \\ \end{gathered}$$

When $p > 1$, the function converges, and when $p \leq 1$, the function
diverges.

# Direct comparison test for divergence or convergence  (First theorem)

Suppose $f(x)$ and $g(x)$ exist such that $x \in [a, \infty)$, $0 \leq f(x)
\leq g(x)$.

1. If $\displaystyle\int_{a}^{\infty}f(x)dx$ diverges then
$\displaystyle\int_{a}^{\infty}g(x)dx$ also diverges.

1. If $\displaystyle\int_{a}^{\infty}g(x)dx$ converges then
$\displaystyle\int_{a}^{\infty}f(x)dx$ also converges.

## Examples

1. $\displaystyle\int_{1}^{\infty} e^{-x^2}dx$

    Considering $e^{-x^2} < e^{-x}$ when $x>1$ and
    $\displaystyle\int_{1}^{\infty}e^{-x}dx=\frac{1}{e}$, the original function
    also converges.

2. $\displaystyle\int_{1}^{\infty}\frac{\sin^2 x}{x^2}dx$

    $\displaystyle 0 \leq \frac{\sin^2 x }{x^2} \leq \frac{1}{x^2}$

    $\displaystyle\int_{1}^{\infty}\frac{1}{x^2}dx$ converges, so our function
    does as well.

3. $\displaystyle\int_{1}^{\infty}\frac{1}{\sqrt{x^2-0.1}}dx$

    $\displaystyle\frac{1}{\sqrt{x^2-0.1}} \geq \frac{1}{x}$ when $x \in [1,
    \infty)$

    Since $\displaystyle\int_{1}^{\infty}\frac{1}{x}dx$ diverges, so does our
    function.

# Limits comparison test (Second theorem)

Suppose $f(x), g(x)$ are positive on the interval $[a, \infty)$ and limit

$$\lim\limits_{x \to \infty} \frac{f(x)}{g(x)} = L \quad\quad (0<L<\infty)$$

exists, then the integrals

$$\int_{a}^{\infty}f(x)dx \text{ and } \int_{a}^{\infty}g(x)dx$$

diverge or converge together.

## Examples

1. $\displaystyle \int_{1}^{\infty}\frac{dx}{4+x^2}$

    Since we know that $\displaystyle \int_{1}^{\infty}\frac{dx}{x^2}$
    converges and

    $$\lim\limits_{x \to \infty} \frac{\frac{1}{4+x^2}}{\frac{1}{x^2}} =
    \lim\limits_{x \to \infty} \frac{x^2}{4+x^2} = 1$$

    our integral also converges.

## Essential condition of convergence

For $\displaystyle\int_{a}^{\infty}f(x)dx$ to converge,
$\displaystyle\lim\limits_{x \to \infty} f(x)$ must approach $0$.
