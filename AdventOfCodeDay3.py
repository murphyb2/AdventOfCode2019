lineA = ["R995","D882","R144","U180","L638","U282","L907","D326","R731","D117","R323","U529","R330","U252","R73","U173","R345","U552","R230","U682","R861","U640","L930","U590","L851","D249","R669","D878","R951","D545","L690","U392","R609","D841","R273","D465","R546","U858","L518","U567","L474","D249","L463","D390","L443","U392","L196","U418","R433","U651","R520","D450","R763","U714","R495","D716","L219","D289","L451","D594","R874","U451","R406","U662","R261","D242","R821","D951","R808","D862","L871","U133","R841","D465","R710","U300","R879","D497","R85","U173","R941","U953","R705","U972","R260","D315","L632","U182","L26","D586","R438","U275","L588","U956","L550","D576","R738","U974","R648","D880","R595","D510","L789","U455","R627","U709","R7","D486","L184","U999","L404","U329","L852","D154","L232","U398","L587","U881","R938","D40","L657","D164","R45","D917","R106","U698","L824","D426","R879","U700","R847","D891","L948","U625","R663","D814","R217","U30","R610","D781","L415","D435","L904","U815","R152","U587","R287","U141","R866","D636","L290","D114","L751","D660","R6","U383","L263","U799","R330","U96","L6","U542","L449","D361","R486","U278","L990","U329","L519","U605","R501","D559","R916","U198","L499","D174","R513","U396","L473","D565","R337","D770","R211","D10","L591","D920","R367","D748","L330","U249","L307","D645","R661","U266","R234","D403","L513","U443","L989","D1","L674","D210","L537","D872","L607","D961","R894","U632","L195","U744","L426","U531","R337","D821","R113","U436","L700","U779","R555","U891","R268","D30","R958","U411","R904","U24","R760","D958","R231","U229","L561","D134","L382","D961","L237","U676","L223","U324","R663","D186","R833","U188","R419","D349","L721","U152","L912","U490","R10","D995","L98","U47","R140","D815","R826","U730","R808","U256","R479","D322","L504","D891","L413","D848","L732","U375","L307","U7","R682","U270","L495","D248","R691","D945","L70","U220","R635","D159","R269","D15","L161","U214","R814","D3","R354","D632","R469","D36","R85","U215","L243","D183","R140","U179","R812","U180","L905","U136","L34","D937","L875"]

class Point:
  def __init__(self, x, y):
    self.X = x
    self.Y = y

def CreateLine(input):
  currentPos = Point(0,0)
  dwg = {}
  for movement in input:
    direction = movement[0]
    distance = int(movement[1:])
    
    if direction == 'R':
      while(distance):
        dwg[currentPos.X] = currentPos.Y

    elif direction == 'L':
      pass
    elif direction == 'U':
      pass
    elif direction == 'D':
      pass

CreateLine(lineA)
