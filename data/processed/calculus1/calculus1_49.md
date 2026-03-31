证明对于双曲函数，下列恒等式成立：

 $$ \cosh^{2}x-\sinh^{2}x=1 $$ 

(2)  $ \sinh^{2}x + \cosh^{2}x = \cosh(2x) $;

 $$ \sinh(x+y)=\sinh x\cosh y+\sinh y\cosh x; $$ 

(4)  $ \cosh(x+y)=\cosh x\cosh y+\sinh x\sinh y; $

(5) $ \cosh x + \cosh y = 2\cosh \frac{x + y}{2}\cosh \frac{x - y}{2} $;

(6)  $ \cosh x - \cosh y = 2 \sinh \frac{x + y}{2} \sinh \frac{x - y}{2} $;

(7) $ \sinh x+\sinh y=2\sinh\frac{x+y}{2}\cosh\frac{x-y}{2}; $

(8)  $ \tanh(x+y)=\frac{\tanh x+\tanh y}{1+\tanh x\tanh y} $;

(9)  $ \coth(x+y)=\frac{1+\coth x\coth y}{\coth x+\coth y}. $

### 2.2 函数极限的概念

本节中我们来讨论函数的极限。函数极限是研究函数最重要的工具之一。

从第1章中知道，讨论数列 $ \{a_{n}\} $的极限问题就是考察当n无限增大时，相应的项 $ a_{n} $的变化趋势。类似地，讨论函数的极限问题就是考察当函数的自变量x无限逼近某个点 $ x_{0} $（但不等于 $ x_{0} $），或趋向于 $ \infty $时，相应的函数值 $ f(x) $的变化趋势。

与数列极限不同的是，函数的自变量 x 是连续变化的，且 x 既可以无限逼近点  $ x_{0} $，又可以无限趋向于  $ +\infty $ 或  $ -\infty $；既可以从  $ x_{0} $ 的左侧（或右侧）趋向于  $ x_{0} $，又可以从  $ x_{0} $ 的两侧任意地趋向于  $ x_{0} $。所以函数极限有多种形式。然而，不同的形式的函数极限在本质上都是类似的，它们都具有类似的性质。

#### 2.2.1 函数在一点的极限

为叙述方便，记  $ N(x_{0},\delta) $ 是以  $ x_{0} $ 为中心的开区间： $ N(x_{0},\delta)=(x_{0}-\delta,x_{0}+\delta) $  $ (\delta>0) $，称为  $ x_{0} $ 的一个邻域或  $ \delta $-邻域.

又记  $  U(x_{0}, \delta) = (x_{0} - \delta, x_{0}) \cup (x_{0}, x_{0} + \delta)  $，称为  $ x_{0} $ 的一个空心邻域或  $ \delta $-空心邻域.

#### 定义 2.2.1

设函数 f 在点  $ x_{0} $ 的某个空心邻域  $ U(x_{0}, \rho) $ 内定义，A 为一实数。如果  $ \forall \varepsilon > 0, \exists \delta > 0 $，当  $ x \in U(x_{0}, \delta) $ 时，就有  $ |f(x) - A| < \varepsilon $，则称  $ f(x) $ 在点  $ x_{0} $ 处有极限 A。或者说当 x 趋向于  $ x_{0} $ 时， $ f(x) $ 趋向于 A。记作  $ \lim_{x \to +\infty} f(x) = A $，或  $ f(x) \to A(x \to x_{0}) $。

 $$ x\rightarrow x_{0} $$ 