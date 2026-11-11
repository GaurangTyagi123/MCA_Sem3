# Recommender Systems Notes: Matrix Factorization, NMF, and Dimensionality Reduction

These notes summarize the concepts explained in our chat, with definitions, equations, intuition, and numerical examples.

---

## 1. Latent Factor Models

### Core idea
A user-item ratings matrix often contains repeated patterns. Instead of modeling every user-item relationship independently, a latent factor model represents users and items using a small number of hidden characteristics called **latent factors**.

For example, in a movie recommender, latent factors might loosely correspond to action preference, comedy preference, or romance preference. The factors do not always have an obvious real-world meaning.

### Matrix factorization
Approximate the ratings matrix \(R\) as:

\[
R \approx UV^T
\]

- \(R\): user-item matrix, with \(m\) users and \(n\) items.
- \(U\): user-factor matrix, size \(m \times k\).
- \(V\): item-factor matrix, size \(n \times k\).
- \(k\): number of latent factors, usually much smaller than \(m\) and \(n\).

For user \(i\) and item \(j\), the predicted rating is:

\[
\hat r_{ij}=u_i^T v_j=u_i\cdot v_j
\]

Here, \(u_i\) and \(v_j\) are the factor vectors for user \(i\) and item \(j\). The transpose notation \(u_i^T v_j\) and dot-product notation \(u_i\cdot v_j\) both represent the same dot product.

### Why use latent factors?
- Compresses a large user-item matrix into smaller representations.
- Can infer missing ratings from patterns in known ratings.
- Can generalize to user-item pairs that were not observed.
- Captures relationships that are not explicitly represented as input features.

### Low-rank intuition
If many features or ratings are correlated, the data may be explained by fewer underlying patterns. A low-rank approximation tries to retain those patterns using fewer dimensions.

---

## 2. Stochastic Gradient Descent (SGD) for Matrix Factorization

SGD updates factor vectors using one observed rating at a time.

For an observed rating \(r_{ij}\):

\[
e_{ij}=r_{ij}-u_i^T v_j
\]

A basic update is:

\[
u_i \leftarrow u_i+\alpha e_{ij}v_j
\]

\[
v_j \leftarrow v_j+\alpha e_{ij}u_i
\]

- \(e_{ij}\): prediction error.
- \(\alpha\): learning rate.
- The updates move the factors to reduce the error.

In a practical implementation, both updates should use the intended old/current factor values consistently. Regularization can be added to discourage excessively large factor values and reduce overfitting.

### SGD intuition
1. Predict a rating.
2. Calculate the error.
3. Adjust the user and item factors.
4. Repeat for observed ratings over multiple passes.

SGD requires choosing a learning rate. A learning rate that is too high can make learning unstable; one that is too low can make it slow.

---

## 3. Alternating Least Squares (ALS)

ALS is another way to learn the factor matrices.

### Main procedure
1. Fix the user-factor matrix \(U\).
2. Solve for the item-factor vectors in \(V\), using least squares.
3. Fix \(V\).
4. Solve for the user-factor vectors in \(U\).
5. Repeat until the solution stabilizes.

Each user or item subproblem can often be solved independently while the opposite factor matrix is fixed.

### Example from our chat

Observed ratings:

\[
R=\begin{bmatrix}
5&3\\
4&?
\end{bmatrix}
\]

There are two users, two movies, and one latent factor (\(k=1\)). Start with all factors equal to 1 and ignore regularization.

#### ALS: update item factors first
Fix \(u_1=u_2=1\).

For Movie 1, the observed ratings are 5 and 4. Its objective is:

\[
J(v_1)=(5-u_1v_1)^2+(4-u_2v_1)^2
\]

Substitute \(u_1=u_2=1\):

\[
J(v_1)=(5-v_1)^2+(4-v_1)^2
\]

This is the sum of squared errors for the two observed ratings. Minimizing it gives:

\[
v_1=\frac{5+4}{2}=4.5
\]

For Movie 2, only the rating 3 is observed:

\[
J(v_2)=(3-v_2)^2
\]

So:

\[
v_2=3
\]

#### ALS: update user factors
Now fix \(v_1=4.5\) and \(v_2=3\).

For User 1, the least-squares solution is:

\[
u_1=\frac{4.5(5)+3(3)}{4.5^2+3^2}
=\frac{31.5}{29.25}\approx1.0769
\]

For User 2, only Movie 1's rating is observed:

\[
u_2=\frac{4}{4.5}\approx0.8889
\]

The missing rating is estimated as:

\[
\hat r_{22}=u_2v_2\approx0.8889(3)\approx2.67
\]

This is the estimate after one ALS iteration; it may change with more iterations and with regularization.

### SGD vs. ALS

| SGD | ALS |
|---|---|
| Updates factors using one observed rating at a time | Alternates between solving for user and item factors |
| Uses a learning rate | Does not use an SGD-style learning rate |
| Often efficient for very large sparse explicit-rating data | Subproblems can be parallelized; weighted ALS is widely used for implicit feedback |
| Sensitive to learning-rate choice | Can be more stable with respect to step-size issues, though it has its own computational trade-offs |

---

## 4. Singular Value Decomposition (SVD)

### Basic form
SVD decomposes a matrix into three matrices:

\[
R=Q\Sigma P^T
\]

- \(Q\): left singular vectors.
- \(\Sigma\): diagonal matrix of singular values.
- \(P\): right singular vectors.

A truncated rank-\(k\) approximation is:

\[
R\approx Q_k\Sigma_kP_k^T
\]

Keeping the largest singular values retains the most important components according to the SVD approximation criterion.

### Geometric intuition
SVD identifies orthogonal directions that describe patterns in the matrix. The singular values indicate the importance or strength of those directions.

### SVD in recommender systems
Real rating matrices usually contain missing entries, so ordinary SVD cannot simply be applied to the incomplete matrix as if every entry were known. One approach described in the book is to:
1. Center observed ratings by subtracting user means.
2. Fill missing centered entries with zero (equivalent to the user's average on the original rating scale).
3. Apply a low-rank SVD.
4. Re-estimate missing entries and repeat.

This approach can introduce bias because the initial imputed values are estimates, not real observations.

### Important distinction: SVD vs. matrix factorization
In recommender-system literature, “SVD” is sometimes used loosely to describe learned low-rank matrix factorization. Such methods do not necessarily use the orthogonal singular vectors of classical SVD. For example, learned factor vectors need not be orthogonal.

---

## 5. Non-Negative Matrix Factorization (NMF)

### Definition
NMF approximates a non-negative matrix \(R\) using two non-negative factor matrices:

\[
R\approx UV^T
\]

subject to:

\[
U\geq0,\qquad V\geq0
\]

A basic objective is:

\[
\min_{U,V} J=\frac12\|R-UV^T\|_F^2
\]

The goal is to make the reconstructed matrix \(UV^T\) close to \(R\), while keeping every factor value non-negative.

### Why non-negativity matters
NMF's main advantage is often **interpretability**. Positive factors can represent additive aspects, such as:
- dairy preference,
- drinks preference,
- action-movie preference,
- comedy-movie preference.

NMF is especially useful when matrix entries represent positive activity, such as purchases, clicks, likes, or browsing frequency.

### How NMF learns the factors
A typical iterative process is:
1. Initialize \(U\) and \(V\) with non-negative values.
2. Reconstruct the matrix using \(UV^T\).
3. Measure the reconstruction error.
4. Update the factor values using a suitable NMF algorithm, such as multiplicative updates or constrained optimization.
5. Repeat until convergence.

Regularization can be added to discourage overly large factor values and reduce overfitting.

### Limitations
- Standard NMF requires a non-negative input matrix.
- The non-negativity constraint can increase reconstruction error on observed data compared with an unconstrained model.
- Semantic interpretability depends on the dataset and the learned factors.
- If explicit ratings include both likes and dislikes, the additive interpretation may be less meaningful.
- Treating missing implicit-feedback entries as zero is a modeling assumption and can introduce bias.

---

## 6. The “Sum-of-Parts” Interpretation in NMF

### Main idea
A predicted user-item value is the sum of the contributions of each latent aspect:

\[
\hat r_{ij}=\sum_{s=1}^{k}u_{is}v_{js}
\]

Each product \(u_{is}v_{js}\) is the contribution of aspect \(s\) to the prediction.

### Numerical example
Suppose User 1 has these factors:

\[
u_1=[0.8,\ 0.1]
\]

The two aspects are dairy and drinks.

Suppose Milk has factors:

\[
v_{\text{Milk}}=[5,\ 0]
\]

Then:

\[
\begin{aligned}
\hat r_{\text{User 1, Milk}}
&=(0.8\times5)+(0.1\times0)\\
&=4+0\\
&=4
\end{aligned}
\]

Interpretation:
- Dairy contributes 4.
- Drinks contributes 0.
- Total prediction = 4.

For Juice, suppose:

\[
v_{\text{Juice}}=[0,\ 4]
\]

Then:

\[
\begin{aligned}
\hat r_{\text{User 1, Juice}}
&=(0.8\times0)+(0.1\times4)\\
&=0+0.4\\
&=0.4
\end{aligned}
\]

The predicted value is 0.4, coming from the drinks aspect.

These are illustrative factor values, not probabilities or real learned ratings.

### Matrix form of sum-of-parts
The full factorization can be written as:

\[
UV^T=\sum_{s=1}^{k}U_sV_s^T
\]

Here, \(U_s\) and \(V_s\) are the \(s\)-th columns of the factor matrices. Each product \(U_sV_s^T\) is a rank-one matrix representing one aspect's contribution to the reconstructed matrix.

### Why this is useful
NMF can help explain a prediction by showing which latent aspects contributed to it. Ordinary matrix factorization also sums factor contributions mathematically, but because its factors may be negative, the contributions can cancel one another and may be harder to interpret semantically.

---

## 7. Implicit Feedback and Missing Entries

### Explicit feedback
The user directly provides a rating, such as 1–5 stars. This can express both liking and disliking.

### Implicit feedback
The system observes behavior, such as:
- buying a product,
- clicking an item,
- watching a video,
- browsing a page,
- liking a post.

Such activity usually indicates positive interest, but absence of activity does not necessarily mean dislike.

### Why zero treatment matters
For purchase-count data, an unpurchased item may reasonably be represented by zero when the data captures all relevant purchases. But a missing value can also mean the user never saw the item or purchased it elsewhere.

For implicit-feedback matrix factorization, treating all missing entries as zero can create a huge number of zero-valued entries. The book discusses sampling zero entries or assigning them lower weights so that zeros do not dominate the objective.

**Remember:** an observed positive interaction is evidence of activity; an unobserved interaction is not automatically evidence of dislike.

---

## 8. Geometric Meaning of Dimensionality Reduction

### What is a dimension?
A dimension corresponds to a coordinate or feature needed to represent a data point.

For example, a point described by three features:

\[
\mathbf{x}=(x_1,x_2,x_3)
\]

lies in a 3D feature space.

### Correlated features
Suppose three features—action, superhero, and adventure preference—are strongly correlated. Data points may lie close to a plane or line instead of filling the entire 3D space.

This suggests that fewer underlying directions may explain most of the variation.

### Projection
Dimensionality reduction represents the data using fewer coordinates, ideally preserving important patterns.

For example, if points lie exactly on the line \(y=x\), then the second coordinate is redundant once the first is known. A 2D representation can be reduced to one coordinate along the line.

One possible coordinate is:

\[
z=\frac{x+y}{\sqrt2}
\]

For the point \((3,3)\):

\[
z=\frac{3+3}{\sqrt2}=3\sqrt2
\]

Because the points lie exactly on the line, this reduction loses no information about their positions along that line. In real datasets, reduction is often approximate.

### Connection to matrix factorization
Suppose there are 1,000 users and 500 items. The rating matrix has 500,000 possible entries. A factorization with \(k=10\) represents:
- each user using 10 latent values,
- each item using 10 latent values.

The prediction is computed from the dot product of their factor vectors.

**Important distinction:** PCA projects data onto directions in the original feature space, while recommender-system matrix factorization learns user and item representations that reconstruct the rating matrix. Both use lower-dimensional representations, but their objectives differ.

---

## 9. Quick Comparison

| Method | Main idea | Main strength | Important limitation |
|---|---|---|---|
| Latent factor model | Represent users and items with hidden factors | Captures compact patterns | Factors may be hard to interpret |
| SGD matrix factorization | Update factors using observed ratings one at a time | Flexible and often efficient | Needs learning-rate tuning |
| ALS | Alternate least-squares solutions for users and items | Parallelizable subproblems; useful for implicit feedback variants | Can be computationally expensive |
| SVD | Use orthogonal singular directions and singular values | Strong mathematical/geometric interpretation | Missing ratings require care |
| NMF | Factorize with non-negative factors | Sum-of-parts interpretability | Requires non-negative factors and can be less flexible |
| Dimensionality reduction | Represent data with fewer coordinates | Simplifies data while retaining useful structure | Some information may be lost |

---

## 10. Key Equations to Remember

**Matrix factorization**

\[
R\approx UV^T
\]

**Predicted rating**

\[
\hat r_{ij}=u_i^Tv_j
\]

**SGD error**

\[
e_{ij}=r_{ij}-u_i^Tv_j
\]

**Basic SGD updates**

\[
u_i\leftarrow u_i+\alpha e_{ij}v_j
\]

\[
v_j\leftarrow v_j+\alpha e_{ij}u_i
\]

**Truncated SVD**

\[
R\approx Q_k\Sigma_kP_k^T
\]

**NMF objective and constraints**

\[
\min_{U,V}\frac12\|R-UV^T\|_F^2
\quad\text{subject to}\quad U,V\geq0
\]

**NMF sum of parts**

\[
\hat r_{ij}=\sum_{s=1}^{k}u_{is}v_{js}
\]

**Dimensionality reduction example**

\[
z=\frac{x+y}{\sqrt2}
\]

---

## Final mental model

- **Latent factor models:** learn compact representations of users and items.
- **SGD:** adjusts factors a rating at a time.
- **ALS:** alternates between solving for user and item factors.
- **SVD:** identifies important orthogonal directions.
- **NMF:** uses non-negative factors that can be interpreted as additive aspects.
- **Sum of parts:** each aspect contributes to a prediction, and those contributions add up.
- **Dimensionality reduction:** represents data in fewer dimensions while preserving useful structure.
