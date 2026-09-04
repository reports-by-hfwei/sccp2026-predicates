# Review of `speech-1(1).md`

## 1. 总体结论

这一版相比上一版已经有明显改进：

- 正文从约 **690 词**降到了约 **634 个实际口述词**；
- 多处拼写和语法问题已经修正；
- 标题页更紧凑；
- `3. Characterizations` 已明显缩短；
- 整体叙事仍然保持清楚的主线：
  **item-only baseline → predicates introduce a gap → contributions → technical core → downstream analysis → takeaway**。

现在已经接近一个可用的 5 分钟版本，但我仍然认为它处于 **“可以讲完，但还不够稳妥”** 的状态。主要原因不是总字数本身，而是：

1. 25 页 Slides 带来频繁翻页、指图和视觉定位；
2. 前 18 页 Review 仍占用了过多时间；
3. Slide 22 `3. Characterizations` 虽然缩短了，但现在反而删掉了该页最值得讲的 predicate-specific insight，而且没有按此前约定对页内两个具体 witness 图作点拨式说明。

我建议再做一轮**小幅、定向压缩**，最终控制在约 **605–615 词**。这样会比目前的 634 词安全很多，而且不需要牺牲核心技术内容。

---

## 2. 五分钟时长重新评估

### 2.1 当前字数

排除 Markdown 标题和 `[PAUSE]` 后，这一版正文约为：

> **634 spoken words**

这是比上一版的约 690 词更合理的长度。

### 2.2 不同语速下的纯口述时间

| 语速 | 634 词纯口述时间 |
|---:|---:|
| 125 wpm | 5:04 |
| 130 wpm | 4:53 |
| 135 wpm | 4:42 |
| 140 wpm | 4:32 |
| 145 wpm | 4:22 |

但这些数字**没有包含**：

- 24 次左右的翻页；
- `Look at the employee table`、`Look at this example` 等指图动作；
- 两处 `[PAUSE]`；
- 技术词汇带来的自然减速；
- 现场可能出现的轻微迟疑。

对于这类短技术报告，我建议额外预留至少 **10–20 秒**。

因此比较现实的估算是：

| 自然语速 | 预计实际总时长 |
|---:|---:|
| 130 wpm | 约 5:03–5:13 |
| 135 wpm | 约 4:52–5:02 |
| 140 wpm | 约 4:42–4:52 |

所以：

> **634 词已经比上一版好很多，但如果你的自然技术演讲语速是 130–135 wpm，它仍然处于临界区。**

如果你的目标是允许最多提前 15 秒，即希望稳定落在 **4:45–5:00**，更稳妥的正文长度仍是：

> **约 605–615 词**

如果多次完整彩排证明你在不赶语速的情况下稳定达到 138–140 wpm，那么当前 634 词也可能保留；否则建议再删约 **20–30 词**。

---

## 3. 一个仍然比较明显的时间分配问题：Contributions 出现得偏晚

当前前 18 页，也就是进入 `Contributions: Fill and Exploit the Gap` 之前，共约：

> **391 词**

这占全文约 **62%**。

仅按纯口述计算：

- 130 wpm：到 Contributions 前约 **3:00**
- 135 wpm：约 **2:54**
- 140 wpm：约 **2:48**

再加翻页和停顿，实际很容易到 **3 分钟左右**才进入自己的工作。

对于 5 分钟 research talk，我认为这仍然偏晚。

建议目标是：

> **Contributions 最好在 2:40–2:50 左右开始。**

因此，这一轮最值得做的压缩仍然是 **Slides 3–18 的 Review**，而不是后面的 contributions。

如果把 Review 从 391 词压到约 **355–365 词**，整体节奏会明显改善。

---

## 4. 明显或值得修正的英文表达

### Slide 2: Item Operations vs. Predicate Operations

当前：

> An item read identifies a key and returns a value.

语法没有问题，但从数据库语义看，`identifies a key` 稍微有些不自然。更直接、更符合 point access 的说法是：

> An item read **names a key** and returns a value.

或者：

> An item read **accesses one named key** and returns a value.

第一种最简洁，建议采用。

---

### Review: Axiomatic Specs

当前：

> We have several axiomatic specification frameworks that formally define the consistency models.

没有语法错误，但比较泛，也浪费了一点时间。因为听众是领域专家，可以更紧凑：

> **Axiomatic frameworks formally specify these models.**

如果想保留该 Slide 的核心术语，可以说：

> **Axiomatic frameworks such as VIS/AR give implementation-independent specifications.**

后者信息密度更高。

---

### 第一处 Review: Dependency Graphs

当前：

> For example, T reads a version written by T', and S later overwrites that version.
> Therefore, T anti-depends on S.

整体已经比上一版准确，但口头上 `T'` 最好明确读成 **T-prime**。

另外，从版本语义看，与其说 S “overwrites that version”，不如直接说它覆盖同一个 item：

> For example, T reads **x from T-prime**, and S later overwrites **x**, creating an anti-dependency from T to S.

这既更短，也更容易配合图示。

---

### Predicate-aware Review: Intuitive or Operational Specs

当前：

> SER and SI retain their intuitive or operational specs.

能理解，但不够自然。更适合口语：

> **The intuitive operational views of SER and SI still apply.**

或者更短：

> **The operational views of SER and SI still apply.**

---

### Review: SER Characterization

当前：

> ... lacks a rigorous iff proof.

`iff` 在论文中很好，但在演讲中直接说 “iff proof” 略显书面和生硬。

建议：

> ... **has not been established by a rigorous two-way proof.**

或者更短：

> ... **lacks a rigorous two-way correspondence proof.**

---

### Review: SI Characterization

当前：

> For SI, the gap is sharper: Adya's formulation uses lower-level timing information, while the characterization theorem was proved based on the item-only properties of SI.

这里仍然存在一个**指代不够清楚**的问题：`the characterization theorem` 到底是指 Adya 的 formulation，还是后来 item-only 的 theorem？

如果你要表达 Slide 上的两个批评点，建议明确主语：

> **For SI, Adya's formulation uses lower-level timing information, and its proof relies on item-only properties of SI.**

这更直接，也更短。

如果你想强调 Introduction 中“later implementation-independent characterization is item-only”的 gap，则可以说：

> **For SI, Adya's formulation uses lower-level timing information, while the later implementation-independent characterization is item-only.**

两种表述侧重点不同。就当前 Slide 17 的文字而言，第一种与 Slide 更直接对应。

---

### 1. Axiomatic Specs

当前：

> The key axiom in the specs is that the latest visible writer must explain either the returned value or the omission.

整体很好。若追求形式上更精确，可以把 `latest` 明确为 arbitration order：

> ... the **AR-latest visible writer** must explain ...

不过在 5 分钟口述中，如果前面已经展示 `(VIS, AR)`，目前的 `latest visible writer` 足够自然，不必为了形式精确增加口述负担。

---

### 4. Design Space

当前：

> We identify an interval and every admissible choice in this interval preserves ...

建议在 `interval` 后加一个自然停顿，或者稍微改写：

> **We identify an interval in which every admissible relation preserves the same existential SER and SI characterization.**

`relation` 比 `choice` 更准确，因为这里选择的是 predicate anti-dependency relation。

---

### Future Work

当前：

> As mentioned before, our theory enables downstream analysis.

`As mentioned before` 是纯 filler，在 5 分钟 talk 中建议删除。

可直接说：

> **Our theory enables downstream analysis.**

甚至可以进一步压成一句：

> **For example, the lower and upper bounds can guide predicate-aware history checking.**

这样该页一句就足够。

---

## 5. 当前最重要的问题：Slide 22 `3. Characterizations`

这一页现在有：

> With these specs and dependency graphs, we can now lift the familiar SER and SI graph characterizations to histories with predicates.

> There are two witness-mismatch issues in the "if" proofs: one common to both SER and SI, and one specific to SI.

> We omit the details here.

这一版虽然从原来的约 88 词降到了约 **47 词**，时长上改善很大，但存在两个新的问题。

### 5.1 “We omit the details here” 太空

Slide 22 明明有两个具体 witness 图，而你此前对讲稿的要求是：

> 如果当前 Slide 包含具体例子，需要对例子作简要、点拨式说明。

因此在这里直接说 `We omit the details here`，然后翻页，会使两个最重要的图完全没有发挥作用。

这也是目前全文中最明显不符合既定演讲策略的一页。

### 5.2 删掉了本工作很重要的 SI-specific insight

论文 Introduction 中这一点实际上非常重要：

> 对 SI，observationally equivalent writers 可能都能解释相同 omission，因此 graph witness 与 execution witness 不必一致；soundness 不需要 exact graph recovery。

这是一个很好的、真正 predicate-specific 的技术洞见，值得在 5 分钟报告中用一句话留下来。

### 5.3 推荐整页替换

建议把 Slide 22 整页改为下面约 **54 词**的版本：

> We lift the familiar SER and SI characterizations to predicate histories.
> The challenge in the "if" direction is witness mismatch.
> Look at the two cases: on the left, a mismatch changes the predicate outcome and exposes a forbidden anti-dependency; on the right, the SI witnesses are observationally equivalent, so exact graph recovery is unnecessary.

它有几个优点：

1. 仍然只有约 54 词；
2. 对两个图都作了点拨；
3. 不展开证明细节；
4. 把 SI 最重要的 predicate-specific insight 讲出来；
5. 与论文 Introduction 的贡献表述一致。

这一页我建议**增加约 7 词也值得**，然后从 Review 中把这些词和更多时间省回来。

---

## 6. 推荐的一组“精确压缩”方案

如果采用上面 Slide 22 的版本，会从 47 词增加到约 54 词。

因此建议在前面的 Review 中做以下五处小改动。

### (1) Review: Axiomatic Specs

当前约 12 词：

> We have several axiomatic specification frameworks that formally define the consistency models.

改为约 6 词：

> **Axiomatic frameworks formally specify these models.**

节省约 **6 词**。

---

### (2) Item-only Review: Dependency Graphs

当前约 33 词，改为：

> **Dependency graphs summarize read, write, and anti-dependencies. Here T reads x from T-prime, and S later overwrites x, creating an anti-dependency from T to S.**

约 25 词。

节省约 **8 词**。

---

### (3) Predicate-aware Review: Axiomatic Specs

当前：

> Recent predicate-aware semantics rigorously model SQL operations and support checking, but do not provide the dependency graph correspondence.

改为：

> **Recent predicate-aware semantics model SQL operations rigorously, but do not establish the dependency-graph correspondence.**

节省约 **4 词**，而且 `establish` 比 `provide` 更适合 theorem/correspondence 的语境。

---

### (4) Review: SER Characterization

当前：

> Predicate-aware SER graph conditions have long been used, but their exact correspondence to predicate-aware semantics lacks a rigorous iff proof.

改为：

> **Predicate-aware SER graph conditions exist, but lack a rigorous two-way correspondence with predicate-aware semantics.**

节省约 **6 词**。

---

### (5) Review: SI Characterization

当前约 25 词：

> For SI, the gap is sharper: Adya's formulation uses lower-level timing information, while the characterization theorem was proved based on the item-only properties of SI.

改为约 17 词：

> **For SI, Adya's formulation uses lower-level timing information, and its proof relies on item-only properties of SI.**

节省约 **8 词**。

---

这五处合计大约可省：

> **32 词**

再把 Slide 22 增加约 7 词后，全文大约从：

> **634 词 → 609 词**

这恰好进入我认为比较理想的范围。

更重要的是，前 18 页会从约：

> **391 词 → 359 词**

这样以 135 wpm 计算，纯口述到 Contributions 约为：

> **2:40**

加上正常翻页与指图后，大约在 **2:45–2:50** 进入自己的贡献，非常合适。

---

## 7. 609 词版本的预计时长

如果按上述方案压到约 609 词：

| 语速 | 纯口述时间 |
|---:|---:|
| 125 wpm | 4:52 |
| 130 wpm | 4:41 |
| 135 wpm | 4:31 |
| 140 wpm | 4:21 |

考虑 10–20 秒翻页、停顿、指图：

- 125 wpm：约 **5:02–5:12**，仍偏慢；
- 130 wpm：约 **4:51–5:01**；
- 135 wpm：约 **4:41–4:51**；
- 如果实际技术演讲语速约 132–135 wpm，基本会落在目标窗口内。

因此约 **605–615 词**是一个比当前 634 词明显更安全的区间。

---

## 8. 建议的彩排检查点

这一版已经到了“必须以真实彩排而不是字数估算为最终依据”的阶段。

完整彩排时，应：

1. 实际翻 Slide；
2. 真正停下来指向 table / graph；
3. 按照计划保留 `[PAUSE]`；
4. 不为了时间故意加速；
5. 连续做至少三次。

建议记录以下累计时间：

- Slide 10 `Review (Summary)` 结束：**约 1:25–1:35**
- Slide 18 predicate `Review (Summary)` 结束：**约 2:40–2:50**
- Slide 19 `Contributions` 开始：**最好不晚于 2:50**
- Slide 23 `Design Space` 开始：**约 4:05–4:15**
- Slide 25 `Takeaways` 开始：**约 4:30–4:40**
- 结束：**4:45–5:00**

最重要的判断标准仍然是：

> **三次完整彩排中最慢的一次也不要超过 5:00。**

如果只有最快的一次可以压进 5 分钟，就仍然不够安全。

---

## 9. 最终建议

这一版已经不需要结构性重写，主要做三件事即可：

1. **再从 Review 中删约 30 词**，把 Contributions 提前到约 2:45；
2. **恢复 Slide 22 对两个 witness 图的点拨式解释**，尤其保留 SI 中“不需要 exact graph recovery”这一关键 insight；
3. 修正少数不够自然的表达，如：
   - `identifies a key` → `names a key`
   - `iff proof` → `two-way proof`
   - `choice in this interval` → `relation in this interval`
   - 删除 `As mentioned before`

如果按上述精确压缩方案调整，正文约 **609 词**，我认为会比当前 634 词版本更适合作为正式的 5 分钟会议演讲稿。