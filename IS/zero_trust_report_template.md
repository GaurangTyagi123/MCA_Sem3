# Zero-Trust Security and Dynamic Trust Evaluation of IoT Devices

**name:** Gaurang TYagi
**Date:** 24/10/26



## 1. Introduction and Literature Review

### 1.1 Background

In Zero Trust, the rule is “never trust, always verify”. A device is not trusted just because it behaved well yesterday. Its trust must be re-checked continuously.

### 1.2 Aim and Objectives

This project implements a small, reproducible trust-scoring simulation. At every time step it calculates Behaviour (B), Context (C), History (H) and Risk (R), combines them into a security assessment, updates a running trust score, and maps the score to ALLOW, MONITOR, RESTRICT or ISOLATE.


## 2. IoT Simulation

### 2.1 Simulated Devices

\[Describe the five simulated devices and why their expected behaviour
differs.\]

  -----------------------------------------------------------------------------
| Device ID | Device type | Expected normal behaviour / permitted destinations | Criticality |
|---|---|---|---|
| D1 | Smart Camera | Sends video streams and periodic status updates to an authorized local video server; uses predictable bandwidth and operates mainly during configured monitoring hours. | High |
| D2 | Smart Sensor | Sends periodic temperature or environmental readings to an authorized monitoring server; low bandwidth and regular transmission intervals. | Medium |
| D3 | Smart Lock | Exchanges authentication and lock-status messages with an authorized access-control server; accepts commands only from trusted controllers. | Critical |
| D4 | Smart TV | Communicates with authorized streaming, media, and update services; traffic varies with user activity. | Low |
| D5 | Medical/Environmental Sensor | Sends regular sensor readings and alerts to an authorized monitoring gateway; requires reliable communication and prompt delivery of critical readings. | Critical |
  -----------------------------------------------------------------------------

### 2.2 Simulated States

\[Explain how Normal, Suspicious, Attack-like, and Recovery states are
represented and how the simulation transitions between them.\]

### 2.3 Dataset

\[Report the number of devices, time steps per device, total rows,
random seed, and CSV columns. Verify these against the notebook and
exported CSV.\]

## 3. Dynamic Trust Model

### 3.1 Trust Inputs

\[Define Behaviour (B), Context (C), History (H), and Risk (R) as
implemented in your code. Explain how each is calculated.\]

### 3.2 Trust Equations

\[Insert and explain the exact equations used in your implementation.
Define every symbol and list the weights.\]

### 3.3 Memory Factor and Decision Thresholds

\[Explain the role of alpha and document the actual thresholds used for
ALLOW, MONITOR, RESTRICT, and ISOLATE.\]

### 3.4 Resource Awareness

\[Explain how CPU, memory, and battery are simulated, and describe any
way resource conditions affect the trust calculation or weights.\]

## 4. Experimental Setup

\[Document the Python environment and libraries, random seed, simulation
length, device scenarios, attack-like conditions, recovery behaviour,
and values of alpha compared. Describe how each performance metric is
calculated.\]

## 5. Results

### 5.1 Trust Score Over Time

**Insert Graph 1 here.**\
**Figure 1.** \[Write a caption describing the device, states, and main
pattern visible in the plot.\]

\[Describe what you observe directly from the graph and connect it to
the simulated states.\]

### 5.2 Behaviour Over Time

**Insert Graph 2 here.**\
**Figure 2.** \[Write a caption.\]

\[Describe the behaviour score across the states and point to relevant
time ranges.\]

### 5.3 Trust Inputs Over Time

**Insert Graph 3 here.**\
**Figure 3.** \[Write a caption.\]

\[Compare B, C, H, and R using the plotted values. Explain any important
changes.\]

### 5.4 Trust and Decision Thresholds

**Insert Graph 4 here.**\
**Figure 4.** \[Write a caption.\]

\[Explain when the trust line crosses thresholds and which decisions
result.\]

### 5.5 Performance Metrics

\[Insert the verified performance metrics table from your CSV.\]

  ---------------------------------------------------------------------------
  Device ID    Detection         False     Recovery        Trust  Mean normal
                   delay   restriction         time    stability        trust
                                  rate                           
  --------- ------------ ------------- ------------ ------------ ------------
  D1           \[Value\]     \[Value\]    \[Value\]    \[Value\]    \[Value\]

  D2           \[Value /     \[Value\]    \[Value /    \[Value\]    \[Value\]
                   N/A\]                      N/A\]              

  D3           \[Value\]     \[Value\]    \[Value\]    \[Value\]    \[Value\]

  D4           \[Value\]     \[Value\]    \[Value\]    \[Value\]    \[Value\]

  D5           \[Value\]     \[Value\]    \[Value\]    \[Value\]    \[Value\]
  ---------------------------------------------------------------------------

\[Define the metric units and explain any N/A values. Do not treat a
missing value as zero.\]

### 5.6 Comparison of Alpha Values

\[Insert or summarize the alpha-comparison CSV. Explain the observed
trade-off between responsiveness, stability, and recovery using actual
values.\]

### 5.7 Security Events

\[Include 5--10 verified records from security_events.csv. Explain the
event time, state, trust change, decision, and recorded reason.\]

## 6. Discussion

\[Interpret the results against your objectives. Discuss detection
behaviour, false restrictions, recovery, trust stability, differences
among devices, the alpha comparison, and resource-awareness behaviour.
Separate observations from possible explanations.\]

## 7. Limitations

\[Describe at least two limitations of the simulation. Consider
synthetic data, manually selected weights or thresholds, simplified
attack patterns, and dependence on the chosen random seed where
applicable.\]

## 8. Conclusion

\[Summarize what you implemented, the main findings supported by your
results, and one or two realistic improvements for future work.\]

## References

\[Provide complete references for every paper, standard, library, or
external source cited in the report. Use one consistent citation style
and verify all bibliographic details.\]

## Final Verification Checklist

-   [ ] Notebook runs from top to bottom without errors.
-   [ ] CSV row count and required columns have been verified.
-   [ ] All four graphs are included, readable, numbered, and captioned.
-   [ ] Metrics and security events match the exported CSVs.
-   [ ] Missing values are explained rather than silently replaced with
    zero.
-   [ ] The report's claims are supported by my own outputs.
-   [ ] References and permitted assistance are acknowledged accurately.
-   [ ] Report length meets the assignment's 5--7 page requirement.
