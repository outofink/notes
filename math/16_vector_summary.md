---
title: Vector Summary
author: Moshe Krumbein
date: Spring 2021
---

# Vectors

## Vector Coordinates

$$A(a_1,a_2,a_3), \; B(b_1,b_2,b_3)$$

From $A$ to $B$:

$$\vec{AB}=\vec{(b_1-a_1.b_2-a_2,b_3-a_3)}$$

All vectors with the same coordinates are *equivalent*.

## Operations On and Between Vectors

### Adding Vectors

$$
\begin{gathered}
    \vec v = \vec{(v_1,v_2,v_3)}, \; \vec u = \vec{(u_1,u_2,u_3)} \\
    \vec v + \vec u = \vec{(v_1+u_1,v_2+u_2,v_3+u_3)} \\
\end{gathered}
$$

### Multiplication Between a Vector with a Scalar

$$
\begin{gathered}
    \alpha \in \mathbb{R}, \; \vec v= \vec{(v_1,v_2,v_3)} \\
    \alpha \cdot \vec v = \vec{(\alpha \; v_1, \alpha \; v_2, \alpha \; v_3)} \\
\end{gathered}
$$

### Scalar Multiplication Between Vectors

$$
\begin{gathered}
    \vec v = \vec{(v_1,v_2,v_3)}, \; \vec u = \vec{(u_1,u_2,u_3)} \\
    \vec v \cdot \vec u = v_1 u_1 + v_2 u_2 + v_3 u_3 \\
\end{gathered}
$$

## Uses for Scalar Multiplication

### Normal of a Vector (Length)

Given:

$$\vec v = \vec{(v_1,v_2,v_3)}$$

Its normal ($\hat v$) is defined by:

$$\frac{\vec v}{||\vec v||} = \hat v$$

Where:

$$||\vec v|| = \sqrt{v_1^2+v_2^2+v_3^2}$$

### Alternative Definition of Scalar Multiplication

$$
    \vec v \cdot \vec u = ||\vec v|| \cdot ||\vec u||
    \cdot \cos \measuredangle (\vec v, \vec u)
$$

From here, the angle between two vectors can be defined as:

$$
    \cos \measuredangle (\vec v, \vec u)
    = \frac{\vec v \cdot \vec u}{||\vec v|| \cdot ||\vec u||}
    = \hat v \cdot \hat u
$$

If $\vec v \cdot \vec u = 0$, then $\vec v \perp \vec u$ (perpendicular to each
other).

If $\cos \measuredangle (\vec v, \vec u) = 0$, then $\vec v \perp \vec u$.

And if $||\vec u|| = 0$, then $\forall \; \alpha \in \mathbb{R}: \vec v \cdot
\vec u = 0$.

Conclusion: vector zero is perpendicular to all other vectors.

#### Claim:

If $||\vec u|| = 0$, then $u_1=u_2=u_3=0$, because:

$$0 = ||\vec u||^2 = u_1^2+u_2^2+u_3^2 \implies u_1=u_2=u_3=0$$

### Plane

![Plane](plane.svg){ width=50% }

$$
\begin{gathered}
    \vec n \perp P \\
    \vec n \perp \mu_0\vec \mu \\
    \vec{(a,b,c)} \cdot \vec{(x-x_0,y-y_0,z-z_0)} = 0 \\
    a(x-x_0)+b(y-y_0)+c(z-z_0)=0 \\
    ax+by+cd=d \\
    d=ax_0+by_0+cz_0
\end{gathered}
$$

### Angle Between a Vector to a Plane

$$
\begin{gathered}
    \vec v = \vec{(v_1,v_2,v_3)}, \; P\!: ax+by+cz=d \\
    \varphi = \measuredangle(\vec v, P): \quad
    \sin \varphi = \cos \left(\frac{\pi}{2}-\varphi\right)
    = \frac{\vec n \cdot \vec v}{||\vec n|| \cdot ||\vec v||}
\end{gathered}
$$

## Parallel Vectors

If $\vec v \parallel \vec u$ then there exists a constant $c$ such that
$\vec v = c \cdot \vec u$.

### Parametric Equation of the Line $L$

![Parallel Lines](parallel.svg){ width=50% }

$$
\begin{gathered}
    L \parallel \vec v \\
    \vec{\mu_0\mu} \parallel \vec v \\
\end{gathered}
$$

Therefore, there exists a constant $t$, such that:

$$
\begin{gathered}
    \vec{\mu_0\mu} = t \vec v \\
    \vec{(x-x_0,y-y_0,z-z_0)} = t \vec{(v_1,v_2,v_3)} \\
    \\
    L:\begin{cases}
        x = x_0+tv_1 \\
        y = y_0+tv_2 \\
        z = z_0+tv_3
    \end{cases}
\end{gathered}
$$

## Applications for Gradient Vectors

$$
\vec{\mathrm{grad}f(\mu_0)} = \vec \nabla f(\mu_0) =
\vec{(f_x'(\mu_0), f_y'(\mu_0))}
$$

At extreme points:

$$\vec \nabla g(\mu) \parallel \vec \nabla g(\mu)$$

Therefore, there exists a constant $\lambda$ such that:

$$
\begin{cases}
    \vec \nabla f(\mu) = \lambda \vec \nabla g(\mu) \\
    g(x,y)=0
\end{cases}
$$
