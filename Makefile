#convenient Makefile (I think) -MN

#targets:
#  make           - builds the text
#  make refcheck  - check \label{} and \ref{} and friends for consistency
#                   Result is in "latex_refs.log"
#  make clean     - removed Latex' auxiliary files
#  make ps        - create PS file
#  make pdf       - create PDF file
#  make html      - create HTML file
#  make changelog - creates ChangeLog
TEX=xelatex
FILE=pygis
WDIR=$(FILE)
all: 
	# make pics
	# /home/bk/bkcase/bin/bk.texin.py
	python3 bk.texin.py
	$(TEX) $(FILE)
	makeindex $(FILE).idx
#fuer einfache Referenz
#	bibtex $(FILE)
#fuer zweifache referenz
	# bibtex $(FILE)
	#now loop over Latex files, until stable:
	# echo Rerun > $(FILE).log
	# while grep Rerun $(FILE).log >/dev/null 2>&1 ; do $(TEX) $(FILE) ; done
	$(TEX) $(FILE)
	$(TEX) $(FILE)
	$(TEX) $(FILE)
	cp -f $(FILE).pdf ../ 
	# evince $(FILE).pdf &

view:
	evince $(FILE).pdf & 
clean:
	rm -f *.log *.aux $(FILE).dvi *.bbl *.blg *.ind *.ilg *.toc *.tof *.lof *.lot *.pdf *.ps *.idx *.brf *.out *~ *.cjk  $(FILE).pdf *.mtc*

