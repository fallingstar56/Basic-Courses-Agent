于是点 P 的坐标为  $ P\left(0,\frac{-t^{2}}{2b}\right) $. 直接计算线段  $ \overline{FM} $ 与  $ \overline{FP} $ 的长度可得

 $$ \overline{FM}=\sqrt{t^{2}+\left(\frac{p}{2}-\frac{t^{2}}{2p}\right)^{2}}=\frac{p}{2}+\frac{t^{2}}{2p}=\overline{FP}. $$ 

所以 MC 平行于 y 轴.

#### 3.1.2 微分

与函数在一点的导数密切相关的另一概念是函数在一点的微分.

定义 3.1.3

设函数 f 在点  $ x_{0} $ 的某个邻域内定义，如果当自变量的增量  $ \Delta x $ 充分小时，相应的函数值的增量  $ \Delta f(x_{0}) = f(x_{0} + \Delta x) - f(x_{0}) $ 可以表示为

 $$ \Delta f(x_{0})=a\Delta x+o(\Delta x)(\Delta x\rightarrow0), $$ 

其中 a 为常数，则称 f 在点  $ x_{0} $ 可微，并称  $ \mathrm{d}f(x_{0})=a\cdot\Delta x $ 为 f 在点  $ x_{0} $ 处的微分.

 $ \mathrm{d}f(x_{0})=a\cdot\Delta x $ 是一个（关于自变量  $ \Delta x $ 的）线性函数，它是函数增量  $ \Delta f(x_{0}) $ 的线性主要部分，与  $ \Delta f(x_{0}) $ 仅相差一个  $ \Delta x $ 的高阶无穷小量  $ o(\Delta x) $，因而当  $ \Delta x $ 充分小时，可以用  $ \mathrm{d}f(x_{0}) $ 作为  $ \Delta f(x_{0}) $ 的近似值。这一事实使得微分在很多实际问题中具有应用价值。

下面的定理揭示了导数与微分之间的联系.

定理 3.1.1

f 在点  $ x_{0} $ 可微的充要条件是 f 在点  $ x_{0} $ 可导. 此时

 $$ \mathrm{d}f(x_{0})=f^{\prime}(x_{0})\cdot\Delta x. $$ 

证明 充分性 设 f 在点  $ x_{0} $ 可导，即下面极限存在：

 $$ \lim_{\Delta x\to0}\frac{f(x_{0}+\Delta x)-f(x)}{\Delta x}=f^{\prime}(x_{0}), $$ 

亦即

 $$ \lim_{\Delta x\to0}\frac{f(x_{0}+\Delta x)-f(x_{0})-f^{\prime}(x_{0})\Delta x}{\Delta x}=0. $$ 

所以，当  $ \Delta x \to 0 $ 时，

 $$ \Delta f(x_{0})=f^{\prime}(x_{0})\Delta x+o(\Delta x). $$ 

由此知 f 在点  $ x_{0} $ 可微，并且  $ \mathrm{d}f(x_{0})=f'(x_{0})\Delta x. $

必要性 设 f 在点  $ x_{0} $ 可微，则  $ \exists a \in \mathbb{R} $，使得当  $ \Delta x \to 0 $ 时，

 $$ \Delta f(x_{0})=a\Delta x+o\left(\Delta x\right). $$ 

于是