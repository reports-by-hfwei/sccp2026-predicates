# Speech Backup

The operational models remain meaningful, but the semantic-to-graph bridge becomes much less settled.

SER and SI retain their intuition, but that does not tell us which graph edges represent a predicate observation.

Predicate reads make omitted items semantically relevant, and graph reasoning lacked an exact bridge to that fact.

If the execution chooses a writer that changes the predicate outcome, the mismatch exposes a forbidden anti-dependency.
But if both candidate versions fail the predicate, they are observationally equivalent, so exact graph recovery is unnecessary.

We can now lift the familiar SER and SI graph characterizations to histories with predicates. The difficult part is the “if” direction, where graph and execution witnesses may differ. If the mismatch changes the predicate outcome, it exposes a forbidden anti-dependency. For SI, observationally equivalent witnesses create no such edge, so we prove soundness without requiring exact graph recovery.

We lift the familiar SER and SI characterizations to predicate histories.
The challenge in the "if" direction is witness mismatch.
Look at the two cases: on the left, a mismatch changes the predicate outcome and exposes a forbidden anti-dependency; on the right, the SI witnesses are observationally equivalent, so exact graph recovery is unnecessary.

There are two witness-mismatch issues in the "if" direction proofs: one common to both SER and SI, and one specific to SI.

We omit the details here.

Here T reads x from T-prime, and S later overwrites x, creating an anti-dependency from T to S.

The challenge in the "if" direction is witness mismatch.
On the left, a mismatch changes the predicate outcome and exposes a forbidden anti-dependency; on the right, the SI witnesses are observationally equivalent, so exact graph recovery is unnecessary.