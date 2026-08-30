# 三审三校（一审）：技术正确性与范围

审校对象：`sccp2026-predicates.tex`、`predicates.tex`，论文范围截至 Section 6.2（含）。

结论：通过。

核查要点：

- 动机准确：谓词读的观察同时涉及返回项与被覆盖但未返回的项；报告没有重复介绍隔离级别背景。
- 语义锚点准确：使用 VIS/AR 执行语义，并以最新可见写者解释每个被覆盖项。
- 图关系准确：`PredWR` 表示谓词观察的版本见证；`PredRW` 表示后来写入改变观察结果的关系。
- 主结果准确：SER 对应内部一致性加谓词依赖图无环；SI 对应内部一致性，且每个环含两个相邻的反依赖（`RW` 或 `PredRW`）。
- 设计空间表述限定为 history-level、existential characterization；未错误声称不同关系在每个 history 上相同。
- Future work 与 Section 6.2 一致：efficient black-box checking、robustness analysis。

修改：无。未发现虚构的实验结论、定理或相关工作事实。

编译核验：`latexmk -pdf -interaction=nonstopmode -halt-on-error sccp2026-predicates.tex` 成功，PDF 共 13 页。
