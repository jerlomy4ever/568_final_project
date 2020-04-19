set term png size 500,250 font "Helvetica" 11
set output "00_ts.png"
set size ratio 0.5
set yrange [0:*]
set xlabel "Speed [km/h]"
set ylabel "Translation Error [%]"
set key left bottom
plot "00_ts_o.txt" using ($1*3.6):($2*100) title 'Original SuMa++' lc rgb "#e35933" pt 4 w linespoints, \
"00_ts_c.txt" using ($1*3.6):($2*100) title 'SuMa++ w/ correntropy' lc rgb "#df8c932" pt 4 w linespoints, \
"00_ts_l.txt" using ($1*3.6):($2*100) title 'SuMa++ w/ heuristic idea' lc rgb "#0000FF" pt 4 w linespoints, \
"00_ts_b.txt" using ($1*3.6):($2*100) title 'SuMa++ w/ both ideas ' lc rgb "#27ad81" pt 4 w linespoints
