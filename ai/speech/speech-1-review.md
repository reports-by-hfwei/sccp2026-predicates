# Review of `speech-1.md`

## 1. 总体结论

这个版本的整体叙事已经比较成熟，主线清楚：

**item operations → item-only theory → predicates introduce a gap → contributions → technical ideas → downstream analysis → takeaway**。

尤其是现在加入了针对 Slide 中具体例子的点拨式说明，例如 employee table、`PredRW` 示例和 witness mismatch，这比纯粹概述 bullet points 更适合现场报告。标题页也已经改成简短自我介绍、合作者和一句话工作定位，然后立即进入主题。

目前最需要处理的并不是结构，而是两件事：

1. **时长仍然偏长，而且风险比较明显。**
2. **有若干明显的拼写、语法和技术措辞问题，需要在正式演讲前修正。**

我的建议是：不要大改结构，而是在保持现有叙事的前提下，将正文从目前约 **690 个口述英文词**压缩到 **600–620 词**；如果实际英文演讲语速偏慢，最好进一步控制在 **590–610 词**。

---

## 2. 五分钟时长评估

### 2.1 当前字数

排除 Markdown 标题和 `[PAUSE]` 后，当前正文约为：

> **690 spoken words**

这是一个相当关键的数字。因为这是 25 页 Slides 的 5 分钟报告，不仅有纯粹说话时间，还要考虑：

- 24 次左右的翻页和视觉定位；
- 至少两处显式 `[PAUSE]`；
- 指向 table / figure 时自然产生的停顿；
- `serializability`、`predicate anti-dependency`、`characterization`、`observationally equivalent` 等技术词汇通常不能像普通对话一样快速带过。

因此，不能简单按日常英语的最高语速来估算。

### 2.2 不同语速下的纯口述时间

| 语速 | 690 词纯口述时间 | 加 10–20 秒翻页/停顿后的实际时间 |
|---:|---:|---:|
| 120 wpm | 5:45 | 5:55–6:05 |
| 125 wpm | 5:31 | 5:41–5:51 |
| 130 wpm | 5:18 | 5:28–5:38 |
| 135 wpm | 5:07 | 5:17–5:27 |
| 140 wpm | 4:56 | 5:06–5:16 |
| 145 wpm | 4:46 | 4:56–5:06 |
| 150 wpm | 4:36 | 4:46–4:56 |

对于这种高密度技术报告，**125–135 wpm** 是更适合清晰表达的区间；对于非英语母语演讲者，若还需要指图、强调概念和处理现场节奏，我不会把 140–150 wpm 当作安全目标。

换言之：

> **当前 690 词版本理论上可以在 5 分钟内说完，但只有在接近 145–150 wpm、并且翻页和停顿极少的情况下才比较可靠。作为正式会议报告，这个余量太小。**

如果目标是 **4:45–5:00**，我建议把实际口述正文控制在：

- **600–620 词**：适合约 130 wpm；
- **590–610 词**：对于非母语技术演讲更稳妥；
- 不建议超过 **630 词**，除非多次计时彩排已经证明自己的自然语速足够快。

### 2.3 当前内容分配也略偏向 Review

前 18 页、也就是进入 Contributions 之前，目前约有 **396 词，占全文约 57%**。这意味着按照 130 wpm，仅背景与 gap 铺垫就需要约 3 分钟，还没有算翻页。

对于 5 分钟 research talk，这个比例偏高。

更合适的目标是：

- Slides 1–2：约 30–35 秒；
- item-only review（Slides 3–10）：约 50–60 秒；
- predicate-aware gap（Slides 11–18）：约 65–75 秒；
- contributions + technical core（Slides 19–23）：约 2 分钟；
- future + takeaway（Slides 24–25）：约 30–35 秒。

因此，**最应该删减的是 Review，而不是 contributions。**

---

## 3. 明显的英文问题

下面这些建议应直接修改。

### Slide 2

原文：

> An item read **identfies** a key and returns a value.

拼写错误：

> An item read **identifies** a key and returns a value.

也可以更自然、更贴近 slide：

> An item read names a key and returns a value.

后者更短，也更容易口述。

---

### Review: Intuitive or Operational Specs

原文：

> snapshot isolation combines **read snapshots** with write-conflict control.

`read snapshots` 略不自然，而且 slide 本身是 “snapshot + write-conflict control”。

建议：

> snapshot isolation combines **a snapshot** with write-conflict control.

或者：

> snapshot isolation combines **snapshot reads** with write-conflict control.

第一种更简洁。

---

### 第一处 Review: Dependency Graphs

原文：

> For example, T read from T' and S overwrites T'.
> Therefore, T anti-depends on S.

这里既有时态问题，也有语义表达问题：严格来说，`S` 并不是 “overwrite transaction `T'`”，而是覆盖 `T'` 写出的同一 item/version。

建议：

> For example, T reads a version written by T', and S later overwrites that version.
> Therefore, T anti-depends on S.

如果还想更短：

> For example, T reads T's version, and S later overwrites it, giving an anti-dependency from T to S.

不过这里 `T'` 在口语中容易听混，最好现场指图。

---

### Predicate-aware Review: Dependency Graphs

原文：

> The dependency graph **capture** this change via the PredRW edge from T to S.

应为：

> The dependency graph **captures** this change via the PredRW edge from T to S.

---

### 第二处 Review: Dependency Graphs

原文：

> some **definition keep** all match-changing successors

应为：

> some **definitions keep** all match-changing successors

原文：

> uniform **definiton**

应为：

> uniform **definition**

另外：

> retain an earliest frontier

语义能够理解，但口语中不够直接。建议与 slide 对齐：

> retain only the earliest match-changing successor

因此这一页可以整体改为更自然的版本：

> But existing work captures this differently: some definitions keep all match-changing successors, while others keep only the earliest one or drop the match-changing condition altogether. So there is no uniform definition of predicate anti-dependency.

这同时更简洁。

---

### Review: SER Characterization

原文：

> their exact correspondence to predicate-aware specifications lacks a rigorous iff proof.

语法没有大问题，但从论文的核心术语看，`predicate-aware execution semantics` 比 `predicate-aware specifications` 更精确：

> their exact correspondence to predicate-aware **execution semantics** lacks a rigorous iff proof.

演讲中也可以直接说：

> ... has not been established by a rigorous two-way proof.

比口头说 “iff proof” 更自然。

---

### Review: SI Characterization

当前版本：

> For SI, there is also a gap:
> First, it uses lower-level timing information.
> Second, the characterization theorem was proved based on the item-only properties of SI.

这里最大问题是两个 `it` / `the characterization theorem` 的指代不够清楚，现场听众容易不知道你是在说 Adya 还是后来的 item-only characterization。

建议改成一句更加明确、也更符合论文 Introduction 的话：

> For SI, the gap is sharper: Adya's formulation uses lower-level timing information, while the later implementation-independent characterization is item-only.

这一版同时显著省时。

如果你确实希望保留 Slide 上 “proof based on item-only properties” 这一点，则至少需要把主语说清楚，而不要使用 `it`。

---

### Contributions

原文：

> In this work, we **fill that bridge** ...

`fill a bridge` 不是自然搭配。

建议二选一：

> In this work, we **build that bridge** ...

或

> In this work, we **close this gap** ...

由于 slide 标题就是 “Fill and Exploit the Gap”，我更建议：

> In this work, we **close this gap and build the missing bridge** ...

但考虑 5 分钟时长，最简洁的是：

> We build that bridge by extending the specification framework, defining predicate-aware dependency graphs, proving SER and SI characterizations, and identifying a design space of predicate anti-dependencies.

---

### 1. Axiomatic Specs

原文：

> The key **in** the axiomatic specs is that ...

更自然的是：

> The key **idea in** the axiomatic specification is that ...

或者更精确地对应 Slide：

> The key axiom is that the AR-latest visible writer must explain either the returned value or the omission.

后者更专业，也没有增加多少口述负担。

---

### 3. Characterizations

这一页目前是全文最需要修改的一页。

原文：

> Under **this specs** and dependency graph, the SER and SI characterization theorems are natural **generialization** of those for item-only histories.

问题包括：

- `this specs` → `these specifications`
- `dependency graph` 应为复数或换一种结构
- `generialization` 拼写错误，应为 `generalization`
- 主语是两个 theorems，应为 `generalizations`
- “natural generalizations” 容易让贡献听起来过于 trivial

更推荐：

> With these specifications and dependency graphs, the SER and SI characterizations retain the familiar forms from item-only histories.

或者，更突出“lift”：

> We can now lift the familiar SER and SI graph characterizations to histories with predicates.

第二种更短、更有力。

---

原文：

> There are two challenges in the ''if'' direction proofs due to mismatched witness.
> One for both SER and SI proofs, and one is specific to the SI proof.

第二句是 sentence fragment，`mismatched witness` 也不自然。

建议合并：

> There are two witness-mismatch issues in the “if” proofs: one common to SER and SI, and one specific to SI.

---

原文：

> We omit the details here.

后面马上又用了两句话解释两个 case，因此逻辑上稍显矛盾。

建议：

> I will only give the intuition.

然后再说后面的两个 case。

---

### 4. Design Space

原文：

> the lower and upper **bound corresponds** to ...

应为：

> the lower and upper **bounds correspond** to ...

更适合演讲且更清晰的版本是：

> The lower bound is sufficient for the “if” direction, while the upper bound is safe for the “only if” direction.

这样听众不需要解析 `respectively`。

---

### Future Work

原文：

> guide **the history checker**

除非前文已经定义了某个特定 checker，否则建议：

> guide **a history checker**

或者直接：

> guide predicate-aware history checking.

后者更自然。

---

### Takeaways

原文：

> We provide the bridge between specs and dependency graphs: **including** predicate-aware semantics, dependencies, ...

冒号后接 `including` 略别扭，而且 “dependencies” 太抽象。

建议：

> We build the bridge through predicate-aware semantics, dependency graphs, exact SER and SI characterizations, and a proof-theoretic design space.

这是更适合作为最后一句总结的 parallel structure。

---

## 4. 内容与表达层面的几个重要建议

### 4.1 Slide 1 现在是合适的

当前开场已经符合 5 分钟学术报告的需求：

- 自我介绍；
- joint work；
- 一句话定位 contribution；
- 立即进入 item vs. predicate。

不需要再加入额外 hook。对于只有 5 分钟的专家报告，这种直接开场比额外创造一个 slide 中没有的案例更合适。

唯一可进一步压缩的是：

> This work provides a semantic and graph-theoretic foundation for specifying and analyzing transactional consistency models with predicate operations.

句子本身很好，但比较长。若彩排发现时间紧，可改为：

> This work develops a semantic and graph-theoretic foundation for transactional consistency with predicates.

可省约 8–10 个词。

---

### 4.2 Item-only review 应该再快一些

Slides 3–10 的任务只是建立一个已知基线：

> specs → depgraphs → exact characterizations → downstream analysis.

听众是数据库一致性领域专家，因此这一段不需要逐项解释太久。

特别是 SER 和 SI characterization 页，只需让听众重新激活这两个经典结果，而不是“重新讲授”它们。

因此建议把 item-only review 再删 **20–30 词**。

---

### 4.3 Predicate-aware review 是背景部分真正应该保留的重点

Slides 14–18 比 Slides 3–10 更重要，因为它们定义了本文真正的 gap。

尤其应保留：

1. omission 也需要 witness；
2. later writer 可以 change matches；
3. predicate anti-dependency definitions differ；
4. SER 缺少 rigorous two-way semantic correspondence；
5. SI 缺少你所追求的 implementation-independent predicate-aware characterization。

如果必须在 Review 中取舍，宁可进一步压缩 item-only review，也不要把这一段削得过薄。

---

### 4.4 Slide 22 “3. Characterizations” 当前 88 词，明显过长

这是当前单页最长的一页，约 **88 词**。

按 130 wpm，它单独需要约 **41 秒**；对于 25 页 / 5 分钟的报告，这是不可接受的占比。

这一页最重要的信息其实只有三个：

1. SER/SI characterizations 保持 familiar graph form；
2. “if” direction 有 predicate-specific witness mismatch；
3. SI 的关键洞见是：不需要 exact graph recovery，只需要 constructed execution satisfies SI。

建议控制在 **55–65 词**。

例如：

> We can now lift the familiar SER and SI graph characterizations to histories with predicates. The difficult part is the “if” direction, where graph and execution witnesses may differ. If the mismatch changes the predicate outcome, it exposes a forbidden anti-dependency. For SI, observationally equivalent witnesses create no such edge, so we prove soundness without requiring exact graph recovery.

这段约 60 词，已经覆盖本页最关键的 insight。

---

### 4.5 Slide 23 Design Space 可以保留，但应尽量用 “proof obligation” 的语言

当前思路正确，但这一页真正值得让听众记住的不是“有一个 interval”本身，而是：

- lower bound：足以 expose violations / support the “if” direction；
- upper bound：足以 safely orient edges / support the “only if” direction；
- 因而 interval 内不同表示具有相同 existential characterization，但未必具有相同 analysis cost。

在 5 分钟里最后一点可以不展开。

建议约 **35–40 词**即可。

---

## 5. 推荐的压缩方案

当前约 690 词。建议至少删掉 **70–90 词**，最好删到 **600–620 词**。

优先级如下：

### 第一优先级：Slide 22

从 **88 词**压到 **55–65 词**。

预计节省：**25–30 词**。

### 第二优先级：item-only Review

Slides 3–10 总体再压缩。

预计节省：**20–30 词**。

例如：

- axiomatic specs 页可以只说一句；
- depgraph example 保留一句点拨即可；
- SER/SI theorem 页各一句；
- downstream 页一句；
- summary 页一句。

### 第三优先级：predicate Review 中的重复措辞

Slides 12、13、15、16、17 可以合计再省 **15–20 词**，但不要删除核心 gap。

### 第四优先级：Slide 23 与标题页

各省 5–10 词即可。

这样能够自然落到约 **605–620 词**。

---

## 6. 一个更可靠的现场计时标准

不要只做一次快速朗读然后看是否低于 5 分钟。建议按正式演讲方式做至少三次：

1. 必须实际翻页；
2. 必须实际指向 table / graph；
3. 保留计划中的 `[PAUSE]`；
4. 不刻意加速；
5. 每次从第一句话到最后一句完整计时。

判断标准建议用：

> **三次中最慢的一次 ≤ 5:00，最好在 4:45–4:55。**

如果只有最快的一次能做到 5:00，那么正式场合大概率会超时。

此外，应重点记录到达下面几个页面时的累计时间：

- Slide 10：约 **1:25–1:35**
- Slide 18：约 **2:35–2:45**
- Slide 19 Contributions：最好 **不晚于 2:45**
- Slide 23 Design Space：约 **4:15–4:25**
- Slide 25 Takeaways：最好在 **4:35 左右开始**

如果到 Contributions 已经超过 3 分钟，后半部分几乎必然需要赶语速。

---

## 7. 最终建议

这个版本**没有结构性问题**，也不需要重新设计讲稿。当前最重要的是：

1. 修正上述明显拼写、语法和 technical phrasing；
2. 将 690 词压到约 **600–620 词**；
3. 主要压缩 item-only review 和 Slide 22，而不是删减 predicate-specific gap；
4. 保留目前这种“look at this example / for example”式的点拨，不展开公式和证明；
5. 用完整翻页彩排而不是单纯朗读来测量 5 分钟。

如果只做一项实质修改，我会首先压缩 **Slide 22**；如果做第二项，就压缩 **Slides 3–10 的 item-only review**。完成这两项后，这篇讲稿会明显更适合 5 分钟现场报告。