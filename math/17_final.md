---
title: Final C2 Summary
author: Moshe Krumbein
date: Spring 2021
toc: yes
---

# Taylor Series and Maclaurin Series

Maclaurin series of trigonometric functions and $e^x$ can be used to solve
limits.

## Using the Maclaurin Series for Calculating Limits

#### Example:

$$\lim\limits_{x \to 0} \frac{\cos x -1 }{x^2} = \left(\frac{0}{0}\right)$$

$$\cos x = 1 +\frac{x^2}{2} + o(x^2)$$

$o(x^n)$, also known as _little o notation_, represents a set of terms with a
powers larger than $n$, such that:
$$\lim\limits_{x \to 0} \frac{o(x^n)}{x^n} = 0$$

Therefore:
$$\lim\limits_{x \to 0} \frac{\cos x -1 }{x^2} = \lim\limits_{x \to 0} \frac{1-\frac{x^2}{2}-1+o(x^2)}{x^2} = -\frac{1}{2}$$

# Domain and Contour Lines of Functions with Two Variables

Given $z=f(x,y)$, the graph of the contour lines can be found by defining
$f(x,y)=c$ and graphing that function, where $c$ is either given or we can find it
given points $(a,b)$ by defining $c=f(a,b)$.

#### Example:

$$z=f(x,y)=\frac{1}{\sqrt{25-x^2-y^2}}$$

$$\text{Dom } f = \{(x,y):x^2+y^2<25\}$$
$$\text{Im }  f = \left\{z \geq \frac{1}{5}\right\}$$

# Limits of Functions with Two Variables

$$\lim\limits_{(x,y) \to (a,b)} f(x,y) = f(a,b)$$

#### Example:

$$f(x,y) = x^2+y^2$$
$$\lim\limits_{(x,y) \to (1,2)} f(x,y)=5$$

## Finding the Limit or Proving the Limit Does Not Exist

#### 1.

Using $t$-substitution:
$$\lim\limits_{(x,y) \to (1,2)} \frac{\arctan(x+y-3)}{\ln(x+y-2)}$$
$$t=x+y-1$$
$$(x,y) \to (1,2) \implies t \to 1$$
$$\lim\limits_{t \to 1} \frac{\arctan(t-1)}{\ln t} \overset{\mathrm{LH}}{=} 1$$

#### 2.

Completing the square:
$$\lim\limits_{(x,y) \to (1,1)} \frac{xy-y^2}{\sqrt x - \sqrt y} = \frac{y(x-y)}{\sqrt x - \sqrt y}= y(\sqrt x + \sqrt y) = 2$$

#### 3.

Unclear:
$$\lim\limits_{(x,y) \to (0,0)} \frac{x^3+y^2}{x^2+y^2}$$

We say the limit only exists if it doesn't matter what way we get to the limit.

#### Approach A:

$$\lim\limits_{\substack{x \to 0\\ y=x}} \frac{x^3 + y^2}{x^2+y^2} = \frac{x^3 + x^2}{2x^2} = \frac{1}{2}$$
$$\lim\limits_{\substack{x \to 0\\ y=2x}} \frac{x^3 + y^2}{x^2+y^2} = \frac{x^3 + 4x^2}{5x^2} = \frac{4}{5}$$

$\frac{1}{2} \neq \frac{4}{5}$, so the limit does not exist.

#### Approach B:

$$\lim\limits_{\substack{x \to 0\\ y=kx}} \frac{x^3+k^2x^2}{x^2+k^2x^2} = \frac{k^2}{1+k^2}$$

The limit is dependent on $k$, and therefore does not exist.

#### Approach C:

The limit is dependent on the angle, where:

$$
\begin{gathered}
    x=r\cos \varphi \\
    y=r\sin \varphi
\end{gathered}
$$

#### Approach D:

Find the limit of first $x$ and then $y$. Then find the limit of $y$ and then $x$.
If the limits are not equal the limit does not exist.

## So how can we prove the limit _does_ exist?

### Sandwich Rule

$$\lim\limits_{(x.y) \to (0,0)} \frac{xy^3}{y^2+x^2}$$
$$\left|\frac{xy^3}{x^2+y^2}\right| \leq \left|\frac{xy^3}{y^2}\right| = |xy| =|x||y| \to 0$$

If the numerator has a higher power than the denominator, we know that the
numerator approaches zero faster than the denominator.

If the denominator is larger on the numerator, we will see that the limit will
approach infinity.

If the powers are equal than we know that the limit will not exist.

# Continuity of Functions with Two Variables

A function $z=f(x,y)$ is defined as continuous at $(a,b)$ if:

1. The function is defined at $(a,b)$
2. $\lim\limits_{(x,y) \to (a,b)} f(x,y)$ exists
3. $\lim\limits_{(x,y) \to (a,b)} f(x,y) = f(a,b)$

# Partial Differentiation

## Partial Derivative in Terms of $x$

$$\frac{\partial}{\partial x} f(x_0,y_0) = f'_x(x_0,y_0) = \lim\limits_{h \to 0} \frac{f(x_0+h,y_0)-f(x_0,y_0)}{h}$$

## Partial Derivative in Terms of $y$

$$\frac{\partial}{\partial y} f(x_0,y_0) = f'_y(x_0,y_0) = \lim\limits_{h \to 0} \frac{f(x_0,y_0+h)-f(x_0,y_0)}{h}$$

## Calculating Partial Derivatives

Consider all other variables as constants and differentiate.

## Second Order Partial Differentiation

#### Example:

$$
\begin{gathered}
    f(x,y) = x^3y^2+x^2y -xy^3 \\
    f'_x(x,y) = 3x^2y^2+2xy-y^3 \\
    f'_y(x,y) = 2x^3+x^2-3xy^2 \\
    \\
    f''_{xy}(x,y) = 6x^2y - 6xy\\
    f''_{yx}(x,y) = 6x^2y - 6xy\\
    \\
    f''_{xy} = f''_{yx}
\end{gathered}
$$

## Differentiability of Functions with Two Variables

A function is differentiable at a point $(x_0,y_0)$ when:

$$\lim\limits_{(x,y) \to (x_0,y_0)} \alpha = \frac{f(x,y)-g(x,y)}{\sqrt{(x-x_0)^2+(y-y_0)^2}} = 0$$

Where:
$$g(x,y)=f(x_0,y_0)+f'_x(x_0,y_0)(x-x_0)+f'_y(x_0,y_0)(y-y_0)$$

In order to solve when $(x_0,y_0) \neq (0,0)$, the following substitution is
done:

$$
\begin{gathered}
    u = x - x_0 \\
    v = y - y_0
\end{gathered}
$$

Producing:
$$\lim\limits_{(u,v) \to (0,0)} \alpha = \frac{f(u+x_0,v+y_0)-g(u+x_0,v+y_0)}{\sqrt{u^2+v^2}} = 0$$

#### Note:

If a function $f(x,y)$ is differentiable at $(x_0,y_0)$, then it is also
continuous at that point.

# Linear Approximation with Two Unknowns

Similar to testing differentiability, we can use $g$ in order to approximate a
harder to evaluation function $f$.

Where $(x_0,y_0)$ are easy to solve and $(x,y)$ are the desired values:
$$f(x,y) \approx g(x,y) = f(x_0,y_0) + f_x(x_0,y_0)(x-x_0) + f_y(x_,y_0)(y-y_0)$$

#### Example:

$$
\begin{gathered}
    \arctan\left(\frac{1.01}{0.98}\right) \\
    \\
    f(x,y) = \arctan\left(\frac{x}{y}\right) \\
    g(x,y) = f(1,1) + f_x(1,1)(x-1)+f_y(1,1)(y-1) \\
    = \frac{\pi}{4}+\frac{1}{2}(x-1)-\frac{1}{2}(y-1) = \frac{x-y}{2}+\frac{\pi}{4} \\
    f(1.01,0.98) \approx g(1.01,0.98) = \frac{0.03}{2}+\frac{\pi}{4}
\end{gathered}
$$

# Chain Rule for Multi-Variable Functions

## Functions with Only One Variable

$$f(g(x))' = f'(g(x))g'(x)$$

If we define $t=g(x)$:
$$f(g(x))' = f_t t_x$$

## Functions With Two Variables

#### Case 1:

$$z=f(u,v), \quad u=u(x,y), v=v(x,y)$$

$$dz=z_xdx+z_ydy$$
$$z_x = z_u u_x + z_v u_x$$
$$z_y = z_u u_y + z_u v_y$$

#### Case 2:

$$z=z(x,y), \quad x=x(t), y=y(t)$$
$$dz=z_x dx + z_y dy$$
$$z_t=z_xx_t+z_yy_t$$

#### Case 3:

$$z=z(t), \quad t=t(x,y)$$
$$z_xdx+z_ydy=dz=z_tdx$$

$$
\begin{gathered}
        z_x=z_tt_x \\
        z_y=z_tt_y \\
\end{gathered}
$$

# Directional Derivatives and Gradient Vectors

For multi-variable functions until now, we were able to calculate the
derivative in the $x$ or $y$ directions. Directional derivatives allow us to
find the directive of a function in any direction.

Given the function $f(x,y)$, to find the directional derivative at point
$\mu_0$ in the direction $\vec u = \vec{(a,b)}$:

$$
    \frac{\partial f(\mu_0)}{\partial L}
    = \underbrace{\vec{(f_x'(\mu_0),f_y'(\mu_0))}}_{\vec{\mathrm{grad}} f(\mu_0)}
        \cdot
    \frac{\vec{(a,b)}}{\sqrt{a^2+b^2}}
    = \vec{\mathrm{grad}} f(\mu_0) \cdot \hat u
    = \vec \nabla f(\mu_0) \cdot \hat u
$$

## Attributes of Gradient Vectors

$$
\frac{\partial f(\mu_0)}{\partial \vec u} = \vec\nabla f(\mu_0)\cdot \hat u
= \vec{||\nabla f(\mu_0)}||\cdot ||\vec u||\cdot \cos \varphi
$$

$$
\max \frac{\partial f(\mu_0)}{\partial \vec u} = ||\vec\nabla f(\mu_0)||
\iff \cos \varphi = 1 \iff \varphi = 0
$$

$$
\min \frac{\partial f(\mu_0)}{\partial \vec u} = -||\vec\nabla f(\mu_0)||
\iff \cos \varphi = -1 \iff \varphi = \pi
$$

$$
\frac{\partial f(\mu_0)}{\partial \vec u} = 0 \iff \cos \varphi = 0 \iff
\varphi = \frac{\pi}{2}
$$

The use of $||\vec\nabla f(\mu_0)||$ is the finding the maximal directional
derivative.

#### Note:

Gradient vectors are perpendicular to the contour line $c=f(\mu_0).$

# Local Extrema of Multi-Variable Functions

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

## Finding Extrema under Constraints

We are able to check local maxima and minima under constraint of another
function $g$ (either implicit or explicit).

With an _explicit_ constraint (any function that can easily be solved for $x$),
one can find the extrema in the same way one would for a single variable
function (because the entire function is now only in terms of $x$).

#### Example:

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
    \vec \nabla f = \lambda \vec \nabla g \\
    g = 0
\end{cases}
\implies
\begin{cases}
    f_x'=\lambda g_x' \\
    f_y'=\lambda g_y' \\
    g = 0
\end{cases}
$$

Where $\lambda$ is the _Lagrange multiplier_ (an arbitrary constant).

For each potential extremum ($\mu$), its height is $f(\mu)$. The maximum and
minimum can be found accordingly.

#### Note:

If only one extremum is found, we cannot determine whether it is a
maximum or maximum using this method.

# Advanced Integrals

## Double Integrals

$$\iint\limits_D f(x,y)\,dx\,dy = \iint\limits_D f(x,y)\,dA$$
Where $dA$ is the area.

In essence, a double integral is the integral in terms of $y$ and then in term
of $x$ or visa versa.

For example:
$$\int\limits_{a}^{b}\int\limits_{c}^{d}f(x,y)\,dy\,dx = \int\limits_{a}^{b}\left[\int\limits_{c}^{d}f(x,y)\,dy\right]dx$$

Furthermore, the limits of the integrals can include $x$ and $y$ as well, and
can be solved in a similar fashion.

## Polar Coordinates

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

into much easer to solve integrals, such as:

$$\int_{0}^{2\pi}\int_{0}^{2}r^2drd\varphi$$

#### Note:

This makes integrals around a circles (specifically when its center is
on the origin) but slightly more difficult in other cases.

In the case of finding the area of a triangle, the radius will be in the form
$\frac{a}{\sin\varphi}$ or $\frac{a}{\cos\varphi}$ if the triangle is resting
on the $y$-axis or $x$-axis respectively.

In a case of integrating around a circle but its center is not at the origin,
the radius will be in the form $2r\sin\varphi$ or $2r\cos\varphi$, if the center
is offset vertically or horizontally, respectively.

## Line Integrals

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

# Vectors

## Vector Coordinates

$$A(a_1,a_2,a_3), \; B(b_1,b_2,b_3)$$

From $A$ to $B$:
$$\vec{AB}=\vec{(b_1-a_1.b_2-a_2,b_3-a_3)}$$

All vectors with the same coordinates are _equivalent_.

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

If $\vec v \cdot \vec u = 0$, then $\vec v \perp \vec u$ (are perpendicular to each
other).

If $\cos \measuredangle (\vec v, \vec u) = 0$, then $\vec v \perp \vec u$.

And if $||\vec u|| = 0$, then $\forall \; \alpha \in \mathbb{R}: \vec v \cdot
\vec u = 0$.

#### Conclusion:

vector zero is perpendicular to all other vectors.

#### Claim:

If $||\vec u|| = 0$, then $u_1=u_2=u_3=0$, because:

$$0 = ||\vec u||^2 = u_1^2+u_2^2+u_3^2 \implies u_1=u_2=u_3=0$$

### Angle Between a Vector to a Plane

![Plane](plane.svg){ width=50% }

$$
\begin{gathered}
    \vec n \perp P, \quad
    \vec n \perp \mu_0\vec \mu \\
    \vec{(a,b,c)} \cdot \vec{(x-x_0,y-y_0,z-z_0)} = 0 \\
    a(x-x_0)+b(y-y_0)+c(z-z_0)=0 \\
    ax+by+cd=d \\
    d=ax_0+by_0+cz_0
\end{gathered}
$$

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
    L \parallel \vec v, \quad
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
