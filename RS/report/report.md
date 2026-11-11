# Recurrent Neural Networks (RNNs)
## Background, Limitations, and the LSTM Solution

---

## 1. Background of Recurrent Neural Networks

Recurrent Neural Networks (RNNs) are a family of neural networks designed specifically for **processing sequential data**. Unlike conventional feedforward networks, RNNs process data sequentially and maintain a **hidden state** that carries information from previous time steps.

For example:

```text
x(1), x(2), x(3), ..., x(t)
```

At each time step, the RNN receives the current input and the hidden state from the previous time step:

```text
                 ┌───────────────┐
x(t) ───────────►│               │
                 │      RNN      │───► h(t)
h(t-1) ─────────►│               │
                 └───────────────┘
```

The basic recurrent operation can be represented as:

$h^{(t)} = f(h^{(t-1)}, x^{(t)};\theta)$

where:

- $(x^{(t)})$ = input at time $(t)$
- $(h^{(t)})$ = hidden state at time $(t)$
- $(h^{(t-1)})$ = previous hidden state
- $(f)$ = recurrent transformation
- $(\theta)$ = model parameters

The hidden state acts as a **summary of the information seen so far**. However, this summary is generally lossy because an arbitrarily long sequence must be represented by a fixed-size vector.

---

## 1.1 Parameter Sharing

One of the most important characteristics of RNNs is **parameter sharing across time**.

Instead of learning separate parameters for every position in a sequence, the same parameters are reused at every time step. This allows the network to process sequences of different lengths and generalize across different positions in a sequence.

For example:

```text
x(t-1) ──► h(t-1) ──► h(t) ──► h(t+1)
              │          │          │
              └──── same parameters ────┘
```

This is one of the fundamental ideas behind recurrent networks.

---

## 1.2 Unfolding an RNN

An RNN can be represented as a recurrent loop:

```text
          ┌──────────┐
          │          │
          ▼          │
        h(t) ────────┘
          ▲
          │
        x(t)
```

For training, this recurrent structure can be **unfolded through time**:

```text
x(t-1)        x(t)        x(t+1)
  │             │             │
  ▼             ▼             ▼
h(t-1) ──────► h(t) ───────► h(t+1)
```

Unfolding makes the flow of information and gradients through time explicit. The same parameters are used at every step.

---

## 1.3 Standard RNN Equations

A representative RNN uses the following equations:

$a^{(t)} = b + Wh^{(t-1)} + Ux^{(t)}$

$h^{(t)} = \tanh(a^{(t)})$

$o^{(t)} = c + Vh^{(t)}$

$\hat{y}^{(t)} = \text{softmax}(o^{(t)})$

where:

- $(U)$ = input-to-hidden weights
- $(W)$ = hidden-to-hidden/recurrent weights
- $(V)$ = hidden-to-output weights
- $(b,c)$ = bias vectors
- $(h^{(t)})$ = hidden state
- $(\hat{y}^{(t)})$ = predicted output

These equations describe how the RNN processes each time step.

---

# 2. Cons / Limitations of RNNs

Although RNNs are useful for sequential data, ordinary RNNs have several important limitations.

The most important one is their difficulty in learning **long-term dependencies**.

---

## 2.1 Vanishing Gradient Problem

When an RNN is trained over a long sequence, gradients have to propagate backward through many time steps.

This process involves repeatedly multiplying derivatives/Jacobians.

Conceptually:

$
\frac{\partial L}{\partial h^{(t-k)}} =
\frac{\partial L}{\partial h^{(t)}}
\prod_{i=t-k+1}^{t}
\frac{\partial h^{(i)}}{\partial h^{(i-1)}}
$

If the values involved in this repeated multiplication are smaller than 1, the gradient can become extremely small.

This is called the **vanishing gradient problem**.

### Effect

The network receives an extremely weak learning signal from distant time steps.

Therefore, it becomes difficult for the RNN to learn relationships where an earlier input is important for a much later prediction.

```text
Important information
       │
       ▼
t=1 ──► t=2 ──► t=3 ──► ... ──► t=50
                                      │
                                      ▼
                                  Prediction
```

---

## 2.2 Exploding Gradient Problem

The opposite problem can also occur.

If repeated multiplication causes the gradients to grow rather than shrink, their magnitude can become extremely large.

This is called the **exploding gradient problem**.

Large gradients can result in extremely large parameter updates and unstable training.

### Gradient Clipping

A common technique for dealing with exploding gradients is **gradient clipping**.

If the gradient norm is larger than some threshold \(v\):

$|g| > v$

the gradient can be rescaled:

$g \leftarrow g\frac{v}{|g|}$

This limits the magnitude of the update while preserving its direction.

> **Gradient clipping helps with exploding gradients, but it does not solve the vanishing-gradient problem.**

---

## 2.3 Difficulty Learning Long-Term Dependencies

A normal RNN must carry information through its recurrent hidden state:

```text
h(t-3) → h(t-2) → h(t-1) → h(t)
```

For short dependencies this can work well.

However, for very long dependencies, information has to pass through many recurrent transformations. Consequently, the network can have difficulty remembering information from far back in the sequence.

Specialized mechanisms are therefore needed to create paths through the recurrent computation where gradients can remain sufficiently large for long-term dependencies.

---

## 2.4 Sequential Computation

RNNs are inherently sequential.

To calculate:

$h^{(t)}$

we need:

$h^{(t-1)}$

and therefore cannot calculate all hidden states independently.

```text
h(1) → h(2) → h(3) → h(4) → h(5)
```

This limits parallelization across time steps.

Training with Back-Propagation Through Time (BPTT) requires processing the sequence through time and storing intermediate states.

---

## 2.5 Fixed-Size Hidden-State Bottleneck

An RNN compresses the history of a sequence into a fixed-size hidden vector:

$(x^{(1)},x^{(2)},...,x^{(t)})
\rightarrow h^{(t)}$

This means that an arbitrarily long sequence must ultimately be represented by a fixed-size vector.

Consequently, the hidden state can act as a **lossy summary** of the past.

---

# 3. LSTM: A Solution to the RNN Problem

**Long Short-Term Memory (LSTM)** is a type of gated RNN designed to make learning **long-term dependencies easier**.

The key idea behind LSTM is to introduce an internal memory/cell state with a **self-loop whose behavior is controlled by gates**.

---

## 3.1 The Key Idea Behind LSTM

A traditional RNN essentially has:

```text
       x(t)
        │
        ▼
   ┌─────────┐
   │   RNN   │
   └─────────┘
        │
        ▼
      h(t)
        │
        ▼
     next step
```

LSTM introduces an additional memory pathway:

```text
                 ┌─────────────────────┐
                 │     Cell State       │
                 │         c(t)         │
                 └─────────────────────┘
                    ▲      ▲       │
                    │      │       │
              Forget   Input    Output
               Gate     Gate      Gate
```

The cell state provides a path through time along which information can persist.

The LSTM cell contains a linear self-loop whose effective weight is controlled by the forget gate.

---

## 3.2 Why the Self-Loop Helps

Conceptually:

```text
RNN:

h(t-1) ──► transformation ──► h(t)
               │
               ▼
          repeated nonlinear
          transformations


LSTM:

c(t-1) ───────────────► c(t)
       controlled by
       forget gate
```

The LSTM cell state provides a more direct path for information and gradients across many time steps.

When the forget gate allows the state to be retained, useful information can persist over a longer period.

---

# 3.3 The Three Main LSTM Gates

An LSTM primarily uses three gates:

1. **Forget gate**
2. **Input gate**
3. **Output gate**

---

## 3.3.1 Forget Gate

The forget gate determines how much of the previous cell state should be retained.

It is calculated using a sigmoid:

$f^{(t)} =
\sigma
\left(
b_f + U_f x^{(t)} + W_f h^{(t-1)}
\right)$

Since the sigmoid produces values between 0 and 1, the gate can control the amount of information retained.

Conceptually:

```text
Previous memory
      │
      ▼
  Forget Gate
      │
 ┌────┴────┐
 │         │
retain    forget
more      more
 │         │
 ▼         ▼
Memory    Remove
```

---

## 3.3.2 Input Gate

The input gate determines how much new information should be added to the cell state.

It is also calculated using a sigmoid:

$g^{(t)} =
\sigma
\left(
b_g + U_gx^{(t)} + W_gh^{(t-1)}
\right)$

The cell state can conceptually be updated as:

$s^{(t)}
=
f^{(t)}s^{(t-1)}
+
g^{(t)}\cdot candidate^{(t)}$

Therefore:

- $(f^{(t)})$ controls **what old information is kept**
- $(g^{(t)})$ controls **what new information is added**

---

## 3.3.3 Output Gate

The output gate determines how much of the internal cell state should be exposed as the hidden output.

The LSTM formulation gives:

$h_i^{(t)}
=
\tanh(s_i^{(t)})q_i^{(t)}$

where \(q_i^{(t)}\) is the output gate.

Conceptually:

```text
       Cell State
           │
           ▼
      Output Gate
           │
           ▼
      Hidden State
```

Thus, the LSTM can maintain information internally without necessarily exposing all of it at every time step.

---

# 3.4 How LSTM Solves the RNN Problem

The relationship can be summarized as:

| Problem in RNN | LSTM mechanism | Effect |
|---|---|---|
| Vanishing gradients | Cell-state self-loop | Provides a path for information/gradients across many steps |
| Difficulty remembering old information | Forget gate | Controls how much previous memory is retained |
| New information may overwrite useful memory | Input gate | Controls how much new information enters memory |
| Internal memory should not always be exposed | Output gate | Controls what becomes the hidden output |
| Long-term dependency learning | Gated memory pathway | Makes long-term dependencies easier to learn |

The supplied LSTM material reports that LSTMs learn long-term dependencies more easily than simple recurrent architectures.

---

# 3.5 RNN vs LSTM

### Ordinary RNN

```text
       x(t)
        │
        ▼
   ┌─────────┐
   │   RNN   │
   └─────────┘
        │
        ▼
      h(t)
        │
        ▼
     next step
```

The hidden state has to carry the relevant information from the past.

### LSTM

```text
             ┌─────────────────────┐
             │     Cell State       │
             │         c(t)         │
             └─────────────────────┘
                 ▲     ▲      │
                 │     │      │
              Forget Input  Output
               Gate   Gate   Gate
                 ▲     ▲      │
                 │     │      ▼
                x(t)  h(t-1) h(t)
```

The LSTM separates the **memory pathway** from the ordinary hidden output pathway and uses gates to control information flow.

---

# 4. Conclusion

RNNs were developed to process **sequential data** by maintaining a hidden state that carries information from one time step to the next. Parameter sharing allows the same recurrent transformation to be applied across the entire sequence.

However, ordinary RNNs face significant difficulties when learning **long-term dependencies**. During back-propagation through time, gradients can vanish or explode as they pass through many recurrent steps. RNNs also require sequential computation and compress the history of the sequence into a fixed-size hidden state.

LSTM addresses the long-term dependency problem by introducing a **cell state and gated information flow**. The forget gate controls what information should be retained, the input gate controls what new information should be stored, and the output gate controls what information should be exposed.

The central idea can be summarized as:

> **RNN:** Carry the past through a recurrent hidden state.  
>
> **LSTM:** Carry the past through a gated memory pathway that learns what to keep, what to add, and what to expose.

---

## References

> DEEP LEARNING by lan Goodfellow, Yoshua Bengio,and Aaron Courville
