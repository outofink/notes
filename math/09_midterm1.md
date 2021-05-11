---
title: First Midterm
author: Moshe Krumbein
date: Spring 2021
---

# Summary

## Theorems

1. Cauchy's mean value theorem

    If $f(x)$ and $g(x)$ are continuous on $[a,b]$ and are differentiable on
    $(a,b)$ and $g'(x) \neq 0$ for all $x \in (a,b)$, then there exists $c \in
    (a, b)$ such that:
$$\frac{f(b)-f(a)}{g(b)-g(a)} = \frac{f'(c)}{g'(c)}$$

2. Lagrange's mean value theorem (specific case of Cauchy's mean value theorem)

    If $g(x) = x$ and $f(x), g(x)$ satisfy Cauchy's mean value theorem:
$$\exists \; c \in (a,b): \frac{f(b)-f(b)}{b-a}=f'(c)$$

3. Role's theorem (specific case of Lagrange's theorem)

    If $f(x)$ satisfies Lagrange's theorem and $f(a) = f(b)$:
$$\exists \; c \in (a,b): f'(c) = 0$$

4. Cauchy's intermediate value theorem

    If $f(x)$ is continuous on $[a,b]$ and $f(a) \cdot f(b) < 0$:
$$\exists \; a < c < b: f(c) = 0$$

## Integrals

1. Immediate (anti-derivatives)
2. Inverse chain rule ($t$-substitution)

    $$\int f'(g(x))g'(x)dx = f(g(x)) + c$$

3. Integration by parts

    $\int uv'dx = uv - \int vu'dx$

    a. $\int p_m(x)e^{ax}dx, \int p_m(x)\sin(ax)dx, \int p_m(x)\cos(ax)dx$

    > Where $p_m$ is a polynomial to the $m^{\text{th}}$ power.

    > Define $u = p_m(x)$ and do integration by parts $m$ times.

    b. Contains $\ln$, $\arcsin$, $\arccos$, $\arctan$

    > Define $a$ as that function.

    c. $\int e^{ax}\sin(bx)dx, \int e^{ax}\cos(bx)dx, \int \ln (\sin x)dx,
    \int \ln (\cos x) dx$

    >Any integral that after integrating by parts twice contains the original
    >integral.

    >Define $I$ as that integral and solve algebraically.

4. Substitution
    a. Polynomials (partial fractions)
    b. Trigonometric substitution to get out of square roots (trigonometric
    substitution)
    c. Trigonometric substitution to get to a rational function (universal
    trigonometric substitution)
