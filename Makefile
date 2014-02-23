all:
	make clean
	make html

clean:
	rm -rf -- *.html pages feeds

html:
	polo -input content

github:
	make all
	git add -A .
	git commit -m 'Publishing';git push
