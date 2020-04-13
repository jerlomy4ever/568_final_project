import numpy as np
confusion = [[0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0 ,0 ,0 ,0, 0], 
[  3258930,  30355003,      6801,     59345,    150137,    977899,     15511,
       6966,       615,    363762,     69591,    298305,      1079,    636901,
     105316 ,  1484800 ,    43830 ,   340715,     19627 ,     3631],
 [     9809  ,     262  ,   77627  ,     275,         0  ,    1004 ,      284,
         55   ,     59   ,    271   ,     22 ,    35019   ,    124  ,   18671,
       6210    ,  8882    ,    33    ,  8661  ,     371    ,     2],
 [    19914     , 3890     ,13697    ,200674   ,      0     ,25947   ,    371,
        286      ,4403,      6315,      9788,     10049,        39 ,     6811,
       2872,     11482,         8,      9277     ,  415,        72],
 [    46639,     15728,        24,       386    ,282100 ,   150653 ,       41,
          3,         0,      3836,       110      ,8401  ,       0  ,    4747,
        309,      3894,       959,      2977      , 289     ,   85],
 [   316199,     97155,       840,      8558     ,58775   , 620909   ,     37,
        106,       170,      8115,      5142     ,14453    ,    37    , 11819,
       3189,     21960,      1172,      5526       ,720      , 374],
 [    80149,      2268,      1665,       409      ,  14       ,169 ,   271328,
      26123,      7510,      8361,       370     ,25363        ,48  ,   24143,
       9751,     45178,      3542,      8084      ,1622      ,2963],
 [    34994,      7366,        94,        22      , 495       , 87   ,   8003,
     233782,      3154,     36420,       116     ,12704        ,13    ,  3419,
        811,     11950,       758,     23791       ,118         ,7],
 [      127,        20,         0,         0        , 0         ,0       ,196,
      12867,         0,      2874,         0       ,118         ,0        , 0,
          0,        38,        10,       267      ,   0         ,0],
 [   246786,     65939,        10,       567     , 1367      ,2304       ,613,
       1825,         0 , 84807637,   1029570    ,940916,     92026      ,  65,
        596,     22854 ,       11 ,   229862     ,  241 ,       54],
 [    13472,     45389 ,        0 ,      608    ,   220  ,    4071     ,   12,
          4,         0 ,   139430 ,  3011715   , 234284   ,   1211    ,   228,
        159,      2643,        77 ,    79633  ,     220    ,     0],
 [   351883,     37869,      6387 ,     1233 ,      341     ,14004   ,   3763,
        166,       665,   2058146  , 1478459,  54691315     ,85055    ,138039,
     122189,    554742,      1290  , 2133315     ,11355      ,  62],
 [     9966,        54,         8   ,      7      ,   5       , 16   ,    241,
          1,         0,     13639   ,    317     ,54607      ,1383  ,   14467,
       3686,      9761,       997,    101145     ,   68       ,  8],
 [  2546477,     30530,     13243 ,     4966    ,   205    ,169110 ,    29606,
         94,        35,      1854,      1151    ,125549     , 9295,  48891614,
    2020536,   1593940,     53487 ,   199114     ,29806      ,4707],
 [  3104583,     30269,     38168  ,   35915     ,  431    ,111050   ,  27275,
        391,       350,     13707   ,   8910    ,379302      ,9925  ,  788551,
    8799052,   2520582,     43411    ,386176     ,29456     ,14056],
 [  9687082 ,   118012,     74662,     28802     ,13118    ,132056 ,    96587,
      20156,      5739,     61168 ,    33008    ,700968    ,111184,   5731795,
    1360489, 134786757,   1461119  , 8900625   , 167770     ,48899],
 [   895160,     15447,       520   ,    777  ,     455      ,5693     ,15999,
       2195,         0,      8640    ,  1869 ,    23284      ,3008    ,208742,
      25054,   1257102,   3767109    ,412260,    139607     ,14664],
 [  1091199,      8068,     10073,      1228    ,    57      ,5047     , 2411,
        498,        26,    404458 ,   291887   ,2640646    ,141633    ,219168,
     134052,   3082381,     84499  ,51132687  ,   22532        ,53],
 [   492169,     22313,      3575   ,   1210     ,  977      ,1707   ,   3323,
       1115,        11,     24320    ,  5517    , 84348      ,1546  ,  172811,
      46899,    483310,     39228    ,134081   ,1217314    ,116970],
 [   116301,       523,       402,       886  ,       7     ,  542 ,     1345,
        227,         0,       673,       150 ,      865      ,  44,      6909,
       1487,     34760,      1739,      3058,     24896    ,174835]]
confusion = np.array(confusion)
a = np.zeros((20, 20))
for i in range(20):
    a[:,i] = np.sum(confusion, axis = 1)
a[0,:] = np.ones((1,20))
confusion = confusion / a
print(np.dot(confusion[:,1], confusion[:,1]))
confusion = confusion.reshape(-1)
i=0
# for item in confusion:
#     print("c["+str(i)+"]=", end='')
#     print(item, end='')
#     print("; ", end='')
#     i=i+1
# print('\n')

label_map = [[0,0], [10, 1], [11, 2], [15, 3], [18, 4], [20, 5], [30, 6], [31, 7], [32, 8], [40, 9], [44, 10], [48, 11], [49, 12], [50, 13], [51, 14], [70, 15], [71, 16], [72, 17], [80, 18], [81, 19]]
vec = -np.ones((82,1))
for item in label_map:
    vec[item[0]] = item[1]

i=0
vec = vec.reshape(-1)
# for item in vec:
#     print("m["+str(i)+"]=", end='')
#     print(int(item), end='')
#     print('; ', end='')
#     i=i+1
# print('\n')


