8. 证明不等式： $ \frac{1}{2n} < \frac{1}{2} \cdot \frac{3}{4} \cdot \cdots \cdot \frac{2n-1}{2n} < \frac{1}{\sqrt{2n+1}} $，并求极限  $ \lim_{n\to\infty}\sqrt[n]{\frac{1}{2} \cdot \frac{3}{4} \cdot \cdots \cdot \frac{2n-1}{2n}} $.

9. 已知  $ a_{n}>0(n=1,2,\cdots) $， $ \lim_{n\to\infty}a_{n}=A $。证明： $ \lim_{n\to\infty}\sqrt[n]{a_{1}a_{2}\cdots a_{n}}=A $；并求  $ \lim_{n\to\infty}\sqrt[n]{\frac{1}{n!}} $。

10. 已知  $ a_{n}>0(n=1,2,\cdots) $， $ \lim_{n\to\infty}\frac{a_{n+1}}{a_{n}}=a. $

(1) 证明： $ \lim_{n\to\infty}\sqrt[n]{a_n}=a;\quad(2) $ 若  $ a<1 $，求证： $ \lim_{n\to\infty}a_n=0;\quad(3) $ 求  $ \lim_{n\to\infty}\frac{n}{\sqrt[n]{n!}} $

### 1.4 单调数列

定义 1.4.1

(1)对于数列 $ \{a_{n}\} $，如果 $ \forall n\in\mathbb{N}^{*} $，都有 $ a_{n}\leqslant a_{n+1}(a_{n}\geqslant a_{n+1}) $，则称数列 $ \{a_{n}\} $单调递增（单调递减）；(2)对于数列 $ \{a_{n}\} $，如果 $ \forall n\in\mathbb{N}^{*} $，都有 $ a_{n}<a_{n+1}(a_{n}>a_{n+1}) $，则称数列 $ \{a_{n}\} $严格单调递增（严格单调递减）。

单调递增与单调递减的数列统称为单调数列.

定理 1.4.1（单调收敛定理）

(1)单调递增且有上界的数列必收敛；(2)单调递减且有下界的数列必收敛.

证明 （1）设数列  $ \{a_{n}\} $ 单调递增且有上界。根据确界定理， $ \{a_{n}\} $ 有上确界： $ A=\sup_{n\geq1}\{a_{n}\} $。由于  $ \forall\varepsilon>0,A-\varepsilon $ 不再是  $ \{a_{n}\} $ 的上界，于是， $ \exists N\in\mathbb{N}^{*} $ 使得  $ A-\varepsilon<a_{N}\leqslant A $。注意到  $ \{a_{n}\} $ 单调递增，从而当 n>N 时，有  $ A-\varepsilon<a_{N}\leqslant a_{n}\leqslant A $，所以  $ \lim_{n\to\infty}a_{n}=A $。

同理可证明(2).

单调收敛定理是实数系的一个非常重要的结论，在今后将有许多应用。

▶ 例 1.4.1

求证：极限 $ \lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n $存在.

证明 记  $ a_{n}=\left(1+\frac{1}{n}\right)(n=1,2,\cdots) $. 先来证明数列  $ \{a_{n}\} $ 单调递增：  $ \forall n\in\mathbb{N}^{*} $,