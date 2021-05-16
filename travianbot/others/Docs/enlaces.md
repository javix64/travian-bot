url_base = 'https://ts2.x1.europe.travian.com/'

materiales : id
    wood = l1
    clay = l2
    iron = l3
    cereal = l4

produccion por hora : css selector
    #production >tbody >tr > td.num

tropas : css selector
    #troops >tbody >tr > td.num

tropas en movimiento : 
        aventura = class adventure
        refuerzos = class d1
    tipo de tropas: #movements >tbody  >tr > td > .mov >span 
    minutos : #movements >tbody  >tr > td > .dur_r >span (value)  

hacer funciones:
    - cola de construccion
    - suba todos los recursos a un nivel determinado
    - hacer aventuras

que estructura sigue para hacer un post:
url o ejecutar comando,
ejemplo url: /start_adventure.php?from=list&kid=49758
ejecutar js: jQuery("#goToAdventure49758 form").submit()

recursos:
    dorf1.php
    lo ideal seria que fuera desde el id 1 hasta el 18, que comprobara que tipo de material es y lo guardara en un array o en un objeto.
        wood:
        https://ts2.x1.europe.travian.com/build.php?id=1
        https://ts2.x1.europe.travian.com/build.php?id=3
        https://ts2.x1.europe.travian.com/build.php?id=14
        https://ts2.x1.europe.travian.com/build.php?id=17
        clay:
        https://ts2.x1.europe.travian.com/build.php?id=5
        https://ts2.x1.europe.travian.com/build.php?id=6
        https://ts2.x1.europe.travian.com/build.php?id=16
        https://ts2.x1.europe.travian.com/build.php?id=18
        iron:
        https://ts2.x1.europe.travian.com/build.php?id=4
        https://ts2.x1.europe.travian.com/build.php?id=7
        https://ts2.x1.europe.travian.com/build.php?id=10
        https://ts2.x1.europe.travian.com/build.php?id=11
        cereal:
        https://ts2.x1.europe.travian.com/build.php?id=2
        https://ts2.x1.europe.travian.com/build.php?id=8
        https://ts2.x1.europe.travian.com/build.php?id=9
        https://ts2.x1.europe.travian.com/build.php?id=12
        https://ts2.x1.europe.travian.com/build.php?id=13
        https://ts2.x1.europe.travian.com/build.php?id=15
Centro de la aldea:
    dorf2.php
        edificio principal:
        

aventuras:


build.php?id=1