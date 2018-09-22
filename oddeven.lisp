(defun oddeven(n)
	(cond 
		( 
			(= (mod n 2) 0)
		
		
			(princ "Even!")	
		)
		(
		
			(princ "Odd!")
		
		)
	
	
	)
)
(princ "Enter number:")
(terpri)
(defvar x)
(setq x (read))
(oddeven x)
