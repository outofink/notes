---
title: Mathematical Methods - Chapter 3
author: Moshe Krumbein
date: Fall 2021
header-includes: |
    \usepackage{pgfplots}
    \usepackage{gensymb}
---

## Spherical Coordinate System

It consists of of the radius $r$ (the distance of the point from the origin),
theta $\theta$ (the angle above the $x$-axis towards the $y$-axis), and phi
$\phi$ (the angle above the $z$-axis along towards the point), such that:

$$0 \leq \theta \leq 2 \pi \quad 0 \leq \phi \leq \pi$$

In Cartesian coordinates:
$$
\begin{gathered}
    x = r \sin \phi \cos \theta \\
    y = r \sin \phi \sin \theta \\
    z = r \cos \phi \\
    \\
    r = \sqrt{x^2+y^2+z^2} \\
    \phi = \arccos\left(\frac{z}{r}\right) \\
    \theta = \arctan\left(\frac{y}{x}\right) \underbrace{+\pi}_{y<0}
    = \arccos\left(\frac{x}{\sqrt{x^2+y^2}}\right)
    = \arcsin\left(\frac{y}{\sqrt{x^2+y^2}}\right)
\end{gathered}
$$

# Chapter 3 - [Complex Numbers](https://en.wikipedia.org/wiki/Complex_number)

$$\mathbb{C} = \{a +bi \mid a, b \in \mathbb{R}\}$$

*Inception:* To help solve 3rd degree polynomials.

### Fundamental theorem of algebra:

For all polynomial ($a_nx_n+a_{a-1}x^{x-1}+\ldots+a_1x+a_0$) with *complex
coefficients* has *complex roots*.

## Operations:

$$
\begin{gathered}
    (a+bi)+(c+di) = (a+d)+(b+d)i \\
    (a+bi)-(c+di) = (a-d)+(b-d)i \\
    (a+bi)(c+di) = (ac - bd) + (ad + bc)i \\
    \frac{a+bi}{c+di} = \frac{(a+bi)(c-di)}{(c+di)(c-di)}
    = \frac{e+fi}{c^2+d^2} = \frac{e}{c^2+d^2}+\frac{f}{c^2+d^2}i
\end{gathered}
$$

## Complex Plane

Every complex number $z=a+bi$ can be represented on the complex plane at the
point $(a,b)$.

It can also be represented in the polar form:
$$
\begin{gathered}
    r=|z| \quad \theta = \arg(z) \\
    z = r \cos \theta + r \sin \theta i \quad (\operatorname{cis} \theta)\\
\end{gathered}
$$


### Characteristics

1. Properties of four algebraic operations of the real numbers also apply to
   the complex ones (i.e. associative, distributive, etc.)
2. *Complex conjugate*:
$$\begin{gathered}
    \overline{z_1 \pm z_2} = \overline z_1 \pm \overline z_2 \\
    \overline{z_1 \cdot z_2} = \overline z_1 \cdot \overline z_2 \\
    \overline{\frac{z_1}{z_2}} = \frac{\overline z_1}{\overline z_2} \\
    \frac{1}{z}=\frac{\overline z}{|z|^2}, \; z \cdot \overline z  = |z|^2 \\
\end{gathered}
$$

### Analysis

$$
\begin{gathered}
    z_1 = r_1(\cos \theta_1 + i \sin \theta_1) \\
    z_2 = r_2(\cos \theta_2 + i \sin \theta_2) \\
    z_1 z_2= r_1 r_2 [
        (\underbrace{\cos \theta_1 \cos \theta_2 - \sin \theta_1 \sin\theta_2}
            _{\cos (\theta_1 + \theta_2)})
        +i(\underbrace{\sin \theta_1 \cos \theta_2 + \sin \theta_2 \cos \theta_1}
            _{\sin(\theta_1 + \theta_2)})
    ] \\
\end{gathered}
$$

#### Conclusion:

$$
\begin{gathered}
    |z_1 z_2| = r_1 r_2 \\
    \arg(z_1 z_2) = \theta_1 + \theta_2
\end{gathered}
$$

## De Moivre's formula

$$(r \operatorname{cis}\theta)^n=r^n \operatorname{cis}(n \theta)$$

## $n$th-root of a complex number

$$
\begin{gathered}
    z^n = r \operatorname{cis} \theta \\
    z = \sqrt[n]{r} \operatorname{cis}\left(\frac{\theta + 2 \pi k}{n}\right),
    \quad k = 0, 1, 2, \ldots, n-1
\end{gathered}
$$
