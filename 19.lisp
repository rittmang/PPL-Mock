(defun perim_ground(l b)
	
	(format t "Perimeter of the cricket ground=: ~5f units" (* 2 (+ l b)))
)

(princ "Enter length and breadth of cricket ground:")
(terpri)
(defvar x)
(defvar y)
(setq x (read))
(setq y (read))
(terpri)
(perim_ground x y)

