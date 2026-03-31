 $$ \frac{S(t_{0}+\Delta t)-S(t_{0})}{\Delta t}. $$ 

显然， $ \Delta t $ 越小，这个平均速度就越接近于质点在时刻  $ t_{0} $ 的瞬时速度。因此，如果极限

 $$ v=\lim_{\Delta t\to0}\frac{S(t_{0}+\Delta t)-S(t_{0})}{\Delta t} $$ 

存在，则此极限 v 就是质点在  $ t_{0} $ 时刻的瞬时速度.

在上面两个来自不同领域的问题中，我们遇到了相同类型的极限：“函数的改变量与自变量的改变量之比当自变量的改变量趋向于零时的极限”，也可以叫做“函数对于其自变量的变化率”。

现在抛开问题的具体背景，着重研究上述形式的极限，便需要引入导数的概念.

设函数 f 在  $ x_{0} $ 点的某个邻域内定义，如果极限

 $$ \lim_{\Delta x\to0}\frac{f(x_{0}+\Delta x)-f(x_{0})}{\Delta x} $$ 

存在，则称 f 在  $ x_{0} $ 点可导，称这个极限值为 f 在  $ x_{0} $ 点的导数，记作  $ f'(x_{0}) $

根据导数定义，在上面两个问题中，曲线 C 在点  $ P(x_{0}, f(x_{0})) $ 处的切线斜率就等于  $ f'(x_{0}) $；而质点在时刻  $ t_{0} $ 的瞬时速度即为  $ S'(t_{0}) $.

▶ 例 3.1.1 ……

设  $ f(x) \equiv C $，求  $ f'(x) $.

解 对任意 x，由导数定义

 $$ f^{\prime}(x)=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x}=\lim_{\Delta x\to0}\frac{C-C}{\Delta x}=0. $$ 

这就是说，常值函数在任一点的导数等于0。

▶ 例 3.1.2 ……

 $ f(x)=\sin x $，求 $ f'(x) $.

解 由导数定义，

 $$ \lim_{\Delta x\to0}\frac{\sin(x+\Delta x)-\sin(x)}{\Delta x}=\lim_{\Delta x\to0}\frac{2\sin\frac{\Delta x}{2}\cos\left(x+\frac{\Delta x}{2}\right)}{\Delta x}. $$ 

注意到：

 $$ \lim_{\Delta x\to0}\frac{2\sin\frac{\Delta x}{2}}{\Delta x}=1,\lim_{\Delta x\to0}\cos\left(x+\frac{\Delta x}{2}\right)=\cos x, $$ 

就得到