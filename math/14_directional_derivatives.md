---
title: Directional Derivatives and Extrema
author: Moshe Krumbein
date: Spring 2021
---

# Directional Derivatives and Gradient Vectors

For multi-variable functions until now, we were able to calculate the
derivative in the $x$ or $y$ directions. Directional derivatives allow us to
find the directive of a function in any direction.

$$
L: \begin{cases}
   x=x_0 + at \\
   y=y_0 + bt
\end{cases}
$$

$$L \parallel \vec u = \vec{(a,b)}$$

$$\frac{\partial f (\mu_0)}{\partial L} = \lim\limits_{\mu \to \mu_0} \frac{f(\mu)-f(\mu_0)}{||\mu_0 \vec \mu||}$$

$$
\varphi (t) = f(x+0+at, y_0+bt) \quad \frac{\partial f(\mu_0)}{\partial L} =
\frac{\varphi ' (0)}{\sqrt{a^2+b^2}}
$$

$$
\varphi '(t) = f_x'x_t'+f_y'y_t' = af_x' +bf_y' = \vec{(f_x',f_y')}\cdot
\vec{(a,b)}
$$

$$\varphi'(0) = \vec{(f_x'(x_0,y_0),f_y'(x_0,y_0)} \cdot \vec{(a,b)}$$

$$
\frac{\partial f(\mu_0)}{\partial L} = \underbrace{\vec{(f_x'(\mu_0),f_y'(\mu_0))}}_{\vec{\mathrm{grad}f(\mu_0)}} \cdot
\frac{\vec{(a,b)}}{\sqrt{a^2+b^2}} = \vec{\mathrm{grad} f(\mu_0)}\cdot \hat u = \vec{\nabla
f(\mu_0)} \cdot \hat u
$$

## Attributes of Gradient Vectors

### 1.

$$
\frac{\partial f(\mu_0)}{\partial \vec u} = \vec{\nabla f(\mu_0)}\cdot \hat u
= \vec{||\nabla f(\mu_0)}||\cdot ||\vec u||\cdot \cos \varphi
$$

$$
\max \frac{\partial f(\mu_0)}{\partial \vec u} = ||\vec{\nabla f(\mu_0)}||
\iff \cos \varphi = 1 \iff \varphi = 0
$$

$$
\min \frac{\partial f(\mu_0)}{\partial \vec u} = -||\vec{\nabla f(\mu_0)}||
\iff \cos \varphi = -1 \iff \varphi = \pi
$$

$$
\frac{\partial f(\mu_0)}{\partial \vec u} = 0 \iff \cos \varphi = 0 \iff
\varphi = \frac{\pi}{2}
$$

The use of $||\vec{\nabla f(\mu_0)}||$ is the finding the maximal directional
derivative.

### 2.

#### Claim:

Gradient vectors is perpendicular the contour line $c=f(\mu_0).$

#### Proof:

Contour line $f(x,y) = f(\mu_0) = \text{const}$
$$\Downarrow$$
$$df(x,y) = 0$$
$$f_x'(\mu_0)dx+f_y'(\mu_0dy)=0$$

$$
\vec{(f_x'(\mu_0),f_y'(\mu_0))}\cdot \vec{(dx,dy)} =0 \implies \vec{\nabla
f(\mu_0)} \perp \vec{(dx,dy)}
$$

Suppose $y=y(x)$:

$$\vec{(dx,dy)} = (dx,y_x'(x_0)dx) = (1,y'(x_0)dx)$$

# Local extrema of multi-variable functions

Suppose $z=f(x,y)$ is differentiable at $\mu_0$ and $z, z_x, z_y, z_{xy},
z_{yz}$ are all continuous.

If an extremum exists than the directional derivative for any given
direction will be equal to $0$.

$$\frac{\partial f(\mu_0)}{\partial \vec u} = \vec{\nabla} f(\mu_0) \hat u = 0$$

For all $\hat u$: $\vec{\nabla} f(\mu_0) \perp 0$, which is only true if
$\vec{\nabla} f(\mu_0) = 0$ which means:

$$
\begin{cases}
    f_x'(\mu_0) = 0 \\
    f_y'(\mu_0) = 0
\end{cases}
$$

## Conditions

Given $z=f(x,y)$ and the coordinate $\mu_0$. Given an direction $\vec u
=\vec{(a,b)}$ at $\mu_0$:

$$z=f(x_0+at,y_0+bt) \quad (z=z(f))$$
$$z_t = z_xx_t+z_yy_t = xf_x+bf_y$$
$$z_{tt} = a(f_{xx}x_t+f_{xy}y_t)+b(f_{yx}x_t+f_{yy}y_t)$$
$$=a^2f_{xx}+2abf_{xy}+b^2f_{yy}$$
$$=b^2\left(f_{xx}\left(\frac{a}{b}\right)^2+2f_{xy}\left(\frac{a}{b}\right)+f_{yy}\right)$$
$$w=\frac{a}{b}$$
$$\Delta = b^2-4ac = f_{xy}^2(\mu_0) - f_{xx}(\mu_0) f_{yy}(\mu_0)$$
$$...$$

So when will $z_{tt}(\mu_0)>0$ (minimum) for all $w$:

$$
\begin{cases}
    f_{xx}(\mu_0)>0 \\
    \Delta < 0
\end{cases}
$$

$$\frac{\Delta}{4} < 0 : f_{xy}^2(\mu_0)-f_{xx}(\mu_0)f_{yy}(\mu_0)<0$$

Otherwise written as:

$$
\boxed{\begin{cases}
    f_{xx}(\mu_0) > 0 \\
    f_{xx}(\mu_0) f_{yy}(\mu_0) - f_{xy}^2(\mu_0) > 0
\end{cases}}
$$

And for the maximum:

$$
\boxed{\begin{cases}
    f_{xx}(\mu_0) < 0 \\
    f_{xx}(\mu_0) f_{yy}(\mu_0) - f_{xy}^2(\mu_0) > 0
\end{cases}}
$$

### Note:

If $z_{tt}(\mu_0) = 0$ we cannot find the characteristics at $\mu_0$.

If $\Delta > 0$ aka $f_{xx}(\mu_0) f_{yy}(\mu_0) - f_{xy}^2(\mu_0) < 0$
there directions such that $z_{tt}(\mu_0) < 0$ and some $z_{tt}(\mu_0) > 0$,
also known as a _saddle point_ (because it looks like a saddle).

## Summary

To find local maxima/minima of $z=f(x,y)$, first ensure that it is
differentiable at the point of inspection ($\mu_0$) and that
$z,z_x,z_y,z_{xy},z_{yz}$ are all continuous.

In order to find potential points, find that points that satisfy:

$$
\begin{cases}
    f_x = 0 \\
    f_y = 0
\end{cases}
$$

For each potential extremum ($\mu_0$):

$$
\begin{array}{c|c}
\begin{gathered}
    \text{Minimum:} \\
    \begin{cases}
        f_{xx}(\mu_0) > 0 \\
        f_{xx}(\mu_0) f_{yy}(\mu_0) - f_{xy}^2(\mu_0) > 0
    \end{cases} \\
    \text{Unknown using this method:} \\
    f_{xx}(\mu_0) = 0
\end{gathered}
&
\begin{gathered}
    \text{Maximum:} \\
    \begin{cases}
        f_{xx}(\mu_0) < 0 \\
        f_{xx}(\mu_0) f_{yy}(\mu_0) - f_{xy}^2(\mu_0) > 0
    \end{cases} \\
    \text{Saddle point:} \\
    f_{xx}(\mu_0) f_{yy}(\mu_0) - f_{xy}^2(\mu_0) < 0
\end{gathered}
\end{array}
$$

# Extrema under constraints

Given $z=f(x,y)$, if exists the condition $g(x,y)=0$:

### Explicit function constraint y=y(x)

$$z=f(x,y(x))$$

#### Example

$$f(x,y)=x^2+y^2-xy+x+y$$

Constraint:

$$y=-x-3$$
$$x^2+(x+3)^2+x(x+3)+x-x-3$$
$$=3(x^2+3x+2)$$
$$z'=3(2x+3) = 0 \implies x=-\frac{3}{2}$$
$$z''=6>0 \implies \text{Minimum} \to \min \left(-\frac{3}{2},-\frac{3}{2},-\frac{3}{4}\right)$$

### Constraint of an implicit function

Constraint:

$$g(x,y)=0$$

$$
\begin{cases}
    x=x(t) \\
    y=y(t)
\end{cases}
$$

$$z=f(x,y)=f(x(t),y(t))$$

$\mu_0$ will be a suspect point if $z_t'(\mu_0)=0$.

$$
z_t=z_xx_t+z_yy_t=\vec{(z_x,z_y)}\cdot \vec{(x_t,y_t)} = \vec \nabla f \cdot
\vec{(x_t,y_t)} \implies \vec \nabla f \perp \vec{(x_t,y_t)}
$$

$$g(x(t),y(t))$$

$$
0=g_t'=g_xx_t+g_yy_t = \vec{(g_x,g_x)}\cdot \vec{(x_t,y_t)} \implies \vec
\nabla g \perp \vec{(x_t,y_t)}
$$

$$\vec \nabla f \parallel \vec \nabla g$$

$$
\begin{cases}
    \vec \nabla f = \lambda \vec \nabla g \\
    g = 0
\end{cases}
\implies
\begin{cases}
    f_x'=\lambda g_x' \\
    f_y'=\lambda g_y'
\end{cases}
$$

## Summary

We are able to check local maxima and minima under constraint of another
function (either implicit or explicit).

With an _explicit_ constraint (any function that can easily be solved for $x$),
one can find the extrema in the same way one would for a single variable
function (because the entire function is now only in terms of $x$).

Example:

$$
\begin{gathered}
    f(x,y) = x^2+y^2 \quad y=2x \\
    f(x,y)=f(x,2x)=x^2+(2x)^2 \\
    \dots \\
\end{gathered}
$$

With an _implicit_ constraint (a function which cannot be easily solved for
$x$), potential extrema can be found using the following system of equations:

$$
\begin{cases}
    f_x' = \lambda g_x' \\
    f_y' = \lambda g_y' \\
    g = 0
\end{cases}
$$

Where $\lambda$ is the _Lagrange multiplier_ (an arbitrary constant).

For each potential extremum ($\mu$), its height is $f(\mu)$. The maximum and
minimum can be found accordingly.

_Note:_ If only one extremum is found, we cannot determine whether it is a
maximum or maximum using this method.
