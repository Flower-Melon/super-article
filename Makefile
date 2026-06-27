# ============================================================
#  LaTeX 编译 Makefile
#  用法:
#    make         - 编译一次 (xelatex)
#    make pdf     - 完整编译 (xelatex + bibtex + xelatex*2)
#    make clean   - 删除辅助文件
#    make cleanall- 删除辅助文件 + PDF
#    make view    - 编译后用 SumatraPDF 打开（Windows）
# ============================================================

MAIN   = main
TEX    = xelatex
BIB    = bibtex
VIEWER = "C:/Program Files/SumatraPDF/SumatraPDF.exe"

.PHONY: all pdf clean cleanall view fast

# 快速编译（仅 xelatex 一次，适合写作中预览）
all: fast
fast:
	$(TEX) -synctex=1 -interaction=nonstopmode $(MAIN).tex

# 完整编译（含参考文献）
pdf:
	$(TEX) -synctex=1 -interaction=nonstopmode $(MAIN).tex
	$(BIB)  $(MAIN)
	$(TEX) -synctex=1 -interaction=nonstopmode $(MAIN).tex
	$(TEX) -synctex=1 -interaction=nonstopmode $(MAIN).tex

# 用 SumatraPDF 打开（需要在 PATH 中或有绝对路径）
view: fast
	$(VIEWER) "$(MAIN).pdf" &

# 清理辅助文件
clean:
	del /Q *.aux *.log *.out *.toc *.blg *.bbl *.synctex.gz 2>nul || true

# 清理所有生成文件（含 PDF）
cleanall: clean
	del /Q "$(MAIN).pdf" 2>nul || true
