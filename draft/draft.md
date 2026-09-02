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

1. **The missing bridge.**  Put predicate-aware execution specifications on
   the left and predicate dependency graphs/downstream analyses on the right.
   The red, dashed middle panel is the central gap: no exact two-way
   execution--graph characterization for histories that contain predicate
   observations.  This replaces the weaker claim that predicates merely cause
   phantoms.
2. **Why predicates are different.**  Reuse the running predicate-observation
   example: a query observes both returned items and covered items that are
   absent.  A phantom is a change to that absence, so a graph must record a
   version witness for an omitted key.
3. **The proof obligation.**  State the target as an iff: a SER/SI execution
   exists iff an appropriate predicate dependency graph exists.  Explain that
   recovering a legal execution from a graph is the difficult direction.

`contribution.tex`
# Contributions

1. **Solution overview figure.**  Mirror the gap figure: semantic interface
   and dependency graph are now connected by an extraction/recovery bridge;
   both feed into exact SER/SI theorems, and the graph side additionally feeds
   the anti-dependency design space.  The two results feed a reusable
   correctness contract for downstream work.
2. **Four contributions.**  (i) item-wise external predicate semantics in
   $(VIS,AR)$; (ii) $PredWR$, $PredRW$, and observation change $\Delta$;
   (iii) exact SER/SI characterizations and the SI witness-ambiguity repair;
   (iv) the lower-frontier/upper-closure interval.
3. **Claim boundary.**  Emphasize that this is a theory contribution enabling
   tools, not an unsubstantiated claim of a faster full SQL checker or a direct
   identity between physical lock events and semantic graph edges.

`tech.tex`

1. **External observation witness.**  Use a three-transaction example in
   which $T$ omits $x$ from a predicate result because $U$ wrote $x=80$ and a
   later $S$ writes $x=40$.  Show $PredWR$, $WW$, and the resulting $PredRW$
   edge: absence is semantically explained, rather than treated as missing
   data.
2. **Mismatch-to-edge proof move.**  Explain the constructive direction:
   when the execution reconstructed from a graph selects a different latest
   visible writer, observable disagreement forces a predicate anti-dependency,
   contradicting the graph condition.
3. **Proof-relevant design space.**  Visualize
   $PredRW^+\subseteq\mathcal R\subseteq PredRW^-$.  The lower frontier
   exposes violations; the upper closure is safe to orient; the relations may
   differ on fixed graphs while preserving the same existential SER/SI result.

`future.tex`

1. **Predicate-aware stateless model checking.**  Build a theorem-specific
   checker kernel/policy laboratory: construct the common base, use
   lower/upper relations for pruning and refinement, validate with bounded
   $(VIS,AR)$ enumeration, and return locally checkable anomaly certificates.
   This is deliberately more specific than ``build another black-box checker.''
2. **Predicate-aware robustness analysis.**  Lift item-only robustness from
   histories to transaction programs: use a finite predicate/write abstraction
   and SMT/CEGAR search to determine whether all SI executions are serializable
   in the presence of phantoms.
3. **Certified DBMS-event abstraction.**  Prove when recorded range/predicate
   conflict events are sound lower or upper approximations of semantic edges;
   connect one real DBMS trace adapter to the common history model without
   conflating physical locks with committed-history dependencies.
