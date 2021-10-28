---
title: Mathematical Methods - Chapter 1
author: Moshe Krumbein
date: Fall 2021
---

Email: moria.sigron@mail.huji.ac.il

Phone: 054-571-1113 (math)

# Set Theory

See Discrete Mathematics.

$$A \times B = \{(x,y) \;|\; x \in A, y \in B\}$$
$$\mathbb{R} \times \mathbb{R} = \mathbb{R}^2 = \{(x,y)\;|\;x,y \in \mathbb{R}\}$$

Circle:

$$\left\{(x,y) \in \mathbb{R}^2 \;|\; (x-x_0)^2 + (y-y_0)^2 = r^2\right\}$$

Graph:

$$G_f = \left\{(x,y) \in \mathbb{R}^2 \;|\; y=f(x)\right\}$$

# Vectors in $\mathbb{R}^n$

## What is a vector?

A *vector* is a is a arrow with a *direction* and *magnitude*.

It can express:

1. Displacement
1. Angular velocity

Two vectors with the same magnitude and direction are *equal*.

## Definitions and Symbols

## What is $\mathbb{R}^n$?

Plane: $\mathbb{R}^2=\{(x,y)\;|\;x,y \in \mathbb{R}\}$

Space: $\mathbb{R}^3=\{(x,y,z)\;|\;x,y,z \in \mathbb{R}\}$

$$\mathbb{R}^n = \{(x_0,x_1,x_2,\mathellipsis)\;|\;\underset{1 \leq i \leq n}{x_i} \in \mathbb{R}\}$$

$$\mathbb{R}^n=\left\{
\begin{pmatrix}
   x_1 \\
   \vdots \\
   x_n \\
\end{pmatrix} \;|\;
\underset{1 \leq i \leq n}{x_i \in \mathbb{R}}
\right\}$$

Points: $A,B,C$

Parallel line: $AB \parallel CD$

Perpendicular: $AB \perp CD$

Distance between points (on a plane): $AB = \sqrt{(a_1-b_1)^2+(a_2-b_2)^2}$

Distance between points (in $\mathbb{R}^3$ space): $AB = \sqrt{(a_1-b_1)^2+(a_2-b_2)^2+(a_3-b_3)^2}$

Distance (in $\mathbb{R}^2$): $AB= \sqrt{\displaystyle\sum_{i=1}^n(a_i-b_i)^2}$

## Expressing vectors mathematically

We place the *tail* of the vector and put it at the *origin* $(0,0)$ and the
head at point $P(x,y)$.

If $\underline u = \vec{(x,y)}$ that means that $u$ is a vector that starts at $(0,0)$ and ends $x$ to the right and $y$ up.

## Symbol:

#### Vector:
$\underline u$, $\vec{AB}$

#### Zero vector:
$\underline 0 = \begin{pmatrix}
    0 \\
    \vdots \\
    0
\end{pmatrix}$

#### Magnitude:
$||\underline u||$

#### Position vector at $(x,y,z)$:
$\underline r =
\begin{pmatrix}
    x \\y\\z
\end{pmatrix}$

#### Unit vector (magnitude of 1):
$\underline{\hat e}$

#### On $\mathbb{R}^2$:

$\underline{\hat i} = \begin{pmatrix}
    1\\0
\end{pmatrix}
\quad
\underline{\hat j} =  \begin{pmatrix}
    0\\1
\end{pmatrix}$

### Adding vectors

$$\underline u + \underline v = \underline v + \underline u$$
$$\begin{pmatrix}
    a_1 \\a_2\\\vdots\\a_n
\end{pmatrix}+\begin{pmatrix}
    b_1 \\b_2\\\vdots\\b_n
\end{pmatrix}=\begin{pmatrix}
    a_1+b_1\\a_2+b_2\\\vdots\\a_n+b_n
\end{pmatrix}$$

### Multiplying a vector with a scalar

$$\lambda \cdot \underline a  = \lambda \cdot \begin{pmatrix}
    a_1\\a_2\\\vdots\\a_n
\end{pmatrix} = \begin{pmatrix}
    \lambda \cdot a_1 \\
    \lambda \cdot a_2 \\
    \vdots \\
    \lambda \cdot a_n
\end{pmatrix}$$

$$- \underline a = \begin{pmatrix}
    -a_1\\\vdots\\-a_n
\end{pmatrix} = (-1) \cdot \underline a$$

### Finding getting a unit vector from a vector (normal)

$$\underline{\hat a} = \frac{\underline a}{||\underline a||}$$

Sometimes we *symbolize* the length of $\underline r$ as $r$.

$$\underline r = r \cdot \underline{\hat r}$$

### Subtracting vectors

$$\underline u + (-\underline v) = \underline u - \underline v$$

### Expressing vectors
$$\begin{pmatrix}
    x\\y\\z
\end{pmatrix} = x\begin{pmatrix}
    1\\0\\0
\end{pmatrix} + y\begin{pmatrix}
    0\\1\\0
\end{pmatrix} + z\begin{pmatrix}
    0\\0\\1
\end{pmatrix}
= x\;\underline{\hat i} + y\;\underline{\hat j} + z\;\underline{\hat k}$$


### Finding a line that passes through two position vectors $\underline a,\underline b$

### Parametric Form

$$\underline v = \underline b - \underline a$$

$$l = \{ \underline a + t \underline v \;|\; t \in \mathbb{R}\}$$
$$= \{(1-t)\underline a + t \underline b \;|\; t \in \mathbb{R}\}$$
$$= \{(1-t)\underline a + t \underline b \;|\; 0<=t<=1\}$$

If $t \in (0,1)$, the point is between $\underline a$ and $\underline b$ ($AB$).

#### Example:

$$A=(1,0,6) \quad B=(2,1,3)$$


$$
    \left\{(1-t)\begin{pmatrix}
        1\\0\\6
    \end{pmatrix}+t \begin{pmatrix}
        2\\1\\-3
    \end{pmatrix}\;|\; t \in \mathbb{R}\right\}
$$
$$
    \left\{\begin{pmatrix}
        1+t\\t\\6-9t
    \end{pmatrix} \;|\; t \in \mathbb{R} \right\}
$$

$$
    AB=\underline r = \begin{pmatrix}
        1+t\\t\\6-9t
    \end{pmatrix}_{0 \leq t \leq 1}
$$

### Scalar multiplication (between two vectors)

$\underline a, \underline b \in \mathbb{R}^n$:

$$\begin{pmatrix}
    a_1 \\ \vdots \\ a_n
\end{pmatrix} \cdot \begin{pmatrix}
    b_1 \\ \vdots \\ b_n
\end{pmatrix} = a_1 b_1 + \mathellipsis a_n b_n$$

$$\underline a \cdot \underline b = \sum_{i=1}^n a_i b_i$$

#### Example:

$$\begin{pmatrix}
    2\\1\\7
\end{pmatrix} \cdot \begin{pmatrix}
    1\\-5\\2
\end{pmatrix} = 2 \cdot 1 + 1 \cdot (-5) + 7 \cdot 2 = 11$$

#### Characteristics:

1. $\underline a \cdot \underline b = \underline b \cdot \underline a$
2. $(\lambda \underline a) \cdot \underline b = \lambda (\underline a \cdot
   \underline b)$
3. $\underline a \cdot (\underline b + \underline c) = \underline a \cdot
   \underline b + \underline a \cdot \underline c$
4. $\underline a \cdot \underline a = ||a||^2$

#### Geometric meaning:

$\underline a, \underline b \in \mathbb{R}^n$:


$$||\underline a - \underline b||^2=(\underline a - \underline
b)\cdot(\underline a - \underline b)$$
$$=||a||^2+||b||^2 - 2(\underline a \cdot \underline b)$$

#### Reminder:

Law of Cosines

$$c^2=a^2+b^2+2ab\cos \theta$$

#### Conclusion

$$\underline a \cdot \underline b = ||a|| \cdot ||b|| \cos \theta$$
$$\cos \theta = \frac{\underline a \cdot \underline b}{||a||\cdot||b||}$$
$\underline a, \underline  b \neq \underline 0$:

$$
\begin{gathered}
    \underline a \cdot \underline b = 0 \iff \underline a \perp \underline b \\
    \underline a \cdot \underline b > 0 \iff \theta \text{ is acute } \left(0 \leq
    \theta < \frac{\pi}{2}\right)\\
    \underline a \cdot \underline b < 0 \iff \theta \text{ is obtuse } \left(\frac{\pi}{2} < \theta \leq \pi\right)\\
\end{gathered}
$$

### Projection

Let $\underline{\hat e}$ be a unit vector and $\underline a$ be some vector,
such that $\underline a \cdot \underline e = ||a||\cos \theta$
(*projection* of $\underline a$ on $\underline{\hat e}$).

### Planes in $\mathbb{R}^3$

Consider a plane $\Pi \subseteq \mathbb{R}^3$, the *normal vector* to $\Pi$,
$\underline n$ (perpendicular to the plane), and the *unit vector* in the direction of the normal,
$\underline{\hat n}$.

$$\forall \; \underline r \in \Pi : \underline r \cdot
\underline{\hat n} = \bold 0$$

#### Example:

$$
\begin{gathered}
    \underline n = \begin{pmatrix}
        1\\0\\6
    \end{pmatrix}, ||\underline n|| = 3 \\
    \underline{\hat r} = \begin{pmatrix}
        \frac{1}{\sqrt{37}} \\
        0 \\
        \frac{6}{\sqrt{37}}
    \end{pmatrix} \\
    \underline r \cdot \begin{pmatrix}
        \frac{1}{\sqrt{37}} \\
        0 \\
        \frac{6}{\sqrt{37}}
    \end{pmatrix} = 3 \\
    \begin{pmatrix}
        x\\y\\z
    \end{pmatrix} \cdot \begin{pmatrix}
        \frac{1}{\sqrt{37}} \\
        0 \\
        \frac{6}{\sqrt{37}}
    \end{pmatrix} = 3
\end{gathered}
$$

$$\underline r \cdot \underline n = \alpha ||\underline n||$$
$$\underline r \cdot \underline{\hat n} = \alpha$$

Given plane $3x+2y-z=10$, find the normal vector and the distance to the
origin.

Normal vector: $\underline n = \begin{pmatrix}
    3\\2\\-1
\end{pmatrix}$

Distance: $\frac{10}{||\underline n||} = \frac{10}{\sqrt{3^2+2^2+(-1)^2}} = \frac{10}{\sqrt{14}}$

#### In general:

Given the plane $ax+by+cz = d$, the distance from the origin is $\frac{d}{\sqrt{a^2+b^2+c^2}}$.
