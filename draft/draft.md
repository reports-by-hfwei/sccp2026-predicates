# Draft

`section/item-predicate.tex`

# Item Operations vs. Predicate Operations

3 cols of equal width

left:
Read(x, v)     Read(2, 60)
Write(x, v)    Write(3, 40)

point access
single value

mid:
a kv table
Employee

EID  Salary
0    80
1    100
2    60
3    40

right:
PredRead(P, M)

condition-based access
set of values

`section/review-wo-predicates.tex`

# Review

What we know about
transactional consistency models *without* predicates
in terms of both specs and graph-based characterizations.

# Review: Intuitive or Operational Specs

left:
SER: Serializability

fig for notions-cacm1976

right:
SI: Snapshot Isolation

fig for critique-sigmod1995, si-sigmod1995

# Review: Axiomatic Specs

3 cols

left:
fig for framework-concur2015

(VIS, AR)

mid:
fig for clientcentric-podc2017

right:
fig for complexity-oopsla2019

# Review: Extract Dependency Graphs from Histories

fig for notions-cacm1976, cc-stoc1976

# Review: SER Characterization Theorem

fig for notions-cacm1976, cc-stoc1976, adya-phdthesis1999, analysingsi:jacm2018

\begin{theorem}
\end{theorem}

# Review: SI Characterization Theorem

fig for analysingsi-jacm2018

\begin{theorem}
\end{theorem}

`section/review-wo-predicates.tex`

# Review: Downstream Tasks

2-cols table: Tasks & Refs
Black-box Checking & elle-vldb2020, cobra-osdi2020, polysi-vldb2023, viper-eurosys2023, veristrong-vldb2026
CC Protocol &
Verification & xiong-phdthesis2019
Robustness & ra-concur2016

# Review

What we know about
transactional consistency models *with* predicates

# Review: Intuitive or Operational Specs

left:
SER: Serializability

fig for notions-cacm1976

right:
SI: Snapshot Isolation

fig for critique-sigmod1995, si-sigmod1995

# Review: Axiomatic Specs

fig for complexity-cav2025
fig for specs-cav2025

checking-oriented axiom grammar???

# Review: Dependency Graphs

fig for adya-phdthesis1999

Give an concrete example here for predicate read dependency
and predicate anti-dependency

# Review: Dependency Graphs
fig for adya-icde2000, vbox-arxiv2025, complexity-cav2025

Different definitions of predicate read dependency and predicate anti-dependency

# Review: SER Characterization

citation relation between cc:bernstein1987, gray:book1993, adya-phdthesis1999, adya-icde2000, makingsersi-tods2005, emme-eurosys2024, vbox-arxiv2025,  order-tocs2026

fig for proof-phdthesis1999

No rigorous proof!

# Review: SI Characterization

fig for adya-phdthesis1999

`problem.tex`
# The Problem