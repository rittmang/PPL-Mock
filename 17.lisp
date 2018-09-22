;(defconstant pi 3.14156)
(defun area_ground(l b)
	
	(format t "Area of the cricket ground=: ~5f unit^2" (* l b))
)
(defun area_groundc(r)
	(format t "Area of ground circular=: ~5f unit^2" (* pi (* r r)))
)
(princ "Enter length and breadth of cricket ground:")
(terpri)
(defvar x)
(defvar y)
(defvar r)

(setq x (read))
(setq y (read))
(princ "Enter radius of cricket ground:")
(terpri)
(setq r (read))
(area_ground x y)
(terpri)
(area_groundc r)


