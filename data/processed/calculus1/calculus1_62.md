 $$ \left(\frac{x+a}{x-a}\right)^{x}=\left[\left(1+\frac{2a}{x-a}\right)^{\frac{x-a}{2a}}\right]^{\frac{2a x}{x-a}}, $$ 

由于

 $$ \lim_{x\to+\infty}\left(1+\frac{2a}{x-a}\right)^{\frac{x-a}{2a}}=\mathrm{e},\quad\lim_{x\to+\infty}\frac{2ax}{x-a}=2a, $$ 

由例 2.3.8 的结论得到

 $$ \lim_{x\to+\infty}\left(\frac{x+a}{x-a}\right)^{x}=\lim_{x\to+\infty}\left[\left(1+\frac{2a}{x-a}\right)^{\frac{x-a}{2a}}\right]^{\frac{2a}{x-a}}=\mathrm{e}^{2a} $$ 

▶ 例 2.3.10 .....

求极限 $ \lim_{x\to0}(\cos x)^{\frac{1}{x^{2}}} $

解

 $$ \left(\cos x\right)^{\frac{1}{x^{2}}}=\left(1-2\sin^{2}\frac{x}{2}\right)^{\frac{-1}{2\sin^{2}\frac{x}{2}}}\cdot\frac{2\sin^{2}\frac{x}{2}}{-x^{2}} $$ 

注意到当  $ x \rightarrow 0 $ 时，

 $$ u(x)=\left(1-2\sin^{2}\frac{x}{2}\right)^{\frac{-1}{2\sin^{2}\frac{x}{2}}}\rightarrow\mathrm{e}, $$ 

 $$ v(x)=\frac{2\sin^{2}\frac{x}{2}}{-x^{2}}\rightarrow-\frac{1}{2}. $$ 

利用例 2.3.8 的结论便得到

 $$ \lim_{x\to0}\left(\cos x\right)^{\frac{1}{x^{2}}}=\lim_{x\to0}u\left(x\right)^{v\left(x\right)}=\mathrm{e}^{-\frac{1}{2}}. $$ 

### 习题 2.3

1. 证明本节的性质 1 与性质 2.

2. 证明定理 2.3.1.

3. 设  $ \lim_{x\to+\infty}f(x)=A $，证明：

 $$ \lim_{x\to x_{0}}f^{2}(x)=A^{2}\quad(2)\quad\lim_{x\to x_{0}}\sqrt{f(x)}=\sqrt{A}(A>0)\quad(3)\quad\lim_{x\to x_{0}}\sqrt[3]{f(x)}=\sqrt[3]{A} $$ 

4. 若  $ \lim_{x\to0}f(x)=A>B $，则  $ \exists\delta>0 $，当  $ x\in U(x_{0},\delta) $ 时， $ f(x)>B $.

5. 证明定理 2.3.2.

6. 求下列极限（其中各题中的 m 与 n 都是正整数）.

(1)

 $$ \lim_{x\to2}(5-3x)(3x-1); $$ 

(2)

 $$ \lim_{x\to\frac{\pi}{2}}\frac{\sin x}{x}; $$ 

(3)

 $$ \lim_{x\to2}x^{2}-2x $$ 

(4)

 $$ \lim_{x\to1^{-}}\frac{\sqrt{(x-1)^{2}}}{x-1}; $$ 