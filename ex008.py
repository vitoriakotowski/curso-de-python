n = float(input('Isso tem quantos metros? '))
print('Então tem {:.3f} km, {:.3f} hm, {:.3f} dam, {:.0f} dm, {:.0f} cm e {:.0f} mm!'.format((n*0.001), (n*0.01), (n*0.1), (n*10), (n*100), (n*1000)))