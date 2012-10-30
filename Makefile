PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/_content
OUTPUTDIR=$(BASEDIR)/
CONFFILE=$(BASEDIR)/_source/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/_source/publishconf.p
INCLUDES=$(BASEDIR)/_source/includes

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   github                           upload the web site via gh-pages   '
	@echo '                                                                       '


html: clean includes $(OUTPUTDIR)/index.html
	@echo 'Done'

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	# Remove all except the files that start with _, the .git folder, and some other special files as Makefile or README
	find . | egrep -v "/_|static|Makefile|README|.git|^.$$" | xargs rm -rf

includes:
	python $(INCLUDES)/age.py > $(INPUTDIR)/pages/age.inc

regenerate: clean includes
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

github: html
	git add .
	git commit -m 'Publishing';git push
