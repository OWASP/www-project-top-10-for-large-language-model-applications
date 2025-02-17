# simple Makefile to compile the latex

PROJ=`cd ../; basename \`pwd\``
DOC=LLM_AI_Security_and_Governance_Checklist
FILES=$(DOC).tex

# create a random password
# requires pwgen
PW!=pwgen -n1

# create a PDF
pdf: $(FILES) distclean

# lualtex needs to run iteratively so it can process all references
	pdflatex  $(DOC).tex
	pdflatex  $(DOC).tex
	pdflatex  $(DOC).tex

# now clean up the intermediate steps
	make clean

# create an encrypted PDF
# requires pdftk (apt-get install pdftk-java)
crypt: pdf
	pdftk $(DOC).pdf output $(DOC).encrypted.pdf user_pw $(PW) allow allfeatures
	echo "Encryption password" is $(PW)

# create an RTF file for folks that want "Word" versions
rtf: $(FILES)
	latex2rtf $(DOC)

# clear out all the intermediate cruft from a build, but leave the PDFs
clean:
	rm -f *.tmp *.out *.aux *.idx *.log *.ilg *.xref *.lg \
	*.toc *.ind *.4og *.4ct *.4tc *.idv *.lot *.lov *.lltr *.lstr \
	*.ptc *.dvi *.tv *.vrb *.hv *.hst *.ver *.mv *.lv *.odt $(DOC).synctex.gz \
	*.rtf *.cg *.cp *.cpc *.dd *.sc *.xml *.bcf *.loc *.tdo *.4o* $(DOC).txt tex4ht.env \
	*.fdb_latexmk *.fls $(DOC).gz > /dev/null 2>&1
	-find . -name "*.aux" -exec rm {} \;

# clear out all the intermediate cruft and also any PDFs
distclean:
	-rm -f $(DOC).pdf $(DOC).encrypted.pdf *.tmp *.out *.aux *.idx *.log *.ilg *.xref *.lg \
	*.toc *.ind *.4og *.4ct *.4tc *.idv *.lot *.lov *.lltr *.lstr \
	*.ptc *.dvi *.tv *.vrb *.hv *.hst *.ver *.mv *.lv *.odt $(DOC).synctex.gz \
	*.rtf *.cg *.cp *.cpc *.dd *.sc *.xml *.bcf *.loc *.tdo *.4o* $(DOC).txt tex4ht.env \
	*.fdb_latexmk *.fls $(DOC).gz > /dev/null 2>&1
	-find . -name "*.aux" -exec rm {} \;
