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
