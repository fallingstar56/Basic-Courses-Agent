(5)  $ \lim_{x \to 0} \frac{1 - \sqrt{\cos kx^2}}{x^4} $;

(6)  $ \lim_{x\to\infty}x^{2}\ln\left(\cos\frac{1}{x}\right) $;

(7)  $ \lim_{x\to\infty}x(e^{\sin\frac{1}{x}}-1) $;

(8)  $ \lim_{x\to0}\frac{\sqrt{1+\tan x}-\sqrt{1-\tan x}}{e^x-1} $;

(9)  $ \lim_{x\to0}\frac{\sqrt{1+x\sin x}-\cos x}{x^{2}} $;

(10)  $ \lim_{x \to 0} \frac{1 - \sqrt{\cos x}}{\cos \sqrt{x} - 1 + x} $;

(11)  $ \lim_{x \to 0} \frac{e^x - e^{\tan x}}{x - \tan x} $;

(12)  $ \lim_{x \to 0} \frac{1 - \cos(1 - \cos\frac{x}{2})}{x^3 \ln(1 + x)} $;

(13)  $ \lim_{x \to +\infty} x \left[ \ln(x - 2) - \ln x \right] $; (14)  $ \lim_{x \to +\infty} \left( \sqrt{x^2 + 2x} - \sqrt[3]{x^3 - x^2} \right) $.

10. 在乘除运算过程中，可以使用无穷小等价代换，那么在和与差的运算中，是否可以使用等价无穷小代换？需要注意些什么？（可以考察第9题中的(8)(9).）

11. 设当  $ x \to 0 $ 时， $ (1 + \alpha x^{2})^{1/3} - 1 $ 与  $ 1 - \cos x $ 是等价无穷小，求常数  $ \alpha $.

12. 设 a > 0，确定 p 的值，使极限  $ \lim_{x \to a} x^{p} \left( a^{\frac{1}{x}} - a^{\frac{1}{x+1}} \right) $ 存在.

13. 设  $ x \to x_{0} $ 时， $ g(x) \to \infty $，且  $ \lim_{u \to \infty} f(u) = A $，求证： $ \lim_{x \to x_{0}} f(g(x)) = A $。若将其中的  $ \infty $ 换为  $ +\infty (-\infty) $，结论是否成立？

### 2.5 函数的连续与间断

定义 2.5.1 ……

如果  $ \lim_{x\to x_{0}}f(x)=f(x_{0}) $，则称 f 在点  $ x_{0} $ 处连续.

f 在点  $ x_{0} $ 连续用函数极限的语言可表述为：设 f 在点  $ x_{0} $ 的某个邻域  $ N(x_{0},\rho) $ 内定义，若  $ \forall \varepsilon > 0, \exists \delta > 0 $，当  $ x \in N(x_{0},\delta) $ 时，就有  $ \left|f(x)-f(x_{0})\right| < \varepsilon $.

由定义看见，函数 f 在点  $ x_{0} $ 处连续蕴涵下面两个要点：

(1) f 在  $ x_{0} $ 及其附近有定义；

(2) 极限  $ \lim_{x\to x_{0}}f(x) $ 存在且与  $ f(x_{0}) $ 相等.

#### ▶ 例 2.5.1

 $ \cos x, \sin x, \ln x, a^{x} $ 在各自的定义域内每一点处连续.

事实上，由例 2.2.1 与例 2.3.7，

 $$ \lim_{x\to x_{0}}\cos x=\cos x_{0};\quad\lim_{x\to x_{0}}\sin x=\sin x_{0}; $$ 

 $$ \lim_{x\to a}\ln x=\ln a,\quad\lim_{x\to x_{0}}a^{x}=a^{x_{0}}\quad(a>0). $$ 