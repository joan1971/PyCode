inventory={'gold':500,'pouch':['flint','twine','gemstone'],'backpack':['xylophone','dagger','bedroll','bread loaf']}
inventory.update('pocket':['seashell','strange berry','lint'])
(inventory['backpack']).sort()
(inventory['backpack']).remove('dagger')
(inventory['gold'])=(inventory['gold'])+50
(inventory['pouch']).insert(1,'lighter')