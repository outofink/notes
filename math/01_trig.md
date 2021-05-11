---
title: Trigonometry
date: Fall 2020
author: Moshe Krumbein
---

# Trigonometric identities

| $a$      | $0\text{\textdegree}$ | $30\text{\textdegree}$ | $45\text{\textdegree}$ | $60\text{\textdegree}$ | $90\text{\textdegree}$ |
|:--------:|:---------------------:|:----------------------:|:----------------------:|:----------------------:|:----------------------:|
| $\sin a$ | $0$                   | $\frac{1}{2}$          | $\frac{\sqrt{2}}{2}$   | $\frac{\sqrt{3}}{2}$   | $1$                    |
| $\cos a$ | $1$                   | $\frac{\sqrt{3}}{2}$   | $\frac{\sqrt{2}}{2}$   | $\frac{1}{2}$          | $0$                    |
| $\tan a$ | $0$                   | $\frac{1}{\sqrt{3}}$   | $1$                    | $\sqrt{3}$             | $\emptyset$            |
| $\cot a$ | $\emptyset$           | $\sqrt{3}$             | $1$                    | $\frac{1}{\sqrt{3}}$   | $0$                    |

> *Note:* $180\text{\textdegree} = \pi$ radians

Main identity:

$$\sin^2(\alpha) + \cos^2(\alpha) = 1$$
$$\tan^2(\alpha) + 1 = \frac{1}{\cos^2(\alpha)} = \sec^2(\alpha)$$
$$\cot^2(\alpha) + 1 = \frac{1}{\sin^2(\alpha)} = \csc^2(\alpha)$$

Example:
$$
\begin{gathered}
    \cos^2 \alpha - \cos^2 \beta = \sin^2 \beta - \sin^2 \alpha \\
    \Updownarrow \\
    \sin^2 \alpha + \cos^2 \alpha = \sin^2 \beta + \cos^2 \beta \\
    \Updownarrow \\
    1=1 \\
    \blacksquare
\end{gathered}
$$

# Trigonometric equations

***

$$\sin x=a$$

$$
\begin{gathered}
    a<-1, a>1 \\
    x = \emptyset
\end{gathered}
\quad \vline \quad
\begin{gathered}
    \sin x = 1 \\
    x = \frac{\pi}{2} + 2 \pi k, \;k \in \mathbb{Z}
\end{gathered}
\quad \vline \quad
\begin{gathered}
    \sin x = -1 \\
    x = -\frac{\pi}{2} + 2 \pi k, \;k \in \mathbb{Z}
\end{gathered}
$$

$$1 < a < 1$$
$$
\begin{aligned}
    x_1 &=& \arcsin a + 2 \pi k, \; k \in \mathbb{Z} \\
    x_2 &=& \pi - \arcsin a + 2 \pi k, \; k \in \mathbb{Z} \\
\end{aligned}
$$

***

$$\cos x=a$$

$$
\begin{gathered}
    a<-1, a>1 \\
    x = \emptyset
\end{gathered}
\quad \vline \quad
\begin{gathered}
    \cos x = 1 \\
    x = 2 \pi k, \;k \in \mathbb{Z}
\end{gathered}
\quad \vline \quad
\begin{gathered}
    \cos x = -1 \\
    x = \pi + 2 \pi k, \;k \in \mathbb{Z}
\end{gathered}
$$

$$-1 < a < 1$$
$$
\begin{aligned}
    x_1 &=&  \arccos a + 2 \pi k, \; k \in \mathbb{Z} \\
    x_2 &=& -\arccos a + 2 \pi k, \; k \in \mathbb{Z} \\
\end{aligned}
$$

***

$$\tan x=a$$
$$x \ne \frac{\pi}{2} + \pi n, \; n \in \mathbb{Z}$$
$$x= \arctan a + \pi k$$

***

$$
\begin{gathered}
    \sin \alpha = \sin \beta \\
    \\
    \begin{alignedat}{2}
        \alpha &=       &\beta + 2 \pi k \\
        \alpha &= \pi - &\beta + 2 \pi k
    \end{alignedat}
\end{gathered}
\quad \vline \quad
\begin{gathered}
    \cos \alpha = \cos \beta \\
    \\
    \begin{alignedat}{2}
        \alpha &=   &\beta + 2 \pi k \\
        \alpha &= - &\beta + 2 \pi k
    \end{alignedat}
\end{gathered}
\quad \vline \quad
\begin{gathered}
    \tan \alpha = \tan \beta \\
    \\
    \alpha =   \beta + \pi k \\
    \\
\end{gathered}
$$

$$
\begin{gathered}
    \sin x = 0 \\
    x= \pi k \;(k \in \mathbb{Z})
\end{gathered}
\quad \vline \quad
\begin{gathered}
    \cos x = 0 \\
    x= \frac{\pi}{2} + \pi k \;(k \in \mathbb{Z})
\end{gathered}
$$

# Evenness and symmetry of trigonometric functions

$\cos$ is an even function, meaning $\cos (- \alpha) =   \cos (\alpha)$

$\sin$ is an odd  function, meaning $\sin (- \alpha) = - \sin (\alpha)$

$\tan$ is an odd  function, meaning $\tan (- \alpha) = - \tan (\alpha)$

$$
\begin{gathered}
    \sin (\pi - \alpha) = \sin  \alpha \\
    \cos (\pi - \alpha) = -\cos \alpha \\
    \tan (\pi - \alpha) = -\tan \alpha
\end{gathered}
$$

$$
\begin{gathered}
    \sin (\frac{\pi}{2} - \alpha) = \cos \alpha \\
    \cos (\frac{\pi}{2} - \alpha) = \sin \alpha \\
    \tan (\frac{\pi}{2} - \alpha) = \cot \alpha
\end{gathered}
$$

# trig "trick"

Given trigonometric function in the form of $\sin(\pm \alpha \pm \frac{\pi n}{2})$,
we can simplify if the following way:

If $n$ is even (which is to say, we are adding or subtracting a full multiple
of $\pi$), the function stays the same (i.e. $\sin \to \sin, \cos \to \cos$)

If $n$ is odd (which is to say we are adding or subtracting by a multiple of
$\frac{\pi}{2}$), the function switches to its "co" or not-"co" counterpart
(i.e. $\sin \to \cos, \cos \to \sin, \tan \to \cot$)

Now, in order to determine the sign of the answer, the sign of the answer is
the sign of the original function given $\alpha = \frac{\pi}{4}$ (i.e.
$\sin(\pi + \alpha) = -, \cos(\frac{3\pi}{2} + \alpha) = +$)

# Multiple angle identities

If we rotate $A_1(a, 0)$ by angle $\alpha$, we get $B_1( a\cos \alpha, a\sin \alpha)$

If we rotate $A_2(0, b)$ by angle $\alpha$, we get $B_2(-b\sin \alpha, b\cos \alpha)$

Therefore, knowing $\vec{OA}(x, y) = \vec{OA_1}(x, 0) + \vec{OA_2}(0,y)$:

Rotating $A(a,b)$ by $\alpha \to B_1(a\cos \alpha, a\sin \alpha) + B_2(-b\sin
\alpha, b\cos \alpha) = B(a\cos \alpha - b\sin \alpha, a\sin \alpha + b\cos
\alpha)$

This proves:

$$\sin(\alpha + \beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta$$
$$\cos(\alpha + \beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta$$

$$\sin(\alpha - \beta) = \sin \alpha \cos \beta - \cos \alpha \sin \beta$$
$$\cos(\alpha - \beta) = \cos \alpha \cos \beta + \sin \alpha \sin \beta$$

$$\tan(\alpha + \beta) = \frac{\tan \alpha + \tan \beta}{1-\tan \alpha
\tan \beta}$$
$$\tan(\alpha - \beta) = \frac{\tan \alpha - \tan \beta}{1+\tan \alpha
\tan \beta}$$

$$\sin(2\alpha) = 2\sin \alpha \cos \alpha$$
$$
\begin{aligned}
  \cos(2\alpha) \\
  &=\cos^2 \alpha -\sin^2 \alpha \\
  &=1 - 2\sin^2 \alpha \\
  &=2\cos^2 \alpha - 1
\end{aligned}
$$
$$\tan(2\alpha) = \frac{2\tan \alpha}{1-\tan^2 \alpha}$$

$$2\sin\left(\frac{\alpha+\beta}{2}\right)\cos\left(\frac{\alpha-\beta}{2}\right) = \sin\alpha + \sin\beta$$

$$2\cos\left(\frac{\alpha+\beta}{2}\right)\cos\left(\frac{\alpha-\beta}{2}\right) = \cos\alpha + \cos\beta$$

# Homogeneous equations

## First degree

$$
\begin{gathered}
    A \sin x = B \cos x \\
    x = \arctan \frac{B}{A} + \pi k,\quad k \in \mathbb{Z}
\end{gathered}
$$

## Second degree

$$
\begin{gathered}
    Ax^2 + Bxy + Cy^2 = 0 \\
    At^2 + Bt + C = 0, \quad t = \frac{x}{y} \\
\end{gathered}
$$

If $x=\sin x$ and $y=\cos x$, then:

$$
\begin{gathered}
    A\sin^2{x}+B\sin x \cos x + C \cos^2{x} = 0 \\
    At^2 + Bt + C = 0, \quad t = \tan x \\
\end{gathered}
$$

$$
\begin{gathered}
    A \sin x + B \cos x = C \\
    A \sin 2 \alpha + B \cos 2 \alpha = C, \quad x = 2 \alpha \\
    A (2 \sin \alpha \cos \alpha) + B (\cos^2 \alpha - \sin^2 \alpha) = C
    (\sin^2 \alpha + \cos^2 \alpha) \\
    -(B+C)\tan^2 \alpha + 2A\tan \alpha + (B-C) = 0
\end{gathered}
$$
