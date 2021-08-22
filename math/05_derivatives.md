---
title: Derivatives
date: Fall 2020
author: Moshe Krumbein
---

# What are they good for?

For finding the slope at a single point.
$$f(x)=y$$
$$ f'(x) = \lim\limits\_{h \to 0} \frac{f(x_0+h)-f(x_0)}{h}$$

# Identities

$$(\sin x)' = \cos x$$
$$(\ln x)' = \frac{1}{x}$$
$$(x^2)'= 2x$$
$$(\sqrt{x})' =\frac{1}{2\sqrt{x}}$$
$$\left(\frac{1}{x}\right)' =-\frac{1}{x^2}$$
$$(x^3)' = 3x^2$$
$$(e^x)' = e^x$$
$$(x^n)'=nx^{n-1}$$
$$(a^x)' = a^x \cdot \ln a$$
$$(\log_a x)' = \frac{1}{x \ln a}$$

# Differentially

If $\lim\limits_{h \to a^+} \frac{y_1 - y_0}{h} \neq \lim\limits_{h \to a^-}
\frac{y_1 - y_0}{h}$, then the function is not differentiable at point $a$.

# Rules

$$(f(x) \pm g(x))' = f'(x) \pm g'(x) \tag{1}$$
$$(kf(x))' = kf'(x) \tag{2}$$
$$(f(x) \cdot g(x))' = f'(x)g(x) + f(x)g'(x) \tag{3}$$
$$(f(g(x)))' = f'(g(x))g'(x) \tag{4}$$
$$\left(\frac{f(x)}{g(x)}\right)' = \frac{f'(x)g(x)-f(x)g'(x)}{g(x)^2} \tag{5}$$

# Derivative of an inverse function

$$f(f^{-1}(x)) = x$$
$$(f(f^{-1}(x)))' = (x)' = 1$$
$$f'(f'(x)) \cdot (f'(x))' = 1$$
$$(f^{-1}(x))' = \frac{1}{f'(f^{-1}(x))}$$

# Derivative of powers

$$\left(f(x)^{g(x)}\right)' = f(x)^{g(x)} \cdot \left(g'(x)\ln(f(x)) + g(x) \cdot \frac{f'(x)}{f(x)}\right)$$

# L'H$\text{\^{o}}$pital's Rule

Given $f(x), g(x)$ are differentiable and $f(a) = 0, g(a) = 0$, then:

$$\lim\limits_{x \to a} \frac{f(x)}{g(x)} = \lim\limits_{x \to a} \frac{f'(x)}{g'(x)}$$

This is also true where $\lim\limits_{x \to a} f(x) = + \infty, \lim\limits_{x \to a} g(x) = +\infty$.
