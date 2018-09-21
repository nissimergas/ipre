(define (problem problema5)
(:domain  gripper2)

(:objects x1 x2 x3 x4 x5 x6
y1 y2 y3 y4 y5 y6
ball1 ball2
left right)

(:init
(coord_x x1) (coord_y y1)
(coord_x x2) (coord_y y2)
(coord_x x3) (coord_y y3)
(coord_x x4) (coord_y y4)
(coord_x x5) (coord_y y5)
(coord_x x6) (coord_y y6)

(next x1 x2) (next y1 y2)
(next x2 x3) (next y2 y3)
(next x3 x4) (next y3 y4)
(next x4 x5) (next y4 y5)
(next x5 x6) (next y5 y6)



(next x6 x5) (next y6 y5)
(next x5 x4) (next y5 y4)
(next x4 x3) (next y4 y3)
(next x3 x2) (next y3 y2)
(next x2 x1) (next y2 y1)



(BALL ball1) (BALL ball2)
(GRIPPER left) (GRIPPER right) (free left) (free right)
(at-robby_x x1) (at-robby_y y1)
(at-ball_x ball1 x1)(at-ball_y ball1 y1)
(at-ball_x ball2 x2)(at-ball_y ball2 y2)

)

(:goal (and
(at-robby_x  x1) (at-robby_y  y1)


))
)