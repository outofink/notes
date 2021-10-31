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

$$
0 \leq \theta \leq 2 \pi \quad 0 \leq \phi \leq \pi
$$

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

$$
\mathbb{C} = \{a +bi \mid a, b \in \mathbb{R}\}
$$

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
$$
\begin{gathered}
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

$$
(r \operatorname{cis}\theta)^n=r^n \operatorname{cis}(n \theta)
$$

## $n$th-root of a complex number

$$
\begin{gathered}
    z^n = r \operatorname{cis} \theta \\
    z = \sqrt[n]{r} \operatorname{cis}\left(\frac{\theta + 2 \pi k}{n}\right),
    \quad k = 0, 1, 2, \ldots, n-1
\end{gathered}
$$

## Euler's Symbol

$$
\begin{gathered}
    e^{i \theta} = \cos \theta + i \sin \theta \\
    e^{-i \theta} = \cos  \theta - i \sin \theta \\
    \cos \theta = \frac{1}{2}(e^{i \theta}+e^{-i \theta})
    \quad \sin \theta = \frac{1}{2i}(e^{i \theta} - e^{-i \theta})
\end{gathered}
$$

$e$ to a complex number:

$$
e^{a+ib} = e^a e^{ib} = e^a(\cos b + i\sin b)
$$

Our goal is to:

1. Express $\cos(nx)$ in terms of $\sin x, \cos x$.
2. Express $\sin^n(x)$ as a sum of $\sin x, \cos x$, without multiplying them.

#### Example:

$$
\begin{gathered}
    \cos(5x) = \Re(e^{i5x}) = \Re((e^{ix})^5) \\
    = \Re((\cos x+i\sin x)^5) \\
    (a+b)^5 = a^5 + 5a^4b+10a^3b^2 + 10a^2b^3 + \ldots
\end{gathered}
$$

To simplify our calculation since we are only looking for the real part of our solution, we can ignore any place where $\sin$ is raised to an odd power (since $i^2 = -1$).
$$
    = \cos^5x-10\cos^x\sin^2x+5\cos x\sin^4x
$$
Now for an example in the opposite direction:
$$
\begin{gathered}
    \sin^5x = \left(\frac{1}{2i}\right)^4(e^{ix}-e^{-ix})^4 \\
    \frac{1}{16}(e^{i4x}-4e^{i2x} +6 -4 e^{-i2x}+e^{-i4x}) \\
    =\frac{1}{16}(2\cos (4x)-8 \cos (2x)+6)
\end{gathered}
$$

Another example:
$$
\begin{gathered}
    a \cos (\omega t) + b\sin(\omega t) \\
    \Re(\underbrace{(a+bi)}_{re^{i \theta}}\underbrace{(\cos(\omega t)- i \sin (\omega t)}_{e^{-i\omega t}}) \\
    = \Re\left(re^{i(\theta - \omega t)}\right)
    = r \cos(\theta - \omega t) = r \cos(\omega t - \theta)\\
    =\sqrt{a^2 + b^2} \cos\left(\omega t -\arctan\left(\frac{a}{b}\right)(+ \pi)\right)
\end{gathered}
$$

## What is $\ln(a+bi)$?



$\ln z$ is the solution to the equation $e^\omega=z \to e^u \cdot e^{iv}=a+bi = re^{i\theta}$.

$$
\begin{gathered}
    u = \ln r = \ln|z| \\
    v= \theta +2\pi k
\end{gathered}
$$

Conclusion:
$$
\ln(z) = \ln|z|+i(\arg(z)+2\pi k)
$$

Example:
$$
\begin{gathered}
    \ln(- \sqrt 3 + i)\\
    -\sqrt 3 + i =2 \operatorname{cis}\left(\underbrace{\arctan\left(-\frac{1}{\sqrt 3}\right)}_{-\frac{\pi}{6}}+\pi\right) \\
    =2 \operatorname{cis}\left(\frac{5\pi}{6}\right) \\
    \ln(-\sqrt 3+i) = ln 2 + i \left(\frac{5\pi}{6} + 2 \pi k\right)
\end{gathered}
$$

## Solving Complex Equations

$$
\begin{gathered}
    z^4+z^3+z^2+z +1 = 0 \;\backslash : z^2 \\
    z^2+z +1 + \frac{1}{z} + \frac{1}{z^2} = 0 \\
    t = z + \frac{1}{z} \quad t^2 = z^2 +2 + \frac{1}{z^2} \\
    t^2 + t - 1= 0 \\
    t_{1,2} = \frac{-1 \pm \sqrt 5}{2} \\
    \Downarrow \\
    2z^2 -(-1 + \sqrt 5) + 2 = 0
\end{gathered}
$$

$z$ can be found given that we know how to find the square root of complex numbers.
$$
    z_{1,2} = \frac{-1 + \sqrt 5 \pm \sqrt{(-1+\sqrt 5)^2-16}}{4}
$$

$$
\begin{gathered}
z^4+z^3+z^2+z+1 = 0 \\
(z-1)(z^4+z^3+z^2+z+1)=0 \\
z^5 = 1 = \boxed{1 \cdot e^{i \cdot 0}}
\end{gathered}
$$

### Fundamental Theorem of Algebra

All polynomials can be factored into a product of linear elements in the complex world.
$$
\begin{gathered}
x^4 -1 = (x^2-1)(x^2+1) \\
=(x-1)(x+1)(x-i)(x+i)\tag{1}
\end{gathered}
$$

$$
\begin{gathered}
\tag{2}
x^3-3x^2+2=(x-1)(x^2-2x-2) \\
x_{1,2}=\frac{2\pm2\sqrt{3}}{2} = 1\pm\sqrt 3 \\ \Downarrow \\
=(x-1)(x-(1+\sqrt 3))(x-(1-(1-\sqrt 3)))
\end{gathered}
$$

$$
\begin{gathered}
\tag{3}\\
x^2 + 6  + 9=(x+3)^2 \\
-3 \text{ is the root (double root)}
\end{gathered}
$$

$$
\begin{gathered}
    x^4+2x^2+1 = (x^2+1)^2 \quad (\text{division over the real numbers}) \\
    (x-i)^2(x+i)^2 \quad (\text{division over the complex numbers}) \\
    \pm i \text{ are each double roots} \tag{4}
\end{gathered}
$$

#### Claim:

$$
p(x)a_nx^n+a_{n-1}x^{x-1}+\ldots+a_1x+a_0
$$

Polynomials with real coefficients if $z$ is a root of $p(x)$ then $\overline z$ is also a root of $p(x)$.

#### Example:

$$
\begin{gathered}
x^3+3x^2+4x+2 \\
\pm1, \pm 2 = (x+1)(x^2+2x+2) \\
x_{1,2} = \frac{-2 \pm \sqrt{2^2{-8}}}{2} = \boxed{-1 \pm i}
\end{gathered}
$$

#### Proof:

Given $a_nz^n+ \ldots + a_0=0$, we have to prove:
$$
a_n(\overline z)^n + a_{n-1}(\overline z)^{n-1}+ \ldots = 0
$$

$$
\begin{gathered}
    \text{Reminder:} \\
    \overline{z_1z_2} = \overline z_1 \overline z_2 \quad \overline{z_1+z_2} = \overline z_1 + \overline z_2 \\
    \Downarrow \\
    (\overline{z^n}) = (\overline z)^n
\end{gathered}
$$

Given: $a_nz^n+a_{a-1}z^{n-1}+\ldots = 0$:
$$
\begin{gathered}
\overline{a_nz^n+a_{a-1}z^{n-1}+\ldots = 0} = \overline 0 \\ \Downarrow \\
\overline{a_nz^n} + \ldots + \overline a_n = 0 \\
\overline{a_n}\overline{z^n} + \ldots + \overline a_n = 0 \\
a_n(\overline z)^n + \ldots + a_n = 0 \\
\implies \overline z \text{ is a root of the polynomial.}
\end{gathered}
$$
Note on $\ln(z)$: There are infinite solutions because $\omega = \ln |z| + i(\arg z+2\pi k)$ where $k \in \mathbb{N}$.

### Examples from the previous week:

$C$ is the cylinder with a radius of $1$ with its axis going through the point  $(1,0,0)$. and parallel to the $z$-axis. $S$ is a sphere with a radius of $2$ with its center at $(0,0,0)$.

1. Write the equations for $C, S$ on the Cartesian coordinate system $(x,y,z)$.


$$
\begin{gathered}
S: x^2+y^2+z^2=4 \\
C: (x-1)^2 + y^2 = 1
\end{gathered}
$$

2. Write the equations for $C, S$ on the cylindrical coordinate system $(\rho,\theta,z)$.

$$
\begin{gathered}
C: \quad\quad \begin{gathered}
(\rho \cos \theta -1)^2 + (\rho\sin\theta)^2=1 \\
\rho^2 = 2\rho\cos \theta \;\backslash :\rho \\
\boxed{\rho=2\cos \theta} \quad\left(-\frac{\pi}{2} \leq \theta \leq \frac{\pi}{2}\right)
\end{gathered} \\
S: \quad\quad \boxed{\rho^2 + z^2=4}
\end{gathered}
$$

3. Write the equations for $C, S$ on the spherical coordinate system $(r,\theta,\phi)$.

$$
C: \begin{gathered}
\rho = r\ sin \phi\\
z = r \cos \phi \\
\boxed{r \sin \phi = 2 \cos \theta}
\end{gathered} \\
S: \boxed{r=z}
$$

4. Find the parametric form for $C\cap S$ on the cylindrical coordinate system.
$$
   \begin{gathered}
   \begin{pmatrix}\rho\\\theta\\z\end{pmatrix} =
   \begin{pmatrix}
   2 \cos t \\
   t \\
   \pm \sqrt{4-(2\cos t)^2} = \pm 2 \sin t
   \end{pmatrix} \quad -\frac{\pi}{2} \leq t \leq \frac{\pi}{2}
    \\
    =  \begin{pmatrix}
   t \\
   \arccos\left(\frac{t}{2}\right) \\
   \pm\sqrt{1-t^2} \quad 0
   \end{pmatrix} \quad 0 \leq t \leq 2
   \end{gathered}
$$

5. Find the parametric form for $C\cap S$ on the spherical coordinate system.
$$
   \begin{gathered}
   \begin{pmatrix}r\\\theta\\\phi\end{pmatrix} =
   \begin{pmatrix}
   2 \\
   t \\
   \frac{\pi}{2}-t
   \end{pmatrix} \quad - \frac{\pi}{2} \leq t \leq \frac{\pi}{2}
   \end{gathered}
$$

5. Find the parametric form for $C\cap S$ on the Cartesian coordinate system.

$$
\begin{gathered}
\begin{pmatrix}x\\y\\z\end{pmatrix} =
\begin{pmatrix}
\rho \cos \theta = 2 \cos^2t \\
\rho  \sin \theta =2 \cos t \sin t\\
z = \pm 2 \sin t
\end{pmatrix} \quad - \frac{\pi}{2} \leq t \leq \frac{\pi}{2}
\end{gathered}
$$

#### Example 2:

$x^4+x^2+1$ can be factored over the real numbers and over the complex numbers.

$$
\begin{gathered}
t = x^2 \to t^2 + t + 1 \\
t_{1,2} = -\frac{1}{2} \pm i \frac{\sqrt 3}{2} \\
z_1 = \pm \sqrt{t} = \pm \sqrt{e^{i+\frac{2 \pi}{3}}} = \pm e^{i\frac{\pi}{3}} \\
z_2 = \pm \sqrt{e^{\frac{4 \pi}{3}i}} = \pm e^{i\frac{2 \pi}{3}} \\\\
(x-e^{i \frac{\pi}{3}})(x+e^{i \frac{\pi}{3}})(x-e^{i\frac{2 \pi}{3}})(x+e^{i\frac{2 \pi}{3}}) \\ \\
e^{i \frac{\pi}{3}} = \\operatorname{cis} \frac{\pi}{3} = \frac{1}{2}+ \frac{\sqrt 3}{2}i \implies \\
\pm e^{i\frac{2 \pi}{3}} = \pm\left(-\frac{1}{2}+\frac{\sqrt 3}{2}i\right) \\
=(x^2+x+1)(x^2+x+1)
\end{gathered}
$$

$$
\begin{gathered}
(x-z)(x-\overline z) \\
= x^2 - (\underbrace{z + \overline z}_{real}) x + \underbrace{z \cdot \overline z}_{real}
\end{gathered}
$$

All real polynomials can be factored into real linear or double roots.

#### Example 3

$$
\begin{gathered}
(\underbrace{2+i}_{\theta_1})(\underbrace{3+i}_{\theta_2}) = 5+ 2i +3i + i^2 = \underbrace{5+5i}_{\theta_1 + \theta_2} \\
\theta_1 =\arctan \frac{1}{2} \quad \theta_2 = \arctan \frac{1}{3} \\
\theta_ 1+ \theta_2 = \frac{\pi}{4}
\end{gathered}
$$
