---
title: Multivariable Functions
author: Moshe Krumbein
date: Spring 2021
---

# Functions with two variables

$$z=f(x,y)=\frac{1}{\sqrt{25-x^2-y^2}}$$

$$\text{Dom } f = \{(x,y):x^2+y^2<25\}$$
$$\text{Im }  f = \left\{z \geq \frac{1}{5}\right\}$$

*Elevation lines* are horizontal cross-sections of the graph.

# Limits of functions with two variables

$$\lim\limits_{(x,y) \to (a,b)} f(x,y) = f(a,b)$$

For example $f(x,y) = x^2+y^2$:
$$\lim\limits_{(x,y) \to (1,2)} f(x,y)=5$$

## Calculation of the limit or proving the limit does not exist

1.

$$\lim\limits_{(x,y) \to (1,2)} \frac{\arctan(x+y-3)}{\ln(x+y-2)}$$
$$t=x+y-1$$
$$(x,y) \to (1,2) \implies t \to 1$$
$$\lim\limits_{t \to 1} \frac{\arctan(t-1)}{\ln t}$$

is $1$ using L'Hospital's rule.

2.

$$\lim\limits_{(x,y) \to (1,1)} \frac{xy-y^2}{\sqrt x - \sqrt y} = \frac{y(x-y)}{\sqrt x - \sqrt y}= y(\sqrt x + \sqrt y) = 2$$

3.

$$\lim\limits_{(x,y) \to (0,0)} \frac{x^3+y^2}{x^2+y^2}$$

We say the limit only exists if it doesn't matter what way we get to the limit.

Approach A:

$$\lim\limits_{x \to 0, y=x} \frac{x^3 + y^2}{x^2+y^2} = \frac{x^3 + x^2}{2x^2} = \frac{1}{2}$$
$$\lim\limits_{x \to 0, y=2x} \frac{x^3 + y^2}{x^2+y^2} = \frac{x^3 + 4x^2}{5x^2} = \frac{4}{5}$$

$\frac{1}{2} \neq \frac{4}{5}$, so the limit does not exist.

Approach B:

$$\lim\limits_{x \to 0, y=kx} \frac{x^3+k^2x^2}{x^2+k^2x^2} = \frac{k^2}{1+k^2}$$

The limit is dependent on $k$, and therefore does not exist.

Approach C:

The limit is dependent on the angle.

Approach D:

Find the limit of first $x$ and then $y$. Then find the limit of $y$ and then $x$.
If time limits are not equal the limit does not exist.

## So how can we prove the limit *does* exist?

### Sandwich Rule

$$\lim\limits_{(x.y) \to (0,0)} \frac{xy^3}{y^2+x^2}$$
$$\left|\frac{xy^3}{x^2+y^2}\right| \leq \left|\frac{xy^3}{y^2}\right| = |xy| =|x||y| \to 0$$

If the numerator has a higher power than the denominator, we know that the
numerator approaches zero faster than the denominator.

If the denominator is larger  on the numerator, we will see that the limit will
approach infinity.

If the powers are equal than we know that the limit will not exist.

# Continuity of functions with two variables

Function $z=f(x,y)$ is defined as continuous at $(a,b)$ if:

1. The function is defined at $(a,b)$
2. $\lim\limits_{(x,y) \to (a,b)} f(x,y)$ exists
3. $\lim\limits_{(x,y) \to (a,b)} f(x,y) = f(a,b)$

# Partial differentiation

## Partial derivative in terms of $x$

$$\frac{\partial}{\partial x} f(x_0,y_0) = f'_x(x_0,y_0) = \lim\limits_{h \to 0} \frac{f(x_0+h,y_0)-f(x_0,y_0)}{h}$$

## Partial derivative in terms of $y$

$$\frac{\partial}{\partial y} f(x_0,y_0) = f'_y(x_0,y_0) = \lim\limits_{h \to 0} \frac{f(x_0,y_0+h)-f(x_0,y_0)}{h}$$

## Calculating partial derivatives

Consider all other variables as constants and differentiate.

##  Second order partial differentiation

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

## Euler's Theorem

If $f(x,y)$ and its partial derivatives $f'_x,f'_y,f''_{xy},f''_{yx}$ are all
continuous.

# Differentiability

> *Reminder:* A function $y=f(x)$ is defined as differentiable at $x=x_0$ if:

$$\alpha = \frac{f(x)-g(x)}{x-x_0} \to 0$$

> as $x \to x_0$.

$$z=f(x,y)$$

A tangent plane is defined as $g(x,y)=ax+by+c$

## Definition

### First Definition

The tangent of the function $f(x,y)$ at the point $(x_0,y_0)$ where the relative
error ($\alpha$):

$$\alpha = \frac{f(x,y)-g(x,y)}{\sqrt{(x-x_0)^2+(y-y_0)^2}}$$

Given:

$$f(x_0,y_0) = g(x_0,y_0)$$
$$\alpha \to 0$$

### Second Definition

A function is called differentiable if at the point exists the tangent plane.

## Rule 1

If the function $f(x,y)$ is differentiable at $(x_0,y_0)$, then the
tangent plane is:

$$g(x,y)=f(x_0,y_0)+f'_x(x_0,y_0)(x-x_0)+f'_y(x_0,y_0)(y-y_0)$$

Simplified is:

$$g(x,y) = xa+by+f(x_0,y_0)-ax_0-by_0$$

The limit exists if we get the same answer no matter the method.

## Rule 2

If a function $f(x,y)$ is differentiable at $(x_0,y_0)$ then it is also
continuous at that point.

# Chain rule for multi-variable functions

## Function with only one variable

$$f(g(x))' = f'(gx))g'(x)$$

If we define $t=g(x)$:
$$f(g(x))' = f'_tt'_x$$

## Function with two variables

### Case 1
$$z=f(u,v), \quad u=u(x,y), v=v(x,y)$$

One the one hand:
$$dz=z'_xdx+z'_ydy$$
On the other hand:
$$dz=z_udu+z_vdv=z_u(u_xdx+u_ydy)+z_v(v_xdx+v_ydy)$$
$$=(z_u u_x + z_v u_x)dx+(z_u u_y +z_v v_y)dy$$

$$z'_x = z_u u_x + z_v u_x = \frac{\partial z}{\partial u}\cdot\frac{\partial
u}{\partial x} + \frac{\partial z}{\partial v}\cdot\frac{\partial v}{\partial x}$$
$$z'_y = z_u u_y + z_u v_y = \frac{\partial z}{\partial u}\cdot\frac{\partial
u}{\partial y} + \frac{\partial z}{\partial v}\cdot\frac{\partial v}{\partial y}$$

### Case 2

$$z=z(x,y), \quad x=x(t), y=y(t)$$
$$dz=z'_x dx + z'_y dy$$
$$=z'_xx'_tdt+z'_yy'_tdt = (z_xx_t+z_yy_t)dt$$

$$z'_t=z'_xx'_t+z'_yy'_t$$
$$\frac{\partial z}{\partial t} = \frac{\partial z}{\partial x}\cdot\frac{\partial
x}{\partial t} + \frac{\partial z}{\partial y}\cdot\frac{\partial y}{\partial t}$$

### Case 3

$$z=z(t), \quad t=t(x,y)$$
$$z'_xdx+z'_ydy=dz=z'_tdx$$
$$=z'_t(t'_xdx+t'_ydy)$$
$$=z'_tt'_xdx+z'_tt'_ydy$$
$$
\begin{gathered}
        z'_x = z'_tt'_x \\
        z'_y=z'_tt'_y \\
        \frac{\partial z}{\partial x} = \frac{\partial z}{\partial t}\cdot \frac{\partial t}{\partial x} \\
        \frac{\partial z}{\partial y} = \frac{\partial z}{\partial t}\cdot \frac{\partial t}{\partial y} \\
\end{gathered}
$$

## Examples

1.
$$z=u^2v, u=x\sin y, v= y\cos x$$
Find $z'_x, z'_y$.

First way:
$$z=x^2\sin^2(y)y\cos x = x^2\cos(x)y\sin^2(y)$$
$$z'_x=(2x\cos x -x^2\sin x)y\sin^2x$$
$$z'_y=(\sin^2y+2y\sin y \cos y) x^2\cos x$$

Second way:

2.
$$z=x^2y^3+f\left(\frac{x^2}{y}\right)$$

$$z'_x=2xy^3+f'_tt'_x$$
$$=2xy^3+f'_t \cdot \frac{2x}{y}$$

# Vectors

## Geometric definition

Line segment with direction.

$\vec{AB}$, where $A$ is the starting point and $B$ in the end.

## Algebraic definition

On $\mathbb{R}^2$: $\vec{AB} = \vec{(x_B-x_A,y_B-y_A)}$

On $\mathbb{R}^3$: $\vec{AB} = \vec{(x_B-x_A,y_B-y_A,z_B-z_A)}$

## Examples

1. $\mathbb{R}^2: A(1,2), B(0,-2)$

    $\vec{AB} = \vec{(0-1,-2-2)}=\vec{(-1,-4)}$

2. $\mathbb{R}^3:A(1,2,3),B(2,1,4)$

    $\vec{AB}=\vec{(2-1,1-2,4-3)}=\vec{(1,-1,1)}$

    $C(-1,2,5), D(0,1,6)$

    $\vec{CD} = \vec{(0-(-1),1-2,6-5)} = \vec{(1,-1,1)}$

    $\vec{AB} \equiv \vec{CD} \quad (\vec{AB} = \vec{CD})$

## Operations between vectors

### Scalar multiplication

Given $\vec{u} = \vec{(u_1,u_2)}\;(\mathbb{R}_2)$ or $\vec{v}=\vec{(v_1,v_2,v_3)}\;(\mathbb{R}_3)$:

For $\alpha,\beta \in \mathbb{R}$, then:

$\beta \vec{u} = \vec{(\beta u_1, \beta u_2)}$

$\alpha \vec{v}=\vec{(\alpha v_1, \alpha v_2, \alpha v_3)}$

### Sum

$\mathbb{R}^2: \vec{v}=\vec{(v_1,v_2)},\quad\vec{u}=\vec{(u_1,u_2)} \implies \vec{v}+ \vec{u} = \vec{(v_1+u_1,v_2+u_2)}$

$\mathbb{R}^3: \vec{v}=\vec{(v_1,v_2,v_3)},\quad\vec{u}=\vec{(u_1,u_2,u_3)} \implies \vec{v} + \vec{u} = \vec{(v_1+u_1,v_2+u_2, v_3+u_3)}$

### Linear Combination

Given a group of $n$ vectors ($\vec{v_1}, \cdots, \vec{v_n}$) and a group of $n$ scalars ($\alpha_1,\cdots, \alpha_n$).

The vectors $\alpha_1\vec{v_1}, \alpha_2\vec{v_2},\cdots, \alpha_n \vec{v_n}$ is
called the linear combination of $n$ vectors.

## Standard vectors

$\vec{(1,2,3)} = 1 \cdot \vec{(1,0,0)} + 2 \cdot \vec{(0,1,0)} + 3 \cdot \vec{(0,0,1)}$

$=1\vec i + 2\vec j + 3 \vec k$

$$\vec{(x,y,z)} = x \vec i + y \vec j + z \vec k$$

## Scalar multiplication between vectors

A function that take each real vector pair ($\vec v, \vec u$) is called scalar multiplication if
there exists the following four axioms:

1. Similarity: $\vec v \cdot \vec u = \vec u \cdot \vec v$
2. Homogamy: $(\alpha \vec v) \cdot \vec u = \alpha (\vec v \cdot \vec u)$
3. Additivity: $(\vec v_1 + \vec v_2) \cdot \vec u = \vec v_1 \cdot \vec u + \vec v_2 \cdot
   \vec u$

(2 and 3 are also called linearity)

4. Positivity; $\vec v \cdot \vec v \geq 0$

Then:

$\vec v = \vec{(v_1,v_2,v_3)}\quad \vec u =\vec{(u_1,u_2,u_3)}$

Where $u_i, v_i \in \mathbb{R}$, then;

$\vec v \cdot \vec u = v_1u_1 + v_2u_2+v_3u_3$

$||\vec v|| = \sqrt{\vec v^2}$

## Angle between  vectors

### Cosine rule

$$b^2=a^2+c^2-2ac\cos \beta$$
$$||\vec u - \vec v||^2 = ||\vec v||^2+||\vec u||^2 - 2 \cdot ||\vec v|| \cdot
||\vec u|| \cdot \cos \beta$$

Example:

$$\vec v = \vec{(v_1,v_2,v_3)}\quad \vec u =\vec{(u_1,u_2,u_3)}$$
$$||\vec u -\vec v||^2 = ||(u_1-v_1),(u_2-v_2),(u_3-v_3)||$$
$$=u_1^2+v_1^2-2u_1v_1+u_2^2+v_2^2-2u_2v_2+u_3^2+v_3^2-2u_3v_3$$
$$=||\vec u||^2+||\vec v||^2-2 \cdot \vec u \cdot \vec v$$
$$\boxed{\cos \varphi = \frac{\vec u \cdot \vec v}{||\vec u|| \cdot ||\vec v||}}$$

### Alternative definition of scalar multiplication

$$\vec v \cdot \vec u = ||\vec v|| \cdot ||\vec u|| \cdot \cos \varphi$$

If $\varphi = \frac{\pi}{2}$ then $\cos \varphi = 0$ and therefore $\vec v
\cdot \vec u$.

If $\vec v \cdot \vec u = 0$ then $\vec v \perp \vec u$

Given plane $p$ and vector $\vec n$; $\vec n \perp p$ is called the normal
vector.

If $\vec n \perp p$ then $\vec n$ is perpendicular to every vector on the
plane.

### Angle between vector and a plane

$$\boxed{\sin \varphi = \cos (90 \text{\textdegree} - \varphi) = \frac{\vec n \cdot \vec v}{||\vec n|| \cdot ||\vec v||}}$$
