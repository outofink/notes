---
title: Polynomials
author: Moshe Krumbein
date: Fall 2020
---

# Inequalities

> *Note:* We must always first define the domain of the function

There are two main approaches to solving inequalities:

1. Multiply both sides of the equation by the square of the common denominator

For example:

$$
\begin{aligned}
   \frac{2x+3}{x-4} &> 0 \\
   \quad \\
   \frac{2x+3}{x-4} &> 0, \quad x \neq 4 \\
   \frac{2x+3}{x-4} &> 0 \;\| \cdot (x-4)^2 \\
   (2x+3)(x-4) &> 0
\end{aligned}$$

$$
\begin{gathered}
   x < -\frac{3}{2},\quad x > 4 \\
   \text{or} \\
   (-\infty, -1.5)\cup(4, +\infty)
\end{gathered}
$$

$$\pagebreak$$

2. Build a table

> *Note:* Can only be done if one side of the equation is zero

Example:

$$
\begin{aligned}
    (x-2)(4-x)(9+x) &\le 0
\end{aligned}
$$
$$\text{Domain: } x \in \mathbb{R}$$

|                   | $(-\infty, -9)$ | $-9$ | $(-9, 2)$ | $2$ | $(2, 4)$ | $4$ | $(4, +\infty)$ |
|:-----------------:|:---------------:|:----:|:---------:|:---:|:--------:|:---:|:--------------:|
| $(x-2)$           | $-$             | $-$  | $-$       | $0$ | $+$      | $+$ | $+$            |
| $(4-x)$           | $+$             | $+$  | $+$       | $+$ | $+$      | $0$ | $-$            |
| $(9+x)$           | $-$             | $0$  | $+$       | $+$ | $+$      | $+$ | $+$            |
| $(x-2)(4-x)(9+x)$ | $+$             | $0$  | $-$       | $0$ | $+$      | $0$ | $-$            |

$$
\begin{gathered}
    -9\le x \le2,\quad x \ge 4 \\
    \text{or} \\
    [-9, 2]\cup[4, +\infty)
\end{gathered}
$$

This works whilst dividing as well, just make sure the domain is taken into
account.

# Polynomials

> A *polynomial* is a sum of monomials.

>  A *monomial* is any expression in the form of $Ax^H$.

> Examples: $2\sqrt{x} \;(2x^\frac{1}{2}), 4x^3 \;(4x^3), \frac{x}{4}\;(\frac{1}{4}x^1), x\;(1x^1), 12\;(12x^0)$

## Rules

1. Can combine monomials of the same degree
    - $ax^n + bx^n = (a+b)x^n$
1. Is ordered according to degree
    - $A_{n}x^{n} + A_{n-1}x^{n-1}+A_{n-2}x^{n-2}\dots + A_2x^2+A_1x+A_0,
        A_n \neq 0$
    - $ax^3+bx^2+cx+d$
1. The *degree* of a polynomial is defined by the highest exponent in the
   expression

Examples:

- $x^8 -4$ is a polynomial to the $8^{\text{th}}$ degree
- $4x^3 -2x^2-5x+13$ is a polynomial to the $3^{\text{rd}}$ degree

## Characteristics

Given polynomials $p_1, p_2$ to the $m$ and $n$ degrees respectively:

- $p_1(x) + p_2(x)$ is a polynomial to either the $m$ or $m$ degree, or lower

- $p_1(x) \cdot p_2(x)$ is a polynomial to the $m+n$ degree

- $\frac{p_1(x)}{p_2(x)}$ is not necessarily a polynomial

> i.e. $\frac{x+2}{x-1}$ is not a polynomial

## Polynomial division

$$a \;\vdots\; b \equiv \exists \; c \in \mathbb{R} \;|\; b \cdot c = a$$

Or in English, $a \;\vdots\; b$ states that there exists $c$ (real number) such that $b \cdot c = a$.

For binomials $(p,q) \to \frac{p(x)}{q(x)} = r(x)$ such that $r(x) = ax+b$

If $r(x)$ does not exist, $p \not \vdots \; q$

## Does $P(x) \;\vdots\; x-B$?

Or in other words, is $p(b) = 0 \iff p(x) \;\vdots\; (x-b)$ true?

### Proof:

$$
    p(b) = 0 \iff p(x) \;\vdots\; (x-b) \equiv p(b) \neq 0 \iff p(x) \not\vdots\; (x-b)
$$

If $p(x) \not \vdots\; (x-b)$, there will be a remainder $c$ or the $0^\text{th}$ degree
(number) such that:

$$
\begin{aligned}
    p(x) &= (x-b)\cdot r(x)+c \\
    p(b) &= (b-b)\cdot r(b)+c \\
\end{aligned}
$$

$$
\because c \neq 0,\; p(b) \neq 0 \therefore 0 \neq 0 \\
$$
$$\text{Contradiction, Q.E.D.}$$

## Approach

$$
\begin{aligned}
    \frac{x^5-3x^4+7x^3+x^2-5x-1}{x-1}
\end{aligned}
$$

Basically we do polynomial long division, I'll add an example in later...

- Given polynomials $(p,q)$, if dividing $q$ from $p$ produces a remainder,$\quad$ $p(x)
\not \vdots \;\; q(x)$

- Given $p:q = r \text{ with remainder } s \implies \frac{p}{q}=r+\frac{s}{q}$

## Implications

$$\text{For any $b$ such that $p(b) = 0 \implies p(b) \;\vdots\; (x-b)$}$$

Example:

$$p(x)=x^2-3x-18$$
$$\because$$
$$
\begin{aligned}
    p(6)&=6^2-3(6)-18 \\
    p(6)&=0 \\
\end{aligned}
$$
$$\therefore$$
$$(x^2 -3x-18) \;\vdots\; (x-6)$$

## Large exponents

$$p = a^n$$
$$
\text{sgn}(p) := \begin{cases}
   +1 &\text{if $n$ is even and } a \neq 0 \text{,} \\
   +1 &\text{if $n$ is odd and } a > 0 \text{,} \\
   -1 &\text{if $n$ is odd and } a < 0 \text{,} \\
   0 &\text{if } a = 0 \text{.}
\end{cases}
$$

In other words, any inequality that has zero on one side and polynomials that
are multiplying or dividing, we can reduce any odd exponent to $1$ and any even exponent to $2$.

### Example

$$
\begin{gathered}
    \frac{(x^2-4)^{17} (x^2-3)^{33}}{(x-2)^5 (4x^2 - 7)^{40}} \leq 0 \\
    \text{Is equivalent to:} \\
    \frac{(x^2-4) (x^2-3)}{(x-2) (4x^2 - 7)^{2}} \leq 0 \\
\end{gathered}
$$

# Functions

$$f(x) > 0$$

This is asking which $x$ is greater than $0$ in $y=f(x)$ where $y=f(x)$ is *continuous*.

## Continuous function

A *continuous* function is a function that does not have any abrupt changes in value, known as
discontinuities.

## Defining the domain

The *domain* of a function is the set of all possible inputs for the function.
For example, the domain of $f(x)=x^2$ is all real numbers, and the domain of $g(x)=\frac{1}{x}$ is
all real numbers except for $x=0$.

## Implications

If $f(x)$ is continuous, and $f(a)$ is positive and $f(b)$ is negative, there
exists *at least* one point between $f(a)$ and $f(b)$ that is equal to $0$.

If $f(x)$ is continuous, and $f(x)$ does not cross the
$x$-axis, if $f(a)$ is positive, all other points are positive, or if $f(a)$ is
negative, all other points in the function is negative.

## Example

$$
\begin{aligned}
    (x^2 -2x -15)(64-x^2) = 0
\end{aligned}
$$

The solutions are $x = -8, -3, 5, 8$.

We know that there are no other values for $x$ where $f(x) = 0$ and between each solution, all
values are either positive or negative.

$$
\begin{gathered}
    16x^4 - 17x^2      + 1 \\
    16x^4 - 16x^2 - x^2 + 1 \\
    16x^2(x^2 - 1) - 1(x^2 - 1) \\
    (16x^2-1)(x^2-1) \\
    (4x-1)(4x+1)(x-1)(x+1) \\
    \{\frac{1}{4}, -\frac{1}{4}, 1, -1\}
\end{gathered}
$$

## Irrational equations

$$\sqrt{a}, \text{Domain: }a\geq0$$

$$
\begin{gathered}
    \sqrt{3x^2+9x-14}-x=2 \\
    \text{Domain: } (-\infty, \frac{-9-\sqrt{249}}{6}]\cup[\frac{-9+\sqrt{349}}{6},+\infty) \\
    \sqrt{3x^2+9x-14}=x+2 \| ^2 \\
    3x^2+9x-14=x^2+4x+4 \\
\end{gathered}
$$

1. Define the domain (everything inside the root has to be $\geq0$)
2. We have to check our answers afterwards

$$
\begin{gathered}
    \sqrt{2x+1}=\sqrt{x-3}+2\|^2 \\
    2x+1=x-3+4\sqrt{x-3} +4 \|-x-1 \\
    4\sqrt{x-3} = x \| ^2 \\
    x^2 = 16(x-3) \\
    x^2 -16x +48 = 0 \\
    x=4, 12 \\
    \{4, 12\}
\end{gathered}
$$

## Irrational inequalities

$$A, B \geq 0 \to A>B \iff A^2 > B^2$$

$$
\begin{gathered}
    \sqrt{11-x} < x-1 \\
    \{x \;|\; x\leq 11\} \\
    \sqrt{11-x}-x-1 < 0 \\
\end{gathered}
$$

## Absolute value inequalities

### Definition

1. $$|a| \text{ is the distance from $0$}$$

2. $$
|a| := \begin{cases}
   a &\text{if $a \geq 0$} \\
   -a &\text{if $a < 0$} \\
\end{cases}
$$

### Characteristics

$$|a \cdot b| = |a| \cdot |b|$$
$$\left|\frac{a}{b}\right| = \frac{|a|}{|b|}$$
$$|a^h| = |a|^h$$

### Example


$$3|x+2| = 5-x$$

There are two parts:

1. If $x\geq-2$, then $|x+2| = x+2$

$$
\begin{aligned}
    3(x+2) &= 5-x \\
    3x + 6 &= 5-x \\
    x&=-\frac{1}{4}
\end{aligned}
$$

2. If $x<-2$, then $|x+2| = -(x+2)$

$$
\begin{aligned}
    -3(x+2) &= 5-x \\
    -3x - 6 &= 5-x \\
    x&=-\frac{11}{2}
\end{aligned}
$$

$$\left\{-\frac{1}{4}, -\frac{11}{2}\right\}$$

---


$$
    (2x+3)^2 - |2x+3| = -12
$$

### Tricks to solve

$$|x| = b$$
$$|x+a| + |x+b| + |x+c| = d $$

## Exponents

For all natural numbers ($m,n \in \mathbb{N}$):

$$a^n = \underbrace{a \cdotp a \cdotp \mathellipsis a}_{\text{n times}}$$

$$a^m \cdot a^n = n^{m+n}$$
$$\frac{a^m}{a^n} = n^{m-n}$$
$$(a^m)^n = a^{m \cdot n}$$
$$a^{-n}=\frac{1}{a^n}$$
$$a^n \cdot b^n = (a \cdot b )^n$$

$$a^0 = 1$$
$$0^m = 0$$
$$0^0 = \emptyset$$

> *Note:* When $m,n \not \in \mathbb{N}$, $x> 0$, otherwise we run into issues...

### Exponential equations

$$a^x=a^y \;|\; a > 0 \implies x= y$$
$$a^m = a^n, m=n \text{ or } a=1$$

### Special solutions

"Special" solutions are those that the base of the exponents are either $0$ or
negative and still are true.

### Exponential inequalities

$$a^m > a^n$$
$$
\begin{gathered}
    a \geq 1 \to \\
    m>n
\end{gathered}
\quad \vline \quad
\begin{gathered}
    a<1 \to \\
    m<n
\end{gathered}
$$

### Inequalities with variables in the base and the exponent

$$\begin{gathered}
    b^a > b^c  \\
    \text{Where $a, b, c$ contain $x$}
\end{gathered}
$$
For any base $b$, we must consider:
$$
\begin{gathered}
    0<b<1 \\
    a<c
\end{gathered}
\quad \vline \quad
\begin{gathered}
    b=1 \\
    \emptyset
\end{gathered}
\quad \vline \quad
\begin{gathered}
    b>1 \\
    a>c
\end{gathered}
$$

However, if $b^a \geq b^c$:
$$
\begin{gathered}
    0<b<1 \\
    a<c
\end{gathered}
\quad \vline \quad
\begin{gathered}
    b=1 \\
    \mathbb{R}
\end{gathered}
\quad \vline \quad
\begin{gathered}
    b>1 \\
    a>c
\end{gathered}
$$

# Logarithms

$$\log_a{b}=n \iff a^n=b$$
$$\text{$a$ is called the base and $b$ is called the argument.}$$
$$a>0, \quad b > 0, \quad a\neq 1$$

Example:

$$
\begin{aligned}
   8&=2^3 \\
   2&=8^{\frac{1}{3}}=\sqrt[3]{8} \\
   3&= \log_2{8}
\end{aligned}
$$

## Properties

$$a^{\log_a{b}} = b \tag{1}$$
$$\log_a 1 = 0 \tag{2}$$
$$\log_a a = 1 \tag{2}$$
$$\log_a b + log_a c = log_a (bc) \tag{4}$$
$$\log_a b - log_a c = log_a \left(\frac{b}{c}\right) \tag{5}$$
$$n\log_a b = log_a (b^n) \tag{6}$$
$$\log_a b = \frac{log_c b}{log_c a} \tag{7}$$
$$\log_a b \cdot \log_c a = log_c a^{\log_a b} = log_c b$$
$$log_a b = \frac{1}{log_b a} \tag{8}$$
$$\log_{a^m} b = \frac{1}{m} log_a b\tag{9}$$
$$\log_{a^m} b^n = \frac{n}{m} \log_a b \tag{6+8}$$

$$log_c a > log_c b$$
$$
\begin{gathered}
    0<c<1 \\
    a<b
\end{gathered}
\quad \vline \quad
\begin{gathered}
    c>1 \\
    a>b
\end{gathered}
$$

$$\text{sgn}(log_a b) = \text{sgn}((a-1)(b-1))$$
