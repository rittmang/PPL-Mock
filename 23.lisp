(defun result (m)
	(cond ((> m 80)
			  (princ "You passed with distinction!")
		  )
		  
	      ((and (<= m 80) (> m 60))
	      		(princ "You passed with First Class!")
		  )
		  
		  ((and (<= m 60) (> m 50))
	      		(princ "You passed with Second Class.")
		  )
		  
		  ((and (<= m 50) (> m 40))
	      		(princ "You passed.")
		  )
		  (
		  		(princ "You failed.")
		  )
		  
	);cond	
)
(defun average (temp_one temp_two temp_three)
	(/ (+ temp_one temp_two temp_three) 3)
)
(princ "Enter marks for three subjects:")
(terpri)
(defvar a)(defvar b)(defvar c)(defvar avg)
(setq a (read))
(setq b (read))
(setq c (read))
(setq avg (average a b c))
;(format t "Your average = ~f~%" avg)
(format t "Your average= ~,1f~%" avg);round/1 decimal place 
(result avg)

