#Мой вес на земле = 75кг 
#Мой вес на луне(16,5%) = 12.375кг ( округляем = 12.4)
#Набор веса + 1кг на луне = 0,165кг (округляем = 0,17)
moonMass = 12.4
everyYear = 0.17 
newYear = moonMass

for x in range(1, 16):
    newYear = float(newYear) + float(everyYear) 
    print('Мой вес %sкг %s год на луне' % (newYear, x))