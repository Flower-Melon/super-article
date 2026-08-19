# 论文

## 项目结构

```
├── main.tex          # 主文件
├── sections/         # 各章节
│   ├── 01-introduction.tex
│   ├── 02-related-work.tex
│   ├── 03-system-overview.tex
│   ├── 04-evaluation-suite-design.tex
│   ├── 05-experiments.tex
│   └── 06-conclusion.tex
├── figures/          # 图片
├── tables/           # 表格
├── references.bib    # 参考文献
└── Makefile          # 编译脚本
```

## 编译

需要 pdfLaTeX 环境（TeX Live 2024）。主文件优先使用 TII 模板的
`ieeecolor.cls` 和 `generic.sty`；未安装模板配套文件时自动使用
标准 `IEEEtran` 类编译。

```bash
make          # 快速编译（仅 pdflatex 一次）
make pdf      # 完整编译（含参考文献）
make clean    # 清理辅助文件
```
