于是由极限定义即得 $ \lim f(g(x))=A. $

注 从定理 2.3.3 的证明中不难发现，条件“当  $ x \neq x_{0} $ 时  $ g(x) \neq u_{0} $”可以替换为如下条件：“ $ f(u_{0}) = A $”.

性质1, 性质2, 性质3与定理2.3.1, 定理2.3.2与定理2.3.3中的极限过程 $ x\rightarrow x_{0} $可以换成其他5种极限过程的任一种，其证明也是完全类似的.

应用夹逼原理，可以得到下面的重要极限。

▶ 例 2.3.1

求证 $ \lim_{x\to0}\frac{\sin x}{x}=1. $

证明 不妨设 $ -\frac{\pi}{2}<x<\frac{\pi}{2} $. 如图 2.3.1 所示, 当  $ 0<x<\frac{\pi}{2} $ 时,  $ \triangle OAC $ 的面积 < 扇形 OAC 的面积 <  $ \triangle OAB $ 的面积, 即

 $$ \sin x<x<\tan x. $$ 

由此可得

 $$ \cos x<\frac{\sin x}{x}<1. $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_436_308_634_500.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;">图 2.3.1</div>


注意到此不等式对于 $ -\frac{\pi}{2}<x<\frac{\pi}{2} $成立，且 $ \lim_{x\to0}\cos x=1 $（例2.2.1），于是由夹逼定理得到

 $$ \lim_{x\to0}\frac{\sin x}{x}=1. $$ 

▶ 例 2.3.2

求极限： $ \lim_{x\to0}\frac{1-\cos x}{x^{2}} $

 $$ \lim_{x\to0}\frac{1-\cos x}{x^{2}}=\lim_{x\to0}\frac{2\sin^{2}(x/2)}{x^{2}}=\frac{1}{2}\lim_{x\to0}\left[\frac{\sin(x/2)}{x/2}\right]^{2}=\frac{1}{2}\cdot1^{2}=\frac{1}{2} $$ 

求极限： $ \lim_{x\to0}\frac{\sin(\tan x)}{\sin x} $

解 令  $ u = \tan x $，则当  $ x \to 0 $ 时， $ u \to 0 $。由定理 2.2.3 可得

 $$ \lim_{x\to0}\frac{\sin(\tan x)}{\sin x}=\lim_{x\to0}\frac{\sin(\tan x)}{\tan x}\cdot\lim_{x\to0}\frac{1}{\cos x}=\lim_{x\to0}\frac{\sin u}{u}=1. $$ 

应用夹逼定理与例 1.4.1 的结果，可以得到另一个重要极限：