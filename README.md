# 论文

## 项目结构

```
├── main.tex          # 主文件
├── sections/         # 各章节
│   ├── 01-introduction.tex
│   ├── 02-related-work.tex
│   ├── 03-method.tex
│   ├── 04-experiments.tex
│   └── 05-conclusion.tex
├── figures/          # 图片
├── tables/           # 表格
├── references.bib    # 参考文献
└── Makefile          # 编译脚本
```

## 编译

需要 XeLaTeX 环境（TeX Live 2024）。

```bash
make          # 快速编译（仅 xelatex 一次）
make pdf      # 完整编译（含参考文献）
make clean    # 清理辅助文件
```
