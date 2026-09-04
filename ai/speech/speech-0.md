# Speech

## Specifying and Analyzing Transactional Consistency Models with Predicates

Consider a transaction that asks for all open orders. What matters is not only what it returns, but also what it omits: a concurrent insert can turn an omitted item into a phantom. [PAUSE] Our question is how to reason about such observations with the same precision we already have for item reads.

## Item Operations vs. Predicate Operations

An item read names one key and returns one value. A predicate read selects a set by a condition, so both matched and omitted covered items can matter under concurrency.

## Review

I will first separate what is well understood without predicates from what becomes unclear once predicates are admitted.

## Review: Intuitive or Operational Specs

For item operations, the intuition is classical: serializability corresponds to serial execution, while snapshot isolation combines a snapshot with write-conflict control.

## Review: Axiomatic Specs

The visibility-and-arbitration framework gives an implementation-independent semantic language and supports reasoning without committing to a particular protocol.

## Review: Dependency Graphs

The graph view summarizes conflicts through read, write, and anti-dependencies. This is the representation many analyses actually use.

## Review: SER Characterization Theorem

For serializability, the bridge is exact: roughly, an item-only history is serializable exactly when its dependency graph is acyclic.

## Review: SI Characterization Theorem

For snapshot isolation, there is also an exact graph condition: every cycle must contain two adjacent anti-dependencies.

## Review: Downstream Analysis Tasks

These characterizations support downstream tasks such as black-box checking, protocol verification, and robustness analysis.

## Review (Summary)

So without predicates, we have a clean chain from specifications, to dependency graphs, to characterization theorems, and then to analysis.

## Review

Now add predicates. The operational models still make sense, but the semantic-to-graph bridge becomes much less settled.

## Review: Intuitive or Operational Specs

SER and SI retain their familiar operational intuition, but that intuition does not tell us which graph edges should represent a predicate observation.

## Review: Axiomatic Specs

Recent predicate-aware semantics can model SQL operations rigorously and support checking, but they do not provide the dependency-graph correspondence needed here.

## Review: Dependency Graphs

The key complication is omission. If a predicate does not return a key, some version must still explain that absence; a later write may change the result.

## Review: Dependency Graphs

Existing work captures this in different ways. Predicate anti-dependency definitions retain different amounts of information, from observation-changing successors to broader structural candidates.

## Review: SER Characterization

Predicate-aware SER graph conditions have long been used, but their exact correspondence to a predicate-aware execution semantics lacks a rigorous two-way proof.

## Review: SI Characterization

For SI, the gap is sharper: Adya uses lower-level timing information, while the later implementation-independent characterization is item-only.

## Review (Summary)

This leaves three missing pieces: a semantic interface, uniform predicate dependencies, and exact SER and SI graph characterizations. [PAUSE]

## Contributions: Fill and Exploit the Gap

We fill that bridge and then exploit it: extend the semantic framework, define predicate-aware graphs, prove SER and SI characterizations, and identify a design space of predicate anti-dependencies.

## 1. Axiomatic Specs

We extend visibility and arbitration with item-wise external predicate observations. For each covered key, the latest visible writer must explain either the returned value or why the key is absent.

## 2. Dependency Graphs

The graph records that explanation as a predicate-read dependency. A predicate anti-dependency points to a later writer when that writer changes what the predicate would observe.

## 3. Characterizations

We then recover the familiar forms: acyclicity for SER, and the adjacent-anti-dependency cycle condition for SI. The SI subtlety is witness mismatch: equivalent versions can explain the same omission, so soundness need not reconstruct exactly the input graph.

## 4. Design Space (of Predicate Anti-Dependencies)

The proofs show that one precise anti-dependency relation is not mandatory. Between a lower frontier and an upper structural relation, every admissible choice preserves the same existential SER and SI characterization.

## Future Work: Downstream Analysis

This suggests a practical direction: use the lower and upper relations as bounds for predicate-aware history checking, then extend the same foundation to verification and robustness.

## Takeaways: Theory Established, Downstrem Analysis Enabled

The takeaway is simple. Predicate reads make omitted items semantically relevant, and existing graph reasoning lacked an exact bridge to that fact. We provide that bridge: predicate-aware semantics, dependencies, SER and SI characterizations, and a proof-guided design space. [PAUSE] This gives downstream analyses a correctness foundation without forcing one unique predicate-edge representation.
