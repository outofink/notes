---
title: Integrals
author: Moshe Krumbein
date: Spring 2021
---

# Basics

$$
\begin{gathered}
    d(f(x))=f'(x)dx \\
    d(f(x)+C)=f'(x)=d(f(x)) \\
    \int f'(x)dx = \int d(f(x))=f(x)+C
\end{gathered}
$$

$$
\begin{gathered}
   \int x^m dx = \frac{x^{m+1}}{m+1} +C \\
   (m \neq -1)
\end{gathered}
$$

$$\int \frac{1}{x} = \ln{|x|}+C$$

$$\int a^x dx = \frac{1}{\ln a} \cdot a^x + c$$
$$\int e^x dx = e^x +C$$

## Properties

$$\int c \cdot f'(x)dx = c \int f'(x) dx \tag{1}$$
$$\int (f'(x)+g'(x))dx = \int f'(x)dx + \int g'(x)dx \tag{2}$$

# Inverse chain rule (t-substitution)

$$
\begin{gathered}
    (f(g(x)))' = f'(g(x)) \cdot g'(x) \\
    (f(g(xx))' dx = f'(g(x)) \cdot g'(x) dx \\
    \int d(f(g(x)+c) = \int f'(g(x)) \cdot g'(x)dx \\
    \boxed{\int f'(g(x))g'(x) = f(g(x)) + c}
\end{gathered}
$$

## Example

$$
\int \frac{\arctan x}{1+x^2}dx =
\begin{vmatrix}
    t  &= \arctan x \\
    dt &= \frac{1}{1+x^2}dx
\end{vmatrix}
= \int t dx
$$

$$\int \frac{g'(x)}{g(x)}dx=\ln|g(x)|+c$$

# Integration by Parts

$$
\begin{gathered}
    (u(x) \cdot v(x))' = v(x) \cdot u'(x) + u(x) \cdot v'(x) \\
    (u(x) \cdot v(x))'dx = v(x) \cdot u'(x) + u(x)dx \cdot v'(x)dx \\
    \int (u(x) \cdot v(x))' = \int v(x) \cdot u'(x) + \int u(x) \cdot v'(x) \\
    \int d(u(x) \cdot v(x)) = \int v(x)d(u(x)) + \int u(x)d(v(x)) \\
    u(x) \cdot v(x) = \int v(x)d(u(x)) + \int u(x)d(v(x)) \\
    \int u(x)d(v(x)) = u(x) \cdot v(x) - \int v(x)d(u(x)) \\
    \boxed{\int udv = u v - \int v du}
\end{gathered}
$$

## Example

$$
\int xe^x dx =
\begin{vmatrix}
   u = x &\; | \;& v' = e^x \\
   u' = 1 &\; | \;& v= \int e^x dx =e^x
\end{vmatrix}
$$

$$xe^x - \int e^x dx =xe^x -e^x +c$$

## Cases

### Type I

$$\int p_m(x) \cdot e^ax, \int p_m(x) \cdot \sin(ax), \int p_m(x) \cdot \cos(ax)$$

Define $u=p_m(x)$ and do integration by parts $m$ times

### Type II

Integrals that contain $\ln$ or $arc$-functions.

$$
\int \ln x dx =
\begin{vmatrix}
    u=\ln x & | & v' = 1 \\
    u' = \frac{1}{x} & | & v= \int dx=x
\end{vmatrix}
$$

$$x \ln x - \int x \cdot \frac{1}{x} = x \ln x - \int dx = x \ln x - x + c$$

### Type III

Repeating integrals

$$\int \cos (\ln x)$$
$$\int e^{ax} \cdot \cos(bx), \int e^{ax} \cdot \sin(bx)$$

$$
\int \frac{\ln x}{x} dx =
\begin{vmatrix}
    u=\ln x & | & v' = \frac{1}{x} \\
    u' = \frac{1}{x} & | & v= \ln x
\end{vmatrix}
$$

$$
\begin{gathered}
    =\ln^2 x - \int \frac{\ln x}{x} dx \\
    I = \int \frac{\ln x}{x} dx \\
    I = \ln^2 x - I \\
    =\frac{\ln^2 x}{2}
\end{gathered}
$$

# Integrals of rational functions (partial fractions)

1. $\int \frac{dx}{x-a} = ln|x-a|+c$
2. $\int \frac{dx}{(x-a)^k} = \int (x-a)^{-k}dx = \frac{(x-a)^{1-k}}{1-k}+c$, $k \neq 1$
3. $\int \frac{dx}{x^2 +px + q} = \frac{\sqrt{q-\frac{p^2}{4}}}{q-\frac{p^2}{4}} \arctan\left(\frac{x+\frac{p}{2}}{\sqrt{q-\frac{p^2}{4}}}\right)+c$
4. $\int \frac{dx}{(x^2 +px +q)^k}$

$\int \frac{p_m(x)}{p_n(x)}$

$n>m$:

1. $\int \frac{dx}{(x-a)(x-b)} = \int \frac{Adx}{x-a} + \int \frac{Bdx}{x-b} =
   A\ln|x-a|+B\ln|x-b|+c$

   $A= \frac{1}{a-b}$, $B = -\frac{1}{a-b}$

   $\int \frac{x^2+x-1}{(x-1)(x+2)(x+1)}dx$

   $\frac{x^2+x-1}{(x-1)(x+2)(x+1)} = \frac{A}{x-1} + \frac{B}{x+2} + \frac{C}{x+1}$

   $A(x+2)(x+1) + B(x+1)(x-1) + C(x+2)(x-1) = x^2+x+1$

   $A = -\frac{1}{2}, B=-\frac{1}{6}, C=\frac{5}{3}$

2. $\int \frac{x^2-x+2}{(x-1)^3}dx$

   $\frac{x^2-x+2}{(x-1)^3} = \frac{(x-1+1)^2 +(x-1+1)+2}{(x-1)^3} = \frac{(x-1)^2+2(x-1)+1+(x-1)-1+2}{(x-1)^3}$

   $\frac{(x-1)^2+(x-1)+2}{(x-1)^3} = \frac{1}{x-1} + \frac{1}{(x-1)^2} +
    \frac{2}{(x-1)^3}$

   Second approach:

   $\frac{x^2-x+2}{(x-1)^3} = \frac{A}{x-1} + \frac{B}{(x-1)^2} + \frac{C}{(x-1)^3}$

   Example:

   $\int \frac{x^3+1}{(x-2)^5}dx$

   $\frac{x^3+1}{(x-2)^5} = \frac{A}{x-2} + \frac{B}{(x-2)^2} + \frac{C}{(x-2)^3}+ \frac{D}{(x-2)^4}+ \frac{E}{(x-2)^5}$

3. $\int \frac{x^3-x^2+x-2}{(x+1)(x-1)^5}dx$

   $\frac{x^3-x^2+x-2}{(x+1)(x-1)^5}=\frac{A}{x+1} +\frac{B}{x-1} + \frac{C}{(x-1)^2} + \frac{D}{(x-1)^3}$

# Trigonometric integrals

$\int (\cos^2 x -\sin^2 x)dx = \int \cos 2x dx = \frac{1}{2} \sin 2x+c$

Essentially, the way to solve trigonometric integrals is by getting rid of the
exponents of the trig functions using the following:

$$2\cos^2 x = 1+\cos 2x \quad\quad 2\sin^2x = 1 -\cos 2x$$

# Trigonometric substitution

If an integral is in the form $\int \sqrt{a^2-x^2} dx$, substitute $x= a\sin t$.

If an integral is in the form $\int \sqrt{a^2+x^2} dx$, substitute $x= a\tan t$.

If an integral is in the form $\int \sqrt{x^2-a^2} dx$, substitute $x= \frac{a}{\cos t}$.

# Universal trigonometric substitution ($t = \tan \frac{x}{2}$)

Basically, when integrating a function with more than one trigonometric
function, use $t=\tan \frac{x}{2}$.

$$
    dx=\frac{2}{1+t^2}dt \quad\quad \cos x = \frac{1-t^2}{1+t^2} \quad\quad \sin
    x = \frac{2t}{1+t^2}
$$
