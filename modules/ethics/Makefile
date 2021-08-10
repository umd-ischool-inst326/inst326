all: index

index: README.adoc ../../includes/navigation.html
	asciidoctor README.adoc -o index.html

clean:
	rm -f index.html slides.html
