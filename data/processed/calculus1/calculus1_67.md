 $$ \begin{aligned}\lim_{x\rightarrow0}\frac{1-\cos(1-\cos x)}{x^{4}}&=\frac{1}{8}\lim_{x\rightarrow0}\frac{1-\cos(1-\cos x)}{\frac{1}{2}\left(1-\cos x\right)^{2}}\cdot\left(\frac{1-\cos x}{x^{2}/2}\right)^{2}\\&=\frac{1}{8}\times1\times1^{2}=\frac{1}{8}.\end{aligned} $$ 

(3) 当  $ x \to 0 $ 时， $ \sqrt{1+2x^{4}}-1 \sim x^{4} $， $ \sqrt[3]{1-x^{4}}-1 \sim \frac{-1}{3}x^{4} $，所以

 $$ \begin{aligned}&\lim_{x\rightarrow0}\frac{\sqrt{1+2x^{4}}-\sqrt[3]{1-x^{4}}}{\sin^{2}x(1-\cos x)}\\&=\ 2\lim_{x\rightarrow0}\left(\frac{\sqrt{1+2x^{4}}-1}{x^{4}}+\frac{1}{3}\ \frac{\sqrt[3]{1-x^{4}}-1}{-x^{4}/3}\right)\cdot\frac{x^{2}}{\sin^{2}x}\cdot\frac{\frac{x^{2}}{2}}{(1-\cos x)}\\&=2\Big(1+\frac{1}{3}\Big)\times1\times1=\frac{8}{3}.\end{aligned} $$ 

仔细观察上例中求极限的过程不难发现：待求极限函数的分子、分母的无穷小因子可以用等价的无穷小代换。这种方法常称为等价无穷小量代换法。例如，

 $$ \lim_{x\to0}\frac{\tan x-\sin x}{x^{2}\ln(1+x)}=\lim_{x\to0}\frac{\sin x(1-\cos x)}{x^{2}\ln(1+x)\cos x}=\lim_{x\to0}\frac{x\cdot\frac{1}{2}x^{2}}{x^{2}\cdot x\cos x}=\frac{1}{2}. $$ 

但是必须要注意的是，如果待求极限函数或其分子、分母中有多个加项，则其中的某一个加项不能随意用等价的无穷小量代换。例如，虽然当 $ x\to0 $时， $ \tan x\sim x,\sin x\sim x $，但下列做法是错误的：

 $$ \lim_{x\to0}\frac{\tan x-\sin x}{x^{2}\ln(1+x)}=\lim_{x\to0}\frac{x-x}{x^{2}\ln(1+x)}=0. $$ 

对于同一个极限过程的两个无穷大量，可以完全类似于无穷小量情形定义高阶、同阶和等价无穷大量的概念。

设  $ x \rightarrow x_{0} $ 时， $ f(x) $ 与  $ g(x) $ 都是无穷大量.

(1) 若  $ \lim_{x\to x_{0}}\frac{f(x)}{g(x)}=0 $，则称当  $ x\to x_{0} $ 时  $ g(x) $ 是  $ f(x) $ 的高阶无穷大量，记作

 $$ f(x)=o(g(x))\quad(x\rightarrow x_{0}); $$ 

(2) $ \lim_{x\to x_{0}}\frac{f(x)}{g(x)}=c\neq0 $，则称当 $ x\to x_{0} $时， $ f(x) $与 $ g(x) $是同阶无穷大量.

特别地，若 $ \lim_{x\to x_{0}}\frac{f(x)}{g(x)}=1 $，则称当 $ x\to0 $时 $ f(x) $与 $ g(x) $是等价无穷大量，记作

 $$ f(x)\sim g(x)\quad(x\rightarrow x_{0}). $$ 