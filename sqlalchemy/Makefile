all: html

activate_and_compile = @. $(HOME)/.virtualenvs/landslide/bin/activate;$(1)

html:
	$(call activate_and_compile,\
		landslide -it light 0.md)

pdf:
	$(call activate_and_compile,\
		landslide -d presentation.pdf 0.md)
