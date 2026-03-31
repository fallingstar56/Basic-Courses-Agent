(9)  $ \lim_{x\to x_0}\arctan x=\arctan x_0(x_0>0) $; (10)  $ \lim_{x\to x_0}\tan x=\tan x_0\left(x_0\neq k\pi+\frac{\pi}{2}\right) $.

4. 设  $ \lim_{x\to x_{0}}f(x)=A $，证明： $ \lim_{x\to x_{0}}|f(x)|=|A| $.

5. 讨论下列函数在 x=0 处的极限是否存在.

(1)  $  f(x) = \frac{|x|}{x}  $;

(2)  $  f(x) = \begin{cases} 2x, & x > 0, \\ a\sin x + b\cos x, & x < 0. \end{cases}  $

6. 设函数 f 在开区间  $ (a, b) $ 上单调递增，求证：

(1) 若 f 在  $ (a, b) $ 上有上界，则  $ \lim f(x) $ 存在；

 $$ x\rightarrow b $$ 

(2) 若 f 在  $ (a, b) $ 上有下界，则  $ \lim_{x \to a} f(x) $ 存在.

 $$ x\rightarrow a^{+} $$ 

7. 设函数 f 在开区间  $ (a, +\infty) $ 上单调有界，求证： $ \lim_{x \to +\infty} f(x) $ 存在.

8. 设  $ f(\text{是}(-\infty,+\infty)\text{上的周期函数, 求证: 若 } \lim_{x\to+\infty}f(x)=0, $ 则  $ f(x)\equiv0. $

### 2.3 函数极限的性质

在上一节中我们给出了函数极限的六种形式. 本节中我们将讨论函数极限的一些基本性质. 为叙述方便, 主要对  $ x \rightarrow x_{0} $ 的情形加以叙述.

若极限 $ \lim_{x\to x_{0}}f(x) $存在，则极限值是唯一的。

设 $ \lim_{x\to x_0}f(x) $存在，则存在 $ \delta>0 $及正数M，使得当 $ x\in U(x_0,\delta) $时，有 $ |f(x)|<M $。

性质1与性质2的证明可仿照数列情形进行，我们把它留给读者完成。

## 性质 3(极限的保序性)

设  $ \lim_{x\to x_{0}}f(x)=A,\lim_{x\to x_{0}}g(x)=B. $

(1) 若 A > B，则存在  $ \delta > 0 $，使得当  $ x \in U(x_{0}, \delta) $ 时，有  $ f(x) > g(x) $.

(2) 若存在  $ \rho > 0 $，使得当  $ x \in U(x_{0}, \rho) $ 时，有  $ f(x) \geqslant g(x) $，则  $ A \geqslant B $.

证明 （1）若 A > B，令  $ \varepsilon = \frac{1}{2}(A - B) $。由于  $ \lim_{x \to x_0} f(x) = A $， $ \exists \delta_1 > 0 $，当  $ x \in U(x_0, \delta_1) $ 时，有  $ f(x) - A - \varepsilon = \frac{1}{2}(B - A) $，即  $ f(x) > \frac{1}{2}(A + B) $。再由  $ \lim_{x \to x_0} g(x) = B $， $ \exists \delta_2 > 0 $，使得当  $ x \in U(x_0, \delta_2) $ 时，有  $ g(x) - B < \varepsilon = \frac{1}{2}(A - B) $，即  $ g(x) < \frac{1}{2}(A + B) $。若取  $ \delta = \min\{\delta_1, \delta_2\} $，则当  $ x \in U(x_0, \delta) $ 时，就有  $ f(x) > \frac{1}{2}(A + B) $。