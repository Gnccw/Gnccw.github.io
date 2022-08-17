### 1、基本概念

1. **s-polytope:** An `s-polytope` in $F_{2}^{n}$ is an s-tuple of values in $F_{2}^{n}$ .

2. **d-difference**:  A `d-difference` over $F_{2}^{n}$ is a d-tuple of values in $F_{2}^{n}$ describing the relative position of the texts of a `(d+1)-polytope` from one point of reference. 

&emsp;**convention**: For a `(d+1)-polytope` $(m_{0},m_{1},\cdots,m_{d})$ , the corresponding `d-difference` is created as $(m_{0}\oplus m_{1},m_{0}\oplus m_{2},\cdots,m_{0}\oplus m_{d})$ .

### 2、undisturbed bits 和 d-difference

对于几乎所有的操作来说，`d-difference` 的undisturbed-bits并没有增加undisturbed-bits的数量，只是简单的多个差分集合的连接，导致并不能搜索到更长的不可能差分。

$$\Delta X \rightarrow \alpha \neq \beta \leftarrow \Delta Y$$

$$\Delta X' \rightarrow \alpha' \neq \beta' \leftarrow \Delta Y'$$

相当于是两条不可能差分迹的并行，最多能够增加一部分中间比特的矛盾$(0,1)(1,0)\Rightarrow (0,1)(1,0),(1,0)(0,1)$ .