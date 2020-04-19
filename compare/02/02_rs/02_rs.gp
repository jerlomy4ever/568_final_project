set term png size 500,250 font "Helvetica" 11
set output "02_rs.png"
set size ratio 0.5
set yrange [0:*]
set xlabel "Speed [km/h]"
set ylabel "Rotation Error [deg/m]"
plot "02_rs.txt" using ($1*3.6):($2*57.3) title 'Original SuMa++' lc rgb "#e35933" pt 4 w linespoints, \
"c.txt" using ($1*3.6):($2*57.3) title 'SuMa++ w/ correntropy' lc rgb "#df8c932" pt 4 w linespoints, \
"l.txt" using ($1*3.6):($2*57.3) title 'SuMa++ w/ heuristic idea' lc rgb "#0000FF" pt 4 w linespoints, \
"b.txt" using ($1*3.6):($2*57.3) title 'SuMa++ w/ both ideas ' lc rgb "#27ad81" pt 4 w linespoints
