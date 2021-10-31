---
title: Linear 3
author: Moshe Krumbein - 209133123
date: Linear Algebra 1
header-includes: |
---

1.

$$
\vec u_1 = \begin{bmatrix}
1\\3\\-1\\4
\end{bmatrix}, \vec u_2 = \begin{bmatrix}
-5\\9\\15\\-4
\end{bmatrix}, \vec u_3 = \begin{bmatrix}
2\\0\\4\\-4
\end{bmatrix}, \vec u_4 = \begin{bmatrix}
3\\6\\0\\6
\end{bmatrix}
$$

$$
\left[
\begin{array}{cccc|c}
1 & -5 & 2 & 3 & b_1 \\
3 & 9 & 0 & 6 & b_2\\
-1 & 15 & 4  & 0 & b_3\\
4 & -4 & -4 & 6 & b_4
\end{array}
\right]
\begin{array}{c}
R_2 \to R_2 - 3R_1 \\
R_3 \to R_3 + 4R_1 \\
R_4 \to R_4 - 4R_1
\end{array}
$$

$$
\left[
\begin{array}{cccc|c}
1 & -5 & 2 & 3 & b_1 \\
0 & 24 & -6 & -3 & b_2 -3b_1\\
0 & 10 & 6  & 3 & b_3 + b_1\\
0 & 16 & -12 & -6 & b_4 -4 b_1
\end{array}\right]
\begin{array}{c}
~\\
R_2 \to R_2 \cdot \frac{1}{24} \\
~\\
~\\
\end{array}  \to \quad
\left[
\begin{array}{cccc|c}
1 & -5 & 2 & 3 & b_1 \\
0 & 1 & -\frac{1}{4} & -\frac{1}{8} & \frac{b_2 -3b_1}{24}\\
0 & 10 & 6  & 3 & b_3 + b_1\\
0 & 16 & -12 & -6 & b_4 -4 b_1
\end{array}\right]
\begin{array}{c}
~\\
~\\
R_3-10R_2 \\
R_4-16R_2 \\
\end{array}
$$

$$
\left[
\begin{array}{cccc|c}
1 & -5 & 2 & 3 & b_1 \\
0 & 1 & -\frac{1}{4} & -\frac{1}{8} & \frac{b_2 -3b_1}{24}\\
0 & 0 & \frac{17}{2} & \frac{17}{4} & b_3 + b_1 -10\left(\frac{b_2 -3b_1}{24}\right)\\
0 & 0 & -8 & -4 & b_4 -4 b_1 -16\left(\frac{b_2 -3b_1}{24}\right)
\end{array}\right]
\begin{array}{c}
~\\
~\\
R_3 \cdot \frac{2}{17} \\
~\\
\end{array} \to \quad
\left[
\begin{array}{cccc|c}
1 & -5 & 2 & 3 & b_1 \\
0 & 1 & -\frac{1}{4} & -\frac{1}{8} & \frac{b_2 -3b_1}{24}\\
0 & 0 & 1 & \frac{1}{2} & \frac{2}{17} \left(b_3 + b_1 -10\left(\frac{b_2 -3b_1}{24}\right)\right)\\
0 & 0 & -8 & -4 & b_4 -4 b_1 -16\left(\frac{b_2 -3b_1}{24}\right)
\end{array}\right]
\begin{array}{c}
~\\
~\\
~\\
R_4 + 8 R_3 \\
\end{array}
$$

$$
\left[
\begin{array}{cccc|c}
1 & -5 & 2 & 3 & b_1 \\
0 & 1 & -\frac{1}{4} & -\frac{1}{8} & \frac{b_2 -3b_1}{24}\\
0 & 0 & 1 & \frac{1}{2} & \frac{2}{17} \left(b_3 + b_1 -10\left(\frac{b_2 -3b_1}{24}\right)\right)\\
0 & 0 & 0 & 0 & b_4 -4 b_1 -16\left(\frac{b_2 -3b_1}{24}\right) + 8 \left(\frac{2}{17} \left(b_3 + b_1 -10\left(\frac{b_2 -3b_1}{24}\right)\right)\right)
\end{array}\right]
$$

$$
b_4 -4 b_1 -16\left(\frac{b_2 -3b_1}{24}\right) + 8 \left(\frac{2}{17} \left(b_3 + b_1 -10\left(\frac{b_2 -3b_1}{24}\right)\right)\right) = 0 \\
b_4-4b_1 -\frac{2}{3}b_2+2b_1+\frac{16}{17}b_3+\frac{16}{17}b_1-\frac{20}{51}b_2+\frac{20}{17}b_1=0 \\
b_1\left(-4+2+\frac{16}{17}+\frac{20}{17}\right)+b_2\left(-\frac{2}{3}-\frac{20}{51}\right)+\frac{16}{17}b_3+b_4 = 0 \\
\frac{2}{17}b_1-\frac{18}{17}b_2+\frac{16}{17}b_3+b_4=0 \\
\boxed{\operatorname{sp}\{\vec u_1, \vec u _2, \vec u_3, \vec u_4\}=\left\{\begin{bmatrix}
b_1\\b_2\\b_3\\
-\frac{2}{17}b_1+\frac{18}{17}b_2-\frac{16}{17}b_3
\end{bmatrix} \mid b_1,b_2,b_3 \in \mathbb{R}
\right\}}
$$

2.

$$
W_1:
\left[
\begin{array}{cc|c}
1 & 1 \over 2 & b_1 \\
0 & 1 & b_2 \\
-1 & -8 \over 3 & b_3
\end{array}
\right]
\begin{array}{c}
~\\
~\\
R_3 + R_1\\
\end{array} \to \quad
\left[\begin{array}{cc|c}
1 & 1 \over 2 & b_1 \\
0 & 1 & b_2 \\
0 & -13 \over 6 & b_3+b_1
\end{array}\right]
\begin{array}{c}
~\\
~\\
R_3 + \frac{13}{6}R_2\\
\end{array} \to \quad
\left[\begin{array}{cc|c}
1 & 1 \over 2 & b_1 \\
& 1 & b_2 \\
0 & 0 & b_3+b_1  + \frac{13}{6}b_2
\end{array}\right]
$$

$$
sp\{W_1\} = \left\{\begin{bmatrix}
b_1\\b_2\\-b_1-\frac{13}{6}b_2
\end{bmatrix} \mid b_1,b_2\in \mathbb{R}\right\}
$$

$$
W_2: \\
\left[\begin{array}{cc|c}
3 & -2 & b_1 \\
6 & 0 & b_2 \\
-16 & 2 & b_3
\end{array}
\right]
\begin{array}{c}
R_1 \cdot \frac{1}{3} \\
~ \\
~ \\
\end{array} \to \quad
\left[
\begin{array}{cc|c}
1 & -2 \over 3 & b_1 \over 3\\
6 & 0 & b_2 \\
-16 & 2 & b_3
\end{array}
\right]
\begin{array}{c}
~\\
R_2 - 6R_1\\
R_3 + 16R_1\\
\end{array} \to \quad \left[\begin{array}{cc|c}
1 & -2 \over 3 & b_1 \over 3\\
0 & 4 & b_2 - 2b_1 \\
0 & -26 \over 3 & b_3 + \frac{16}{3}b_1
\end{array}\right]
\begin{array}{c}
~\\
~\\
R_3 + \frac{13}{6}R_2\\
\end{array}
$$

$$
\left[\begin{array}{cc|c}
1 & -2 \over 3 & b_1 \over 3\\
0 & 4 & b_2 - 2b_1 \\
0 & 0 & b_3 + \frac{16}{3} b_1 + \frac{13}{6}(b_2-2b_1)
\end{array}\right] \to \quad
\begin{gathered}
b_3 + \frac{16}{3}b_1 + \frac{13}{6}b_2 - \frac{13}{3}b_1 = 0 \to \\
b_3+b_1+\frac{13}{6}b_2 = 0
\end{gathered}
$$

$$
sp\{W_2\} = \left\{\begin{bmatrix}
b_1\\b_2\\-b_1-\frac{13}{6}b_2
\end{bmatrix} \mid b_1,b_2\in \mathbb{R}\right\}
$$

$$
W_3: \\
\left[\begin{array}{ccc|c}
1 & 1 \over 2 & 0 & b_1\\
0 & 1 & -2 & b_2\\
-1 & -8 \over 3 & 1 & b_3
\end{array}\right]
\begin{array}{c}
~\\
~\\
R_3 + R_1\\
\end{array} \to \quad \left[\begin{array}{ccc|c}
1 & 1 \over 2 & 0 & b_1\\
0 & 1 & -2 & b_2\\
0 & -13 \over 6 & 1 & b_3 + b_1
\end{array}\right]
\begin{array}{c}
~\\
~\\
R_3+\frac{6}{13}R_2\\
\end{array} \to \quad \left[\begin{array}{ccc|c}
1 & 1 \over 2 & 0 & b_1\\
0 & 1 & -2 & b_2\\
0 & 0 & 1 \over 13 & b_3 + b_1 + \frac{6}{13}b_2
\end{array}\right]
$$

$$
sp\{W_3\} = \left\{\begin{bmatrix}
b_1\\b_2\\b_3
\end{bmatrix} \mid b_1,b_2,b_3\in \mathbb{R}\right\}
$$

$$
W_4:
\left[\begin{array}{ccc|c}
3 & -2 & 1 & b_1 \\
6 & 0 & 6 & b_2 \\
-16 & 2 & -14 & b_3
\end{array}\right]
\begin{array}{c}
R_1 \cdot \frac{1}{3}\\
~\\
~\\
\end{array} \to \quad \left[\begin{array}{ccc|c}
1 & -2 \over 3 & 1 \over 3 & b_1 \over 3 \\
6 & 0 & 6 & b_2 \\
-16 & 2 & -14 & b_3
\end{array}\right]
\begin{array}{c}
~\\
R_2-6R_1\\
R_3+16R_1\\
\end{array} \to \quad \left[\begin{array}{ccc|c}
1 & -2 \over 3 & 1 \over 3 & b_1 \over 3 \\
0 & 4 & 4 & b_2 - 2b_2 \\
0 & 2 & -26 \over 3 & b_3 + \frac{16}{3}b_1
\end{array}\right]
\begin{array}{c}
~\\
~\\
R_3-\frac{1}{2}R_2\\
\end{array}
$$

$$
\left[\begin{array}{ccc|c}
1 & -2 \over 3 & 1 \over 3 & b_1 \over 3 \\
0 & 4 & 4 & b_2 - 2b_2 \\
0 & 0 & -32 \over 3 & b_3 + \frac{16}{3}b_1
\end{array}\right] \to \quad sp\{W_4\} = \left\{\begin{bmatrix}
b_1\\b_2\\b_3
\end{bmatrix} \mid b_1,b_2,b_3\in \mathbb{R}\right\}
$$

$$
\boxed{W_1 = W_2,\quad W_3=W_4}
$$

3a.

$$
\begin{bmatrix}
5&2
\end{bmatrix}
\begin{bmatrix}
1&-3\\-5&2
\end{bmatrix} +
\begin{bmatrix}
5&2
\end{bmatrix}\left(
\begin{bmatrix}
-4&-1&0\\
0&2&11
\end{bmatrix}
\begin{bmatrix}
3&-3\\
0&2 \\
1 & 2
\end{bmatrix}
\right)
$$

$$
\begin{bmatrix}
-5 & -9
\end{bmatrix} +
\begin{bmatrix}
5 & 2
\end{bmatrix}
\begin{bmatrix}
-12 & 10 \\
11 & 26
\end{bmatrix} =
\begin{bmatrix}
-5 & -9
\end{bmatrix}
$$
