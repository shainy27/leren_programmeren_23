
aantalminuten = int(input("hoeveel minuten VRgamen?:"))
aantalmensen = int(input("hoeveel mensen?:"))

speelhal = 745
speelhaltotaal = speelhal * aantalmensen 
print(speelhaltotaal, "cent")


vrgamen = 37 * aantalminuten / 5
vrtotaal = vrgamen * aantalmensen 
print(vrtotaal, "cent")

totaalprijs = (vrtotaal + speelhaltotaal)

print(f'Dit geweldige dagje-uit met {aantalmensen} mensen in de Speelhal met {aantalminuten} minuten VR kost je maar {totaalprijs} cent')




