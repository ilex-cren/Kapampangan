all :
	hfst-lexc --Werror pam.lexc -o pam.lexc.hfst
	hfst-twolc pam.twol -o pam.twol.hfst
	hfst-twolc pam.mor.twol -o pam.mor.twol.hfst
	hfst-compose-intersect -1 pam.lexc.hfst -2 pam.twol.hfst | hfst-compose-intersect -1 - -2 pam.mor.twol.hfst -o pam.hfst
	hfst-invert pam.hfst | hfst-fst2fst -w -o pam.hfstol

