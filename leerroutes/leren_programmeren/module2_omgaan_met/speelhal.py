
aantalminuten = int(input("hoeveel minuten?:"))
speelhal = 745
vrgamen = 39 * aantalminuten / 5

aantalmensen = int(input("hoeveel mensen?:"))

speelhaltotaal = speelhal * aantalmensen 
print(speelhaltotaal , "cent")


vrtotaal = vrgamen * aantalmensen 
print(vrtotaal, "cent")

totaalprijs = vrtotaal + speelhaltotaal

print(f'Dit geweldige dagje-uit met {aantalmensen} mensen in de Speelhal met {aantalminuten} minuten VR kost je maar {totaalprijs} cent')




