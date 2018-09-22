(defun add(c1 c2)
	(format t "Sum: ~5f" (+ c1 c2))
)

(defun sub(c1 c2)
	(format t "Diff: ~5f" (- c1 c2))
)

(defun mul(c1 c2)
	(format t "Prod: ~5f" (* c1 c2))
)

(defun div(c1 c2)
	(format t "Quo: ~5f" (/ c1 c2))
)

(princ "Enter numbers: ")
(terpri)
(defvar c1 0)(defvar c2 0)(defvar choice 0)
(setq c1 (read))
(setq c2 (read))
(princ "Enter choice:")(princ "1. Addition  2.Subtraction  3.Multiplication  4.Division")
(terpri)
(setq choice (read))

(case choice 
	(1 (add c1 c2))
	(2 (sub c1 c2))
	(3 (mul c1 c2))
	(4 (div c1 c2))
)
