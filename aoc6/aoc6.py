def numOrbits():
    orbitCount = {}
    totalOrbit = 0
    with open('./input.txt') as fp:
        for cnt, line in enumerate(fp):
            line = line.rstrip('\n')
            split = line.split(')')
            print(split)
            center = split[0]
            orbitedBy = split[1]
            if center not in orbitCount and orbitedBy in orbitCount:
                orbitCount[center] = {'center': None, 'orbits': 0}
                orbitCount[orbitedBy]['center'] = center
                orbitCount[orbitedBy]['orbits'] += 1
                values = orbitCount.values()
                for value in values:
                    if (value['center'] == orbitedBy):
                        value['center'] = center
                        value['orbits'] += 1
            if center not in orbitCount:
                orbitCount[center] = {'center': None, 'orbits': 0}
            if orbitedBy not in orbitCount:
                currCenter = center
                while (orbitCount[currCenter]['center'] != None):
                    currCenter = orbitCount[currCenter]['center']
                orbitCount[orbitedBy] = {'center': currCenter, 'orbits': 0}
                orbitCount[orbitedBy]['orbits'] += 1
                orbitCount[orbitedBy]['orbits'] += orbitCount[center]['orbits']
            if center in orbitCount and orbitedBy in orbitCount:
                orbitCount[orbitedBy]['center'] = orbitedBy
                values = orbitCount.values()
                for value in values:
                    if (value['center'] == orbitedBy):
                        value['center'] = orbitCount[center]['center']
                        value['orbits'] += orbitCount[center]['orbits'] + 1


            
    values = orbitCount.values()
    for value in values:
        totalOrbit += value['orbits']
    
    return totalOrbit

# def numOrbits():
#     orbitCount = {}
#     totalOrbit = 0
#     linkOrbit = {}
#     with open('./input.txt') as fp:
#         for cnt, line in enumerate(fp):
#             line = line.rstrip('\n')
#             split = line.split(')')
#             print(split)
#             direct = split[0]
#             orbitedBy = split[1]
#             if direct not in orbitCount:
#                 orbitCount[center] = []
#             if orbitedBy not in orbitCount:
#                 orbitCount[orbitedBy] = []
#             orbitCount[orbitedBy].append(direct)
#             for orbit in orbitCount[direct]:
#                 orbitCount[orbitedBy].append(orbit)
#                 print(orbitCount[orbitedBy])

#     values = orbitCount.values()
#     for value in values:
#         totalOrbit += len(value)
    
#     return totalOrbit

result = numOrbits()
print(result)