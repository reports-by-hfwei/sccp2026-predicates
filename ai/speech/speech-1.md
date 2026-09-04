# Speech

## Specifying and Analyzing Transactional Consistency Models with Predicates

Hi everyone. I am Hengfeng Wei from Hunan University.
This is joint work with Si Liu and Yuxing Chen.
This work provides a semantic and graph-theoretic foundation for specifying and analyzing transactional consistency models with predicate operations.
Let me start with the key distinction between item operations and predicate operations.

## Item Operations vs. Predicate Operations

Look at the employee table.
An item read identfies a key and returns a value.
The predicate "Salary below 9" instead returns both X and Z, while Y is omitted.
Under concurrency, that omission also matters.

## Review

Now, let me review what is well understood without predicates.

## Review: Intuitive or Operational Specs

For item operations, serializability corresponds to serial execution, while snapshot isolation combines read snapshots with write-conflict control.

## Review: Axiomatic Specs

We have several axiomatic specification frameworks that formally define the consistency models.

## Review: Dependency Graphs

We also have dependency graphs that summarize conflicts through read, write, and anti-dependencies.
For example, T read from T' and S overwrites T'.
Therefore, T anti-depends on S.

## Review: SER Characterization Theorem

For serializability, the bridge between axiomatic specs and dependency graphs is exact: roughly, an item-only history is serializable exactly when its dependency graph is acyclic.

## Review: SI Characterization Theorem

For snapshot isolation, every cycle must contain two adjacent anti-dependencies.

## Review: Downstream Analysis Tasks

These characterizations support history checking, protocol verification, and program robustness analysis.

## Review (Summary)

So without predicates, we have a clean chain from specifications, to graphs, to characterization theorems, and then to downstream analysis.

## Review

Now consider predicates.

## Review: Intuitive or Operational Specs

SER and SI retain their intuition.

## Review: Axiomatic Specs

Recent predicate-aware semantics rigorously model SQL operations and support checking, but do not provide the dependency graph correspondence.

## Review: Dependency Graphs

Look at this example.
Transaction T returns X and Z, while Y is omitted because the visible version has salary 10.
Later, S writes salary 9, so Y would now match.
The dependency graph capture this change via the PredRW edge from T to S.

## Review: Dependency Graphs

But existing work captures it differently:
some definition keep all match-changing successors,
while others retain an earliest frontier or drop the match-changing condition.
That is, we do not have a uniform definiton of predicate anti-dependency in the literature.

## Review: SER Characterization

Predicate-aware SER graph conditions have long been used, but their exact correspondence to predicate-aware specifications lacks a rigorous iff proof.

## Review: SI Characterization

For SI, there is also a gap:
First, it uses lower-level timing information.
Second, the characterization theorem was proved based on the item-only properties of SI.

## Review (Summary)

This leaves three missing pieces: a semantic interface, uniform predicate dependencies, and exact SER and SI graph characterizations. [PAUSE]

## Contributions: Fill and Exploit the Gap

In this work, we fill that bridge: extend the specification framework to support predicates, formally define predicate-aware dependency graphs, prove SER and SI characterizations, and finally identify a design space of predicate anti-dependencies.

## 1. Axiomatic Specs

The key in the axiomatic specs is that the latest visible writer must explain either the returned value or the omission.
For example, the visible writer of Y supplies 10, explaining why Y is omitted: 10 fails the predicate.

## 2. Dependency Graphs

The predicate-read edge records the writer explaining Y.
Since S later changes Y from non-matching to matching, we add a predicate anti-dependency from the reader $T$ to S.

## 3. Characterizations

Under this specs and dependency graph, the SER and SI characterization theorems are natural generialization of those for item-only histories.
There are two challenges in the ''if'' direction proofs due to mismatched witness.
One for both SER and SI proofs, and one is specific to the SI proof.
We omit the details here.

If the execution chooses a writer that changes the predicate outcome, the mismatch exposes a forbidden anti-dependency.
But if both candidate versions fail the predicate, they are observationally equivalent, so exact graph recovery is unnecessary.

## 4. Design Space (of Predicate Anti-Dependencies)

The proofs also show that one precise anti-dependency relation is not mandatory.
We identify an interval and every admissible choice in this interval preserves the same existential SER and SI characterization.
Moreover, the lower and upper bound corresponds to the "if" and the "only if" directions of the proof, respectively.

## Future Work: Downstream Analysis

As mentioned before, our theory enables downstream analysis.
For example, we can use the lower and upper bounds to guide the history checker.

## Takeaways: Theory Established, Downstrem Analysis Enabled

The takeaway is simple.
We provide the bridge between specs and dependency graphs: including predicate-aware semantics, dependencies, SER and SI characterizations, and a proof-theoretic design space.
[PAUSE] This gives downstream analyses a correctness foundation.