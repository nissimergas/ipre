﻿(define (problem problema2)
(:domain  gripper2)

(:objects x0 y0 x1 y1 x2 y2 x3 y3 x4 y4 x5 y5 x6 y6 x7 y7 x8 y8 x9 y9 x10 y10 x11 y11 x12 y12 x13 y13 x14 y14 x15 y15
ball1 ball2 ball3 ball4
left right)

(:init
(coord_x x0 ) (coord_y y0) (coord_x x1 ) (coord_y y1) (coord_x x2 ) (coord_y y2) (coord_x x3 ) (coord_y y3) (coord_x x4 ) (coord_y y4) (coord_x x5 )
                  (coord_y y5) (coord_x x6 ) (coord_y y6) (coord_x x7 ) (coord_y y7) (coord_x x8 ) (coord_y y8) (coord_x x9 )
                  (coord_y y9) (coord_x x10 ) (coord_y y10) (coord_x x11 ) (coord_y y11) (coord_x x12 ) (coord_y y12) (coord_x x13 )
                   (coord_y y13) (coord_x x14 ) (coord_y y14) (coord_x x15 ) (coord_y y15) (next x0 x1) (next y0 y1) (next x1 x0)
                    (next y1 y0) (next x1 x2) (next y1 y2) (next x2 x1) (next y2 y1) (next x2 x3) (next y2 y3) (next x3 x2) (next y3 y2)
                     (next x3 x4) (next y3 y4) (next x4 x3) (next y4 y3) (next x4 x5) (next y4 y5) (next x5 x4) (next y5 y4) (next x5 x6)
                      (next y5 y6) (next x6 x5) (next y6 y5) (next x6 x7) (next y6 y7) (next x7 x6) (next y7 y6) (next x7 x8) (next y7 y8)
                       (next x8 x7) (next y8 y7) (next x8 x9) (next y8 y9) (next x9 x8) (next y9 y8) (next x9 x10) (next y9 y10)
                        (next x10 x9) (next y10 y9) (next x10 x11) (next y10 y11) (next x11 x10) (next y11 y10) (next x11 x12)
                        (next y11 y12) (next x12 x11) (next y12 y11) (next x12 x13) (next y12 y13) (next x13 x12) (next y13 y12)
                         (next x13 x14) (next y13 y14) (next x14 x13) (next y14 y13) (next x14 x15) (next y14 y15) (next x15 x14)
                          (next y15 y14)



(BALL ball1) (BALL ball2) (BALL ball3) (BALL ball4)
(GRIPPER left) (GRIPPER right) (free left) (free right)
(at-robby_x x1) (at-robby_y y7)
(at-ball_x ball1 x1)(at-ball_y ball1 y1)
(at-ball_x ball2 x7)(at-ball_y ball2 y7)
(at-ball_x ball3 x8)(at-ball_y ball3 y4)
)

(:goal (and
(at-ball_x ball1 x5) (at-ball_y ball1 y7)
(at-ball_x ball2 x5) (at-ball_y ball2 y7)
(at-ball_x ball3 x5) (at-ball_y ball3 y7)
))
)