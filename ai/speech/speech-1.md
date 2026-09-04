# Speech

## Specifying and Analyzing Transactional Consistency Models with Predicates

Hi everyone. I am Hengfeng Wei from Hunan University.
This is joint work with Si Liu and Yuxing Chen.
This work develops a semantic and graph-theoretic foundation for transactional consistency with predicates.
Let me start with the key distinction between item operations and predicate operations.

## Item Operations vs. Predicate Operations

Look at the employee table.
An item read identifies a key and returns a value.
The predicate "Salary below 9" instead returns both X and Z, while Y is omitted.
Under concurrency, that omission also matters.

## Review

Now, let me review what is well understood without predicates.

## Review: Intuitive or Operational Specs

For item operations, serializability corresponds to serial execution, while snapshot isolation combines snapshot reads with write-conflict control.

## Review: Axiomatic Specs

We have several axiomatic specification frameworks that formally define the consistency models.

## Review: Dependency Graphs

We also have dependency graphs that summarize conflicts through read, write, and anti-dependencies.
For example, T reads a version written by T', and S later overwrites that version.
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

SER and SI retain their intuitive or operational specs.

## Review: Axiomatic Specs

Recent predicate-aware semantics rigorously model SQL operations and support checking, but do not provide the dependency graph correspondence.

## Review: Dependency Graphs

Look at this example.
Transaction T returns X and Z, while Y is omitted because the visible version has salary 10.
Later, S writes salary 9, so Y would now match.
The dependency graph captures this change via the PredRW edge from T to S.

## Review: Dependency Graphs

But existing work captures this differently:
some definitions keep all match-changing successors, while others keep only the earliest one or drop the match-changing condition altogether.
So there is no uniform definition of predicate anti-dependency.

## Review: SER Characterization

Predicate-aware SER graph conditions have long been used, but their exact correspondence to predicate-aware semantics lacks a rigorous iff proof.

## Review: SI Characterization

For SI, the gap is sharper: Adya's formulation uses lower-level timing information, while the characterization theorem was proved based on the item-only properties of SI.

## Review (Summary)

This leaves three missing pieces: a semantic interface, uniform predicate dependencies, and exact SER and SI graph characterizations. [PAUSE]

## Contributions: Fill and Exploit the Gap

We build that bridge by extending the specification framework, defining predicate-aware dependency graphs, proving SER and SI characterizations, and identifying a design space of predicate anti-dependencies.

## 1. Axiomatic Specs

The key axiom in the specs is that the latest visible writer must explain either the returned value or the omission.
For example, the visible writer of Y supplies 10, explaining why Y is omitted: 10 fails the predicate.

## 2. Dependency Graphs

The predicate-read edge records the writer explaining Y.
Since S later changes Y from non-matching to matching, we add a predicate anti-dependency from the reader $T$ to S.

## 3. Characterizations

With these specs and dependency graphs, we can now lift the familiar SER and SI graph characterizations to histories with predicates.

There are two witness-mismatch issues in the "if" proofs: one common to both SER and SI, and one specific to SI.

We omit the details here.

## 4. Design Space (of Predicate Anti-Dependencies)

The proofs also show that one precise anti-dependency relation is not mandatory.
We identify an interval and every admissible choice in this interval preserves the same existential SER and SI characterization.
Moreover, the lower bound is sufficient for the "if" direction, while the upper bound is safe for the "only if" direction.

## Future Work: Downstream Analysis

As mentioned before, our theory enables downstream analysis.
For example, we can use the lower and upper bounds to guide predicate-aware history checking.

## Takeaways: Theory Established, Downstream Analysis Enabled

In summary, we build the bridge through predicate-aware semantics, dependency graphs, exact SER and SI characterizations, and a proof-theoretic design space.
[PAUSE] This gives downstream analyses a correctness foundation.