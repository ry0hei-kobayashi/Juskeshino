;****************************************
;*                                      *
;* gpsr_deftemplates.clp                *
;*                                      *
;*          University of Mexico        *
;*          Jesus Savage-Carmona        *
;*          November 2022               *
;*                                      *
;*          Tamagawa University         *
;*          Luis Contreras              *
;*          March 2023                  *
;*                                      *
;****************************************

(deftemplate item
	(field type
		(type SYMBOL)
		(default nil)
	)
	(field name
		(type SYMBOL)
		(default nil)
	)
	(field room
		(type SYMBOL)
		(default nil)
	)
	(field zone
		(type SYMBOL)
		(default nil)
	)
	(multifield attributes
		(type SYMBOL)
		(default nil)
	)
	(multifield pose
		(type NUMBER)
		(default 0 0 0)
	)
	(field lower
		(type SYMBOL)
		(default base)
	)
	(field upper
		(type SYMBOL)
		(default nothing)
	)
	(field grasp
		(type SYMBOL)
		(default nil)
	)
	(field possession
		(type SYMBOL)
		(default nobody)
	)
	(multifield objs
        (type SYMBOL)
        (default nil)
        )
	(multifield status
		(type SYMBOL)
		(default nil)
	)
	(field num
		(type NUMBER)
		(default 1)
	)
)


(deftemplate room
	(field type
		(type SYMBOL)
		(default Room)
	)
	(field name
		(type SYMBOL)
		(default nil)
	)
	(field room
		(type SYMBOL)
		(default nil)
	)
	(field zone
		(type SYMBOL)
		(default nil)
	)
	(multifield zones
		(type SYMBOL)
		(default nil)
	)
	(multifield attributes
		(type SYMBOL)
		(default nil)
	)
	(multifield center
		(type NUMBER)
		(default 0 0 0 0)
	)
	(field num
		(type NUMBER)
		(default 1)
	)
)


(deftemplate arm
	(field type
		(type SYMBOL)
		(default Arm)
	)
	(field name
		(type SYMBOL)
		(default nil)
	)
	(field obj
		(type SYMBOL)
		(default nil)
	)
	(field status
		(type SYMBOL)
		(default nil)
	)
	(field num
		(type NUMBER)
		(default 1)
	)
)


(deftemplate memory
	(field type
		(type SYMBOL)
		(default Memory)
	)
	(field name
		(type SYMBOL)
		(default nil)
	)
	(multifield msg
		(type SYMBOL)
		(default nil)
	)
	(field source
		(type SYMBOL)
		(default nil)
	)
	(field target 
		(type SYMBOL)
		(default nil)
	)
	(field status
		(type SYMBOL)
		(default nil)
	)
	(field num
		(type NUMBER)
		(default 1)
	)
)


(deftemplate state
	(field type
		(type SYMBOL)
		(default State)
	)
	(field attribute
		(type SYMBOL)
		(default nil)
	)
	(field obj
		(type SYMBOL)
		(default nil)
	)
	(field human 
		(type SYMBOL)
		(default nil)
	)
	(field value
		(type SYMBOL)
		(default nil)
	)
)

