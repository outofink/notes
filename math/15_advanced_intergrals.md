---
title: Advanced Intergation
author: Moshe Krumbein
date: Spring 2021
---

# Double integrals

$$\iint\limits_D f(x,y)\,dx\,dy = \iint\limits_D f(x,y)\,dA$$
Where $dA$ is the area.

In essence, a double integral is the integral in terms of $y$ and then in term
of $x$ or visa versa.

For example:
$$\int\limits_{a}^{b}\int\limits_{c}^{d}f(x,y)\,dy\,dx = \int\limits_{a}^{b}\left[\int\limits_{c}^{d}f(x,y)\,dy\right]dx$$

Furthermore, the limits of the integrals can include $x$ and $y$ as well, and
can be solved in a similar fashion.

# Polar Coordinates

$$
\begin{gathered}
    x = r\cos\varphi \\
    y = r\sin\varphi \\
    dA = rdrd\varphi \\
    \varphi \in [0, 2\pi]
\end{gathered}
$$

This allows us to transform pretty ugly looking integrals such as:

$$\int_{-2}^{2}\int_{-\sqrt{4-y^2}}^{\sqrt{4-y^2}}\sqrt{x^2+y^2}\;dxdy$$

Into much easer to solve integrals, such as:

$$\int_{0}^{2\pi}\int_{0}^{2}r^2drd\varphi$$

_Note:_ This makes integrals around a circles (specifically when its center is
on the origin) but slightly more difficult in other cases.

In the case of finding the area of a triangle, the radius will be in the form
$\frac{a}{\sin\varphi}$ or $\frac{a}{\cos\varphi}$ if the triangle is resting
on the $y$-axis or $x$-axis respectively.

In a case of integrating around a circle but its center is not at the origin,
the radius will be in the form $2b\sin\varphi$ or $2b\cos\varphi$, if the center
is offset vertically or horizontally, respectively.

# Line Integrals

A _line integral_ is an integral where the function to be integrated is
evaluated along a curve.

$$
c:\begin{cases}
    x=x(t) \\
    y=y(t) \\
    a \leq t \leq b
\end{cases}
$$

$$ds=\sqrt{x'^2(t)+y'^2(t)}dt$$
$$\int_{c} f(x,y)ds = \int_{t=a}^{t=b}f(x(t),y(t))\sqrt{x'^2(t)+y'^2(t)}dt$$
