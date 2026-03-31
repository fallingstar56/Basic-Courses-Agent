求证： $ \lim_{x\to0}x\sin\frac{1}{x}=0. $

证明  $ \forall\varepsilon>0, $ 取  $ \delta=\varepsilon, $ 则当  $ 0<|x|<\delta $ 时，就有  $ \left|x\sin\frac{1}{x}-0\right|\leqslant|x|<\varepsilon. $ 故由极限定义知  $ \lim_{x\to0}x\sin\frac{1}{x}=0. $

注意所给函数在  $ x_{0}=0 $ 处并无定义，但这不妨碍讨论函数在点  $ x_{0}=0 $ 的极限.

图 2.2.1 描述了当  $ x \rightarrow 0 $ 时函数  $ x \sin \frac{1}{x} $ 的变化趋势.

<div style="text-align: center;"><img src="imgs/img_in_image_box_258_346_485_567.jpg" alt="Image" width="31%" /></div>


<div style="text-align: center;">图 2.2.1</div>


求证： $ \lim_{x\to1}\frac{x^{2}-3x+2}{x^{2}-x}=-1. $

证明 由于  $ x \rightarrow 1 $，不妨设  $ \left|x - 1\right| < \frac{1}{2} $。此时  $ x > \frac{1}{2} $。于是有

 $$ \left|\frac{x^{2}-3x+2}{x^{2}-x}-(-1)\right|=2\left|\frac{x-1}{x}\right|\leqslant4\left|x-1\right|. $$ 

所以  $ \forall \varepsilon > 0 $，可取  $ \delta = \min\left\{\frac{\varepsilon}{4}, \frac{1}{2}\right\} $。只要  $ 0 < |x - 1| < \delta $ 就有

 $$ \left|\frac{x^{2}-3x+2}{x^{2}-x}-(-1)\right|\leqslant4\left|x-1\right|<\varepsilon. $$ 

因此 $ \lim_{x\to1}\frac{x^{2}-3x+2}{x^{2}-x}=-1. $