all:
	latexmk -quiet -pdf -bibtex

clean:
	latexmk -C
