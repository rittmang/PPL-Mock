(defun perim_court(l b)
	
	(format t "Perimeter of the volleyball court=: ~5f units" (* 2 (+ l b)))
)

(princ "Enter length and breadth of volleyball court:")
(terpri)
(defvar x)
(defvar y)
(setq x (read))
(setq y (read))
(terpri)
(perim_court x y)

