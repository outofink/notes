---
title: תרגיל 1
author: משה קרומביין - 209133123
date: אלגברה ליניארית 1
lang: he
---

\newcommand{\bm}[1]{\begin{bmatrix}#1\end{bmatrix}}

הערה: שברתי את היד הדומיננטית ולכן אני מקליד במקום לכתוב בכתב יד.

1.

A.

$$s \begin{bmatrix}
    1\\0\\1
\end{bmatrix} + t \begin{bmatrix}
    1\\1\\0
\end{bmatrix}$$
$$=\begin{bmatrix}
    s+t\\t\\s
\end{bmatrix}$$

B.

$$t \begin{bmatrix}
    1\\1\\-1\\1
\end{bmatrix} + s \begin{bmatrix}
    0\\1\\1\\0
\end{bmatrix} + r \begin{bmatrix}
    1\\0\\1\\1
\end{bmatrix}$$
$$=\begin{bmatrix}
    t+r \\
    t+s \\
    s-t+r \\
    t+r
\end{bmatrix}$$

C.

$$s=\frac{2y-x+z}{3}, t=\frac{x+y-z}{3}, r=\frac{2x-y+z}{3}$$

$$=\begin{bmatrix}
    \frac{x+y-z}{3} + \frac{2x-y+z}{3} \\
    \frac{x+y-z}{3} + \frac{2y-x+z}{3} \\
    \frac{2y-x+z}{3} - \frac{x+y-z}{3} + \frac{2x-y+z}{3} \\
    \frac{x+y-z}{3} + \frac{2x-y+z}{3}
\end{bmatrix}$$
$$=\begin{bmatrix}
    \frac{3x}{3} \\
    \frac{3y}{3} \\
    \frac{3z}{3} \\
    \frac{3x}{3}
\end{bmatrix} = \begin{bmatrix}
    x\\y\\z\\x
\end{bmatrix}$$

$$\pagebreak$$

2.

$$
\begin{gathered}
    W_3 \neq W_4: \begin{bmatrix}
        2\\2\\2
    \end{bmatrix} \in W_3, \notin W_4 \\
    W_1 \neq W_4: \begin{bmatrix}
        4\\2\\4
    \end{bmatrix} \in W_1, \notin W_4 \\
    W_2 \neq W_4: \begin{bmatrix}
        1\\3\\1
    \end{bmatrix} \in W_2, \notin W_4 \\
    W_1 \neq W_3: \begin{bmatrix}
        1\\5\\1
    \end{bmatrix} \in W_1, \notin W_3 \\
\end{gathered}
$$

$$\pagebreak$$

3.

A.

i.

$$
\begin{gathered}
    \vec u = \begin{bmatrix}
        1\\2\\1
    \end{bmatrix}, \vec v = \begin{bmatrix}
        -\sqrt 2 \\ 0 \\ \sqrt 2
    \end{bmatrix} \\
    \lambda_1 \begin{bmatrix}
        1\\2\\1
    \end{bmatrix} + \lambda_2 \begin{bmatrix}
        -\sqrt 2\\0\\\sqrt 2
    \end{bmatrix} = \begin{bmatrix}
        x\\y\\z
    \end{bmatrix} \\
    = \begin{cases}
        x = \lambda_1 -\lambda_2 \sqrt 2 \\
        y = 2 \lambda_1 \\
        z = \lambda_1 +\lambda_2 \sqrt 2 \\
    \end{cases} \\
    = \begin{cases}
        \lambda_2 = \frac{y-2x}{2\sqrt 2} \\
        \lambda_1 = \frac{y}{2} \\
        z = \frac{y}{2} + \frac{y}{2} - x = y - x\\
    \end{cases} \\
    = \left\{\begin{bmatrix}
        x\\y\\y-x
    \end{bmatrix} \mid x,y \in \mathbb{R} \right\}
\end{gathered}
$$

A.

ii.

$$
\begin{gathered}
    \vec u = \begin{bmatrix}
        0\\0\\0
    \end{bmatrix}, \vec v = \begin{bmatrix}
        1\\2\\3
    \end{bmatrix} \\
    \lambda_1 \begin{bmatrix}
        0\\0\\0
    \end{bmatrix} + \lambda_2 \begin{bmatrix}
        1\\2\\3
    \end{bmatrix} = \begin{bmatrix}
        x\\y\\z
    \end{bmatrix} \\
    \begin{cases}
        x = \lambda_2 \\
        y = 2 \lambda_2 \\
        z = 3 \lambda_2
    \end{cases} \\
    = \left\{\begin{bmatrix}
        x\\2x\\3x
    \end{bmatrix} \mid x \in \mathbb{R} \right\}
\end{gathered}
$$

B.

$$
\begin{gathered}
    i. \\
    \begin{bmatrix}
        x=b\\2x=b\\3x=b
    \end{bmatrix} \\
    b=0 \\
    \boxed{\begin{bmatrix}
        b\\b\\b
    \end{bmatrix} = \begin{bmatrix}
        0\\0\\0
    \end{bmatrix}}
\end{gathered} \quad | \quad \begin{gathered}
    ii. \\
    \begin{bmatrix}
        x=b\\y=b\\y-z=b
    \end{bmatrix} \\
    b=0 \\
    \boxed{\begin{bmatrix}
        b\\b\\b
    \end{bmatrix} = \begin{bmatrix}
        0\\0\\0
    \end{bmatrix}}
\end{gathered}
$$

4.

$$
\begin{gathered}
    \vec u = \begin{bmatrix}
        1\\3
    \end{bmatrix}, \vec v = \begin{bmatrix}
        1\\-1
    \end{bmatrix} \\
    \lambda_1 \begin{bmatrix}
        1\\3
    \end{bmatrix} + \lambda_2 \bm{1\\-1} = \bm{x\\y}, x, y \in \mathbb{R} \\
    \begin{cases}
        \lambda_1 + \lambda_2 = x \\
        3\lambda_1 - \lambda_2 = y \\
    \end{cases} \implies \begin{cases}
        \lambda_1 = \frac{x+y}{4} \\
        \lambda_2 = \frac{3x-y}{4} \\
    \end{cases} \\
    \lambda_1, \lambda_2 \in \mathbb{R} \quad \text{מש"ל}
\end{gathered}
$$

$$\pagebreak$$

5.

$$
A. \left[
    \begin{array}{cc|c}
        1&2&3 \\
        -3&2&-1 \\
        2&-5&3
    \end{array}\right] \quad \mid \quad
B. \left[
    \begin{array}{ccc|c}
        4 & 6 & 1 & 7 \\
        1 & 0 & -3 & -3 \\
        1 & 3 & -6 & 1
    \end{array}\right]
$$

6.

א. אם יש בהן אותו מספר של נעלמים ושתיהן יש אותו פתרון כללי.

ב. אם עשו פעולות אלמטריות על מטריצה $M$ ליצור מטריצה $N$, אז $M$ ו -$N$ שקולות שורות.

ג. פעולה על שורה במטריצה מסוג: החלפה בין שתי שורות, מפעלה בסקלר $0 \neq$, הוספת מכפלה של שורה אחרת במטריצה. כל פעולה מסוג זה לא משתנה את הפתרון הכללי של המטריצה.

$$\pagebreak$$

7.

A.

שתי השורות האחרונות הן שוות בין המערכות והשורה הראשונה במערכת הימין שווה ל-:

$$2R_3-R_2$$

ולכן הן שוות.

B.

שתי השורות האחרונות הן שוות בין המערכות אבל בין השורות הראשונות:

$$\begin{gathered}
    x_1 + 4x_4 = 1, \quad 2x_1-2x_2+4x_4 = 3 \\
    x_1 + 4x_4 = 1, \quad 2x_1-(2-3x_3)+4x_4 = 3 \\
    x_1 + 4x_4 = 1, \quad 2x_1-(2-(3+x_1))+4x_4 = 3 \\
    x_1 + 4x_4 = 1, \quad 3x_1+4x_4 = 2 \\
\end{gathered}
$$

$x_1=0, x_2=-\frac{1}{2},x_3=1,x_4=1$ פותר את הימין, אך לא את השמאל, ולכן הן לא שוות.

$$\pagebreak$$

8.

A.

$$
\begin{gathered}
    \left[
    \begin{array}{ccccc}
        2 & -6 & -4 & 3 & -2 \\
        -4 & 12 & 8 & 4 & -36 \\
        -3 & 9 & 6 & 1 &-19
    \end{array}\right]
    \begin{array}{c}
        R_1 \to {R_1 \over 2} \\
        ~ \\
        ~
    \end{array} \implies \left[
    \begin{array}{ccccc}
        1 & -3 & -2 & 1.5 & -1 \\
        -4 & 12 & 8 & 4 & -36 \\
        -3 & 9 & 6 & 1 &-19
    \end{array}\right]
    \begin{array}{c}
        ~ \\
        R_2 \to R_2 + 4 R_1 \\
        ~
    \end{array} \implies \\ \left[
    \begin{array}{ccccc}
        1 & -3 & -2 & 1.5 & -1 \\
        0 & 0  & 0  & 10 & -40 \\
        -3 & 9 & 6 & 1 &-19
    \end{array}\right]
    \begin{array}{c}
        ~ \\
        R_2 \to \frac{1}{10} R_2  \\
        R_3 \leftrightarrow R_2
    \end{array} \implies \left[
    \begin{array}{ccccc}
        1 & -3 & -2 & 1.5 & -1 \\
        -3 & 9 & 6 & 1 &-19 \\
        0 & 0  & 0  & 1 & -4
    \end{array}\right]
    \begin{array}{c}
        ~ \\
        R_2 \to R_2 + 3R_1  \\
        \\
    \end{array} \implies \\ \left[
    \begin{array}{ccccc}
        1 & -3 & -2 & 1.5 & -1 \\
        0 & 0 & 0 & 5.5 &-22 \\
        0 & 0  & 0  & 1 & -4
    \end{array}\right]
    \begin{array}{c}
        ~ \\
        R_2 \to R_2 -5.5 R_3  \\
        R_2 \leftrightarrow R_3
    \end{array} \implies \left[
    \begin{array}{ccccc}
        1 & -3 & -2 & 1.5 & -1 \\
        0 & 0  & 0  & 1 & -4 \\
        0 & 0 & 0 & 0 & 0 \\
    \end{array}\right]
    \begin{array}{c}
        ~ R_1 \to R_1 - 1.5 R_2 \
        ~ \\
        \\
    \end{array} \implies\\ \left[
    \begin{array}{ccccc}
        1 & -3 & -2 & 0 & -5 \\
        0 & 0  & 0  & 1 & -4 \\
        0 & 0 & 0 & 0 & 0 \\
    \end{array}\right] \implies
    \begin{cases}
        x = 3y + 2z − 5u \\
        w = 4u
    \end{cases} \implies \boxed{\left\{
    \begin{bmatrix}
        3y + 2x -5u \\
        y \\
        z \\
        4u \\
        u
    \end{bmatrix} \mid u,y,z \in \mathbb{R} \right\}}
\end{gathered}
$$

B.

$$
\begin{gathered}
    \left[
    \begin{array}{ccc|c}
        1 & 1 & 1 & -6 \\
        2 & 2 & 0 & -6 \\
        1 & 2 & 2 & -11
    \end{array}\right]
    \begin{array}{c}
        ~ \\
        R_2 \to R_2 - 2 R_1\\
        R_3 \to R_3 - R_1
    \end{array} \implies \left[
    \begin{array}{ccc|c}
        1 & 1 & 1 & -6 \\
        0 & 0 & -2 & 6 \\
        0 & 1 & 1 & -5
    \end{array}\right]
    \begin{array}{c}
        R_1 \to R_1 - R_3 \\
        R_2 \to -\frac{1}{2} R_2 \\
        R_3 \leftrightarrow R_2
    \end{array} \implies \\ \left[
    \begin{array}{ccc|c}
        1 & 0 & 0 & -1 \\
        0 & 1 & 1 & -5 \\
        0 & 0 & 1 & -3
    \end{array}\right]
    \begin{array}{c}
        \\
        R_2 \to R_2 - R_3 \\
        ~
    \end{array} \implies \left[
    \begin{array}{ccc|c}
        1 & 0 & 0 & -1 \\
        0 & 1 & 0 & -2 \\
        0 & 0 & 1 & -3
    \end{array}\right]
    \implies \boxed{\begin{bmatrix}
        x_1\\x_2\\x_3
    \end{bmatrix} = \begin{bmatrix}
        -1\\-2\\-3
    \end{bmatrix}}
\end{gathered}
$$
