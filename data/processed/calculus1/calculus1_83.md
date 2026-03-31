类似地可以定义函数在点 $ x_{0} $的左导数

 $$ f_{-}^{\prime}(x_{0})=\lim_{\Delta x\to0^{-}}\frac{f(x_{0}+\Delta x)-f(x)}{\Delta x}. $$ 

从例 3.1.5 可以看到，函数  $ f(x)=|x| $ 在  $ x_{0}=0 $ 点的左导数等于 -1，右导数等于 1.

显然，导数  $ f^{\prime}(x_{0}) $ 存在的充分必要条件是  $ f^{\prime}+(x_{0}) $ 与  $ f^{\prime}-(x_{0}) $ 都存在并且相等.

如果 f 在区间  $ (a, b) $ 上每个点 x 处都可导，就称 f 在  $ (a, b) $ 上可导。如果 f 在  $ (a, b) $ 上可导，且在端点 a 和 b 处分别存在右导数和左导数，则称 f 在  $ [a, b] $ 上可导。

设函数  $ f(x)=\left\{\begin{aligned}&x+1,&x\leqslant0,\\&\mathrm{e}^{x},&x>0,\end{aligned}\right. $ 求  $ f^{\prime}(0) $.

解 先计算  $ f(x) $ 在  $ x_{0}=0 $ 点的左、右导数：

 $$ f_{-}^{\prime}(0)=\lim_{x\to0^{-}}\frac{f(x)-f(0)}{x}=\lim_{x\to0^{-}}\frac{x+1-1}{x}=1, $$ 

 $$ f_{+}^{\prime}(0)=\lim_{x\to0^{+}}\frac{f(x)-f(0)}{x}=\lim_{x\to0^{+}}\frac{\mathrm{e}^{x}-1}{x}=1. $$ 

所以  $ f(x) $ 在  $ x_{0}=0 $ 点可导且  $ f^{\prime}(0)=1 $.

应用导数概念，可以证明旋转抛物面的光学性质.

设旋转抛物面由抛物线  $ y=\frac{x^{2}}{2p}(p>0) $ 绕 y 轴旋转而成. 求证：放在焦点  $ F\left(0,\frac{p}{2}\right) $ 处的光源所发出的光，经过抛物面反射后成为平行于 y 轴的光束.

证明 设  $ M\left(t,\frac{t^{2}}{2p}\right) $ 为抛物线上任一点，作抛物线过点 M 的切线与 y 轴交

于点 P（如图 3.1.2 所示）。要证 MC 平行于 y 轴，只需证  $ \angle FPM = \angle CMQ $。根据光的反射定律，入射角等于反射角，即  $ \angle FMP = \angle CMQ $。因而只需证  $ \angle FPM = \angle FMP $，亦即  $ \triangle FPM $ 为等腰三角形。抛物线过点  $ M(t, \frac{t^{2}}{2p}) $ 的切线 MP 的斜率为  $ y'(t) = \frac{t}{p} $，因而切线 MP 的方程为

<div style="text-align: center;"><img src="imgs/img_in_image_box_440_707_626_841.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">图 3.1.2</div>


 $$ y=\frac{t}{p}(x-t)+\frac{t^{2}}{2p}, $$ 