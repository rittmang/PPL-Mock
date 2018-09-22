(defvar arr)
(defvar temp)

(defun swap(x y)
	(setf temp (aref arr x))
	(setf (aref arr x) (aref arr y))
	(setf (aref arr y) temp)
)


(princ "Enter size of array:")
(terpri)
(defvar n (read))
(defvar arr (make-array n))

; Follow format : terpri ===> terminate print line, thus after printing statement
; princ, terpri, define variables / input statement


(princ "Enter elements now:")
(terpri)

(dotimes (i n)
	(setf (aref arr i) (read))
)



(do ((i 0 (+ i 1))) ((= i (- n 1))) ; no of pass

         (do ((j 0 (+ j 1))) ((= j (- (- n i) 1))) ; no of comparision
              
             (if (> (aref arr j) (aref arr (+ j 1) ) )

                (swap j (+ j 1)) 		
		
             )
                           
         )
)
(write arr)


