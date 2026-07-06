# ============================================================
#  LaTeX 编译 Makefile
#  用法:
#    make         - 快速编译 (仅 xelatex 一次)
#    make pdf     - 完整编译 (xelatex + bibtex + xelatex*2)
#    make clean   - 删除辅助文件
# ============================================================

MAIN   = main
TEX    = xelatex
BIB    = bibtex

.PHONY: all pdf clean

all:
	$(TEX) -synctex=1 -interaction=nonstopmode $(MAIN).tex

pdf:
	$(TEX) -synctex=1 -interaction=nonstopmode $(MAIN).tex
	$(BIB)  $(MAIN)
	$(TEX) -synctex=1 -interaction=nonstopmode $(MAIN).tex
	$(TEX) -synctex=1 -interaction=nonstopmode $(MAIN).tex

clean:
	del /Q *.aux *.log *.out *.toc *.blg *.bbl *.synctex.gz *.xdv *.fls *.fdb_latexmk *.lof *.lot *.nav *.snm *.vrb *.run.xml *.bcf 2>nul || true
