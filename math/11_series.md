---
title: Series
author: Moshe Krumbein
date: Spring 2021
---

# Taylor series and Maclaurin series

## Maclaurin polynomial

For any function, we can approximate it with a polynomial (the higher the
power, the better the approximation).

Suppose our function is differentiable infinitely, such that:

$$
\begin{array}{c|c}
\begin{gathered}
    f(0)  =p(x)   = a_0  = a_0 0!\\
    f'(0) =p'(0)  = a_1  = a_1 1!\\
    f''(0)=p''(0) = 2a^2 = a_2 2!\\
    \dots \\
    f^{(n)}(0) = p^{(n)}(0) = a_n n!
\end{gathered}
&
\begin{gathered}
    p_n(x)   = a_1  + a_2x  + \dots + a_nx^n \\
    p'_n(x)  = a_1  + 2a_2x + \dots + a_n nx^{n-1} \\
    p''_n(x) = 2a_2 + 6a_3x + \dots + a_n n (n-1) x^{n-2} \\
    \dots \\
    p_n^{(n)} = a_n n (n-1)(n-2)\dots =a_nn!
\end{gathered}
\end{array}
$$

Providing the following equation:

$$p_n(x) = \frac{f(0)}{0!} + \frac{f'(0)}{1!}x + \frac{f''(0)}{2!}x^2+ \dots + \frac{f^{(n)}(0)}{n!}x^n = \sum_{k=0}^{n}\frac{f^{(k)}(0)}{k!}x^k$$

## Taylor series of trigonometric functions

$$
\begin{gathered}
    \sin x \approx p_n(x) = x-\frac{x^3}{3!}+ \frac{x^5}{5!} - \dots = \sum_{k=0}^{n}(-1)^k \frac{x^{2k+1}}{(2k+1)!} \\
    \cos x \approx q_n(x) = 1-\frac{x^2}{2!}+ \frac{x^4}{4!} - \dots = \sum_{k=0}^{n}(-1)^k \frac{x^{2k}}{(2k)!} \\
\end{gathered}
$$

The remainder of a Taylor series is defined as follows:
$$f(x)- p_n(x) = R_n(x)$$

## Fundamental expansions

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}\tag{1}$$
$$\ln(x+1) = \sum_{n=1}^{\infty}(-1)^{n-1}\frac{x^n}{n}\tag{2}$$
$$\sin x = \sum_{n=0}^{\infty}(-1)^n \frac{x^{2n+1}}{(2n+1)!} \tag{3}$$
$$\cos x = \sum_{n=0}^{\infty}(-1)^n \frac{x^{2n}}{(2n)!} \tag{4}$$

$$
(1+t)^\alpha = 1+\alpha t +\frac{ \alpha (\alpha - 1)}{2!}t^2 + \frac{\alpha
(\alpha - 1)(\alpha - 2)}{3!}t^3 \dots, \;|x| < 1 \tag{5}
$$

### Additional expansions

$$\arctan x = \sum_{n=0}^{\infty}(-1)^n\frac{x^{2n+1}}{2n+1}$$
$$\ln (a-x) = \ln a - \sum_{n=1}^{\infty}\frac{x^n}{n \cdot a^n}$$
$$\frac{1}{x-a}= \sum_{n=0}^{\infty}\frac{x^n}{a^n}$$
$$\frac{1}{1+x}=\sum_{n=0}^{\infty}(-1)^nx^n$$

# Taylor series

A Maclaurin series is specifically around $x=0$, but a Taylor series is around
any given point $(x=a)$.

Maclaurin series:

$$f(t)= \sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}t^n$$

We define $t=x-a$ ($t=0 \implies x=a$) providing:

$$f(x-a) =\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n$$

This can also be stated as:

$$P_n(f,a,x)=\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k$$

Where $a$ is the given point and $x$ is the desired point.

# Using the Maclaurin series for calculating limits

$$\lim\limits_{x \to 0} \frac{\cos x -1 }{x^2} = \left(\frac{0}{0}\right)$$

$$\cos x -1 +\frac{x^2}{2}-\frac{x^4}{4!} = R_4(x)= o(x^4)$$

$$\lim\limits_{x \to 0} \frac{1-\frac{x^2}{2}-1+o(x^2)}{x^2} = -\frac{1}{2}$$

$$\lim\limits_{x \to 0} \frac{o(x^n)}{x^n} = 0$$

# Evaluating error

Definition:

Given $f$ differentiable $n$ times surrounding $x=a$, then the polynomial:

$$P_n(f,a,x)=\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k$$

is called a Taylor polynomial.

The "remainder" is defined as:

$$R_n(f,a,x) = f(x) -P_n(f,a)(x)$$

## Taylor remainder theorem in Lagrange form

Let $f$ be differentiable $(n+1)$ times surrounding point $x$ and $x$ be a
surrounding point of $a$.

Therefore there exists a point $c$ between $x$ and $a$ such that:

$$R_n(f,a,x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$

### Proof

According to Cauchy's theorem: Let $f,g$ be continuous on $[a,b]$ and
differentiable on $(a,b)$ and $g' \neq 0$ on $(a,b)$.

Therefore there exists $c \in (a,b)$ such that:

$$\frac{f(b)-f(a)}{g(b)-g(a)}= \frac{f'(c)}{g'(c)}$$

We will use this theorem on the following two functions:

$$h(t) = R_n(f,t,x)$$
$$g(t) = (x-t)^{n+1}$$
$$\text{($x$ is constant, $t$ is variable)}$$

$$g(t) = (x-t)^{n+1} \implies g'(t) = (n+1)(x-t)^n$$

$g'=0$ only when $t=x$, which is a extreme of the open interval $(a,x)$,
and therefore $g' \neq 0$.

$$h(t) = R_n(f,t,x) = f(x) - P_n(f,t)(x)$$
$$=f(x)-\left(f(t)+f'(t)(x-t)+\frac{f''(t)}{2!}(x-t)^2+\dots+\frac{f^{(n)}(t)}{n!}(x-t)^n\right)$$
$$h'_t(t)=0-f'(t)-f''(t)(x-t)+f'(t)-\frac{f'''(t)}{2!}2(x-t)\frac{f''(t)}{2!}-\cdots + \frac{f^{(n)}(t)}{n!}n(x-t)^{n-1} \cdots$$

Nearly everything crosses out, leaving

$$h'(x) = -\frac{f^{(n+1)}(t)}{n!}(x-t)^n$$

Therefore according to Cauchy's theorem:

$$\frac{h(a)-h(x)}{g(a)-g(x)}=\frac{h'(c)}{g'(c)}$$

Plugging everything in:

$$\frac{R_n(f,a,x) - 0}{(x-a)^{n+1}}= \frac{f^{(n+1)}(c)}{(n+1)!}$$
$$R_n(f,a,x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$
$$\blacksquare$$

## Example

We want to approximate $|\sqrt 8 -x|<\frac{1}{100}$

$$
\begin{gathered}
    f(x)=\sqrt x \quad
    x=8 \quad
    a=9
\end{gathered}
$$

$$P_1(f,9,8) = f(9) + f'(9)(8-9) =\sqrt 9 + \frac{1}{2\sqrt 9}(8-9)=\frac{17}{6}$$
$$R_1(f,9,8) = \frac{f''(c)}{2!}(8-9)^2$$
$$|R_1| = \left|\frac{-\frac{1}{4}c^{-3/2}}{2!}(8-9)^2\right| < \frac{1}{64}$$
$$R_2(f,9,8) = \frac{f'''(c)}{2!}(8-9)^3$$
$$|R_2|<\frac{1}{1664}$$

Now to actually calculate to approximation:

$$P_2(\sqrt x, 9) = f(9)+f'(9)(x-9)+\frac{f''(9)}{2!}(x-9)^2$$
$$P_2(\sqrt x, 9)(8) = 3- \frac{1}{6} - \frac{1}{8\cdot27} \approx 2.8287$$
$$\sqrt 8 \approx 2.8284$$
