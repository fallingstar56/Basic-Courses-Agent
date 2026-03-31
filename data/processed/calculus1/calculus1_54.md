求证 $ \lim_{x\to\infty}\sqrt{\frac{x^{2}+1}{x^{2}-1}}=1. $

证明 注意到

 $$ \begin{aligned}\left|\sqrt{\frac{x^{2}+1}{x^{2}-1}}-1\right|&=\frac{\sqrt{x^{2}+1}-\sqrt{x^{2}-1}}{\sqrt{x^{2}-1}}\\&=\frac{2}{\sqrt{x^{2}-1}\left(\sqrt{x^{2}+1}+\sqrt{x^{2}-1}\right)},\end{aligned} $$ 

由于  $ x \to \infty $，不妨设  $ |x| > \sqrt{2} $。从而有

 $$ \left|\sqrt{\frac{x^{2}+1}{x^{2}-1}}-1\right|<\frac{2}{\left|x\right|}. $$ 

于是， $ \forall\varepsilon>0 $，取 $ M=\max\left\{\sqrt{2},\frac{2}{\varepsilon}\right\} $，则当 $ \left|x\right|>M $时，就有

 $$ \left|\sqrt{\frac{x^{2}+1}{x^{2}-1}}-1\right|<\frac{2}{\left|x\right|}<\varepsilon. $$ 

所以， $ \lim_{x\to\infty}\sqrt{\frac{x^{2}+1}{x^{2}-1}}=1. $

### 习题 2.2

1. 用  $ \varepsilon-\delta $ 语言分别叙述：“ $ \lim_{x\to x_{0}}f(x)\neq A $”与“ $ \lim_{x\to+\infty}f(x)\neq A $”.

2. 下列说法中，哪些与 $ \lim_{x\to x_{0}}f(x)=A $ 等价. 如果等价，请证明；如果不等价，请举出反例.

(1) 对于无限多个正数  $ \varepsilon > 0, \exists \delta > 0 $，只要  $ x \in U(x_0, \delta) $，就有  $ |f(x) - A| \leqslant \varepsilon $;

(2)  $ \forall \varepsilon \in (0,1), \delta > 0 $, 只要  $ x \in U(x_0, \delta) $, 就有  $ |f(x) - A| \leqslant 8\varepsilon $;

(3)  $ \forall k \in \mathbb{N}^* $,  $ \exists \delta_k > 0 $, 只要  $ x \in U(x_0, \delta_k) $, 就有  $ |f(x) - A| < 2^{-k} $;

(4)  $ \forall n \in \mathbb{N}^* $，只要  $ 0 < |x - x_0| < \frac{1}{n} $，就有  $ |f(x) - A| < \frac{1}{n} $.

3. 用函数极限的定义证明下列极限.

(1)  $ \lim_{x \to 2} \sqrt{x^2 + 5} = 3 $;

(2) $ \lim_{x\to3}\frac{x-3}{x^{2}-9}=\frac{1}{6} $;

(3) $ \lim_{x\to2}\frac{x^{2}-3}{x^{2}-4x+3}=-1; $

(4) $ \lim_{x\to1^{+}}\frac{x-1}{\sqrt{x^{2}-1}}=0; $

(5)  $ \lim_{x\to-\infty}(x+\sqrt{x^{2}-a})=0; $

(6)  $ \lim_{x\to\infty}\frac{2x^{2}+3}{x^{2}-2x}=2; $



(7)  $ \lim_{x\to+\infty}\left(\sin\sqrt{x+1}-\sin\sqrt{x}\right)=0 $; (8)  $ \lim_{x\to x_{0}}\cos\frac{1}{x}=\cos\frac{1}{x_{0}}(x_{0}\neq0) $;