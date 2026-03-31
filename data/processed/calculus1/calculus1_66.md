若  $ \lim_{x\to x_{0}^{+}}\frac{f(x)}{|x-x_{0}|^{a}}=c\neq0 $，则称当  $ x\to x_{0}^{\pm} $ 时， $ f(x) $ 是  $ \alpha $ 阶无穷小量.

根据例 2.3.5，便得到下列很有用的两个关系式：若 a > 1，则

 $$ a^{-x}=o\Big(\frac{1}{x}\Big),\quad\frac{1}{x}=o\Big(\frac{1}{\log_{a}x}\Big)\quad(x\rightarrow+\infty). $$ 

下面列出的是一些常用的无穷小量间的等价关系：当  $ x \rightarrow 0 $ 时，

(1)  $ \sin x \sim x, \tan x \sim x $;

(2) $ 1-\cos x\sim\frac{1}{2}x^{2} $;

(3) $ \ln(1+x)\sim x $;

(4)  $  e^x - 1 \sim x  $,  $  a^x - 1 \sim x \ln a  $ (a > 0);

(5) $ (1+x)^{a}-1\sim ax. $

事实上，(1)与(2)可在上一节例题中找到。(3)可由下式得到：

 $$ \lim_{x\to0}\frac{\ln(1+x)}{x}=\lim_{x\to0}\ln\left(1+x\right)^{\frac{1}{x}}=\ln\mathrm{e}=1, $$ 

对(4)，令 $ u=e^{x}-1 $，则 $ x\rightarrow0 $等价于 $ u\rightarrow0 $，并且 $ x=\ln(1+u) $，于是由(3)可得

 $$ \lim_{x\to0}\frac{\mathrm{e}^{x}-1}{x}=\lim_{u\to0}\frac{u}{\ln(1+u)}=1. $$ 

即  $ e^{x}-1\sim x(x\rightarrow0) $. 再注意到  $ a^{x}=e^{x}\cdot\ln a $，从而  $ a^{x}-1=e^{x\ln a}-1\sim x\ln a $.

对(5)，注意到 $ (1+x)^{\alpha}=\mathrm{e}^{\mathrm{a}\ln(1+x)} $，且当 $ x\to0 $时 $ u=\alpha\ln(1+x)\to0 $，应用定理2.3.3，再由(3)与(4)即得(5)：

 $$ \begin{aligned}\lim_{x\to0}\frac{(1+x)^{a}-1}{ax}&=\lim_{x\to0}\frac{\mathrm{e}^{\mathrm{e}\ln(1+x)}-1}{\alpha\ln(1+x)}\cdot\frac{\alpha\ln(1+x)}{\alpha x}\\&=\lim_{u\to0}\frac{\mathrm{e}^{u}-1}{u}\cdot\lim_{x\to0}\frac{\ln(1+x)}{x}=1.\end{aligned} $$ 

在极限运算过程中，利用无穷小量间的等价关系，常常可以使计算得到简化.

▶ 例 2.4.2 ……

求下列极限：

(1)  $ \lim_{x\to0}\frac{\sin3x}{\sin5x} $; (2)  $ \lim_{x\to0}\frac{1-\cos(1-\cos x)}{x^{4}} $; (3)  $ \lim_{x\to0}\frac{\sqrt{1+2x^{4}}-\sqrt[3]{1-x^{4}}}{\sin^{2}x(1-\cos x)} $.

解（1）当  $ x \rightarrow 0 $ 时， $ \sin kx \sim kx $，所以

 $$ \lim_{x\to0}\frac{\sin3x}{\sin5x}=\frac{3}{5}\lim_{x\to0}\frac{\sin3x}{3x}\cdot\frac{5x}{\sin5x}=\frac{3}{5}. $$ 

(2) 当  $ x \rightarrow 0 $ 时， $ 1 - \cos x \sim \frac{1}{2} x^{2} $，所以