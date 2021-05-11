---
title: Second Midterm
author: Moshe Krumbein
date: Spring 2021
---

# Definite Integrals

## Riemann Sum

A *Riemann sum* is a certain kind of approximation of an integral by a finite sum.

The sum is calculated by partitioning the region into shapes (most commonly
rectangles) such that the width of rectangle is infinitesimally small. In
short, this sum produces the following:

$$\int_{a}^{b}f(x)dx \equiv \lim\limits_{n \to \infty} \frac{b-a}{n}
\sum_{k=1}^{n}f\left(a+\frac{k}{n}(b-a)\right)$$

## Newton-Leibniz Theorem

$$\int_{a}^{b} f(x)dx = F(x) \Big|_a^b = F(b) - F(a)$$

### Characteristics

1. If $a<b$ and $f(x)>$ or $a<b$ and $f(x)>0$ then $\int_{a}^{b}f(x)dx<0$.

    If $a<b$ and $f(x)<$ or $a>b$ and $f(x)>0$ then $\int_{a}^{b}f(x)dx>0$.

2. $\int_{a}^{b}f(x)dx = \int_{a}^{c}f(x)dx + \int_{c}^{b}f(x)dx$

3. $\int_{a}^{a}f(x)dx = 0$

4. $\int_{a}^{b}f(x)dx = -\int_{b}^{a}f(x)dx$

5. $\int_{-a}^{a} f(x)dx = 0$ where $f(x)$ is an odd function

6. $\int_{-a}^{a} f(x)dx = 2\int_{0}^{a}f(x)dx$ where $f(x)$ is an even function

### Definite integrals using partial fractions

$$\int_{a}^{b}uv'dx = \Big[uv\Big]_{x=a}^{x=b} - \int_{a}^{b}u'vdx$$

# Applications of Definite Integrals

## Area between curves

If $f$ and $g$ are continuous and $f(x) \ge g(x)$, the area between them is:

$$\int[f(x)-g(x)]dx$$

Naturally, if the shape of the area forms a familiar geometric shape it is
preferable to do the geometric calculation rather than the integral.

# Volumes of Solids of Revolutions

> How to find the volume of a function rotated around the $x$-axis.

## Method of Disks

The volume of a disk is $\pi r^2 h$ so for a function we get between $a$ and
$b$ we get:

$$\lim\limits_{n \to \infty} f(x)\pi \cdot
\frac{b-a}{n}\sum_{k=1}^{n}f^2\left(a+\frac{b-a}{n}k\right)$$
$$\boxed{V=\pi \int_{a}^{b}f^2(x)dx}$$

### Example

$$f(x)=\sqrt x, 1 \leq x \leq 3, \text{rotated around the $x$-axis.}$$
$$V = \pi \int_{1}^{3}(\sqrt x)^dx=\pi \frac{x^2}{2}\Big|_{x=1}^{x=3}=\boxed{4\pi}$$

## Rotation around a shifted axis

$$f(x)=\sqrt x, 1 \leq x \leq 3, \text{rotated around $y=1$.}$$
$$V = \pi \int_{1}^{3}R^2(x)dx= \pi \int_{1}^{3} (\sqrt x - 1)^2dx$$

## Area of washers

The area of the larger circle minus the area of the smaller circle

$$V= \pi \int_{a}^{b} (R^2-r^2)dx$$

# Fundamental theorem of calculus

In class we went through all the proofs, see other notes for details.

## Derivative of anti-derivative theorem - Leibniz's Rule

If functions $f(x)$ and $g(x)$ are differentiable and the function $f(u)$ is
continuous on $g(x) < u < h(x)$, then:

$$\frac{d}{dx} \int_{g(x)}^{h(x)}f(u)du = f(h(x)) \cdot h'(x) = f(g(x) \cdot
g'(x)$$

### Examples and Applications

1.
$$\frac{d}{dx}\int_{5}^{\sin x}t^2dt = \sin^2(x) \cdot (\sin x)' - 5^2 \cdot
(5)'$$
$$=\sin^2x \cdot \cos x$$

2.
$$\frac{d}{dx} \int_{x^3}^{3}\arctan t dt = \arctan 3 \cdot (3)' - \arctan(x^3) \cdot (x^3)'$$
$$=-3x^2 \arctan x^3$$

3.
$$\lim\limits_{x \to 0} \frac{1}{x^3}\int_{0}^{x}\frac{t^2}{t^4+1}dt = \left("\frac{0}{0}"\right)$$
$$\to \lim\limits_{x \to 0} \frac{\frac{d}{dx}\int_{0}^{x}\frac{t^2}{t^4+1}dt}{\frac{d}{dx}(x^3)}$$
$$=\lim\limits_{x \to 0} \frac{\frac{x^2}{x^3+1}}{3x^2} = \lim\limits_{x \to 0} \frac{1}{3(x^4+1)} = \boxed{\frac{1}{3}}$$

# Improper Integrals

1. If $f$ is continuous on $[a, \infty)$, then:
$$\int_{a}^{\infty} f(x)dx = \lim\limits_{b \to \infty} \int_{a}^{b} f(x)dx
\tag{1}$$

1. If $f$ is continuous on $(-\infty, b]$, then:
$$\int_{-\infty}^{b} f(x)dx = \lim\limits_{a \to -\infty} \int_{a}^{b} f(x)dx
\tag{2}$$

1. If $f$ is continuous on $(a, b]$, then:
$$\int_{a}^{b} f(x)dx = \lim\limits_{c \to a^+} \int_{c}^{b} f(x)dx \tag{3}$$

1. If $f$ is continuous on $[a, b)$, then:
$$\int_{a}^{b} f(x)dx = \lim\limits_{c \to b^-} \int_{a}^{c} f(x)dx \tag{4}$$

In each case, if the limit is finite we say that the improper integral
**converges** and the limit is the value of the improper integral. If the
integral fails to exist the improper integral **diverges**.

Basically, whichever part is undefined is replaced with a limit.

$$\begin{gathered}
    \int_{2}^{\infty}\frac{1}{x^p}dx = \lim\limits_{b \to \infty} \int_{1}^{b}\frac{1}{x^p}dx \\
    = \lim\limits_{b \to \infty} \left[\frac{x^{p-1}}{p-1}\right]_{x=1}^{x=b}\\
    = \lim\limits_{b \to \infty} \frac{1}{1-p}\left[b^{1-p}-1\right] \\
\end{gathered}$$

When $p > 1$, the function converges, and when $p \leq 1$, the function diverges.

## Direct Comparison Test for Divergence or Convergence (First Theorem)

Suppose $f(x)$ and $g(x)$ exist such that $x \in [a, \infty)$, $0 \leq f(x)
\leq g(x)$.

1. If $\displaystyle\int_{a}^{\infty}f(x)dx$ diverges then $\displaystyle\int_{a}^{\infty}g(x)dx$ also
diverges.

1. If $\displaystyle\int_{a}^{\infty}g(x)dx$ converges then $\displaystyle\int_{a}^{\infty}f(x)dx$ also
converges.

### Examples

1. $\displaystyle\int_{1}^{\infty} e^{-x^2}dx$

    Considering $e^{-x^2} < e^{-x}$ when $x>1$ and
    $\displaystyle\int_{1}^{\infty}e^{-x}dx=\frac{1}{e}$, the original function also
    converges.

2. $\displaystyle\int_{1}^{\infty}\frac{\sin^2 x}{x^2}dx$

    $\displaystyle 0 \leq \frac{\sin^2 x }{x^2} \leq \frac{1}{x^2}$

    $\displaystyle\int_{1}^{\infty}\frac{1}{x^2}dx$ converges, so our function does as well.

3. $\displaystyle\int_{1}^{\infty}\frac{1}{\sqrt{x^2-0.1}}dx$

    $\displaystyle\frac{1}{\sqrt{x^2-0.1}} \geq \frac{1}{x}$ when $x \in [1, \infty)$

    Since $\displaystyle\int_{1}^{\infty}\frac{1}{x}dx$ diverges, so does our function.

## Limits Comparison Test (Second Theorem)

Suppose $f(x), g(x)$ are positive on the interval $[a, \infty)$ and limit

$$\lim\limits_{x \to \infty} \frac{f(x)}{g(x)} = L \quad\quad (0<L<\infty)$$

exists, then the integrals

$$\int_{a}^{\infty}f(x)dx \text{ and } \int_{a}^{\infty}g(x)dx$$

diverge or converge together.

### Examples

1. $\displaystyle \int_{1}^{\infty}\frac{dx}{4+x^2}$

    Since we know that $\displaystyle \int_{1}^{\infty}\frac{dx}{x^2}$
    converges and

    $$\lim\limits_{x \to \infty} \frac{\frac{1}{4+x^2}}{\frac{1}{x^2}} = \lim\limits_{x \to \infty} \frac{x^2}{4+x^2} = 1$$

    our integral also converges.

## Essential Condition of Convergence

For $\displaystyle\int_{a}^{\infty}f(x)dx$ to converge, $\displaystyle\lim\limits_{x \to \infty} f(x)$ must approach $0$.

# Taylor Series and Maclaurin Series

## Maclaurin Polynomial

For any function, we can approximate it with a polynomial (the higher the
power, the better the approximation).

Suppose our function is differentiable infinitely, such that:
$$
\begin{gathered}
    f(0)  =p(x)   = a_0  = a_0 0!\\
    f'(0) =p'(0)  = a_1  = a_1 1!\\
    f''(0)=p''(0) = 2a^2 = a_2 2!\\
    \dots \\
    f^{(n)}(0) = p^{(n)}(0) = a_n n!
\end{gathered}
\quad \vline \quad
\begin{gathered}
    p_n(x)   = a_1  + a_2x  + \dots + a_nx^n \\
    p'_n(x)  = a_1  + 2a_2x + \dots + a_n nx^{n-1} \\
    p''_n(x) = 2a_2 + 6a_3x + \dots + a_n n (n-1) x^{n-2} \\
    \dots \\
    p_n^{(n)} = a_n n (n-1)(n-2)\dots =a_nn!
\end{gathered}
$$

Providing the following equation:
$$p_n(x) = \frac{f(0)}{0!} + \frac{f'(0)}{1!}x + \frac{f''(0)}{2!}x^2+ \dots + \frac{f^{(n)}(0)}{n!}x^n = \sum_{k=0}^{n}\frac{f^{(k)}(0)}{k!}x^k$$

## Taylor Series of Trigonometric Functions

$$
\begin{gathered}
    \sin x \approx p_n(x) = x-\frac{x^3}{3!}+ \frac{x^5}{5!} - \dots = \sum_{k=0}^{n}(-1)^k \frac{x^{2k+1}}{(2k+1)!} \\
    \cos x \approx q_n(x) = 1-\frac{x^2}{2!}+ \frac{x^4}{4!} - \dots = \sum_{k=0}^{n}(-1)^k \frac{x^{2k}}{(2k)!} \\
\end{gathered}
$$

The remainder of a Taylor series is defined as follows:
$$f(x)- p_n(x) = R_n(x)$$

## Fundamental Expansions

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}\tag{1}$$
$$\ln(x+1) = \sum_{n=1}^{\infty}(-1)^{n-1}\frac{x^n}{n}\tag{2}$$
$$\sin x = \sum_{n=0}^{\infty}(-1)^n \frac{x^{2n+1}}{(2n+1)!} \tag{3}$$
$$\cos x = \sum_{n=0}^{\infty}(-1)^n \frac{x^{2n}}{(2n)!} \tag{4}$$
$$(1+t)^\alpha = 1+\alpha t +\frac{ \alpha (\alpha - 1)}{2!}t^2 + \frac{\alpha
(\alpha - 1)(\alpha - 2)}{3!}t^3 \dots, \;|x| < 1 \tag{5}$$

### Additional Expansions

$$\arctan x = \sum_{n=0}^{\infty}(-1)^n\frac{x^{2n+1}}{2n+1}$$
$$\ln (a-x) = \ln a - \sum_{n=1}^{\infty}\frac{x^n}{n \cdot a^n}$$
$$\frac{1}{x-a}= \sum_{n=0}^{\infty}\frac{x^n}{a^n}$$
$$\frac{1}{1+x}=\sum_{n=0}^{\infty}(-1)^nx^n$$

## Taylor Series

A Maclaurin series is specifically around $x=0$, but a Taylor series is around
any given point $x = a$.

Maclaurin series:
$$f(t)= \sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}t^n$$

We define $t=x-a$ ($t=0 \implies x=a$) providing:
$$f(x-a) =\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n$$

This can also be stated as:
$$P_n(f,a,x)=\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k$$

Where $a$ is the given point and $x$ is the desired point.

## Using the Maclaurin Series for Calculating Limits

$$\lim\limits_{x \to 0} \frac{\cos x -1 }{x^2} = \left(\frac{0}{0}\right)$$

$$\cos x -1 +\frac{x^2}{2}-\frac{x^4}{4!} = R_4(x)= o(x^4)$$

$$\lim\limits_{x \to 0} \frac{1-\frac{x^2}{2}-1+o(x^2)}{x^2} = -\frac{1}{2}$$

$$\lim\limits_{x \to 0} \frac{o(x^n)}{x^n} = 0$$

## Evaluating Error

Given $f$ differentiable $n$ times surrounding $x=a$, then the polynomial:

$$P_n(f,a,x)=\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k$$

is called a Taylor polynomial.

The "remainder" is defined as:

$$R_n(f,a,x) = f(x) -P_n(f,a)(x)$$

### Taylor Remainder Theorem in Lagrange Form

Let $f$ be differentiable $(n+1)$ times surrounding point $x$ and $x$ be a
surrounding point of $a$.

Therefore there exists a point $c$ between $x$ and $a$ such that:

$$R_n(f,a,x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$

#### Proof

See other notes.

### Examples

We want to approximate $|\sqrt 8 -x|<\frac{1}{100}$

$$f(x)=\sqrt x \quad x=8 \quad a=9$$

$$P_1(f,9,8) = f(9) + f'(9)(8-9) =\sqrt 9 + \frac{1}{2\sqrt 9}(8-9)=\frac{17}{6}$$
$$R_1(f,9,8) = \frac{f''(c)}{2!}(8-9)^2$$
$$|R_1| = \left|\frac{-\frac{1}{4}c^{-3/2}}{2!}(8-9)^2\right| < \frac{1}{64}$$
$$R_2(f,9,8) = \frac{f'''(c)}{2!}(8-9)^3$$
$$|R_2|<\frac{1}{1664}$$

Now to actually calculate to approximation:

$$P_2(\sqrt x, 9) = f(9)+f'(9)(x-9)+\frac{f''(9)}{2!}(x-9)^2$$
$$P_2(\sqrt x, 9)(8) = 3- \frac{1}{6} - \frac{1}{8\cdot27} \approx 2.8287$$
$$\sqrt 8 \approx 2.8284$$

## Double Factorials

The *double factorial* of a number $n$, denoted by $n!!$, is the
product of all the integers from $1$ up to $n$ that have the same parity (even or
odd) as $n$.

For example if $n = 7$ then $n!! = 7 \cdot 5 \cdot 3 \cdot 1$.
Likewise, if $n = 6$ then $n!! = 6 \cdot 4 \cdot 2$.

For an even non-negative integer $n=2k$ with $k \geq 0$, the double factorial
may be expressed as:

$$n!! = (2k)!! = 2^kk!$$

For an odd non-negative integer $n=2k-1$ with $k \geq 1$, the double factorial
may be expressed as:

$$n!! = (2k-1)!! = \frac{(2k)!}{2^kk!}$$

# Functions with Two Variables

$$z=f(x,y)=\frac{1}{\sqrt{25-x^2-y^2}}$$

$$\text{Dom } f = \{(x,y):x^2+y^2<25\}$$
$$\text{Im }  f = \left\{z \geq \frac{1}{5}\right\}$$

*Contour lines* are horizontal cross-sections of the graph.

## Limits of Functions with Two Variables

$$\lim\limits_{(x,y) \to (a,b)} f(x,y) = f(a,b)$$

For example $f(x,y) = x^2+y^2$:
$$\lim\limits_{(x,y) \to (1,2)} f(x,y)=5$$

### Calculation of the Limit or Proving the Limit Does Not Exist

1.
$$\lim\limits_{(x,y) \to (1,2)} \frac{\arctan(x+y-3)}{\ln(x+y-2)}$$
$$t=x+y-1$$
$$(x,y) \to (1,2) \implies t \to 1$$
$$\lim\limits_{t \to 1} \frac{\arctan(t-1)}{\ln t}$$
equals $1$ using L'Hospital's rule.

2.
$$\lim\limits_{(x,y) \to (1,1)} \frac{xy-y^2}{\sqrt x - \sqrt y} = \frac{y(x-y)}{\sqrt x - \sqrt y}= y(\sqrt x + \sqrt y) = 2$$

3.
$$\lim\limits_{(x,y) \to (0,0)} \frac{x^3+y^2}{x^2+y^2}$$
We say the limit only exists if it doesn't matter what way we get to the limit.

#### Approach A

$$\lim\limits_{x \to 0, y=x} \frac{x^3 + y^2}{x^2+y^2} = \frac{x^3 + x^2}{2x^2} = \frac{1}{2}$$
$$\lim\limits_{x \to 0, y=2x} \frac{x^3 + y^2}{x^2+y^2} = \frac{x^3 + 4x^2}{5x^2} = \frac{4}{5}$$

$\frac{1}{2} \neq \frac{4}{5}$, so the limit does not exist.

#### Approach B

$$\lim\limits_{x \to 0, y=kx} \frac{x^3+k^2x^2}{x^2+k^2x^2} = \frac{k^2}{1+k^2}$$

The limit is dependent on $k$, and therefore does not exist.

#### Approach C

The limit is dependent on the angle.

#### Approach D

Find the limit of first $x$ and then $y$. Then find the limit of $y$ and then $x$.
If time limits are not equal the limit does not exist.

### So How Can We Prove the Limit *Does* Exist?

#### Sandwich Rule

$$\lim\limits_{(x.y) \to (0,0)} \frac{xy^3}{y^2+x^2}$$
$$\left|\frac{xy^3}{x^2+y^2}\right| \leq \left|\frac{xy^3}{y^2}\right| = |xy| =|x||y| \to 0$$

If the numerator has a higher power than the denominator, we know that the
numerator approaches zero faster than the denominator.

If the denominator is larger  on the numerator, we will see that the limit will
approach infinity.

If the powers are equal then we know that the limit will not exist.
