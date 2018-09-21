(define (domain gripper2)
(:predicates (coord_x ?x) (coord_y ?x) (ball ?x) (GRIPPER ?x)
(at-robby ?x ?y) (at-ball ?b ?x  ?y )
(free ?x) (carry ?x ?y) (next ?x1 ?x2 ) (at-obstaculo ?x2 ?y2))

(:action move :parameters (?x ?y ?x2 ?y2)
:precondition (and (coord_x ?x) (coord_x ?x2) (coord_y ?y) (coord_y ?y2) (not (at-obstaculo ?x2 ?y2) )
(next ?x ?x2) (next ?y ?y2)
(at-robby ?x  ?y))
:effect (and (at-robby ?x2 ?y2)
(not (at-robby ?x ?y) )) )


(:action pick-up :parameters (?b ?x ?y ?z)
:precondition (and (BALL ?b) (coord_x ?x) (coord_y ?y) (GRIPPER ?z)
(at-ball ?b ?x ?y )  (at-robby ?x ?y) (free ?z))
:effect (and (carry ?z ?b)
(not (at-ball ?b ?x ?y )) (not (free ?z))))



(:action drop :parameters (?b ?x ?y ?z)
:precondition (and (BALL ?b) (coord_x ?x) (coord_y ?y) (GRIPPER ?z)
(carry ?z ?b) (at-robby ?x ?y))
:effect (and (at-ball ?b ?x ?y)(free ?z)
(not (carry ?z ?b))))
)