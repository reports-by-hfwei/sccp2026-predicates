# Speech

Hi everyone. I am Hengfeng Wei from Hunan University.
This work aims to develop a semantic and graph-theoretic foundation for transactional consistency with predicates.
Let's start with the distinction between item operations and predicate operations.

An item read operation names a key and returns a value,
and a predicate read operation names a condition and returns a set of matched values.

Now, let's review what we know about transactional consistency without predicates.

We have several spec frameworks which formally specify the consistency models like serializability and snapshot isolation.

Dependency graphs summarize write-read, write-write, and read-write anti-dependencies.

More importantly, we have the SER characterization theorem.
Roughly, an item-only history is serializable iff its dependency graph is acyclic.

For SI, every cycle must contain at least two adjacent anti-dependencies.

These characterizations support history checking, protocol verification, and program robustness analysis.

So without predicates, we have a chain from specs, to graphs, to characterizations, and then to downstream analysis.

Now consider predicates.

Recent predicate-aware semantics model SQL operations rigorously, but do not establish the dependency-graph correspondence.

For dependency graphs, consider this example.
Transaction T returns X and Z, while Y is omitted because it fails the predicate.
Later, S writes salary 7, so Y would now match.
The dependency graph captures this change via the PredRW edge from T to S.

But existing work captures this differently.
For instance, some definitions keep the match-changing condition, while others drop it altogether.
There is no uniform definition of predicate anti-dependency.

Predicate-aware SER graph conditions exist, but lack a rigorous two-way correspondence with predicate-aware semantics.

For SI, Adya's formulation uses lower-level timing information, and its proof relies on item-only properties of SI.

This leaves three missing pieces: a semantic interface, uniform predicate dependencies, and exact SER and SI graph characterizations.

In this work, we build that bridge by extending the specification framework, defining predicate-aware dependency graphs, proving SER and SI characterizations, and identifying a design space of predicate anti-dependencies.

First, the key axiom in the specs is that the latest visible writer must explain either the returned value or the omission.

The predicate-read edge records the writer explaining Y.
Since S later changes Y from non-matching to matching, we add a predicate anti-dependency from the reader T to S.

More importantly, we lift the familiar SER and SI characterizations to histories with predicates.

There are two witness-mismatch challenges in the "if" direction proofs.
But we skip the details here.

Moreover, we identify an interval in which every relation preserves the same SER and SI characterization.
We show that the lower bound is sufficient for the "if" direction, while the upper bound is safe for the "only if" direction.

Our theory enables downstream analysis.
For example, we can use the lower and upper bounds to guide predicate-aware history checking.

In summary, we build the bridge through predicate-aware specs, dependency graphs, SER and SI characterizations, and a proof-theoretic design space.
This gives downstream analyses a correctness foundation.