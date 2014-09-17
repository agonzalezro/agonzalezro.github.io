all:
	make clean
	make html

clean:
	rm -rf -- *.html pages feeds tag tags category

html:
	polo

server:
	polo -daemon

github:
	make all
	git add -A .
	git commit -m 'Publishing';git push
