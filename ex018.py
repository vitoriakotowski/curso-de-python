from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo de {:.0f}° tem como seno {:.2f};'.format(ang, sen))
print('Como cosseno {:.2f}; e'.format(cos))
print('Como tangente {:.2f}.'.format(tan))