day1=1
name1="羽绒服"
price1=253.6
num1=500
sales1=10

day2=2
name2="牛仔裤"
price2=86.3
num2=600
sales2=60

day3=3
name3="风衣"
price3=96.8
num3=335
sales3=43

day4=4
name4="皮草"
price4=135.9
num4=855
sales4=63

day5=5
name5="T恤"
price5=65.8
num5=632
sales5=63

day6=6
name6="衬衫"
price6=49.3
num6=562
sales6=120

day7=7
name7="牛仔裤"
price7=86.3
num7=600
sales7=72

day8=8
name8="羽绒服"
price8=253.6
num8=500
sales8=69

day9=9
name9="牛仔裤"
price9=86.3
num9=600
sales9=90

day10=10
name10="羽绒服"
price10=253.6
num10=500
sales10=140

day11=11
name11="牛仔裤"
price11=86.3
num11=600
sales11=90

day12=12
name12="皮草"
price12=135.9
num12=855
sales12=24

day13=13
name13="T恤"
price13=65.8
num13=632
sales13=45

day14=14
name14="风衣"
price14=96.8
num14=335
sales14=25

day15=15
name15="牛仔裤"
price15=86.3
num15=600
sales15=60

day16=16
name16="T恤"
price16=65.8
num16=632
sales16=129

day17=17
name17="羽绒服"
price17=253.6
num17=500
sales17=10

day18=18
name18="风衣"
price18=96.8
num18=335
sales18=43

day19=19
name19="T恤"
price19=65.8
num19=632
sales19=63

day20=20
name20="牛仔裤"
price20=86.3
num20=600
sales20=60

day21=21
name21="皮草"
price21=135.9
num21=855
sales21=63

day22=22
name22="风衣"
price22=96.8
num22=335
sales22=60

day23=23
name23="T恤"
price23=65.8
num23=632
sales23=58

day24=24
name24="牛仔裤"
price24=86.3
num24=600
sales24=140

day25=25
name25="T恤"
price25=65.8
num25=632
sales25=48

day26=26
name26="风衣"
price26=96.8
num26=335
sales26=43

day27=27
name27="皮草"
price27=135.9
num27=855
sales27=57

day28=28
name28="羽绒服"
price28=253.6
num28=500
sales28=10

day29=29
name29="T恤"
price29=65.8
num29=632
sales29=63

day30=30
name30="风衣"
price30=96.8
num30=335
sales30=78

Z=sales1+sales2+sales3+sales4+sales5+sales6+sales7+sales8+sales9+sales10\
  +sales11+sales12+sales13+sales14+sales15+sales16+sales17+sales18+sales19\
  +sales20+sales21+sales22+sales23+sales24+sales25+sales26+sales27+sales28+sales29+sales30

ZE=round(price1*sales1+price2*sales2+price3*sales3+price4*sales4+price5*sales5
      +price6*sales6+price7*sales7+price8*sales8+price9*sales9+price10*sales10+price11*sales11
      +price12*sales12+price13*sales13+price14*sales14+price15*sales15+price16*sales16+price17*sales17
      +price18*sales18+price19*sales19+price20*sales20+price21*sales21+price22*sales22+price23*sales23
      +price24*sales24+price25*sales25+price26*sales26+price27*sales27+price28*sales28+price29*sales29
      +price30*sales30,2)
#Y=1,8,10,17,28
Y=round((sales1+sales8+sales10+sales17+sales28)/Z*100,2)
Y1=round((sales1+sales8+sales10+sales17+sales28)*price1/ZE,2)
#N=2,7,9,11,15,20,24
N=round((sales2+sales7+sales9+sales11+sales15+sales20+sales24)/Z*100,2)
N1=round((sales2+sales7+sales9+sales11+sales15+sales20+sales24)*price2/ZE,2)
#F=3,14,18,22,26,30
F=round((sales3+sales14+sales18+sales22+sales26+sales30)/Z*100,2)
F1=round((sales3+sales14+sales18+sales22+sales26+sales30)*price3/ZE,2)
#P=4,12,21,27
P=round((sales4+sales12+sales21+sales27)/Z*100,2)
P1=round((sales4+sales12+sales21+sales27)*price4/ZE,2)
#T=5,13,16,19,23,25,29
T=round((sales5+sales13+sales16+sales19+sales23+sales25+sales29)/Z*100,2)
T1=round((sales5+sales13+sales16+sales19+sales23+sales25+sales29)*price5/ZE,2)
#C=6
C=round(sales6/Z*100,2)
C1=round(sales6*price6/ZE,2)

print("--------------------十二月份销售数据--------------------")
print("\t\t羽绒服\t牛仔裤\t风衣\t\t皮草\t\tT恤\t\t衬衫")
print("销售占比",Y,"%",N,"%",F,"%",P,"% ",T,"% ",C,"%")
print("销售额占比",Y1,"% ",N1,"% ",F1,"% ",P1,"% ",T1,"% ",C1,"%")
print("总销售额：￥",ZE,"元整")





