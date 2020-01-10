DESTDIR =
DICTDIR = /usr/share/myspell/dicts
DICTIONARYLIST = $(DICTDIR)/dictionary.lst

INSTALL      = install -m755
INSTALL_DATA = install -m644

all:

install:
	$(INSTALL) -d $(DESTDIR)$(DICTDIR)
	$(INSTALL_DATA) smj.aff smj.dic $(DESTDIR)$(DICTDIR)/.
	cat hunspell-smj >> $(DESTDIR)$(DICTIONARYLIST)
	cd $(DESTDIR)$(DICTDIR) && \
	ln -s smj.dic smj_NO.dic && \
	ln -s smj.aff smj_NO.aff && \
	ln -s smj.dic smj_SE.dic && \
	ln -s smj.aff smj_SE.aff

clean:
