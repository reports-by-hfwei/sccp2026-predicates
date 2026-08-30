# 三审三校（三审）：构建、引用与文字校对

审校对象：最终 `sccp2026-predicates.tex` 与 `sccp2026-predicates.pdf`。

结论：通过。

校对与机械核验：

- 执行 `latexmk -pdf -interaction=nonstopmode -halt-on-error sccp2026-predicates.tex`，构建成功。
- 最终 PDF 为 16:9、13 页；PDF 页数、主讲/参考文献顺序及最终 Take Away 页均正确。
- 日志复核：无 overfull box、未定义控制序列、未定义引用或未定义交叉引用。
- 逐项复核术语和记号：VIS/AR、`PredWR`、`PredRW`、SER、SI 与正文/参考文献一致；`PredRW^- \subseteq PredRW \subseteq PredRW^+` 的含义由图和相邻页面说明。
- `biblatex` author--year 引用与参考文献页均已生成；未出现占位引用。
- 消除了语义锚点页中箭头列的微小排版溢出后重新编译，已同步更新 PDF。
