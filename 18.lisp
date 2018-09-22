(defun area_court(l b)
	
	(format t "Area of the tennis court=: ~5f unit^2" (* l b))
)
(defun perim_court(l b)
	
	(format t "Perimeter of the tennis court=: ~5f units" (* 2 (+ l b)))
)

(princ "Enter length and breadth of tennis court:")
(terpri)
(defvar x)
(defvar y)
(setq x (read))
(setq y (read))
(terpri)
(area_court x y)
(terpri)
(perim_court x y)

